import pandas as pd
import boi
from datetime import date

import boi.settings

today = date.today()
url = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/BR/1.0/"

def get_ir(date_start: str = "1900-1-1",
           date_end: str = today.strftime(boi.settings.format_long)) -> pd.Series:
    s = boi.request_data.get_data(url=url,
                                  series_code='MNT_RIB_BOI_D.D.RIB_BOI',
                                  date_start=date_start,
                                  date_end=date_end,
                                  freq='D')
    s.rename("key_rate", inplace=True)
    return s / 100
