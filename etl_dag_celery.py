from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators import kubernetes_pod_operator

default_args = {
    'owner': 'Damavis',
    'start_date': datetime(2020, 5, 5),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG('etl_dag',
         default_args=default_args,
         schedule_interval=None) as dag:

    extract_tranform = kubernetes_pod_operator.KubernetesPodOperator(
        namespace='airflow',
        image="python:3.7-slim",
        cmds=["echo"],
        arguments=["This can be the extract part of an ETL"],
        labels={"foo": "bar"},
        name="extract-tranform",
        task_id="extract-tranform",
        get_logs=True
    )

    extract_tranform
