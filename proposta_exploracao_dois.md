 # 🔬 Detalhamento da Proposta de Exploração II

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Chart, Lang, Math, Mockito e Time.
- Métricas: ???.
- Heurísticas: ochiai, tarantula, jaccard, op2, barinel e dstar.
- Quantidade mínima de casos de teste: ??.
- Quantidade mínima de casos de teste "+": ??.
- Quantidade mínima de casos de teste "-": ??.

![Total de Testes Repetidos](img/Tab_1_Proposta_Exploracao_II.png "Total de Testes Repetidos")

**Figura 1:** Total de Testes Repetidos (mesma cobertura)

## Descrição dos Experimentos
- **e002_smote_euclidian**
  - Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância Euclidiana. É importante destacar que essa execução foi realizada com o uso da biblioteca "imblearn.over_sampling". Essa execução, foi realizada na matriz de espectro em seu formato original.
- **e007_smote_euclidian_unique_rows**
  - A execução das heurísticas foi conduzida com a aplicação da técnica de balanceamento de dados SMOTE, empregando o cálculo de distância Euclidiana. Este procedimento utilizou a biblioteca imblearn.over_sampling e foi realizado sobre a matriz de espectro em um formato pré-processado, caracterizado pela eliminação de ruídos provenientes de linhas coincidentes.
- **e008_smote_euclidian_unique_rows_coverage**
  - A execução das heurísticas foi conduzida com a aplicação da técnica de balanceamento de dados SMOTE, empregando o cálculo de distância Euclidiana. Este procedimento utilizou a biblioteca imblearn.over_sampling e foi realizado sobre a matriz de espectro em um formato pré-processado, no qual foram eliminados ruídos provenientes de linhas que, além de coincidentes (ou seja, de mesma cobertura), apresentavam resultados distintos ('+' e '-').
