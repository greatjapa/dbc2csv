import os
from csv import DictWriter
from dbfread import DBF

for file in os.listdir("data"):
    if file.endswith(".dbf") and ("*" not in file):
        dbf = DBF(f"data/{file}")
        count = 0
        try:
            with open(f"data/csv/{os.path.splitext(file)[0]}.csv", 'w') as csvfile:
                for record in dbf:
                    if count == 0:
                        writer = DictWriter(csvfile, fieldnames=record.keys())
                        writer.writeheader()
                    writer.writerow(record)
                    count = count + 1

        except UnicodeDecodeError:
            print(f"data/{file} - [unicodeDecodeError] error to convert row {count}")
        count = 0
        print(f"data/{file} converted to csv")