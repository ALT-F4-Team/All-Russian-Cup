import pandas as pd
import compress_fasttext

fasttext = compress_fasttext.models.CompressedFastTextKeyedVectors.load(
    'uploads/geowac_tokens_sg_300_5_2020-400K-100K-300.bin'
)



print(df.question.unique())
