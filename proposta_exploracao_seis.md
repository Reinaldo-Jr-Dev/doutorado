# 🔬 Detalhamento da Proposta de Exploração VI

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Math, Time e Mockito.
- Métricas: pos-fault.
- Heurísticas: Ochiai e Op2.
- Quantidade mínima de casos de teste: 4.
- Quantidade mínima de casos de teste "+": 2.
- Quantidade mínima de casos de teste "-": 2.

## Descrição dos experimentos
Este experimento propõe uma investigação comparativa sobre a aplicação de diferentes heurísticas (Ochiai e Op2) à matriz de espectro de cobertura, tanto em seu formato original quanto com a aplicação da técnica de balanceamento de dados SMOTE. Os resultados serão avaliados de acordo com a métrica pos-fault (posição do elemento defeituoso). O teste estatístico Wilcoxon Signed-Rank e Vargha & Delaney foram aplicados para verificar se os resultados observados no experimento proposto podem ser atribuídos ao acaso ou se evidenciam uma relação significativa entre as variáveis e também identificar a técnica de melhor eficácia.

- **e80_original**
  - Execução das heurísticas aplicadas à matriz de espectro de cobertura em seu formato original.
- **e81_smote**
  - Execução das heurísticas aplicadas à matriz de espectro de cobertura em seu formato transformado, por meio da técnica de balanceamento de dados SMOTE. 

## Resultados dos dados dos experimentos

[Planilha com resultados](https://docs.google.com/spreadsheets/d/e/2PACX-1vQt6L8Z9mk-be_DKJal9ZzuapgrugOYXGz0FqitBYko9ERinjRmeSsUgc85c_INeA/pubhtml?gid=855928177&single=true)

  - Com base no teste estatístico de Wilcoxon Signed-Rank, verificou-se que, em todos os cenários analisados, o p-value foi superior ao nível de significância adotado (0,05). Dessa forma, conclui-se que não há diferença estatisticamente significativa entre os valores de Pos-Fault obtidos nos experimentos e80_original e e81_smote, considerando os projetos do experimento (Math, Time e Mockito) e as heurísticas Ochiai e Op2.
