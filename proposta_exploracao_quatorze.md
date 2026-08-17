# 🔬 Detalhamento da Proposta de Exploração 14

## Descrição geral
- Essa proposta de exploração propõe uma investigação comparativa da aplicação de diferentes heurísticas (Ochiai, Tarantula, Jaccard, Op2, Barinel e DStar) sobre a matriz de espectro de cobertura em seu formato original, considerando as seguintes técnicas de Oversampling e Undersampling: Smote, SmoteN, Smote100, SmoteN_100, SmoteN_200 e SmoteN_300, Original NRS1, Original NRS2, Original NRS3, Original NRS4, Smote100 NRS1, Smote100 NRS2, Smote100 NRS3 e Smote100 NRS4.

## Detalhamento das técnicas
  - Original: Matriz sem balanceamento algum.
  - Smote: Matriz original, com a aplicação da técnica de Oversampling, Smote.
  - SmoteN: Matriz original, com a aplicação da técnica de Oversampling, SmoteN.
  - Smote100: Matriz original, com a aplicação da técnica de Oversampling, Smote100. Considerando a quantidade de casos de teste pertencentes à classe minoritária da matriz de cobertura, a técnica Smote100 gerará uma quantidade de instâncias sintéticas equivalente a 100% dessa classe, resultando na duplicação do número de elementos da classe minoritária.
  - SmoteN_100: Considerando a quantidade de casos de teste pertencentes à classe minoritária da matriz de cobertura, a técnica SmoteN_100 gerará uma quantidade de instâncias sintéticas equivalente a 100% dessa classe, resultando na duplicação do número de elementos da classe minoritária.
  - SmoteN_200: Considerando a quantidade de casos de teste pertencentes à classe minoritária da matriz de cobertura, a técnica SmoteN_200 gerará uma quantidade de instâncias sintéticas equivalente a 200% dessa classe, resultando na triplicação do número de instâncias da classe minoritária.
  - SmoteN_300: Considerando a quantidade de casos de teste pertencentes à classe minoritária da matriz de cobertura, a técnica SmoteN_300 gerará uma quantidade de instâncias sintéticas equivalente a 300% dessa classe, resultando na quadruplicação do número de instâncias da classe minoritária.
  - Original NRS1: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 1 (NRS1), na qual, para cada caso de teste reprovado, são removidos todos os casos de teste aprovados que apresentam espectros idênticos ao do caso de teste defeituoso.
  - Original NRS2: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 2 (NRS2), na qual, para cada caso de teste aprovado, todos os casos de teste reprovados com espectros idênticos ao caso de teste aprovado serão removidos.
  - Original NRS3: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 3 (NRS3), na qual, para cada conjunto de casos de teste aprovados e reprovados com espectros idênticos, todos os casos de teste do conjunto serão removidos.
  - Original NRS4: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 4 (NRS4), na qual, para cada conjunto de casos de teste aprovados com espectros idênticos, todos, exceto um caso de teste, serão removidos.
  - Smote100 NRS1: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 1 (NRS1).
  - Smote100 NRS2: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 2 (NRS2).
  - Smote100 NRS3: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 3 (NRS3).
  - Smote100 NRS4: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 4 (NRS4).


Ao executar o experimento utilizando a técnica Noise Reduction Scheme 3 (NRS3), o projeto Math (versão 101) não pôde ser processado, pois ao eliminar os casos de teste de espectros idênticos, não restou nenhum caso de teste "-". Portanto, as técnicas Original NRS3 e Smote100 NRS3, não foram consideradas para efeito de comparação.

## Resultados
[Pasta com resultados](https://drive.google.com/drive/folders/1sleSIoWoovOXjiRDVmGVgNLtvSohnzyD?usp=drive_link)

## Conclusão
Ao analisar as técnicas Original NRS1, Original NRS2, Original NRS3, Original NRS4, Smote100 NRS1, Smote100 NRS2, Smote100 NRS3 e Smote100 NRS4 por meio da métrica A12 do teste estatístico de Vargha e Delaney, verificou-se que a técnica de eliminação de ruído NRS4 (Original NRS4 e Smote100 NRS4) apresentou os melhores resultados em relação à métrica Pos-Fault em todos os cenários em que foi aplicada. Dessa forma, os resultados sugerem que a presença de coberturas idênticas entre os casos de teste classificados como "+" prejudica o desempenho da métrica Pos-Fault.
