# 🔬 Detalhamento da Proposta de Exploração VIII

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Chart;Lang;Math;Mockito;Time.
- Versão: Todas as versões.
- Quantidade mínima de casos de teste: 4.
- Quantidade mínima de casos de teste "+": 2.
- Quantidade mínima de casos de teste "-": 2.
- Heurísticas: ochiai;tarantula;jaccard;op2;barinel;dstar.

## Descrição dos experimento
Este experimento propõe uma investigação comparativa entre os dados sem aplicação de balanceamento, em sua versão original, e os dados obtidos a partir da aplicação de diversas técnicas de balanceamento, tais como SMOTE, SMOTENC, SMOTEN, ADASYN, Borderline-SMOTE, KMeans-SMOTE e SVM-SMOTE. A investigação tem como objetivo avaliar os novos casos de teste gerados por cada uma dessas técnicas de balanceamento, bem como os resultados da métrica POS-FAULT.

- **Smote (Synthetic Minority Over-sampling Technique)**
  - O algoritmo base que cria amostras sintéticas através da interpolação linear entre vizinhos próximos da classe minoritária.
- **Smotenc (Synthetic Minority Over-sampling Technique for Nominal and Continuous)**
  - Essa técnica, é projetada para datasets mistos (Numéricos/Continuous e Categóricos/Nominal)). Ela identifica quais colunas são categóricas e aplica um tratamento diferenciado nelas durante a geração.
- **Smoten (Synthetic Minority Over-sampling Technique for Nominal)**
  - A técnica Smoten é uma variante do SMOTE desenvolvida especificamente para lidar com conjuntos de dados onde todas as variáveis são categóricas (nominais). Os vizinhos mais próximos, são identificados pelo uso da métrica Value Difference Metric (VDM).
- **Adasyn**
  - A técnica Adasyn (Adaptive Synthetic), prioriza a geração de dados para exemplos da classe minoritária que são "difíceis de aprender" (aqueles cercados por muitos pontos da classe majoritária).
- **BorderlineSmote**
  - Enquanto o SMOTE cria exemplos sintéticos para qualquer ponto da classe minoritária, o Borderline-SMOTE foca exclusivamente nos pontos que estão na fronteira de decisão ("borderline"), onde o classificador costuma ter mais dificuldade para distinguir qual classe determinado ponto pertence. Para cada ponto da classe minoritária, o algoritmo analisa seus k-vizinhos mais próximos (k-NN).
     - Safe (Seguro): Se a maioria dos vizinhos pertence à própria classe minoritária. Esses pontos são ignorados, pois já estão em uma zona "fácil".
     - Noise (Ruído): Se todos os vizinhos pertencem à classe majoritária. O algoritmo assume que esse ponto é um erro ou um outlier e não gera dados novos a partir dele.
     - Danger (Perigo): Se o número de vizinhos da classe majoritária é maior ou igual ao da minoritária. É aqui que o BorderlineSmote atua, gerando dados sintéticos apenas para esses pontos, pois eles definem o limite entre as classes.
- **KMeansSmote**
  - Utiliza o algoritmo K-Means para agrupar os dados antes do over-sampling, gerando amostras apenas em clusters onde a classe minoritária é predominante, o que ajuda a evitar a criação de ruído.
- **SVMSmote**
  - Usa um classificador SVM para encontrar os vetores de suporte (os pontos mais próximos da fronteira de decisão) e gera novas amostras ao redor desses pontos críticos.
 
## Resultados
A seguir, são apresentados, por meio de uma tabela, os resultados da execução das técnicas consideradas neste experimento. Primeiramente, observou-se que algumas dessas técnicas mostraram-se incompatíveis com as características do conjunto de dados analisado, conforme descrito a seguir.

- KMeans-SMOTE: apresenta limitações quando a classe minoritária for muito reduzida, uma vez que a técnica depende da formação de clusters representativos, o que se torna inviável nesse cenário.
- SVM-SMOTE: Quando a classe minoritária é composta por poucos indivíduos, a técnica não consegue estimar de forma adequada as fronteiras de decisão entre as classes.
- SMOTENC: foi desenvolvida especificamente para conjuntos de dados que apresentam atributos mistos (numéricos e categóricos), característica ausente no conjunto de dados considerado neste estudo, o que inviabiliza sua aplicação.
- ADASYN: gera amostras sintéticas apenas para instâncias minoritárias consideradas difíceis de aprender, isto é, aquelas que possuem vizinhos pertencentes à classe majoritária. Na ausência dessa condição, nenhuma instância é classificada como "difícil", resultando na não geração de novos exemplos sintéticos.

Ao aplicar o teste estatístico de Wilcoxon Signed-Rank indicou que, em todas as simulações realizadas, não houve diferença estatisticamente significativa entre os dados analisados. Entretanto, ao empregar o teste estatístico de Vargha e Delaney, com o objetivo de identificar a técnica com melhor resultado, destaca-se:
- Ao considerar o projeto Time, a técnica BorderlineSMOTE apresentou os melhores resultados em todas as heurísticas avaliadas, com exceção das heurísticas DStar e Op2.
- Ao considerar o conjunto de todos os projetos analisados e as heurísticas Tarantula e Barinel, a técnica BorderlineSMOTE obteve os melhores resultados em todos os projetos, exceto no projeto Math.
Acredita-se que a priorização de determinados vizinhos para a geração de novos vizinhos seja o principal elemento responsável pela melhoria dos resultados da métrica Pos-Fault.

[Planilha com resultados](https://docs.google.com/spreadsheets/d/1bzdg6RfBd2IG3oujupAd7J5J-6_RRSzg1PNKdmvn-zk/edit)

