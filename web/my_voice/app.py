from flask import Flask, render_template, request, send_file, url_for, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
import os

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

        # Группировка по названиям колонок
        grouped_data = df.groupby(df.columns.tolist()).size().reset_index(name='Count')
        group_data_dict = grouped_data.to_dict(orient='records')

        return render_template('result.html', group_data=group_data_dict)

    return "File format not allowed. Please upload a CSV file."

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(host='0.0.0.0')
