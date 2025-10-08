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

## Resultados - MFR, ACC@10 e ACC_RAW@10

![Tabela - Resultado do Experimento da Proposta de Exploração III](img/Tab_1_Proposta_Exploracao_III.png "Tabela - Resultado do Experimento da Proposta de Exploração III")

**Tabela 1:** Tabela - Resultado do Experimento da Proposta de Exploração III

![Gráfico - Proposta de Exploração III (MFR)](img/Graf_1_Proposta_Exploracao_III.png "Gráfico - Proposta de Exploração III (MFR)")

**Gráfico 1:** Proposta de Exploração III (MFR)

![Gráfico - Proposta de Exploração III (ACC@10)](img/Graf_2_Proposta_Exploracao_III.png "Gráfico - Proposta de Exploração III (ACC@10)")

**Gráfico 2:** Proposta de Exploração III (ACC@10)

![Gráfico - Proposta de Exploração III (ACC_RAW@10)](img/Graf_3_Proposta_Exploracao_III.png "Gráfico - Proposta de Exploração III (ACC_RAW@10)")

**Gráfico 3:** Proposta de Exploração III (ACC_RAW@10)

## Resultados - Vizinhos Gerados

![Tabela - Resultado do Experimento da Proposta de Exploração III](img/Tab_2_Proposta_Exploracao__III.png "Tabela - Resultado do Experimento da Proposta de Exploração III")

**Tabela 2:** Tabela - Análise da quantidade de Statements cobertos com Smote Original e Smote Modificado

### Conclusões:
  - A comparação entre as formas de interpolação Trunc e Round evidencia que a utilização da interpolação Round promove um incremento no número de casos de teste com statements cobertos. Contudo, tal incremento não se estende à geração de vizinhos únicos, a qual não apresentou variação significativa com o uso da forma Round.
