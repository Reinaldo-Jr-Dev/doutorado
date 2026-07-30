# 🔬 Detalhamento da Proposta de Exploração 13

## Descrição geral
Este experimento propõe uma investigação comparativa da aplicação de diferentes heurísticas (Ochiai, Tarantula, Jaccard, Op2, Barinel e DStar) sobre a matriz de espectro de cobertura em seu formato original, considerando as seguintes técnicas de Oversampling: SmoteN, SmoteN_100, SmoteN_200 e SmoteN_300. A eficácia das abordagens será mensurado por meio da métrica Pos-Fault. Serão aplicados os testes estatísticos de Wilcoxon Signed-Rank e Vargha & Delaney, com o objetivo de avaliar se as diferenças observadas entre as abordagens são estatisticamente significativas, bem como identificar a técnica que apresenta maior eficácia.

## Detalhamento das técnicas
  - SmoteN
  - SmoteN_100: Considerando a quantidade de casos de teste pertencentes à classe minoritária da matriz de cobertura, a técnica SmoteN_100 gerará uma quantidade de instâncias sintéticas equivalente a 100% dessa classe, resultando na duplicação do número de elementos da classe minoritária.
  - SmoteN_200: Considerando a quantidade de casos de teste pertencentes à classe minoritária da matriz de cobertura, a técnica SmoteN_200 gerará uma quantidade de instâncias sintéticas equivalente a 200% dessa classe, resultando na triplicação do número de instâncias da classe minoritária.
  - SmoteN_300: Considerando a quantidade de casos de teste pertencentes à classe minoritária da matriz de cobertura, a técnica SmoteN_300 gerará uma quantidade de instâncias sintéticas equivalente a 300% dessa classe, resultando na quadruplicação do número de instâncias da classe minoritária.

## Resultados
[Planilha com resultados - Pos-Fault](https://docs.google.com/spreadsheets/d/1Kvf2ixdK4Vrwb2ASPU9JkQplyiNc_H8E/edit?usp=sharing&ouid=117308842881598535622&rtpof=true&sd=true)

[Planilha com resultados - MFR, EXAM e ACC](https://docs.google.com/spreadsheets/d/19pq_WAdMKEQ-T8e2m8yduKbA2ju8aEsz/edit?usp=sharing&ouid=117308842881598535622&rtpof=true&sd=true)

## Conclusão
Ao analisar as técnicas SmoteN, SmoteN_100, SmoteN_200 e SmoteN_300 por meio da métrica A12 do teste estatístico de Vargha e Delaney, verificou-se que a técnica SmoteN_100 apresentou os melhores resultados em relação à métrica Pos-Fault. Dessa forma, conclui-se que a geração de uma quantidade menor de casos de teste sintéticos a partir da matriz de cobertura contribui para um melhor desempenho na métrica Pos-Fault.
