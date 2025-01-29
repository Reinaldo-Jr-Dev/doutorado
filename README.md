<h1 align="center"> DOCUMENTAÇÃO - DOUTORADO </h1>

# Artigo de Referência
[Improving Fault Localization Using Model-domain Synthesized Failing Test Generation](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/IEEE-Improving_Fault_Localization_Using_Model-domain_Synthesized_Failing_Test_Generation.pdf)

# Conceitos iniciais (TÓPICO EM ANDAMENTO ...)
- Testes
- Heurísticas de localização de defeitos
- Matriz de espectro
- Balanceamento de dados

# Problemática da pesquisa
- Amostra de dados desbalanceada
  - Um conjunto de testes é indispensável para conduzir uma localização eficaz de defeitos. Considerando o conjunto de testes em sua totalidade, existem duas classes de testes: testes aprovados e testes reprovados. No entanto, na prática, a quantidade de testes aprovados superam em muito a quantidade de testes reprovados, fazendo com que os testes reprovados sejam uma classe minoritária em contraste aos testes aprovados. Trabalhos anteriores mostraram empiricamente que a falta de testes com defeito, tendem a prejudicar a eficácia da localização de defeitos [1] [2]. 

# Objetivo geral
- Aplicar a técnica de balanceamento de dados SMOTE (Synthetic Minority Over-Sampling Technique) [3], como proposta para balanceamento do conjunto de dados, possui como objetivo principal melhorar os resultados das heurísticas de localização de defeitos (Tarantula e Ochiai).

# Técnica proposta
- A técnica SMOTE [3] possui como objetivo principal, criar novos dados (testes/linhas da matriz de espectro), a partir da classe de dados minoritária, através da busca de vizinhos mais próximos.

# Benchmark
- Justificativa:
  - São programas amplamente utilizados na localização de defeitos.
  - São programas com mais de 5 KLOCs.
  - São fáceis de serem adquiridos por permitirem estudos comparáveis ​​e reprodutíveis.
- Projetos
  - Defects4J (chart, math, lang, closure, mockito e time) - http://defects4j.org.
    
![Captura de Tela 2025-01-27 às 20 30 22](https://github.com/user-attachments/assets/2df4cf39-09b3-4f6c-b18d-5a638adb43e2)

- Ponto a ser destacado:
  - Destaca-se a quantidade de casos de testes negativos, que é pequena (média de 0,93% de casos de teste negativos, levando em consideração todos os projetos com todos os seus casos de teste).

# Baseline
- Dados (matriz de espectro) com e sem a aplicação do balanceamento de dados pela técnica SMOTE (Synthetic Minority Over-Sampling Technique) [45]. Aplicação de 2 heuristicas de localização de defeitos (Tarantula e Ochiai).

# Métricas de Avaliação
- Foram considerados todas as métricas descritas no artigo de referência dessa pesquisa.
  - Top-N [4]: Denota a porcentagem de defeitos localizados na posição N de uma lista classificada de todas as declarações em ordem decrescente de suspeita retornadas por uma abordagem de localização de defeitos.
  - Mean Average Rank (MAR) [5]: É a média da classificação de todos os defeitos usando uma abordagem de localização de defeitos. Quanto menor for esse valor, melhor ranqueado estão sendo atribuídos a maioria dos defeitos;
  - Mean First Rank (MFR) [5]: É a média da classificação de todas os defeitos da primeira instrução defeituosa usando uma abordagem de localização de defeitos. Quanto menor for esse valor, melhor ranqueado estão sendo atribuídos a maioria dos defeitos;
  - RIMP [6] - [8]: Percentual de instruções que precisam ser examinadas para encontrar todos os defeitos usando alguma heurística de localização de defeito.

# Experimento
- Aplicação da técnica de balanceamento de dados SMOTE para os projetos do benchmark Defects4J (chart, math, lang, closure, mockito e time), aplicação das heurísticas Tarantula e Ochiai e avaliação do resultados através das seguintes métricas: Top-N (Top-1, Top-5, Top-10 e Top-20), MFR, MAR e RIMP.
- URLs de extração dos dados do experimento
  - Arquivo da matriz de espectro (matrix) e arquivo contendo a descrição das instruções/colunas da matriz (spectra): https://fault-localization.cs.washington.edu/
  - Arquivo contendo a instrução com o defeito (Exemplo de nome do arquivo: Chart-1.buggy.lines): https://bitbucket.org/rjust/fault-localization-data/src/master/analysis/pipeline-scripts/buggy-lines/
- Pontos de destaque do experimento
  - Para a aplicação da técnica SMOTE, foi utilizado o algoritmo SMOTE do pacote "imblearn.over_sampling" do Python.
  - O programa implementado ficou extremamente lento no momento da aplicação do SMOTE em matrizes maiores do projeto Closure (considerando todas as matrizes de espectro do projeto, existem 2199420 colunas), o que inviabilizou a execução do mesmo para esse projeto em específico.
  - Em todos os projetos do benchmark utilizado, houveram casos em que o defeito apontado no arquivo <Projeto>-<Versão>.buggy.lines não foi encontrado no arquivo spectra.txt. Essas versões desses projetos foram desconsiderados para efeito de cálculo das métricas. Veja maiores detalhes na tabela a seguir.
  
![Captura de Tela 2025-01-27 às 20 36 17](https://github.com/user-attachments/assets/8bb4244c-5d7a-4a78-952c-bde7fcb6eac9)

# Resultados Gerais

# Análise I
Foi realizado a comparação das heurísticas Tarantula e Ochiai com e sem a aplicação da técnica de balanceamento de dados (Smote). Essa tabela de resultados considerou a média dos valores calculados considerando todos os projetos e suas versões do benchmark dessa pesquisa. As cores das células da tabela apresentada a baixo se refere a comparação entre os resultados da heurística sem e com a aplicação da técnica de balanceamento de dados.
  
![Captura de Tela 2025-01-27 às 20 32 28](https://github.com/user-attachments/assets/467c4514-5797-4a08-9b04-fe4fec31c6fd)

- Pontos a serem destacados:
  - A heurística Tarantula com o Smote, obteve melhores resultados em relação a aplicação da mesma heurística sem o Smote, para as métricas Top-1, Top-5, MFR e MAR.
  - A heurística Ochiai com o Smote, obteve melhores resultados em relação a aplicação da mesma heurística sem o Smote, para as métricas MFR e MAR.

# Análise II
Foi realizado a comparação das heurísticas Tarantula e Ochiai com e sem a aplicação da técnica de balanceamento de dados (Smote), considerando a análise de cada projeto do benchmark Defects4J (chart, math, lang, closure, mockito e time). As cores das células da tabela apresentada a baixo se refere a comparação entre os resultados da heurística sem e com a aplicação da técnica de balanceamento de dados.

![Captura de Tela 2025-01-27 às 20 33 43](https://github.com/user-attachments/assets/c88cfdf4-b198-4b59-b594-ecae709c2d93)
![Captura de Tela 2025-01-27 às 21 20 53](https://github.com/user-attachments/assets/00355814-d26d-42aa-b1cf-0847f1d24940)

- Pontos a serem destacados para cada métrica:
  - Top-N: exceto a métrica Top-20 e Top-10 (heurística Ochiai), todas as outras aplicações tiveram algum ponto de melhora ao considerar a aplicação da técnica de balanceamento de dados (Smote) para as heurísticas Tarantula e Ochiai.
  - MAR: todas as aplicações das heurísticas com balanceamento de dados obtiveram melhores resultados se comparado as heurísticas sem a aplicação do balanceamento de dados.
  - MFR: a mesma obteve melhores resultados ao aplicar a técnica de balancamento de dados para a heurísticas Tarantula.
  - RIMP: a mesma obteve um melhor resultado ao aplicar a técnica de balancamento de dados, apenas para a heurísticas Tarantula e para o projeto Chart.

# Propostas de Exploração
- A proposta de utilização da técnica SMOTE, se mostrou eficiente quanto ao procedimento de balanceamento dos dados, para alguns cenários considerando a heurística Tarantula). Sendo assim, é proposto a implementação das diversas variações existentes da biblioteca "imblearn.over_sampling" da técnica SMOTE (KMeansSMOTE, ADASYN, SVMSMOTE, BorderlineSMOTE e SMOTENC), como forma de tentar melhorar ainda mais o procedimento de balanceamento dos dados.
- Ao fazer a análise dos dados da matriz de espectro, percebeu-se muitas linhas repetidas, porém, acredita-se que a remoção dessas linhas, poderão potencializar ainda mais os resultados da aplicação da técnica de balanceamento dos dados SMOTE.
- Ao avaliar os dados gerados pela técnica SMOTE, percebeu-se a geração de muitos dados repetidos, para as amostras com pouca quantidade de dados da classe minoritária e isso não foi investigado pelo artigo de referência em questão. Sendo assim, é proposto o uso de alguma técnica de clonagem dos dados da classe minoritária ([A theoretical analysis on cloning the failed test cases to improve spectrum-based fault localization](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/A%20Theoretical%20Analysis%20on%20Cloning%20the%20Failed%20Test%20Cases%20to%20Improve%20Spectrum-based%20Fault%20Localization.pdf)), para que ao aplicar a técnica SMOTE e suas variações, seja gerado novas amostras com menos repetição.

# Referências
- [1] C. Gong, Z. Zheng, W. Li, and P. Hao, “Effects of class imbalance in test suites: An empirical study of spectrum-based fault localization,” in Proceedings of the 36th Annual Computer Software and Applications Conference Workshops, 2012, pp. 470–475.
- [2] L. Zhang, L. Yan, Z. Zhang, J. Zhang, W. Chan, and Z. Zheng, “A theoretical analysis on cloning the failed test cases to improve spectrum- based fault localization,” Journal of Systems and Software, vol. 129, pp. 35–57, 2017.
- [3] N.V.Chawla,K.W.Bowyer,L.O.Hall,andW.P.Kegelmeyer,“Smote: Synthetic minority over-sampling technique,” 2011.
- [4] C. Parnin and A. Orso, “Are automated debugging techniques actually helping programmers?” in International Symposium on Software Testing and Analysis(ISSTA 2011), 2011, pp. 199–209.
- [5] X. Li, W. Li, Y. Zhang, and L. Zhang, “DeepFL: Integrating multiple fault diagnosis dimensions for deep fault localization,” in Proceedings of the 28th ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA 2019), 2019, pp. 169–180.
- [6] V. Debroy, W. E. Wong, X. Xu, and B. Choi, “A grouping-based strategy to improve the effectiveness of fault localization techniques,” in International Conference on Quality Software(QSIC 2010), 2010, pp. 13–22.
- [7] L.C.Briand,Y.Labiche,andX.Liu,“Using machine learning to support debugging with tarantula,” in The IEEE International Symposium on Software Reliability (ISSRE 2007), 2007, pp. 137–146.
- [8] Y. Lei, X. Mao, Z. Dai, and C. Wang, “Effective statistical fault local- ization using program slices,” in Computer Software and Applications Conference (COMPSAC 2012), 2012, pp. 1–10.

# Autores da Pesquisa
- Reinaldo de Souza Júnior: reinaldo.junior@discente.ufg.br
- Plínio Sa Leitão Júnior: plinio.sa.leitao.junior@ufg.br
