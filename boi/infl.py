import pandas as pd
import boi
from datetime import date

today = date.today()


def get_cp(datestart: str = "01/01/1951", dateend: str = today.strftime("%d/%m/%Y")) -> pd.Series:
    s = boi.request_data.get_data_frame(seriescode='CP', datestart=datestart, dateend=dateend, freq='M')
    s.rename("CP based on 2020", inplace=True)
    s = s.pct_change().round(4)
    s.dropna(inplace=True)
    return s
