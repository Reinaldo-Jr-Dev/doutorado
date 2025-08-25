# 🔬 Detalhamento das Propostas de Exploração I

- Projeto: Defects4J.
- Programas: Chart, Lang, Math, Mockito e Time.
- Métricas: ACC@N.
- Heurísticas: ochiai, tarantula, jaccard, op2, barinel e dstar.
- Quantidade mínima de casos de teste: 22.
- Quantidade mínima de casos de teste "+": 11.
- Quantidade mínima de casos de teste "-": 11.

![Resumo geral dos casos de teste da Proposta de Exploração I](img/Tab_1_Proposta_Exploracao_I.png "Resumo geral dos casos de teste da Proposta de Exploração I")

**Figura 1:** Resumo geral dos casos de teste da Proposta de Exploração I

## Descrição dos Experimentos
- e001_original: Execução das heurísticas sem a aplicação de qualquer tipo de balanceamento de dados.
- e002_smote_euclidian: Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância Euclidiana.
- e003_smote_interpolation: Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância Euclidiana. É importante destacar que essa execução foi realizada com o algoritmo original do Smote (sem uso da biblioteca "imblearn.over_sampling").
- e004_smote_jaccard: Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância de Jaccard. É importante destacar que essa execução foi realizada com o algoritmo original do Smote (sem uso da biblioteca "imblearn.over_sampling").
- e005_smote_hamming: Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância de Hamming. É importante destacar que essa execução foi realizada com o algoritmo original do Smote (sem uso da biblioteca "imblearn.over_sampling").
  
## Resultados

![Resultado do Experimento da Proposta de Exploração I](img/Tab_2_Proposta_Exploracao_I.png "Resultado do Experimento da Proposta de Exploração I")

**Figura 2:** Resultado do Experimento da Proposta de Exploração I
