import pandas as pd
import os
import glob
import openpyxl
from pathlib import Path
from typing_extensions import List

'''
função para ler os arquivos de uma pasta de imput uma lista de dataframes
args:
    path: caminho da pasta com os arquivos
returns:
    list: lista com os dataframes lidos
'''
def extract_from_excel(path: str) -> List[pd.DataFrame]:
    folder = Path(path)
    all_files = folder.glob("*.xlsx")

    data_frame_list = [pd.read_excel(f) for f in all_files]
    return data_frame_list

if __name__ == "__main__":
    print(extract_from_excel("data/input"))