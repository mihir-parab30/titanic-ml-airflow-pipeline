FROM apache/airflow:2.10.2
USER airflow
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt