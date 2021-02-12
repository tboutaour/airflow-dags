<h1> Airflow DAGS example.</h1>
Simple ETL pipeline example. It only has didactic purposes.

<h2> Dependencies</h2>

- helm (tested with ``v3.4.1``)
- kubectl (tested with ``v1.18``)

<h2> Deployments </h2>

Types of available deployments:
- Airflow deployment with CeleryExecutor

Use Helm to deploy all the Airflow configuration.

Add Airflow chart repository if not installed:

``helm repo add airflow-stable https://airflow-helm.github.io/charts`` and ``helm repo update``

To install the Airflow Chart into your Kubernetes cluster:

``helm install airflow --namespace airflow airflow-stable/airflow --values [CELERY YAML]``

<h2> DAGs examples</h2>

`etl_dag_celery.py` : DAG example for CeleryExecutor.

Python packages must be added to `requirements.txt`.
