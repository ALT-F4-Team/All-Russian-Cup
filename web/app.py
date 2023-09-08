from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import pandas as pd
import os
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html', title='Улучшение представлений результатов “Мой голос”')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        df = pd.read_csv(file_path)

        preview = []

        for group in set(df.group):
            preview.append([group] + list(df[df.group == group].text[:3]))

        df = df.to_json()

        return render_template('result.html', preview=preview, df=df)

    return "File format not allowed. Please upload a CSV file."


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/download', methods=['GET', 'POST'])
def download():
    df = json.loads(request.form['results'])
    df = pd.DataFrame(data=df)
    filename = 'uploads/output.csv'

    df.to_csv(filename, index=False)
    return send_file(filename, as_attachment=True)


@app.route('/visualization', methods=['GET', 'POST'])
def visualization():
    df = json.loads(request.form['graphics'])
    df = pd.DataFrame(data=df).groupby('group').count().reset_index()

    return render_template('charts.html', labels=list(df['group']), data=list(df['text']))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
