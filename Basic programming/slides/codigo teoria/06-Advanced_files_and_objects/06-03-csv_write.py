import pandas as pd

df = pd.read_csv("example.csv")

new_row = {"name":"Olatz","age":34}

df = df.append(new_row,ignore_index=True)

df.to_csv("proba2.csv")

# try without index index=False
# try index_label index_label="index"
# try separation sep=":"
# try a subset (columns)columns=["name"]
#...