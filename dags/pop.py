import datetime

from airflow.models import DAG
from airflow.operators.bash import BashOperator


dag = DAG(
    dag_id='popppppppp',
    default_args={'start_date': datetime.datetime(2021, 1, 1)},
    schedule_interval='*/5 * * * *',
    catchup=False,
)

t1 = BashOperator(
    task_id='first_task',
    bash_command='echo "first task"',
    dag=dag
)

t2 = BashOperator(
    task_id='second_task',
    bash_command='echo "second task"',
    dag=dag
)

t1 >> t2
