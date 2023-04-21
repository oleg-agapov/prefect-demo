import argparse
import requests
import pandas as pd

from io import BytesIO
from prefect import flow, task


@task(timeout_seconds=60, retries=1)
def extract(date: str, hour: int) -> pd.DataFrame:
    url = f'http://data.gharchive.org/{date}-{hour}.json.gz'
    print(f'Downloading {url} ...')
    r = requests.get(url)
    df = pd.read_json(BytesIO(r.content), compression='gzip', lines=True)
    return df


@task()
def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['type'] == 'PushEvent']
    df = df[['actor', 'repo', 'created_at']]
    df['created_at'] = pd.to_datetime(df['created_at'])
    return df


@task()
def load(df: pd.DataFrame, path: str) -> None:
    date = df['created_at'].dt.date[0]
    hour = df['created_at'].dt.hour[0]
    df.to_parquet(f'{path}/{date}-{hour}.parquet')


@flow(name='Get raw data from Github archive and save to parquet', log_prints=True)
def github_pipeline(date: str, hour: int) -> None:
    df = extract(date, hour)
    df = transform(df)
    load(df, '/Users/oleg/dev/prefect-demo/data')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', type=str, required=True)
    parser.add_argument('--hour', type=int, required=True)
    args = parser.parse_args()
    github_pipeline(args.date, args.hour)
