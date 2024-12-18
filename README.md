<h1 align="center"> DOCUMENTAÇÃO - DOUTORADO </h1>

# Artigo de Referência
[Improving Fault Localization Using Model-domain Synthesized Failing Test Generation](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/IEEE-Improving_Fault_Localization_Using_Model-domain_Synthesized_Failing_Test_Generation.pdf)

# Problema a ser Resolvido
- Amostra de dados desbalanceada
  - Um conjunto de testes é indispensável para conduzir uma localização eficaz de defeitos e existem duas classes de testes: testes aprovados e testes reprovados. No entanto, na prática, a quantidade de testes aprovados superam em muito a quantidade de testes reprovados, fazendo com que os testes reprovados sejam uma classe minoritária em contraste aos testes aprovados. Trabalhos anteriores mostraram empiricamente que a falta de testes com defeito leva a um conjunto de testes com balanceamento de classe, o que tende a prejudicar a eficácia da localização de defeitos. Trabalhos anteriores mostraram empiricamente que a falta de testes com defeito, tendem a prejudicar a eficácia das técnicas de localização de defeitos.

# Objetivo geral
- A técnica proposta (MSGen - Model-domain Synthesized Failing Test Generation) utiliza o modelo de informação amplamente utilizado de localização de defeitos (matriz de espectro de cobertura) e usa a variação do espaço de recursos minoritários para criar novas amostras de testes com defeito.

# Técnica proposta
- É proposto o MSGen (Model-domain Synthesized Failing Test Generation) para sintetizar amostras de teste com defeito no domínio do modelo (isto é, vetores sintetizados de rótulos com defeito) do domínio do modelo (matriz de espectro), em vez do domínio de entrada, para melhorar a localização de defeitos.
- A pesquisa anterior [30] identificou que os dados que cobrem as características de todos os testes com defeito (ou seja, conjunto mínimo suspeito) são benéficos para localização de defeitos. O conjunto mínimo suspeito é definido como o conjunto dessas instruções executadas por todos os testes que falharam. A localização da defeito aumentará a suspeita da declaração defeituosa se a declaração defeituosa estiver nos vetores com um rótulo de defeito.
- MSGen utiliza a técnica SMOTE (synthetic minority over-sampling technique) [45] para sintetizar seus k vizinhos mais próximos a partir de outras amostras de teste com defeito no domínio do modelo. Assim, a interseção (isto é, características comuns) da amostra de teste que falhou no domínio do modelo e seus vizinhos mais próximos cobrem o conjunto mínimo suspeito. Para preservar as características comuns, o MSGen calcula a subtração (ou seja, a diferença) da amostra de teste com defeito no domínio do modelo de seu vetor mais próximo para gerar um novo vetor. Como o novo vetor cobre os recursos comuns, o MSGen considera o novo vetor como uma nova amostra de teste com defeito no domínio do modelo e adiciona a nova amostra com defeito ao modelo de informação original.
- MSGen deve identificar a quantidade de amostras de teste com defeito no domínio do modelo sintetizadas a serem criadas. Muitos estudos descobriram que um conjunto de testes com classe balanceada é útil para localização de defeitos [12], [21], e algoritmos com dados balanceados geralmente devem superar aqueles com dados desequilibrados em desempenho [31], [32]. Portanto, o MSGen produz amostras de teste com defeito no domínio do modelo sintetizadas até obtermos um conjunto de testes balanceado, no qual o número de amostras de teste que passam e de amostras com defeito no domínio do modelo são iguais.

# Benchmark
- Justificativa:
  - São programas amplamente utilizados na localização de defeitos;
  - São programas com mais de 5 KLOCs;
  - São fáceis de serem adquiridos por permitirem estudos comparáveis ​​e reprodutíveis.
- Projetos
  - Defects4J (chart, math, lang, closure, mockito, and time) - http://defects4j.org; 
  - ManyBugs (python, gzip and libtiff) - http://repairbenchmarks.cs.umass.edu/ManyBugs/; 
  - SIR (space e 4 versões do nanoxml) - http://sir.unl.edu/portal/index.php. 

# Baseline
- Os experimentos demonstrados utilizam doze abordagens de localização de defeitos do estado do arte para avaliar a eficácia em dois cenários: usando a abordagem MSGen e sem usá-la. Além disso, é utilizado duas abordagens de balanceamento de dados representativas e eficazes (undersampling and resampling) [12], [21], [38] para melhorar a localização de defeitos, onde um [38] utiliza undersampling removendo as amostras da classe majoritária e o outro [12], [21] utiliza resampling replicando a classe minoritária. 

# Métricas de Avaliação
- Top-N [2]: Denota a porcentagem de defeitos localizados na posição N de uma lista classificada de todas as declarações em ordem decrescente de suspeita retornadas por uma abordagem de localização de defeitos.
- Mean Average Rank (MAR) [13]: É a média da classificação de todos os defeitos usando uma abordagem de localização de defeitos. Quanto menor for esse valor, melhor ranqueado estão sendo atribuídos a maioria dos defeitos;
- Mean First Rank (MFR) [13]: É a média da classificação de todas os defeitos da primeira instrução defeituosa usando uma abordagem de localização de defeitos. Quanto menor for esse valor, melhor ranqueado estão sendo atribuídos a maioria dos defeitos;
- Relative Improvement (RImp) [46]–[48]: É o número total de statements que precisam ser examinados para encontrar todos os defeitos.

# Conclusão e Resultados Gerais
- Neste artigo, é proposto o MSGen que gera amostras de teste sintetizadas a partir do domínio do modelo, em vez de gerar testes reais a partir do domínio de entrada, para melhorar a localização de defeitos.
- MSGen identifica os vizinhos mais próximos das amostras de teste com defeito no domínio do modelo existente e calcula a diferença entre cada teste com defeito e seu vizinho mais próximo para gerar novas amostras de teste no domínio do modelo sintetizadas.
- Os resultados experimentais em doze técnicas de localização de defeitos e duas abordagens de balanceamento de dados mostram que o MSGen pode melhorar significativamente a eficácia da localização de defeitos em até 51,22%.
- No futuro, planejamos estender nossa abordagem MSGen ao cenário de defeitos múltiplos. Também pode-se explorar mais o domínio do modelo para geração de testes sintetizados.

# Propostas de Exploração
- A proposta de utilização da técnica MSGen que utiliza o SMOTE, se mostrou eficiente quanto ao procedimento de balanceamento dos dados. Sendo assim, é proposto a implementação das diversas variações existentes da biblioteca "imblearn.over_sampling" da técnica SMOTE (KMeansSMOTE, ADASYN, SVMSMOTE, BorderlineSMOTE e SMOTENC), como forma de tentar melhorar ainda mais o procedimento de balanceamento dos dados.
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
