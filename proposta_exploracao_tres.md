# 🔬 Detalhamento da Proposta de Exploração III

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Chart, Lang, Math, Mockito e Time.
- Métricas: MFR (Mean First Rank), ACC@10 e ACC_RAW@10.
- Heurísticas: ochiai, tarantula, jaccard, op2, barinel e dstar.
- Quantidade mínima de casos de teste: 8.
- Quantidade mínima de casos de teste "+": 4.
- Quantidade mínima de casos de teste "-": 4.

## Descrição dos Experimentos
- **e100_smote_original**
  - Execução das heurísticas aplicadas à matriz de espectro com a técnica de balanceamento de dados SMOTE em sua forma original.
- **e101_smote_changed**
  - Execução das heurísticas aplicadas à matriz de espectro com a técnica de balanceamento de dados SMOTE, porém com uma modificação no algoritmo responsável pela geração de novos vizinhos, de modo a produzir instâncias com maior cobertura — isto é, com maior incidência de valores “1” nas colunas da matriz.
