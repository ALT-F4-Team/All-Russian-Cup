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
    df = pd.read_csv('uploads/sintetic.csv')
    df_group = df.groupby('sentiment').count().reset_index()

    return render_template('charts.html', labels=list(df_group['group']), data=list(df_group['text']), df=df.to_json())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
