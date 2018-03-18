import numpy as np
import pandas as pd

# %%
np.random.seed(101)

# %%
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

# %%
random = np.random.randn(6, 2)
df = pd.DataFrame(random, index=hier_index, columns='A B'.split())

# %%
df

# %%
df.index.names = ['Grupo', 'Número']

# %%
df.loc['G1'].iloc[0]

# %%
df.xs(1, level='Número')
