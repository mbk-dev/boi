import urllib.parse
from io import StringIO
from datetime import date

import pandas as pd
import requests
from requests import Response
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

from boi.settings import format_long, format_short

today = date.today()

BASE_URL = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/PRI/1.0/"


def get_data(url: str = BASE_URL,
             series_code: str = 'RIB_BOI.D',
             date_start: str = "1900-1-1",
             date_end: str = today.strftime(format_long),
             freq: str = 'D') -> pd.Series:
    request_url = url + series_code
    date_parameter = urllib.parse.unquote('c%5BTIME_PERIOD%5D')
    params = {date_parameter: f'ge:{date_start}+le:{date_end}'}
    # Prepare the HTTP request
    session = requests.session()
    retry_strategy = Retry(
        total=3, backoff_factor=0.1, status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)

    try:
        abc: Response = requests.get(request_url, params=params)
        abc.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise requests.exceptions.HTTPError(
            f"HTTP error fetching data for {series_code}:",
            abc.status_code,
            abc.reason,
            BASE_URL,
        ) from err
    resp = abc.text

    df = pd.read_xml(StringIO(resp), xpath="//Obs")
    df.rename(columns={df.columns[0]: "date"}, inplace=True)
    if freq != 'Q':
        df['date'] = pd.to_datetime(df['date'], format=format_short)
        df.set_index("date", inplace=True)
        df.index = df.index.to_period(freq=freq)
    else:
        df.set_index("date", inplace=True)
        df.sort_index(ascending=True, inplace=True)
    return df.squeeze()
