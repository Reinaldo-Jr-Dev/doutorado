# 🔬 Detalhamento da Proposta de Exploração 11

## Descrição geral
Este experimento propõe uma investigação comparativa da aplicação de diferentes heurísticas (Ochiai, Tarantula, Jaccard, Op2, Barinel e DStar) sobre a matriz de espectro de cobertura em seu formato original, considerando as seguintes técnicas de Undersampling: TomerLinks, Edited Nearest Neighbors (ENN) e Cluster Based Undersampling. A eficácia das abordagens será mensurado por meio da métrica Pos-Fault. Serão aplicados os testes estatísticos de Wilcoxon Signed-Rank e Vargha & Delaney, com o objetivo de avaliar se as diferenças observadas entre as abordagens são estatisticamente significativas, bem como identificar a técnica que apresenta maior eficácia.

## Detalhamento das técnicas
  - TomekLinks: Ocorre quando duas instâncias de classes diferentes (uma da classe majoritária e outra da classe minoritária) são as vizinhas mais próximas imediatas uma da outra. Isso significa que elas estão extremamente próximas na fronteira de decisão, gerando ambiguidade. Dessa forma, essa técnica remove a instância que pertence à classe majoritária.
  - Edited Nearest Neighbors (ENN): Enquanto o TomekLinks foca em pares específicos de vizinhos imediatos (dois vizinhos), o ENN aplica uma regra de limpeza mais ampla baseada em um número de vizinhos maior. Se a classe da instância atual for diferente da classe majoritária de seus vizinhos, ela é removida. Por padrão, essa remoção é aplicada apenas às instâncias da classe majoritária.
  - Cluster Based Undersampling: Como os casos de teste positivos costumam ser redundantes (vários testes que cobrem as mesmas linhas de código), o algoritmo agrupa os casos de teste positivos em clusters e seleciona apenas os representantes de cada grupo. 
  - NearMiss-3: Para cada ponto da classe minoritária, o algoritmo identifica os seus M vizinhos mais próximos da classe majoritária. Dentre esses candidatos, ele mantém apenas aqueles que possuem a menor distância média em relação aos seus vizinhos da classe minoritária. O objetivo é garantir que cada exemplo da classe minoritária tenha uma vizinhança representativa da classe majoritária.

## Resultados

[Planilha com resultados](https://docs.google.com/spreadsheets/d/e/2PACX-1vRy7YjC1LUN2qT5zGf8x-uGNxS2Rvtc_S1UriXLWkRIuRU5SW5Sbe0ou5pylmFsy4082N9SWXgZHbr-/pubhtml)


## Conclusão
Ao analisar as técnicas TomekLinks, Edited Nearest Neighbors (ENN), Cluster Based Undersampling e NearMiss-3, por meio da métrica A12 do teste estatístico de Vargha e Delaney, verificou-se que a técnica TomekLinks apresentou os melhores resultados em relação à métrica Pos-Fault.

