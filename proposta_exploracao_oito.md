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
  - É uma variação do SMOTE dedicada exclusivamente a datasets onde todos os atributos são categóricos (Nominal), utilizando métricas de distância apropriadas para esses tipos de dados.
- **Adasyn**
  - A técnica Adasyn (Adaptive Synthetic), prioriza a geração de dados para exemplos da classe minoritária que são "difíceis de aprender" (aqueles cercados por muitos pontos da classe majoritária).
- **BorderlineSmote**
  - A técnica concentra-se nos dados da classe minoritária localizados próximos à fronteira de decisão, isto é, naqueles mais suscetíveis a erros de classificação. Inicialmente, são identificadas as amostras minoritárias que possuem um grande número de vizinhos pertencentes à classe majoritária, utilizando o algoritmo k-NN. Com base nessa análise, tais amostras são classificadas como dangerous (cercadas predominantemente por instâncias da classe majoritária) ou safe (cercadas majoritariamente por instâncias da própria classe minoritária). A geração de amostras sintéticas é realizada exclusivamente a partir das instâncias classificadas como dangerous.
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

Ao aplicar o teste estatístico de Wilcoxon Signed-Rank indicou que, em todas as simulações realizadas, não houve diferença estatisticamente significativa entre os dados analisados. Entretanto, ao empregar o teste estatístico de Vargha e Delaney, com o objetivo de identificar a técnica com melhor resultado, observou-se destaque para o projeto Mockito associado à técnica Borderline-SMOTE, que apresentou melhoria nos resultados para todas as heurísticas avaliadas, exceto Op2 e Dstar.

[Planilha com resultados](https://docs.google.com/spreadsheets/d/1bzdg6RfBd2IG3oujupAd7J5J-6_RRSzg1PNKdmvn-zk/edit)

