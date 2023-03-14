import plotly

# Importando bibliotecas
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Armazendo dataset na variável
base_treino = pd.read_csv('desafio_manutencao_preditiva_treino.csv')

# Visualizando dataframe
base_treino

# Cabeçalho dataframe
base_treino.head()

# Rodapé dataframe
base_treino.tail()

# Verificando dimensão dos dados
base_treino.shape

# Informações dos dados
base_treino.info

# Verificando dados estatísticos descritivos
base_treino.describe()

# Tipagem dos dados
base_treino.dtypes

# Consulta e soma de valores missing por variável
base_treino.isnull().sum()

### **Visualização dos Dados**

# Contagem de valores únicos e contagem dos registros
np.unique(base_treino['failure_type'], return_counts=True)


# Contando valores: 'failure_type'
base_treino['failure_type'].value_counts()
