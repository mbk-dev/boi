import pandas as pd
import boi
from datetime import date

today = date.today()


def get_ir(datestart: str = "27/01/1994", dateend: str = today.strftime("%d/%m/%Y")) -> pd.Series:
    s = boi.request_data.get_data_frame(seriescode='RIB_BOI.D', datestart=datestart, dateend=dateend, freq='D')
    s.rename("key_rate", inplace=True)
    return s / 100
