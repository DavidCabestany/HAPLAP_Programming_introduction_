import pandas as pd

df = pd.read_csv("example.csv",header=None)
for index,row in df.iterrows():
    print(index,row[0],row[1])
print("-----------types--------------")
df = pd.read_csv("example.csv",header=None)
for index,row in df.iterrows():
    print(index,type(row[0]),type(row[1]))

print("-----------content with header--------------")
df = pd.read_csv("example.csv")
for index,row in df.iterrows():
    print(index,row[0],row[1])

print("-----------types with header--------------")
df = pd.read_csv("example.csv")
for index,row in df.iterrows():
    print(index,type(row[0]),type(row[1]))

print("-----------content with header name--------------")
df = pd.read_csv("example.csv")
for index,row in df.iterrows():
    print(index,row["name"],row["age"])