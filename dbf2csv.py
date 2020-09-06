import os
from simpledbf import Dbf5

for file in os.listdir("data"):
        if file.endswith(".dbf"):
                dbf = Dbf5("data/" + file, codec='utf-8')
                dbf.to_csv("data/csv/" + os.path.splitext(file)[0] + ".csv")
                print("data/" + file + " converted to csv")
