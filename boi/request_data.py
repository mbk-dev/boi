import pandas as pd
import requests
from io import StringIO
from requests import Response
from datetime import date

format_long = "%Y-%m-%d"
format_short = '%Y-%m'

today = date.today()

URL_begin = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/PRI/1.0/"


def get_data_frame(url: str = URL_begin,
                   seriescode: str = 'RIB_BOI.D',
                   datestart: str = "1900-1-1",
                   dateend: str = today.strftime(format_long),
                   freq: str = 'D') -> pd.Series:
    request_url = url + seriescode
    params = {'c[TIME_PERIOD]': f'ge:{datestart}+le:{dateend}'}
    abc: Response = requests.get(request_url, params=params)
    resp = abc.text

    ldf = pd.read_xml(StringIO(resp), xpath="//Obs")
    df = ldf
    df.rename(columns={df.columns[0]: "date"}, inplace=True)
    if freq != 'Q':
        df['date'] = pd.to_datetime(df['date'], format=format_short)
        df.set_index("date", inplace=True)
        df.index = df.index.to_period(freq=freq)
    else:
        df.set_index("date", inplace=True)
        df.sort_index(ascending=True, inplace=True)
    return df.squeeze()
