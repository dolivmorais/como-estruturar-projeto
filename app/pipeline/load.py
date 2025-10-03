import pandas as pd

"""
recebe um dataframe e salva em um arquivo excel
"""

def save_to_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso!"
