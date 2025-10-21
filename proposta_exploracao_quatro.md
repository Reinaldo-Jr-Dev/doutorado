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

## Descrição dos experimentos
Esse experimento propõe uma investigação comparativa sobre a aplicação de diferentes heurísticas (Ochiai, Tarantula, Jaccard, Op2, Barinel e DStar) na matriz de espectro de dados em seu formato original com a eliminação de ruídos, de acordo com as seguintes técnicas: NRS1, NRS2, NRS3, NRS4, NRS5, NRS6 e NRS7. Após isso, será avaliado também, o impacto da eliminação dos ruídos juntamente com a aplicação da técnica de balanceamento de dados SMOTE. Esses resultados serão medidos, de acordo com as métricas MFR (Mean First Rank), ACC@10 e ACC_RAW@10. Vale ressaltar que, no artigo de referência dessas técnicas de eliminação de ruídos, foi utilizada apenas a métrica EXAM.

- **e200_original**
  - Execução das heurísticas aplicadas à matriz de especrtro em seu formato original.
- **e201_original_NRS1**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS1 – Noise Reduction Scheme 1). 
- **e202_original_NRS2**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS2 – Noise Reduction Scheme 2). 
- **e203_original_NRS3**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS3 – Noise Reduction Scheme 3). 
- **e204_original_NRS4**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS4 – Noise Reduction Scheme 4). 
- **e205_original_NRS5**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS5 – Noise Reduction Scheme 5). 
- **e206_original_NRS6**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS6 – Noise Reduction Scheme 6). 
- **e207_original_NRS7**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS7 – Noise Reduction Scheme 7). 
- **e208_NRS1_smote_euclidian**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS1 – Noise Reduction Scheme 1) e posteriormente aplicação da técnica de balanceamento de dados Smote. 
- **e209_NRS2_smote_euclidian**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS2 – Noise Reduction Scheme 2) e posteriormente aplicação da técnica de balanceamento de dados Smote. 
- **e210_NRS3_smote_euclidian**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS3 – Noise Reduction Scheme 3) e posteriormente aplicação da técnica de balanceamento de dados Smote. 
- **e211_NRS4_smote_euclidian**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS4 – Noise Reduction Scheme 4) e posteriormente aplicação da técnica de balanceamento de dados Smote. 
- **e212_NRS5_smote_euclidian**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS5 – Noise Reduction Scheme 5) e posteriormente aplicação da técnica de balanceamento de dados Smote. 
- **e213_NRS6_smote_euclidian**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS6 – Noise Reduction Scheme 6) e posteriormente aplicação da técnica de balanceamento de dados Smote. 
- **e214_NRS7_smote_euclidian**
  - Execução das heurísticas aplicadas à matriz de espectro em seu formato transformado, por meio da técnica de eliminação de ruídos (NRS7 – Noise Reduction Scheme 7) e posteriormente aplicação da técnica de balanceamento de dados Smote.
 
 ## Análise Estrutural dos dados dos experimentos
  [Planilha com resultados da análise estrutural](https://docs.google.com/spreadsheets/d/e/2PACX-1vRxBhUWZfG_yJoFMpFyRFnhXbK-mqb16q55vAimD5zcNqWa0mhV8cuCYlT5bvuidQ/pubhtml?gid=1774065543&single=true)

 ## Resultado dos dados dos experimentos
 [Planilha com resultados](https://docs.google.com/spreadsheets/d/e/2PACX-1vRxBhUWZfG_yJoFMpFyRFnhXbK-mqb16q55vAimD5zcNqWa0mhV8cuCYlT5bvuidQ/pubhtml?gid=727601908&single=true)

Análise por projeto, considerando a métrica MFR
  - Chart
    - Ao comparar o experimento e200_original com os demais, observa-se que, em todas as heurísticas, os outros experimentos apresentaram resultados superiores. Destaca-se o experimento e203_original_NRS3, que obteve melhor desempenho em metade das heurísticas analisadas (Ochiai, Tarantula e Jaccard).
  - Math
    - Ao comparar o experimento e200_original com os demais, observa-se que, em todas as heurísticas, o experimento e200_original apresentou resultados superiores.
  - Time
    - Ao comparar o experimento e200_original com os demais, observa-se que, em todas as heurísticas, os outros experimentos apresentaram resultados superiores. Destaca-se o experimento e203_original_NRS3, que obteve melhor desempenho em metade das heurísticas analisadas (Ochiai, Jaccard e DStar).
  - Lang
    - Ao comparar o experimento e200_original com os demais, observa-se que, em todas as heurísticas, o experimento e200_original apresentou resultados superiores, exceto para as heurísticas Tarantula e Barinel.
  - Mockito
    - Ao comparar o experimento e200_original com os demais, observa-se que, em todas as heurísticas, os outros experimentos apresentaram resultados superiores, exceto a heurística OP2. Destaca-se o experimento e202_original_NRS2, que obteve melhor desempenho em todas as heurísticas analisadas de melhor resultado (Ochiai, Tarantula, Jaccard, Barinel e Dstar).
