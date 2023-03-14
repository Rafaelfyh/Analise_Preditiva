# Analise_Preditiva

1 Descreva graficamente os dados disponíveis, apresentando as principais estatísticas descritivas. Comente o porquê da escolha dessas estatísticas.

Resposta para essa questão está comentada posterior aos gráficos apresentados no código.


2 Explique como você faria a previsão do tipo de falha a partir dos dados. Quais variáveis e/ou suas transformações você utilizou e por quê? Qual tipo de problema estamos resolvendo (regressão, classificação)? Qual modelo melhor se aproxima dos dados e quais seus prós e contras? Qual medida de performance do modelo foi escolhida e por quê?

Fiz o tratamento dos dados, escalonamento,  realizei normalização e transformações para melhorar a performance do modelo.
Eu trabalei com a variavel citada na atividade para a previsão do tipo de falha.
Divisão dos dados em treinamento e teste: Eu dividi os dados em conjuntos de treinamento e teste para avaliar a performance do modelo e evitar overfitting
Trabalhei com um modelo no qual teve uma boa avaliação desempenho em acuracia medida smples e direta o modelo ultilizado foi xgboost .
Este é um problema de classificação, pois estamos prevendo a categoria a que um determinado tipo de falha pertence.