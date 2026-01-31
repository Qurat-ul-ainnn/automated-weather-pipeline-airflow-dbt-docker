import sys
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

default_args = {
    'description': 'Orchestrator for the weather API',
    'start_date': datetime(2026, 1, 30),
    'catchup':'False',
}

dag = DAG(
    dag_id='weather_dbt-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5),
)

with dag:
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