# 🔬 Detalhamento da Proposta de Exploração 14

## Descrição geral
Este experimento propõe uma investigação comparativa da aplicação de diferentes heurísticas (Ochiai, Tarantula, Jaccard, Op2, Barinel e DStar) sobre a matriz de espectro de cobertura em seu formato original, considerando as seguintes técnicas de Undersampling: Sem duplicidades "+ ", Original NRS1, Original NRS4, Smote100 NRS1 e Smote100 NRS4. A eficácia das abordagens será mensurado por meio da métrica Pos-Fault. Serão aplicados os testes estatísticos de Wilcoxon Signed-Rank e Vargha & Delaney, com o objetivo de avaliar se as diferenças observadas entre as abordagens são estatisticamente significativas, bem como identificar a técnica que apresenta maior eficácia.

## Detalhamento das técnicas
  - Sem duplicidades "+ "
  - Original NRS1: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 1 (NRS1), na qual, para cada caso de teste reprovado, são removidos todos os casos de teste aprovados que apresentam espectros idênticos ao do caso de teste defeituoso.
  - Original NRS4: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica Noise Reduction Scheme 4 (NRS4), na qual, para cada conjunto de casos de teste aprovados com espectros idênticos, todos, exceto um caso de teste, serão removidos.
  - Smote100 NRS1: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 1 (NRS1).
  - Smote100 NRS4: Matriz de espectro de cobertura em seu formato original, com a aplicação da técnica SMOTE100 e, posteriormente, a técnica Noise Reduction Scheme 4 (NRS4).

## Resultados
(...)

## Conclusão
(...)
