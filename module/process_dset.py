import pandas as pd
import numpy as np
from tqdm.auto import tqdm
import sklearn

import umap.umap_ as umap
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import normalize
import compress_fasttext
import matplotlib.pyplot as plt

import nltk
import re

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def process_dset(path_to_data):
    # Загрузка опенсорс моделей
    # Модель получение скрытых состояний
    fasttext = compress_fasttext.models.CompressedFastTextKeyedVectors.load(
        'https://github.com/avidale/compress-fasttext/releases/download/gensim-4-draft/geowac_tokens_sg_300_5_2020-400K-100K-300.bin'
    )
    # Модель анализа тональности
    sentiment_model_tokenizer = AutoTokenizer.from_pretrained('cointegrated/rubert-tiny-sentiment-balanced')
    sentiment_model = AutoModelForSequenceClassification.from_pretrained('cointegrated/rubert-tiny-sentiment-balanced')
    # Загрузка обработанного датасета и выбор вопросов для примера
    dataset = pd.read_csv(path_to_data)
    # Функция лематизации и удаление нецензурной лексики
    restricted = open("restricted.txt", "r", encoding="utf8").read().split("  ")
    print(restricted)
    def rid_restricted(sent):
        return " ".join([word for word in sent.split(" ") if word not in restricted])
    def corretor(sentence):
        return re.sub(f"[#$%^&*\(\)\[\]]", "", sentence)
    dataset['answers'] = dataset['answers'].apply(lambda x: corretor(x))
    dataset['answers'] = dataset['answers'].apply(lambda x: rid_restricted(x))
    # Оценка тональности
    tokens = sentiment_model_tokenizer(dataset['answers'].tolist(), padding=True, truncation=True,
                                       return_tensors='pt')
    sentiments = torch.argmax(sentiment_model(**tokens).logits, dim=1)
    dataset['sentiment'] = sentiments

    dataset['sentiment'] = dataset['sentiment'].apply(lambda x: sentiment_model.config.id2label[x])

    dataset['embeds'] = list(fasttext[list(dataset['answers'])])
    # Понижение размерности до 2d
    reducer2d = umap.UMAP(n_components=2)
    dataset['embeds'] = list(reducer2d.fit_transform(list(dataset['embeds'])))
    # Агломеративная класетризация
    agg_clusterer = AgglomerativeClustering(n_clusters=None, distance_threshold=0.7)
    labels = agg_clusterer.fit_predict(list(dataset['embeds']))
    dataset['cluster'] = labels

    return dataset