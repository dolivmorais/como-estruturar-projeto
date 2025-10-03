import pandas as pd
from typing_extensions import List

"""
função para transformar uma lista de dataframes em um unico dataframe
"""

def constact_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list)