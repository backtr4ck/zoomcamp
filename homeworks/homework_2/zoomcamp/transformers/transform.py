if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    import pandas as pd
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    def camel_to_snake(column_name):
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    data['lpep_pickup_date'] = pd.to_datetime(data.lpep_pickup_datetime).dt.date
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
