# importing libraries

from datetime import timedelta
# The DAG object
from airflow import DAG
# Operators
from airflow.operators.bash_operator import BashOperator
# To make scheduling easy
from airflow.utils.dates import days_ago

# defining DAG arguments

default_args = {
    'owner': 'Madesh',
    'start_date': days_ago(0),
    'email': ['madeshcr.mech@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# defining the tasks

#unzipping data
unzip_data = BashOperator(
    task_id="unzip_data",
    bash_command='sudo tar -zxvf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment',
    dag=dag,
)  

#extracting data from csv
extract_data_from_csv = BashOperator(
    task_id="extract_data_from_csv",
    bash_command='cut -d"," -f1-4 /home/project/airflow/dags/finalassignment/vehicle-data.csv >\
        /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

#extracting data from tsv
extract_data_from_tsv = BashOperator(
    task_id="extract_data_from_tsv",
    bash_command='cut -f 5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv >\
        /home/project/airflow/dags/finalassignment/tsv_data.csv --output-delimiter=","',
    dag=dag,
)

#extracting data from fwf
extract_data_from_fixed_width = BashOperator(
    task_id="extract_data_from_fixed_width",
    bash_command='cut -f 59-61,63-67 /home/project/airflow/dags/finalassignment/payment-data.txt >\
        /home/project/airflow/dags/finalassignment/fixed_width_data.csv --output-delimiter=","',
    dag=dag,
)

#consolidating all data into single file
consolidate_data = BashOperator(
    task_id="consolidate_data",
    bash_command='paste /home/project/airflow/dags/finalassignment/csv_data.csv \
        /home/project/airflow/dags/finalassignment/tsv_data.csv \
            /home/project/airflow/dags/finalassignment/fixed_width_data.csv \
                > /home/project/airflow/dags/finalassignment/extracted_data.csv',
    dag=dag,
)

# transforming the vehicle_type field
transform_data = BashOperator(
    task_id="transform_data",
    bash_command='awk \'BEGIN{FS=","; OFS=","} {print $1,$2,$3,toupper($4),$5,$6,$7,$8,$9}\' \
        /home/project/airflow/dags/finalassignment/extracted_data.csv \
            > /home/project/airflow/dags/finalassignment/staging/transformed_data.csv',
    dag=dag,
)

# task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
