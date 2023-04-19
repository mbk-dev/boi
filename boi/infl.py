import pandas as pd
import boi
from datetime import date

import boi.settings

today = date.today()


def get_cpi(date_start: str = "1951-10-01",
            date_end: str = today.strftime(boi.settings.format_long)
            ) -> pd.Series:
    """
    Get Total Consumer Price Index (CPI).

    CPI 2020 is 100%.

    old code: 'CP.CPI.CPI_2_29.MAIN.M.N._Z._Z.I22_L._Z.A._Z._Z'
               CP_PCH.CPI.CPI_2_29.MAIN.M.N._Z._Z.PT._Z.A.G1._Z
    """
    url_cpi = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/PRI/1.0/"
    s = boi.request_data.get_data(
        url=url_cpi,
        series_code='CP.CPI.CPI_2_29.MAIN.M.N._Z._Z.I22_L._Z.A._Z._Z.CP',
        date_start=date_start,
        date_end=date_end,
        freq='M')
    s.rename("CPI_2020", inplace=True)
    return s


def get_inflation(date_start: str = "1951-10-01",
                  date_end: str = today.strftime(boi.settings.format_long)
                  ) -> pd.Series:
    s = get_cpi(date_start, date_end)
    s.rename("Inflation", inplace=True)
    s = s.pct_change().round(4)
    s.dropna(inplace=True)
    return s
