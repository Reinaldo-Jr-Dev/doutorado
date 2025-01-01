<h1 align="center"> DOCUMENTAÇÃO - DOUTORADO </h1>

# Artigo de Referência
[Improving Fault Localization Using Model-domain Synthesized Failing Test Generation](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/IEEE-Improving_Fault_Localization_Using_Model-domain_Synthesized_Failing_Test_Generation.pdf)

# Problema a ser Resolvido
- Amostra de dados desbalanceada
  - Um conjunto de testes é indispensável para conduzir uma localização eficaz de defeitos. Considerando o conjunto de testes em sua totalidade, existem duas classes de testes: testes aprovados e testes reprovados. No entanto, na prática, a quantidade de testes aprovados superam em muito a quantidade de testes reprovados, fazendo com que os testes reprovados sejam uma classe minoritária em contraste aos testes aprovados. Trabalhos anteriores mostraram empiricamente que a falta de testes com defeito, tendem a prejudicar a eficácia da localização de defeitos [1] [2]. 

# Objetivo geral
- Aplicar a técnica de balanceamento de dados SMOTE (Synthetic Minority Over-Sampling Technique) [3], como proposta para balanceamento do conjunto de dados, com o objetivo principal de melhorar os resultados das heurísticas de localização de defeitos (Tarantula e Ochiai).

# Conceitos iniciais (TÓPICO AINDA EM CONSTRUÇÃO ...)
- Validação, verificação e teste de software.
- Teste Estrutural
  - Critérios baseados na complexidade
  - Critérios baseados em fluxo de controle
  - Critérios baseados em fluxo de dados
- Matriz de espectro.
- Spectrum-based fault localization (SBFL).

# Técnica proposta
- A técnica SMOTE (synthetic minority over-sampling technique) [3] possui como objetivo principal, criar novos dados (testes/linhas da matriz de espectro), a partir da classe de dados minoritária, através da busca de vizinhos mais próximos.

# Benchmark
- Justificativa:
  - São programas amplamente utilizados na localização de defeitos.
  - São programas com mais de 5 KLOCs.
  - São fáceis de serem adquiridos por permitirem estudos comparáveis ​​e reprodutíveis.
- Projetos
  - Defects4J (chart, math, lang, closure, mockito, and time) - http://defects4j.org.
    
![Captura de Tela 2025-01-01 às 18 41 59](https://github.com/user-attachments/assets/9ce6d70f-b436-4d6f-8234-2a4ceb837f92)

# Baseline
- Dados sem a aplicação do balanceamento de dados e dados balanceados (SMOTE - Synthetic Minority Over-Sampling Technique) [45].

# Métricas de Avaliação
- Top-N [4]: Denota a porcentagem de defeitos localizados na posição N de uma lista classificada de todas as declarações em ordem decrescente de suspeita retornadas por uma abordagem de localização de defeitos.
- Mean Average Rank (MAR) [5]: É a média da classificação de todos os defeitos usando uma abordagem de localização de defeitos. Quanto menor for esse valor, melhor ranqueado estão sendo atribuídos a maioria dos defeitos;
- Mean First Rank (MFR) [5]: É a média da classificação de todas os defeitos da primeira instrução defeituosa usando uma abordagem de localização de defeitos. Quanto menor for esse valor, melhor ranqueado estão sendo atribuídos a maioria dos defeitos;

# Experimento
- Aplicação da técnica de balanceamento de dados SMOTE para os projetos do benchmark Defects4J (Chart e mockito), aplicação das heurísticas Tarantula e Ochiai e avaliação do resultados, através das seguintes métricas: Top-N (Top-1, Top-5, Top-10 e Top-20), MFR e MAR.
  
![Captura de Tela 2025-01-01 às 18 43 54](https://github.com/user-attachments/assets/485c889a-492c-45f2-9edc-1ae4fd9a722a)
  
![Captura de Tela 2025-01-01 às 18 44 25](https://github.com/user-attachments/assets/a905fe58-f8a0-4d56-bc59-0c364b1de2ce)

- Durante a aplicação desse experimento, algumas versões foram descartadas, pelo fato do defeito real não ter sido encontrado. Segue a lista das versões descartadas de cada programa.
  - Chart (versões 13 e 23)
  - Mockito (versões 7, 8, 15, 30 e 31)

# Resultados Gerais
- A aplicação da técnica de balanceamento de dados SMOTE obteve melhores resultados (métrica de avaliação Top-N), para a heurística Tarantula.

# Propostas de Exploração
- A proposta de utilização da técnica SMOTE, se mostrou eficiente quanto ao procedimento de balanceamento dos dados, para alguns cenários (heurística Tarantula). Sendo assim, é proposto a implementação das diversas variações existentes da biblioteca "imblearn.over_sampling" da técnica SMOTE (KMeansSMOTE, ADASYN, SVMSMOTE, BorderlineSMOTE e SMOTENC), como forma de tentar melhorar ainda mais o procedimento de balanceamento dos dados.
- Ao avaliar os dados gerados pela técnica SMOTE, percebeu-se a geração de muitos dados repetidos, para as amostras com pouca quantidade de dados da classe minoritária e isso não foi investigado pelo artigo de referência em questão. Sendo assim, é proposto o uso de alguma técnica de clonagem dos dados da classe minoritária ([A theoretical analysis on cloning the failed test cases to improve spectrum-based fault localization](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/A%20Theoretical%20Analysis%20on%20Cloning%20the%20Failed%20Test%20Cases%20to%20Improve%20Spectrum-based%20Fault%20Localization.pdf)), para que o SMOTE e suas variações tenham um melhor funcionamento.

# Referências
- [1] C. Gong, Z. Zheng, W. Li, and P. Hao, “Effects of class imbalance in test suites: An empirical study of spectrum-based fault localization,” in Proceedings of the 36th Annual Computer Software and Applications Conference Workshops, 2012, pp. 470–475.
- [2] L. Zhang, L. Yan, Z. Zhang, J. Zhang, W. Chan, and Z. Zheng, “A theoretical analysis on cloning the failed test cases to improve spectrum- based fault localization,” Journal of Systems and Software, vol. 129, pp. 35–57, 2017.
- [3] N.V.Chawla,K.W.Bowyer,L.O.Hall,andW.P.Kegelmeyer,“Smote: Synthetic minority over-sampling technique,” 2011.
- [4] C. Parnin and A. Orso, “Are automated debugging techniques actually helping programmers?” in International Symposium on Software Testing and Analysis(ISSTA 2011), 2011, pp. 199–209.
- [5] X. Li, W. Li, Y. Zhang, and L. Zhang, “DeepFL: Integrating multiple fault diagnosis dimensions for deep fault localization,” in Proceedings of the 28th ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA 2019), 2019, pp. 169–180.

# Autores da Pesquisa
- Reinaldo de Souza Júnior: reinaldo.junior@discente.ufg.br
- Plínio Sa Leitão Júnior: plinio.sa.leitao.junior@ufg.br
