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
  - O ADASYN (ADAptive SYNthetic sampling) é uma técnica de sobreamostragem derivada do SMOTE cujo objetivo é gerar mais exemplos sintéticos da classe minoritária justamente onde o problema é mais difícil, ou seja, é considerado somente os elementos que estão cercados por exemplos da classe majoritária.
- **BorderlineSmote**
  - Enquanto o SMOTE cria exemplos sintéticos para qualquer ponto da classe minoritária, o Borderline-SMOTE foca exclusivamente nos pontos que estão na fronteira de decisão ("borderline"), onde o classificador costuma ter mais dificuldade para distinguir qual classe determinado ponto pertence. Para cada ponto da classe minoritária, o algoritmo analisa seus k-vizinhos mais próximos (k-NN).
     - Safe (Seguro): Se a maioria dos vizinhos pertence à própria classe minoritária. Esses pontos são ignorados, pois já estão em uma zona "fácil".
     - Noise (Ruído): Se todos os vizinhos pertencem à classe majoritária. O algoritmo assume que esse ponto é um erro ou um outlier e não gera dados novos a partir dele.
     - Danger (Perigo): Se o número de vizinhos da classe majoritária é maior ou igual ao da minoritária. É aqui que o BorderlineSmote atua, gerando dados sintéticos apenas para esses pontos, pois eles definem o limite entre as classes.
- **KMeansSmote**
  - O KMeansSMOTE é uma técnica de sobreamostragem que combina métodos de clusterização, por meio do algoritmo K-Means, com o SMOTE. Nessa abordagem, o conjunto de dados é particionado em clusters, dos quais alguns são selecionados para a aplicação do processo de balanceamento. São priorizados os clusters que apresentam quantidade suficiente de instâncias da classe minoritária para a aplicação do SMOTE, bem como uma proporção de elementos minoritários que indique que o cluster não é predominantemente composto por instâncias da classe majoritária.
- **SVMSmote**
  - O SVMSMOTE é uma variação do SMOTE que utiliza uma Support Vector Machine (SVM) para identificar quais instâncias da classe minoritária são mais informativas para a geração de exemplos sintéticos. Essas instâncias são aquelas que mais contribuem para o aprendizado do modelo na tarefa de separação entre as classes. Em geral, não se tratam de pontos “óbvios”, isto é, instâncias localizadas no interior da região minoritária, mas sim daqueles que fornecem informações relevantes sobre a fronteira de decisão ou representam casos difíceis, por estarem próximas de instâncias da classe majoritária.
 
## Resultados
A seguir, são apresentados, por meio de uma tabela, os resultados da execução das técnicas consideradas neste experimento. Primeiramente, observou-se que algumas dessas técnicas mostraram-se incompatíveis com as características do conjunto de dados analisado, conforme descrito a seguir.

- KMeansSmote: A técnica apresenta limitações quando a classe minoritária é muito reduzida, uma vez que depende da formação de clusters representativos, o que se torna inviável nesse cenário.
- SVMSmote: Quando a classe minoritária é composta por poucos indivíduos, a técnica não consegue encontrar as instâncias da classe minoritária são mais informativas, o que se torna inviável nesse cenário.
- Smotenc: Essa técnica foi desenvolvida especificamente para conjuntos de dados que apresentam atributos mistos (numéricos e categóricos), característica ausente no conjunto de dados considerado neste estudo, o que inviabiliza sua aplicação.
- Adasyn: A técnica apresenta limitações quando a classe minoritária é muito reduzida, uma vez que depende da seleção de "elementos difíceis".

Ao analisar a planilha de resultados, destacam-se os seguintes aspectos:
  - Por projeto: Observa-se que o projeto Time apresentou melhoria em 4 das 6 heurísticas avaliadas quando aplicada a técnica de balanceamento BorderlineSMOTE. Ressalta-se que esse projeto possui, proporcionalmente, a maior quantidade de casos de teste negativos em relação ao total de casos de teste positivos, o que pode ter influenciado positivamente o desempenho da técnica de balanceamento.
  - Por heurística: Destacam-se as heurísticas Tarantula e Barinel, que apresentaram melhores resultados quando associadas às técnicas de balanceamento, especialmente à técnica BorderlineSMOTE. De modo geral, para todos os projetos analisados, com exceção do projeto Math, essas heurísticas demonstraram melhores resultados com a aplicação dessa técnica de balanceamento.

[Planilha com resultados](https://docs.google.com/spreadsheets/d/1x7A23No1TfNor-CGn2YfgyXvPvBzVTQl/edit?gid=315647370#gid=315647370)

