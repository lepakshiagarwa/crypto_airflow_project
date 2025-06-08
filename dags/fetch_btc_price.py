from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import csv
import os

def fetch_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    btc_price = data['bitcoin']['usd']
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    os.makedirs('/opt/airflow/data', exist_ok=True)
    with open('/opt/airflow/data/btc_prices.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([now, btc_price])
    print(f"{now} - Bitcoin price is ${btc_price}")

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='fetch_btc_price',
    schedule_interval='@hourly',
    default_args=default_args,
    description='Fetch Bitcoin price and save to CSV',
    tags=['crypto'],
) as dag:
    
    fetch_price = PythonOperator(
        task_id='get_btc_price',
        python_callable=fetch_btc_price,
    )
