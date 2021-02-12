from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

from scripts.etl_kubernetes.etl_module_for_kubernetes import extract_tranform, load

default_args = {
    'owner': 'Damavis',
    'start_date': datetime(2020, 5, 18),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG('etl_dag_for_kubernetes',
         default_args=default_args,
          schedule_interval=None) as dag:

    extract_tranform = PythonOperator(task_id='extract_tranform',
                                      python_callable=extract_tranform)

    load = PythonOperator(task_id='load',
                          python_callable=load)

    extract_tranform >> load
