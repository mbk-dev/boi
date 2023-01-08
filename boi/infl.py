import pandas as pd
import boi
from datetime import date

today = date.today()


def get_cp(datestart: str = "1900-1-1",
           dateend: str = today.strftime(boi.request_data.format_long)) -> pd.Series:
    s = boi.request_data.get_data_frame(seriescode='CP.CPI.CPI_2_29.MAIN.M.N._Z._Z.I20_L._Z.A._Z',
                                        datestart=datestart, dateend=dateend, freq='M')
    s.rename("CP based on 2020", inplace=True)
    return s


def get_inflation(datestart: str = "1900-1-1",
                  dateend: str = today.strftime(boi.request_data.format_long)) -> pd.Series:
    s = get_cp(datestart, dateend)
    s.rename("Inflation", inplace=True)
    s = s.pct_change().round(4)
    s.dropna(inplace=True)
    return s
