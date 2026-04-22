# 🔬 Detalhamento da Proposta de Exploração 9

## Descrição dos experimento
Este experimento propõe investigar a análise da diversidade dos novos casos de teste gerados a partir da aplicação das seguintes técnicas de balanceamento: SMOTE, SMOTEN e Borderline-SMOTE.

- **Smote (Synthetic Minority Over-sampling Technique)**
  - O algoritmo base que cria amostras sintéticas através da interpolação linear entre vizinhos próximos da classe minoritária.
- **Smoten (Synthetic Minority Over-sampling Technique for Nominal)**
  - A técnica Smoten é uma variante do SMOTE desenvolvida especificamente para lidar com conjuntos de dados onde todas as variáveis são categóricas (nominais). Os vizinhos mais próximos, são identificados pelo uso da métrica Value Difference Metric (VDM).
- **BorderlineSmote**
  - Enquanto o SMOTE cria exemplos sintéticos para qualquer ponto da classe minoritária, o Borderline-SMOTE foca exclusivamente nos pontos que estão na fronteira de decisão ("borderline"), onde o classificador costuma ter mais dificuldade para distinguir qual classe determinado ponto pertence. Para cada ponto da classe minoritária, o algoritmo analisa seus k-vizinhos mais próximos (k-NN).
     - Safe (Seguro): Se a maioria dos vizinhos pertence à própria classe minoritária. Esses pontos são ignorados, pois já estão em uma zona "fácil".
     - Noise (Ruído): Se todos os vizinhos pertencem à classe majoritária. O algoritmo assume que esse ponto é um erro ou um outlier e não gera dados novos a partir dele.
     - Danger (Perigo): Se o número de vizinhos da classe majoritária é maior ou igual ao da minoritária. É aqui que o BorderlineSmote atua, gerando dados sintéticos apenas para esses pontos, pois eles definem o limite entre as classes.
 
## Resultados
( ... )

[Planilha com resultados](https://docs.google.com/spreadsheets/d/1x7A23No1TfNor-CGn2YfgyXvPvBzVTQl/edit?gid=315647370#gid=315647370)

