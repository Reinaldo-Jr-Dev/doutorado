 # 🔬 Detalhamento da Proposta de Exploração II

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Chart, Lang, Math, Mockito e Time.
- Métricas: ???.
- Heurísticas: ochiai, tarantula, jaccard, op2, barinel e dstar.
- Quantidade mínima de casos de teste: ??.
- Quantidade mínima de casos de teste "+": ??.
- Quantidade mínima de casos de teste "-": ??.

![Resumo geral dos casos de teste](img/Tab_1_Proposta_Exploracao_I.png "Resumo geral dos casos de teste")

**Figura 1:** Resumo geral dos casos de teste

![Resumo geral dos casos de teste negativos](img/Tab_Resumo_Casos_Teste_Negativos.png "Resumo geral dos casos de teste negativos")

**Figura 2:** Resumo geral dos casos de teste negativos

## Descrição dos Experimentos
- **e001_original**
  - Execução das heurísticas sem a aplicação de qualquer tipo de balanceamento de dados.
- **e002_smote_euclidian**
  - Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância Euclidiana. É importante destacar que essa execução foi realizada com o uso da biblioteca "imblearn.over_sampling".
