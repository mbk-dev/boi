import pandas as pd
import boi
from datetime import date

today = date.today()


def get_cpi(date_start: str = "1900-1-1",
            date_end: str = today.strftime(boi.request_data.format_long)
            ) -> pd.Series:
    """
    Get Total Consumer Price Index (CPI).

    CPI 2020 is 100%.
    """
    url_cpi = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/PRI/1.0/"
    s = boi.request_data.get_data_frame(
        url=url_cpi,
        seriescode='CP.CPI.CPI_2_29.MAIN.M.N._Z._Z.I22_L._Z.A._Z._Z',
        datestart=date_start,
        dateend=date_end,
        freq='M')
    s.rename("CPI_2020", inplace=True)
    return s


def get_inflation(date_start: str = "1900-1-1",
                  date_end: str = today.strftime(boi.request_data.format_long)
                  ) -> pd.Series:
    s = get_cpi(date_start, date_end)
    s.rename("Inflation", inplace=True)
    s = s.pct_change().round(4)
    s.dropna(inplace=True)
    return s
