import sys
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
# Ensure the api-requests folder is importable
sys.path.append('/opt/airflow/api-requests')

def safe_main_callable():
    from insert_records import main
    return main()

# FIX 1: Use colons (:) for dictionary keys, not equals signs (=)
# FIX 2: Only put task-related args here (like start_date)
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 1, 30),
    'retries': 0
}

# FIX 3: Move 'description' and 'catchup' here (these belong to the DAG object)
dag = DAG(
    dag_id='weather_api-dbt-orchestrator',
    default_args=default_args,
    description='Orchestrator for the weather API',
    catchup=False,
    schedule=timedelta(minutes=1),
)

with dag:
    task1 = PythonOperator(
        task_id='ingest-data-task',
        python_callable=safe_main_callable,
    )

    task2 = DockerOperator(
        task_id='transform-data-task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        mounts=[
            Mount(target='/usr/app', 
            source='/home/qurat/repos/weather-data-project/dbt/my_project',
             type='bind'
             ),
            Mount(target='/root/.dbt/profiles.yml', 
            source='/home/qurat/repos/weather-data-project/dbt/profiles.yml',
             type='bind'
             ),
             ],

            working_dir='/usr/app',
            network_mode='weather-data-project_my_network',
            docker_url= 'unix://var/run/docker.sock',
            auto_remove= 'success',
    )

    task1 >> task2