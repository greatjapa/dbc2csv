import os
from simpledbf import Dbf5

for file in os.listdir("data"):
        if file.endswith(".dbf") and ("*" not in file):
                dbf = Dbf5(f"data/{file}", codec='ISO-8859-1')
                dbf.to_csv(f"data/csv/{os.path.splitext(file)[0]}.csv")
                print(f"data/{file} converted to csv")