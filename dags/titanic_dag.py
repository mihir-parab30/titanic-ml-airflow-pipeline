from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
# OLD:
# from src.titanic_utils import download_data, preprocess_data, train_model, evaluate_model

# NEW:
from titanic_utils import download_data, preprocess_data, train_model, evaluate_model

from titanic_utils import download_data, preprocess_data, train_model, evaluate_model

default_args = {
    "owner": "Mihir",
    "start_date": datetime(2025, 10, 1),
    "retries": 1,
}

with DAG(
    dag_id="Titanic_ML_DAG",
    default_args=default_args,
    schedule_interval=None,  # manual trigger
    catchup=False,
    description="Automated Titanic Survival Prediction Pipeline",
) as dag:

    t1 = PythonOperator(
        task_id="download_data",
        python_callable=download_data
    )

    t2 = PythonOperator(
        task_id="preprocess_data",
        python_callable=preprocess_data
    )

    t3 = PythonOperator(
        task_id="train_model",
        python_callable=train_model
    )

    t4 = PythonOperator(
        task_id="evaluate_model",
        python_callable=evaluate_model
    )

    t1 >> t2 >> t3 >> t4
