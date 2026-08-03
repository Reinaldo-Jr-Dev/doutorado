# 🔬 Detalhamento da Proposta de Exploração 14

## Descrição geral
- Este experimento propõe uma investigação comparativa da aplicação de diferentes heurísticas (Ochiai, Tarantula, Jaccard, Op2, Barinel e DStar) sobre a matriz de espectro de cobertura em seu formato original, considerando as seguintes técnicas de Undersampling: Original NRS1, Original NRS2, Original NRS3, Original NRS4, Smote100 NRS1, Smote100 NRS2, Smote100 NRS3 e Smote100 NRS4. A eficácia das abordagens será mensurado por meio da métrica Pos-Fault. Serão aplicados os testes estatísticos de Wilcoxon Signed-Rank e Vargha & Delaney, com o objetivo de avaliar se as diferenças observadas entre as abordagens são estatisticamente significativas, bem como identificar a técnica que apresenta maior eficácia.

## Detalhamento das técnicas
  - Original NRS1: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 1 (NRS1), na qual, para cada caso de teste reprovado, são removidos todos os casos de teste aprovados que apresentam espectros idênticos ao do caso de teste defeituoso.
  - Original NRS2: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 2 (NRS2), na qual, para cada caso de teste aprovado, todos os casos de teste reprovados com espectros idênticos ao caso de teste aprovado serão removidos.
  - Original NRS3: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 3 (NRS3), na qual, para cada conjunto de casos de teste aprovados e reprovados com espectros idênticos, todos os casos de teste do conjunto serão removidos.
  - Original NRS4: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 4 (NRS4), na qual, para cada conjunto de casos de teste aprovados com espectros idênticos, todos, exceto um caso de teste, serão removidos.
  - Smote100 NRS1: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 1 (NRS1).
  - Smote100 NRS2: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 2 (NRS2).
  - Smote100 NRS3: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 3 (NRS3).
  - Smote100 NRS4: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 4 (NRS4).


Ao executar o experimento utilizando a técnica NRS2, o projeto Math (versão 101) não pôde ser processado, pois todos os casos de teste com resultado "-" apresentavam espectros idênticos. Como consequência, a técnica NRS2 eliminou essas coberturas por considerá-las redundantes, resultando na ausência de casos de teste "-" para análise.

## Resultados
[Pasta com resultados] (https://drive.google.com/drive/folders/1sleSIoWoovOXjiRDVmGVgNLtvSohnzyD)

[Planilha com resultados - Pos-Fault](https://docs.google.com/spreadsheets/d/1hiTpf27puy8WQwRuoLL-lGvaPQ3a0fOVrXnHi5s4XfU/edit?usp=sharing)

[Planilha com resultados - MFR, EXAM e ACC](https://docs.google.com/spreadsheets/d/19pq_WAdMKEQ-T8e2m8yduKbA2ju8aEsz/edit?usp=sharing&ouid=117308842881598535622&rtpof=true&sd=true)

## Conclusão
Ao analisar as técnicas Original NRS1, Original NRS4, Smote100 NRS1 e Smote100 NRS4 por meio da métrica A12 do teste estatístico de Vargha e Delaney, verificou-se que a técnica de eliminação de ruído NRS4 (Original NRS4 e Smote100 NRS4) apresentou os melhores resultados em relação à métrica Pos-Fault em todos os cenários em que foi aplicada. Dessa forma, os resultados sugerem que a presença de coberturas idênticas entre os casos de teste classificados como "+" prejudica o desempenho da métrica Pos-Fault.
