# -*- coding: utf-8 -*-
# %%
import numpy as np
import pandas as pd

# %%
# Define um seed para geração de dados aleatórios
np.random.seed(101)

# %%
# Cria um nobo DataFrame com 5 linhas e 4 colunas
df = pd.DataFrame(np.random.randn(5, 4),
                  index='A B C D E'.split(), columns='W X Y Z'.split())
df

# %%
# Seleciona as colunas W e Y
df[['W', 'Y']]

# %%
# Cria uma nova coluna chamada 'new' com o valores da soma entre as colunas W e Y
df['new'] = df['W'] + df['X']
df
df[['W', 'X', 'new']]

# %%
# Remove a coluna 'new'
# Detalhe ao paramêtro **inplace**
df.drop('new', axis=1, inplace=True)
df

# %%
# LOCaliza os valores correspondentes as linhas A e C e as colunas W e Y
df.loc[['A', 'C'], ['W', 'Y']]

# %%
# Realiza uma locaização dos valores baseados na indexação numérica (assim como se faz no numpy)
df.iloc[1:4, 1:3]


# %%
bol = df > 0
df[bol]

# %%
df[df['W'] > 0][['Y']]

# %%
df[df['W'] > 0 & df['Y'] > 1]
