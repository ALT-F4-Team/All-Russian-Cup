<h1 align="center">Хакатон-проект: кейс - Улучшение представлений результатов в сервисе "Мой Голос", Команда ALT+F4 <div align="center"><a href="https://hacks-ai.ru/hackathons.html?eventId=969091&caseEl=1001711&tab=1"><img src="https://img.shields.io/badge/hackathon--project-d513eb"></a></div></h1>

## Инструкция по запуску:

### 💼 1.  <b>Склонировать репозиторий:</b>
   
   ```bash
   git clone https://github.com/notdiff/answers_clustering
   ```
   ```bash
   cd answers_clustering
   ```
### 💻 2.  <b>В папке склонированного репозитория выполнить команды:</b>

   ```bash
   cd module
   ```
   ```bash
   pip install -r requirements.txt
   ```
### 📂 3. <b>В папке <a href=https://github.com/notdiff/answers_clustering/tree/c84931d4abef592ed57d91f0fcd35509e4ea5565/module>`module`</a>:</b>
  - Положить туда файл со своим <a href="https://github.com/notdiff/answers_clustering/blob/c84931d4abef592ed57d91f0fcd35509e4ea5565/module/cropped.csv">`датасетом`</a><i>(по ссылке пример датасета)</i>
  - _создать новый файлик_
  - _прописать в нём_:
    
    ```python
    from process_dset import process_dset
    
    process_dset("./название датасета")
    # --> pd.DataFrame
    # --> columns - answers, sentiment, cluster
    ```
 ### ✅ 4. <b>Запустить программу:</b>
 
  ```bash
  python имя_созданного_файла.py
  ```
### Пример результата <a href="">тут</a>
    


