# Crypto Market Airflow DAG

This project contains an Apache Airflow DAG that fetches Bitcoin prices from the CoinGecko API every hour and logs them to a CSV file.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

##Run AIRFLOW

```
airflow db init
airflow scheduler
airflow webserver
```

## DAG

fetch_btc_price: Gets Bitcoin price and appends to data/btc_prices.csv
