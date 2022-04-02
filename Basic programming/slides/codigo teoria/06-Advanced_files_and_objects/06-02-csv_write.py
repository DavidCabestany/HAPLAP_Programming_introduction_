import pandas as pd
from pandas.core.frame import DataFrame
#df = pd.read_csv("example.csv")
rows = []
rows.append(["Hello","world"])
rows.append(["bye"]*2)

df = pd.DataFrame(rows)

df.to_csv("proba1.csv",header=False,index=False)

# try without header=False
# try without index=False
# try index_label index_label="index"