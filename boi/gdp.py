import pandas as pd
import boi
from datetime import date

import boi.settings

today = date.today()
url = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/NA/1.0/"

def get_gdp(date_start: str = "1900-1-1",
            date_end: str = today.strftime(boi.settings.format_long)) -> pd.Series:
    s = boi.request_data.get_data(url=url,
                                  series_code='GDP_Q_N.GDP.GDP11.Q.N.V.S1._Z.N_CHN.ILS.N',
                                  date_start=date_start,
                                  date_end=date_end,
                                  freq='Q')
    s.rename("GDP in Mil NIS", inplace=True)
    return s
