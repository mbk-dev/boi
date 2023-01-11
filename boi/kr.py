import pandas as pd
import boi
from datetime import date


url = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/BR/1.0/"

def get_ir(start_date: pd.Timestamp = pd.Timestamp(1900, 1, 1),
           end_date: pd.Timestamp = pd.Timestamp.today()) -> pd.Series:

    s = boi.request_data.get_data_frame(url=url, seriescode='MNT_RIB_BOI_D.D.RIB_BOI',
                                        datestart=start_date.strftime(boi.request_data.format_long),
                                        dateend=end_date.strftime(boi.request_data.format_long),
                                        freq='D')
    s.rename("key_rate", inplace=True)
    return s / 100
