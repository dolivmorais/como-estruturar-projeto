from pandas import pandas as pd
from app.pipeline.transform import constact_data_frames
from app.pipeline.extract import extract_from_excel

df1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
df2 = pd.DataFrame({"col1": [5, 6], "col2": [7, 8]})


def test_contact_data_frames():
    result = constact_data_frames([df1, df2])
    assert result.equals(pd.DataFrame({"col1": [1, 2, 5, 6], "col2": [3, 4, 7, 8]}))