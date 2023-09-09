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
    # grouped_data = df.groupby('cluster')['2d_embeds'].apply(list).reset_index()
    grouped_data = df.groupby('cluster').agg({'2d_embeds': list, 'text': list}).reset_index()

    # print(grouped_data)

    # datasets = [
    #     {
    #         'label': 'Scatter Dataset',
    #         'data': [
    #             {'x': 10, 'y': 20},
    #             {'x': 30, 'y': 40},
    #             {'x': 50, 'y': 60},
    #         ]
    #     },
    #     {
    #         'label': 'Scatter Dataset1',
    #         'data': [
    #             {'x': 110, 'y': 210},
    #             {'x': 310, 'y': 410},
    #             {'x': 510, 'y': 610},
    #         ]
    #     }
    # ]
    datasets = []
    for index, row in grouped_data.iterrows():
        label = row['cluster']
        xy_list = row['2d_embeds']
        text_list = row['text']
        data=[]
        # print(text_list)
        # print(xy_list)
        for xy in zip(xy_list, text_list):
            # print(xy)
            # xy[0]=xy[0][1:-1]
            # xy = xy.replace('  ', ' ')
            # if xy[-2] == ' ':
            #     xy=xy[:-2] + "]
            x, y = xy[0][1:-1].split()
            data.append({'x': float(x), 'y': float(y), 'text': xy[1]})
        dataset = {'label': label,'data': data}
        datasets.append(dataset)
    print(datasets)

    return render_template('charts.html', labels=list(df_group['sentiment']), data=list(df_group['text']), df=df.to_json(), datasets=datasets)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
