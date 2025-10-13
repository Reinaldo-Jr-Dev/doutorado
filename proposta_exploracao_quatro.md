# 🔬 Detalhamento da Proposta de Exploração IV

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Chart, Lang, Math, Mockito e Time.
- Métricas: MFR (Mean First Rank), ACC@10 e ACC_RAW@10.
- Heurísticas: ochiai, tarantula, jaccard, op2, barinel e dstar.
- Quantidade mínima de casos de teste: 8.
- Quantidade mínima de casos de teste "+": 4.
- Quantidade mínima de casos de teste "-": 4.
- Parametrização do SMOTE:
  - k= Valor mínimo entre quantidade de casos de teste negativos - 2 e 5.

## Descrição dos Experimentos
- **e200_original**
  - Execução das heurísticas aplicadas à matriz de especrtro em seu formato original.
- **e201_smote_euclidian_NR4**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS4 – Noise Reduction Scheme 4). 
- **e202_smote_euclidian_NR5**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS5 – Noise Reduction Scheme 4). 
- **e203_smote_euclidian_NR7**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS7 – Noise Reduction Scheme 4). 
- **e204_smote_euclidian_NR4_smote**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS4 – Noise Reduction Scheme 4) e posteriormente, execução da técnica de balancamento Smote. 
- **e205_smote_euclidian_NR5_smote**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS5 – Noise Reduction Scheme 5) e posteriormente, execução da técnica de balancamento Smote. 
- **e206_smote_euclidian_NR7_smote**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS7 – Noise Reduction Scheme 7) e posteriormente, execução da técnica de balancamento Smote. 

Foram selecionadas apenas as técnicas de eliminação de ruídos NRS4, NRS5 e NRS7, uma vez que essas apresentaram os melhores resultados no artigo de referência utilizado na pesquisa de referência dessa exploração.
