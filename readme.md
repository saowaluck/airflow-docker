## How to Setup

Run command following below

- mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
- docker-compose up airflow-init
- docker-compose up
- docker exec -it docker-airflow_airflow-webserver_1 bash
- airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

Launch !!!!!
