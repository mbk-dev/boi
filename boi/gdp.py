import pandas as pd
import boi
from datetime import date

today = date.today()
url = "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/NA/1.0/"

def get_gdp(datestart: str = "1900-1-1",
            dateend: str = today.strftime(boi.request_data.format_long)) -> pd.Series:
    s = boi.request_data.get_data_frame(url=url,
                                        seriescode='GDP_Q_N.GDP.GDP11.Q.N.V.S1._Z.N_CHN.ILS.N',
                                        datestart=datestart, dateend=dateend, freq='Q')
    s.rename("GDP in Mil NIS", inplace=True)
    return s
