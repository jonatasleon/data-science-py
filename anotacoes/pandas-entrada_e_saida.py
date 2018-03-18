import numpy as np
import pandas as pd
from os import path

# %%
base_dir = '/home/jonatasleon/Workspace/data-science-py/apostilas/2. Python para análise de dados/Pandas'
df = pd.read_csv(path.join(base_dir, 'exemplo'))

# %%
pd.read_excel(path.join(base_dir, 'Exemplo_Excel.xlsx'), sheet_name='Sheet1')


# %%
df = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
type(df)
df[0]
