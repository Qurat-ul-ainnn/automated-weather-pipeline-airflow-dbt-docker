# Automated Weather Data Pipeline

**Technologies:** `Airflow` · `dbt` · `Docker` · `PostgreSQL` · `Superset`  

---

## 📌 Project Overview

The **Automated Weather Data Pipeline** is an end-to-end solution for ingesting, transforming, and visualizing weather data using modern data engineering practices.  

The pipeline:

- Extracts real-time and historical weather data from an **external API**  
- Processes and transforms data using a **structured ETL approach**  
- Loads **analytics-ready datasets** into **PostgreSQL**  
- Visualizes tables and insights via **Apache Superset dashboards**  

The workflow is **orchestrated with Apache Airflow**, **containerized using Docker**, and transformed using **dbt**, ensuring it is **scalable, reproducible, and production-ready**.

---

## 🎯 Project Goals

<div align="center">

| Goal | Description |
|------|-------------|
| Reliable ETL | Build an automated pipeline for ingesting and processing weather data |
| Orchestration | Schedule and monitor workflows using Apache Airflow |
| Data Modeling | Transform raw data into structured datasets using dbt |
| Layered Architecture | Maintain raw, staging, and analytics layers |
| Analytics | Enable interactive dashboards via Superset |
| Containerization | Ensure reproducible deployments with Docker |
| Industry Standard | Follow modern data engineering best practices |

</div>

---

## 🏗️ High-Level Architecture

<div align="center">

![Architecture Diagram](https://github.com/Qurat-ul-ainnn/automated-weather-pipeline-airflow-dbt-docker/blob/main/static/Architecture.png?raw=true)

</div>

*Illustrates the end-to-end workflow from data extraction to visualization.*

### Architecture Details

- **Data Source:** Weather Stack API (https://weatherstack.com/) providing real-time and historical weather data.  
- **Orchestration Layer (Apache Airflow):** Manages DAG scheduling and task dependencies, automates extract-load-transform workflows, and handles retries, logging, and monitoring.  
- **Extraction Layer:** Python-based Airflow tasks fetch weather data from the API; raw JSON data is validated and prepared for ingestion.  
- **Loading Layer (PostgreSQL – Raw Zone):** Stores raw weather data without transformations, preserving source-level granularity for traceability.  
- **Transformation Layer (dbt):** Cleans, standardizes, and enriches raw data; applies business logic using dbt models; structures data into staging and analytics-ready fact and dimension tables.  
- **Analytics & Visualization Layer (Superset):** Tables are visualized in Superset dashboards, supporting interactive querying and downstream BI reporting.

---

## 🔄 ETL Workflow Breakdown

<div align="center">

| Step | Description | Key Tasks |
|------|-------------|-----------|
| **Extract** | Fetch data from API on schedule | Validate API responses, log metadata |
| **Load** | Insert raw data into PostgreSQL | Preserve original structure, ensure fault tolerance |
| **Transform** | dbt models clean and structure data | Type casting, null handling, aggregations, produce analytics-ready datasets |

</div>

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|------------|---------|
| ![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white) | Workflow orchestration and scheduling |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Data extraction and pipeline logic |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white) | Central data warehouse |
| ![dbt](https://img.shields.io/badge/dbt-E34F26?style=for-the-badge&logo=dbt&logoColor=white) | Data transformation and modeling |
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) | Containerization and reproducibility |
| ![Superset](https://img.shields.io/badge/Superset-563D7C?style=for-the-badge&logo=apache%20superset&logoColor=white) | Data visualization and dashboards |

</div>

---

## ✨ Airflow DAGs

### 1️⃣ Ingest Data DAG

<div align="center">

![Ingest Data DAG](https://github.com/Qurat-ul-ainnn/automated-weather-pipeline-airflow-dbt-docker/blob/main/static/ingest-data.png?raw=true)
<br><br>
![Ingest Data DAG Logs](https://github.com/Qurat-ul-ainnn/automated-weather-pipeline-airflow-dbt-docker/blob/main/static/ingest-data%20dag%20logs.png?raw=true)

</div>

*This DAG is responsible for fetching weather data from the API, validating it, and loading it into the raw PostgreSQL tables.*

<div align="center">

| Component | Description |
|-----------|-------------|
| **DAG Tasks** | Fetch weather data from API, validate, and load into raw PostgreSQL tables |
| **Logs** | Monitor API responses and ingestion status |
| **Schedule** | Runs at defined intervals for real-time and historical data |

</div>

---

### 2️⃣ Transform Data DAG

<div align="center">

![Transform Data DAG](https://github.com/Qurat-ul-ainnn/automated-weather-pipeline-airflow-dbt-docker/blob/main/static/transform-data-task-DAG.png?raw=true)
<br><br>
![Transform Data DAG Logs](https://github.com/Qurat-ul-ainnn/automated-weather-pipeline-airflow-dbt-docker/blob/main/static/transform%20data%20dag%20logs.png?raw=true)

</div>

*This DAG handles dbt transformations, creating staging and analytics-ready tables from raw weather data.*

<div align="center">

| Component | Description |
|-----------|-------------|
| **DAG Tasks** | Run dbt transformations, create staging and analytics-ready tables |
| **Logs** | Monitor dbt model execution and success/failure |
| **Dependencies** | Ensures models run in the correct order for data consistency |

</div>

---

## 📊 Weather Report Dashboard

<div align="center">

![Weather Report Dashboard](https://github.com/Qurat-ul-ainnn/automated-weather-pipeline-airflow-dbt-docker/blob/main/static/weather%20report%20dashbaord.png?raw=true)

</div>


