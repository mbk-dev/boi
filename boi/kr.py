import pandas as pd
import boi
def get_ir() -> pd.Series:
    return boi.request_data.get_data_frame()

