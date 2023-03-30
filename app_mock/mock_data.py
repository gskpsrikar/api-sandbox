import pandas as pd


def get_schema(path: str):
    df = pd.read_csv(path, nrows=1)
    schema = df.dtypes.to_dict()

    for key, value in schema.items():
        schema[key] = str(value)

    header_data = {
        'schema': schema
    }
    return header_data


def get_sample_mock_data_record(path: str):
    df = pd.read_csv(path, nrows=1000)
    df = df.sample(n=1).iloc[0]

    return df.to_dict()


def send_mock_data(path: str, target: str, wait_time: int, number_of_records):
    """
    TODO: Things this function should do
    1. Dump the sample data dict as JSON in local folder or S3 Bucket (AWS)
    2. Hit another POST API and send sample data as JSON payload.
    """
    df = pd.read_csv(path)

    while number_of_records > 0:
        sample = df.sample(n=1).iloc[0].to_dict()

        if target is None:
            print(sample.values())
        else:
            pass

        number_of_records -= 1
