# coding: utf-8
# %%
import numpy as np
import pandas as pd

# %%
labels = ['a', 'b', 'c']

# %%
minha_lista = [10, 20, 30]
arr = np.array([10, 20, 30])
d = dict(a=10, b=20, c=30)

# %%
series = pd.Series(minha_lista)

# %%
series = pd.Series(arr, labels)

# %%
pd.Series([sum, print, len])

# %%
ser1 = pd.Series(np.linspace(1, 4, 4), ['EUA', 'Alemana', 'URSS', 'Japão'])
ser2 = pd.Series(np.linspace(1, 4, 4), ['Alemana', 'EUA', 'Itália', 'Japão'])

# %%
print(ser1)
print(ser2)

ser1 + ser2
