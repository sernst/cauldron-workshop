import cauldron as cd
import pandas as pd
import requests
import io
import string

url_prefix = 'https://s3-us-west-2.amazonaws.com/cauldron-workshop/data'


def pull_data_file(filename: str) -> pd.DataFrame:
    """
    Downloads the CSV data file with the specified name from S3 and returns
    a DataFrame with the loaded contents of that file.

    :param filename:
        The name of the file to pull without extension.
    :return
        A DataFrame containing the downloaded contents of the source CSV file.
    """

    response = requests.get('{}/{}.csv'.format(url_prefix, filename))
    buffer = io.StringIO(response.text)
    return pd.read_csv(buffer)


data_frames = [
    pull_data_file(character)
    for character in string.ascii_lowercase
]

df: pd.DataFrame = pd.concat(data_frames)
cd.display.table(df.head(20))

cd.shared.df = df
