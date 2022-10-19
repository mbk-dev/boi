import pandas as pd
import boi
from datetime import date

today = date.today()


def get_gdp(datestart: str = "27/01/1963", dateend: str = today.strftime("%d/%m/%Y")) -> pd.Series:
    s = boi.request_data.get_data_frame(seriescode='CHAINED.GDP.Q_N', datestart=datestart, dateend=dateend, freq='Q')
    s.rename("GDP in Mil NIS", inplace=True)
    return s
