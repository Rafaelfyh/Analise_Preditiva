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


# Gráfico de barras: 'Type x Total Failure_Type'
# Crie um objeto de figura com um tamanho de 12 polegadas de largura e 8 polegadas de altura
# Gráfico de barras do número de ocorrência "tipo" nos dados "base_treino", 
# agrupar os dados da coluna "type" da "base_treino",
# Em seguida, conta o número de ocorrências de cada "tipo" pelo método count, 
# Sendo o resultado armazenado em uma variável chamada tipos_falha
# Por fim, o gráfico de barras é gerado usando o método plot. 

plt.figure(figsize = (12, 8))
tipos_falha = base_treino.groupby('type').count()['failure_type'].sort_values(ascending=False)
tipos_falha.plot(kind = 'bar', color = '#F06043')
plt.title('Type x Total Failure_Type', fontsize=20)
plt.xlabel('Type', fontsize=12)
plt.ylabel('Quantity', fontsize=12)
plt.xticks(rotation = 0)
plt.show()

Este gráfico apresenta a quantidade de falhas agrupadas por tipo de ferramenta. É possível verificar qual tipo de ferramenta apresenta a maior quantidade de falhas, sendo assim me permiti identificar possíveis pontos críticos no processo e a necessidade de melhorias.

A escolha dessas estatísticas descritivas permite uma análise mais visual da distribuição das falhas por tipo de ferramenta, fornecendo uma base para a tomada de decisão quanto ao uso dessas ferramentas e o que pode ser possível para a minimização das falhas.

# Gráfico de barras: 'Type x Total Failure_Type'
# Cria um objeto de figura no Matplotlib,
# Método groupby, conta numero de cada tipo falha usando count, 
# o resultados e classificado em ordem decrescente com sort values,
# Gerar grafico númerico de cada tipo falha
# definindo x  para type e y para Quantity
# exibir o grafico

plt.figure(figsize = (12, 8))
tipos_falha = base_treino.groupby('failure_type').count()['tool_wear_min'].sort_values(ascending=False)
tipos_falha.plot(kind = 'bar', color = '#F06043')
plt.title('Failure Type x Tool Wear Min', fontsize=20)
plt.xlabel('Type', fontsize=12)
plt.ylabel('Quantity', fontsize=12)
plt.xticks(rotation = 0)
plt.show()

Este gráfico de barras mostra a quantidade de cada tipo de falha na variável "tool_wear_min". Foi ultilizado para visualizar qual é o tipo de falha mais frequente, permitindo uma análise mais aprofundada da variável e possibilitando uma tomada de decisão mais informada.

# Filtro aplicado com base_treino para encontrar todos os labels contendo falha, 
# Removendo apenas equipamentos sem falha
base_treino = base_treino[base_treino['failure_type'] != 'No Failure']
base_treino

# Resetando Index após excluír diversos registros
base_treino = base_treino.reset_index(drop = True)
base_treino


# Gráfico de barras: 'Type x Total Failure_Type'
plt.figure(figsize = (12, 8))
tipos_falha = base_treino.groupby('failure_type').count()['tool_wear_min'].sort_values(ascending=False)
tipos_falha.plot(kind = 'bar', color = '#F06043')
plt.title('Failure Type x Tool Wear Min', fontsize=20)
plt.xlabel('Type', fontsize=12)
plt.ylabel('Quantity', fontsize=12)
plt.xticks(rotation = 0)
plt.show()











