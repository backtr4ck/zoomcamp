import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import gzip

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    data = pd.DataFrame()
    for year in [19,20,21]:
        for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
            try:
                url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_20{year}-{month}.csv.gz'
                response = requests.get(url)
                content = io.BytesIO(response.content)
                with gzip.open(content, 'rt', encoding='utf-8') as f:
                    _data = pd.read_csv(f, low_memory=False)
                    data = pd.concat([data, _data])
                    print(f"done {year}-{month}")
            except:
                pass
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
