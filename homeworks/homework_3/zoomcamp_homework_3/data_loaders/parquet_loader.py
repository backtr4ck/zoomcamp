import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    data = pd.DataFrame()
    for i in range(12):
        if i+1 < 10:
            url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-0{i+1}.parquet'
            _data = pd.read_parquet(url)
            data = pd.concat([data, _data])
        else:
            url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{i+1}.parquet'
            _data = pd.read_parquet(url)
            data = pd.concat([data, _data])

    data.lpep_pickup_datetime = pd.to_datetime(data.lpep_pickup_datetime)
    data['lpep_pickup_date'] = data.lpep_pickup_datetime.dt.date
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
