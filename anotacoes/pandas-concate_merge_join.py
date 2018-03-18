import numpy as np
import pandas as pd
from pprint import pprint

# %%
col = list('ABCDEFG')
length = len(col)
c_range = range(0, 10)
data = []
for i in c_range:
    d = {}
    for letter in col:
        start = i * length
        counter = range(start, start + length)
        values = list(zip(list(letter * length), counter))
        d[letter] = ['{}{}'.format(*v) for v in values]

    data.append(d)


# %%
data
df1 = {'A': ['A0', 'A1', 'A2', 'A3'],
       'B': ['B0', 'B1', 'B2', 'B3'],
       'C': ['C0', 'C1', 'C2', 'C3'],
       'D': ['D0', 'D1', 'D2', 'D3']}
df1 = pd.DataFrame(df1, index=range(0, 4))

# %%
df2 = {'A': ['A4', 'A5', 'A6', 'A7'],
       'B': ['B4', 'B5', 'B6', 'B7'],
       'C': ['C4', 'C5', 'C6', 'C7'],
       'D': ['D4', 'D5', 'D6', 'D7']}
df2 = pd.DataFrame(df2, index=range(4, 8))

# %%
df3 = {'A': ['A8', 'A9', 'A10', 'A11'],
       'B': ['B8', 'B9', 'B10', 'B11'],
       'C': ['C8', 'C9', 'C10', 'C11'],
       'D': ['D8', 'D9', 'D10', 'D11']}
df3 = pd.DataFrame(df3, index=range(8, 12))

# %%
# Concatenação
pd.concat([df1, df2, df3])[['A']]

df3[~df3.isnull()]
