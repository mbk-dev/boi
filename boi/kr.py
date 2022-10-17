import pandas as pd
import boi


def get_ir(datestart: str = "27/01/1994", dateend: str = '13/10/2022') -> pd.Series:
    s = boi.request_data.get_data_frame(seriescode='RIB_BOI.D', datestart=datestart, dateend=dateend)
    s.rename("key_rate", inplace=True)
    return s / 100

