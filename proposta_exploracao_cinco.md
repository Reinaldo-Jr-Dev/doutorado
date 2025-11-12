# 🔬 Detalhamento da Proposta de Exploração V

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Math.
- Métricas: pos-fault.
- Heurísticas: Ochiai e Op2.
- Quantidade mínima de casos de teste: 6.
- Quantidade mínima de casos de teste "+": 3.
- Quantidade mínima de casos de teste "-": 3.
- Parametrização do SMOTE:
  - k= Valor mínimo entre quantidade de casos de teste negativos - 2 e 5.

## Descrição dos experimentos
Este experimento propõe uma investigação comparativa sobre a aplicação de diferentes heurísticas (Ochiai e Op2) à matriz de espectro de dados, tanto em seu formato original quanto com a aplicação da técnica de balanceamento de dados SMOTE. Os resultados serão avaliados de acordo com a métrica pos-fault (posição do elemento defeituoso).

- **e90_original**
  - Execução das heurísticas aplicadas à matriz de especrtro em seu formato original.
- **e91_smote**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de balanceamento de dados SMOTE. 

![Planilha - Proposta de Exploração V](img/Tab_1_Proposta_Exploracao_V.png)
