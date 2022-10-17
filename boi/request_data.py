import pandas as pd
import requests
from io import StringIO
from requests import Response
from datetime import date

today = date.today()

URL_begin = "https://www.boi.org.il/en/DataAndStatistics/Pages/boi.ashx"



def get_data_frame(seriescode: str = 'RIB_BOI.D',
                   datestart: str = "27/01/1994", dateend: str = today.strftime("%d/%m/%Y")) -> pd.Series:
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
    ldf = pd.read_html(StringIO(resp))
    df = ldf[1]
    df.rename(columns={df.columns[0]: "date"}, inplace=True)
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    df.set_index("date", inplace=True)
    df.index = df.index.to_period(freq='D')
    return df.squeeze()
