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
  - A execução das heurísticas foi realizada com a aplicação da técnica de balanceamento de dados SMOTE, adotando como métrica de proximidade a distância Euclidiana. Ressalta-se que tal implementação foi conduzida por meio da biblioteca imblearn.over_sampling. Ademais, o procedimento foi aplicado diretamente sobre a matriz de espectro em sua forma original.
- **e007_smote_euclidian_unique_rows**
  - A execução das heurísticas foi realizada por meio da aplicação da técnica de balanceamento de dados SMOTE, utilizando a distância Euclidiana como métrica de proximidade. O procedimento foi implementado com o suporte da biblioteca imblearn.over_sampling e aplicado à matriz de espectro em um formato pré-processado, no qual foram eliminados ruídos decorrentes de linhas coincidentes.
- **e008_smote_euclidian_unique_rows_coverage**
  - A execução das heurísticas foi conduzida mediante a aplicação da técnica de balanceamento de dados SMOTE, adotando a distância Euclidiana como métrica de similaridade. O procedimento foi implementado com o auxílio da biblioteca imblearn.over_sampling e aplicado sobre a matriz de espectro em um formato previamente pré-processado, no qual foram eliminados ruídos oriundos de linhas que, além de apresentarem cobertura coincidente, exibiam resultados distintos ('+' e '-').
