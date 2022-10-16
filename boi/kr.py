import pandas as pd
import boi
def get_ir() -> pd.Series:
    df = boi.request_data.get_data_frame()
    return df

