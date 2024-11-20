import os
import pandas as pd
from dbfread import DBF

for file in os.listdir("data"):
    if file.endswith(".dbf") and ("*" not in file):
        dbf = DBF(f"data/{file}", load=True, encoding='ISO-8859-1')
        dbf_df = pd.DataFrame(dbf.records)
        dbf_df.to_csv(f"data/csv/{os.path.splitext(file)[0]}.csv")
        print(f"data/{file} converted to csv")
