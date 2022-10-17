import pandas as pd
import requests
from io import StringIO

from requests import Response

URL_begin = "https://www.boi.org.il/en/DataAndStatistics/Pages/boi.ashx"


def get_data_frame(seriescode: str = 'RIB_BOI.D',
                   datestart: str = "27/01/1994", dateend: str = '13/10/2022') -> pd.Series:
    request_url = URL_begin
    params = {'Command': 'DownloadSeriesExcel',
              'SeriesCode': seriescode,
              'DateStart': datestart,
              'DateEnd': dateend,
              'Level': '3',
              'Sid': '22'
              }
    abc: Response = requests.get(request_url, params=params)
    resp = abc.text
    ldf = pd.read_html(StringIO(resp), parse_dates=[0])
    df = ldf[1]
    df.rename(columns={df.columns[0]: "date"}, inplace=True)
    df.set_index("date", inplace=True)
    df.index = df.index.to_period(freq='D')
    return df.squeeze()
