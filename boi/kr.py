import pandas as pd
import boi
from datetime import date

today = date.today()
url = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/BR/1.0/"

def get_ir(datestart: str = "1900-1-1",
           dateend: str = today.strftime(boi.request_data.format_long)) -> pd.Series:
    s = boi.request_data.get_data_frame(url=url, seriescode='MNT_RIB_BOI_D.D.RIB_BOI',
                                        datestart=datestart, dateend=dateend, freq='D')
    s.rename("key_rate", inplace=True)
    return s / 100
