import numpy as np
import pandas as pd

# %%
data = dict(
    Empresa=['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    Nome=['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    Venda=[200, 120, 340, 124, 243, 350],
)

# %%
df = pd.DataFrame(data)

# %%
group = df.groupby('Empresa')
group.mean()
group.describe()
group.count()

# %%
group = df.groupby('Nome')
group.mean()
group.describe()
group.count()
