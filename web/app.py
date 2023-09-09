from flask import Flask, render_template, request, send_file
import pandas as pd
import json

app = Flask(__name__)
app.secret_key = 'a66ee1919de09f25451412411bed2fb755f845d70f96bf0a'


@app.route('/download', methods=['GET', 'POST'])
def download():
    df = json.loads(request.form['results'])
    df = pd.DataFrame(data=df)
    filename = 'uploads/output.csv'

    df.to_csv(filename, index=False)
    return send_file(filename, as_attachment=True)


@app.route('/', methods=['GET', 'POST'])
def visualization():
    df = pd.read_csv('uploads\main_v1.csv')
    df_group = df.groupby('sentiment').count().reset_index()
    grouped_data = df.groupby('cluster').agg({'2d_embeds': list, 'text': list}).reset_index()

    grouped = df.groupby('cluster').count().reset_index()

    mean_group_count = int(grouped['text'].sum() / len(df['cluster'].unique()))
    group_count = len(df['cluster'].unique())

    max_cluster = grouped[grouped.text == grouped.text.max()]
    max_cluster_count = int(max_cluster['text'].iloc[0])
    top_elemnts = list(df[df['cluster'] == max_cluster.iloc[1, 0]].text[:3])

    datasets = []
    for index, row in grouped_data.iterrows():
        label = row['cluster']
        xy_list = row['2d_embeds']
        text_list = row['text']
        data = []
        for xy in zip(xy_list, text_list):
            x, y = xy[0][1:-1].split()
            data.append({'x': float(x), 'y': float(y), 'text': xy[1]})
        dataset = {'label': label, 'data': data}
        datasets.append(dataset)

    return render_template('charts.html', labels=list(df_group['sentiment']), data=list(df_group['text']),
                           df=df.to_json(), datasets=datasets, mean_group_count=mean_group_count, top_elemnts=top_elemnts, group_count=group_count, max_cluster_count=max_cluster_count)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
