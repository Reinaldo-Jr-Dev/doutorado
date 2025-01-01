<h1 align="center"> DOCUMENTAÇÃO - DOUTORADO </h1>

# Artigo de Referência
[Improving Fault Localization Using Model-domain Synthesized Failing Test Generation](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/IEEE-Improving_Fault_Localization_Using_Model-domain_Synthesized_Failing_Test_Generation.pdf)

# Problema a ser Resolvido
- Amostra de dados desbalanceada
  - Um conjunto de testes é indispensável para conduzir uma localização eficaz de defeitos. Considerando o conjunto de testes em sua totalidade, existem duas classes de testes: testes aprovados e testes reprovados. No entanto, na prática, a quantidade de testes aprovados superam em muito a quantidade de testes reprovados, fazendo com que os testes reprovados sejam uma classe minoritária em contraste aos testes aprovados. Trabalhos anteriores mostraram empiricamente que a falta de testes com defeito, tendem a prejudicar a eficácia da localização de defeitos [??]. 

# Objetivo geral
- Aplicar a técnica de balanceamento de dados SMOTE (Synthetic Minority Over-Sampling Technique) [45], como proposta para balanceamento do conjunto de dados, com o objetivo principal de melhorar os resultados das heurísticas de localização de defeitos.

# Conceitos iniciais
- Matriz de espectro, heurísticas de localzação de defeito, etc.

# Técnica proposta
- A técnica SMOTE (synthetic minority over-sampling technique) [45] criar novos dados (testes/linhas da matriz de espectro) através da busca de vizinhos mais próximos a partir de outras amostras de teste com defeito no domínio do modelo.

# Benchmark
- Justificativa:
  - São programas amplamente utilizados na localização de defeitos;
  - São programas com mais de 5 KLOCs;
  - São fáceis de serem adquiridos por permitirem estudos comparáveis ​​e reprodutíveis.
- Projetos
  - Defects4J (chart, math, lang, closure, mockito, and time) - http://defects4j.org; 

# Baseline
- Dados sem a aplicação do balanceamento e dados balanceados (SMOTE - Synthetic Minority Over-Sampling Technique).

# Métricas de Avaliação
- Top-N [2]: Denota a porcentagem de defeitos localizados na posição N de uma lista classificada de todas as declarações em ordem decrescente de suspeita retornadas por uma abordagem de localização de defeitos.
- Mean Average Rank (MAR) [13]: É a média da classificação de todos os defeitos usando uma abordagem de localização de defeitos. Quanto menor for esse valor, melhor ranqueado estão sendo atribuídos a maioria dos defeitos;
- Mean First Rank (MFR) [13]: É a média da classificação de todas os defeitos da primeira instrução defeituosa usando uma abordagem de localização de defeitos. Quanto menor for esse valor, melhor ranqueado estão sendo atribuídos a maioria dos defeitos;
- Relative Improvement (RImp) [46]–[48]: É o número total de statements que precisam ser examinados para encontrar todos os defeitos.

# Conclusão e Resultados Gerais
- A aplicação da técnica de balanceamento de dados teve melhores resultados para a métrica de avaliação Top-N, para a heurística Tarantula.

# Propostas de Exploração
- A proposta de utilização da técnica SMOTE, se mostrou eficiente quanto ao procedimento de balanceamento dos dados, para alguns cenários. Sendo assim, é proposto a implementação das diversas variações existentes da biblioteca "imblearn.over_sampling" da técnica SMOTE (KMeansSMOTE, ADASYN, SVMSMOTE, BorderlineSMOTE e SMOTENC), como forma de tentar melhorar ainda mais o procedimento de balanceamento dos dados.
- Ao avaliar os dados gerados pela técnica SMOTE, percebeu-se a geração de muitos dados repetidos, para as amostras com pouca quantidade de dados da classe minoritária e isso não foi investigado pelo artigo em questão. O artigo apenas faz um destaque, relatando que o MSGen, considera apenas as amostras que possuem dois casos de teste com defeito no conjunto de testes original. Atualmente, ao considerar o benchmark Defects4J (projeto Char) em todas as suas 26 versões, 16 delas possuem apenas um caso de teste com defeito. Sendo assim, é proposto o uso de alguma técnica de clonagem dos dados da classe minoritária ([A theoretical analysis on cloning the failed test cases to improve spectrum-based fault localization](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/A%20Theoretical%20Analysis%20on%20Cloning%20the%20Failed%20Test%20Cases%20to%20Improve%20Spectrum-based%20Fault%20Localization.pdf)), para que o SMOTE e suas variações tenham um melhor funcionamento.

# Referências
- [2] C. Parnin and A. Orso, “Are automated debugging techniques actually helping programmers?” in International Symposium on Software Testing and Analysis(ISSTA 2011), 2011, pp. 199–209.
- [11] Z. Zhang, Y. Lei, X. Mao, and P. Li, “CNN-FL: An effective approach for localizing faults using convolutional neural networks,” in the 26th International Conference on Software Analysis, Evolution and Reengi- neering (SANER 2019). IEEE, 2019, pp. 445–455.
- [12] Z. Zhang, Y. Lei, X. Mao, M. Yan, L. Xu, and J. Wen, “Improving deep- learning-based fault localization with resampling,” Journal of Software: Evolution and Process, vol. 33, no. 3, p. e2312, 2021.
- [13] X. Li, W. Li, Y. Zhang, and L. Zhang, “DeepFL: Integrating multiple fault diagnosis dimensions for deep fault localization,” in Proceedings of the 28th ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA 2019), 2019, pp. 169–180.
- [14] J. Sohn and S. Yoo, “Fluccs: Using code and change metrics to improve fault localization,” in Proceedings of the 26th ACM SIGSOFT Interna- tional Symposium on Software Testing and Analysis (ISSTA 2017), 2017, pp. 273–283.
- [15] Z. Zhang, Y. Lei, X. Mao, M. Yan, L. Xu, and X. Zhang, “A study of effectiveness of deep learning in locating real faults,” Information and Software Technology, vol. 131, p. 106486, 2021.
- [12] Z. Zhang, Y. Lei, X. Mao, M. Yan, L. Xu, and J. Wen, “Improving deep- learning-based fault localization with resampling,” Journal of Software: Evolution and Process, vol. 33, no. 3, p. e2312, 2021.
- [21] L. Zhang, L. Yan, Z. Zhang, J. Zhang, W. Chan, and Z. Zheng, “A theoretical analysis on cloning the failed test cases to improve spectrum- based fault localization,” Journal of Systems and Software, vol. 129, pp. 35–57, 2017.
- [30] Y. Lei, C. Sun, X. Mao, and Z. Su, “How test suites impact fault localization starting from the size,” IET Software, vol. 12, no. 3, pp. 190–205, 2018.
- [31] H. He and E. A. Garcia, “Learning from imbalanced data,” IEEE Transactions on Knowledge and Data Engineering(TKDE), no. 9, pp. 1263–1284, 2008.	
- [32] B. Krawczyk, “Learning from imbalanced data: open challenges and future directions,” Progress in Artificial Intelligence, vol. 5, no. 4, pp. 221–232, 2016.
- [38] H. Wang, B. Du, J. He, Y. Liu, and X. Chen, “Ietcr: An information entropy based test case reduction strategy for mutation-based fault localization,” IEEE Access, vol. 8, pp. 124 297–124 310, 2020.
- [45] N.V.Chawla,K.W.Bowyer,L.O.Hall,andW.P.Kegelmeyer,“Smote: Synthetic minority over-sampling technique,” 2011.
- [46] V. Debroy, W. E. Wong, X. Xu, and B. Choi, “A grouping-based
strategy to improve the effectiveness of fault localization techniques,” in International Conference on Quality Software(QSIC 2010), 2010, pp. 13–22.
- [47] L.C.Briand,Y.Labiche,andX.Liu,“Usingmachinelearningtosupport debugging with tarantula,” in The IEEE International Symposium on Software Reliability(ISSRE 2007), 2007, pp. 137–146.
- [48] Y. Lei, X. Mao, Z. Dai, and C. Wang, “Effective statistical fault local- ization using program slices,” in Computer Software and Applications Conference(COMPSAC 2012), 2012, pp. 1–10.

# Autores da Pesquisa
- Reinaldo de Souza Júnior: reinaldo.junior@discente.ufg.br
- Plínio Sa Leitão Júnior: plinio.sa.leitao.junior@ufg.br
