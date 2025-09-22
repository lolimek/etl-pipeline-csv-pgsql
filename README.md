Прототип ETL: скачивание CSV → raw/ → загрузка в Postgres → простая визуализация.

Запуск локально (пример):
1. Скопировать .env.example → .env и заполнить.
2. docker-compose up -d
3. python src/ingestion/download_data.py --url https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv
4. python src/ingestion/load_to_postgres.py --file data/raw/iris.csv --table raw_trips
5. streamlit run src/api/app.py
