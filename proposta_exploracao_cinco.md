# 🔬 Detalhamento da Proposta de Exploração V

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Math, Time e Mockito.
- Métricas: pos-fault.
- Heurísticas: Ochiai e Op2.
- Quantidade mínima de casos de teste: 6.
- Quantidade mínima de casos de teste "+": 3.
- Quantidade mínima de casos de teste "-": 3.
- Parametrização do SMOTE:
  - k= Valor mínimo entre quantidade de casos de teste negativos - 2 e 5.

## Descrição dos experimentos
Este experimento propõe uma investigação comparativa sobre a aplicação de diferentes heurísticas (Ochiai e Op2) à matriz de espectro de cobertura, tanto em seu formato original quanto com a aplicação da técnica de balanceamento de dados SMOTE. Os resultados serão avaliados de acordo com a métrica pos-fault (posição do elemento defeituoso). O teste estatístico Wilcoxon Signed-Rank foi aplicado para verificar se os resultados observados no experimento proposto podem ser atribuídos ao acaso ou se evidenciam uma relação significativa entre os valores.

- **e90_original**
  - Execução das heurísticas aplicadas à matriz de espectro de cobertura em seu formato original.
- **e91_smote**
  - Execução das heurísticas aplicadas à matriz de espectro de cobertura em seu formato transformado, por meio da técnica de balanceamento de dados SMOTE. 

![Planilha - Proposta de Exploração V](img/Tab_1_Proposta_Exploracao_V.png)

## Resultados
  - Com base no teste estatístico de Wilcoxon Signed-Rank, verificou-se que, em todos os cenários analisados, o p-value foi superior ao nível de significância adotado (0,05). Dessa forma, conclui-se que não há diferença estatisticamente significativa entre os valores de Pos-Fault obtidos nos experimentos e90_original e e91_smote, considerando os projetos do experimento (Math, Time e Mockito) e as heurísticas Ochiai e Op2.
  - Ao se considerarem as médias de Pos-Fault entre as versões de cada projeto, conclui-se que, para os projetos que utilizaram a heurística Ochiai, o experimento e90_original apresentou os melhores resultados. Em contrapartida, nos projetos que empregaram a heurística Op2, o experimento e91_smote obteve desempenho superior. Logo a baixo, segue o detalhamento desses resultados.
    - Math e Ochiai: o experimento e90_original, obteve melhores resultados.
    - Math e Op2: o experimento e91_smote, obteve melhores resultados.
    - Time e Ochiai: o experimento e90_original, obteve melhores resultados.
    - Time e Op2: o experimento e91_smote, obteve melhores resultados.
    - Mockito e Ochiai: o experimento e90_original, obteve melhores resultados.
    - Mockito e Op2: o experimento e91_smote, obteve melhores resultados.

