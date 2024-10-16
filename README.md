<h1 align="center"> DOCUMENTAÇÃO - DOUTORADO </h1>

# Introdução
As técnicas de localização de defeitos baseada em espectro (SBFL - Spectrum-based Fault Localization) compõem uma das principais vertentes de pesquisa quanto à automatização do processo de localização de defeitos de software. Como parte essencial do teste de software, a qualidade dos dados de teste afeta diretamente a eficacia das técnicas de localização de defeitos de software. Dessa forma, existem algums estudos direcionados a melhorar a qualidade dos dados de teste, que é o foco principal dessa pesquisa.

# Implementações
- Um conjunto de dados está desbalanceado se as categorias de classificação não forem representadas de forma aproximadamente igual. Muitas vezes, os conjuntos de dados do mundo real são predominantemente compostos por exemplos “normais”, com apenas uma pequena percentagem de exemplos “anormais”. A técnica de balancemaento de dados Smote, propoem uma abordagem de sobreamostragem em que a classe minoritária é sobreamostrada através da criação de exemplos “sintéticos” em vez de sobreamostragem com substituição. Sendo assim, foi implementado dois formatos da técnica SMOTE, uma delas foi utilizado a técnica importada da biblioteca "imblearn.over_sampling" (SMOTE I), já a outra implementação todo o algoritmo foi codificado, conforme instruções do artigo [2] (SMOTE II).
  - Algoritmos - Códigos 
    - [SMOTE I](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/master/smote/smote-v1.py)
    - [SMOTE II](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/master/smote/smote-v2.py)
  - Algoritmos - Execução
    - [Ambiente de Execução](https://github.com/Reinaldo-Jr-Dev/doutorado/tree/main/.github/workflows)

# Benchmark
- O artigo em questão [1], escolheu como benchmarks, as seguintes bases de dados: Defects4J (http://defects4j.org), ManyBugs (http://repairbenchmarks.cs.umass.edu/ManyBugs/) e SIR (http://sir.unl.edu/portal/index.php). O artigo escolheu esses benchmarks por três razões principais:
  - (1) eles são os programas de grande porte amplamente utilizados na localização de defeitos.
  - (2) são programas de grande porte com pelo menos mais de 5 KLOC.
  - (3) são fáceis de serem adquiridos por permitirem estudos comparáveis e reprodutíveis.
- Para a realização deste projeto, utilizaremos os dados referentes ao espectro da execução gerados previamente no trabalho realizado por Pearson et al. (2017). O espectro foi construído com a utilização da ferramenta GZoltar. O trabalho foi conduzido utilizando uma versão anterior do repositório Defects4J, responsável por conter 438 bugs reais, distribuídos em um total de seis programas open-source escritos em Java, conforme demonstrado na tabela a baixo. Foi escolhido o benchmark Defects4J, para essa documentação, pelo fato da mesma já se encontrar disponibilizada e de fácil acesso em http://fault-localization.cs.washington.edu/. O GZoltar (https://gzoltar.com/) é um framework voltado para a automação da fases de teste e depuração presentes no ciclo de desenvolvimento de software. O framework é voltado para se integrar de forma simples e eficiente com o conjunto de testes JUnit presentes no programa alvo a ser instrumentado. O mesmo realiza a leitura dos casos de teste e realiza a geração de dados da matriz de espectro de fluxo de controle.
  
![Captura de Tela 2024-10-10 às 17 16 45](https://github.com/user-attachments/assets/4b031250-cac6-45b6-9bef-11f9f83c8b98)
- Para evitar que pessoas interessadas no experimento precisassem replicar o processo de geração dos espectros a partir da execução dos testes, os dados gerados foram disponibilizados para utilização e estão disponíveis em http://fault-localization.cs.washington.edu/. Para cada versão defeituosa presente no conjunto de dados baixado, foram disponibilizados três arquivos referentes aos dados da execução dos casos de testes:
  - Um arquivo denominado **log.txt** responsável por armazenar todas as informações de depuração geradas pela execução da Gzoltar.
  - Um arquivo denominado **spectra** responsável por armazenar uma lista com informações de todas as linhas de código das classes cobertas pelos respectivos casos de testes. A Figura a baixo demonstra um exemplo de arquivo de espectro gerada para a versão 8b do programa Chart da Defects4J.    
    ![Captura de Tela 2024-10-10 às 17 10 32](https://github.com/user-attachments/assets/e5e0e774-0c22-41f4-8cbe-0b5b00c044ff)    
  - Um arquivo denominado **matrix** que representa a matriz de cobertura binária produzida pela GZoltar. Cada linha da matriz representa uma abstração do caso de teste executado sob a versão defeituosa. Cada linha contém o respectivo resultado da execução do teste (sinal - representa a falha do teste e o sinal + representa um execução bem-sucedida).
![Captura de Tela 2024-10-10 às 17 18 22](https://github.com/user-attachments/assets/5afa3930-6bb1-438a-80e1-4d30d3af9b1c)


# Métricas
Conforme descrito no artigo [1], objeto de análise profunda dessa documentação, segue a métricas a serem utilizadas: 
- **Top-N**
  - Representa a porcentagem de defeitos localizadas na posição N de uma lista classificada de todas as declarações em ordem decrescente de suspeita retornadas por uma abordagem de localização. Para valores de n iguais a 1 e 10, top-1 e top-10 contabilizam quantas vezes o defeito da versão defeituosa ficou na primeira posição e nas dez primeiras posições na lista de suspeita, respectivamente.
- **Mean Average Rank (MAR)**
  - É a classificação média de todos os defeitos usando uma abordagem de localização.
- **Mean First Rank (MFR)**
  - Para um defeito com múltiplas declarações defeituosas, localizar a primeira é fundamental, uma vez que as outras podem ser localizadas depois dela. MFR é a média da classificação de todas as falhas da primeira instrução defeituosa usando uma abordagem de localização.
- **Relative Improvement (RImp)**
  - É comparar o número total de instruções que precisam ser examinadas para encontrar todos os defeitos utilizando uma abordagem de localização de defeitos.

# Referências
- [1] [Zhuo Zhang, Yan Lei, Xiaoguang Mao, Meng Yan, Xin Xia Improving Fault Localization Using Model-domain Synthesized Failing Test Generation, 2022.](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/master/artigos/IEEE-Improving_Fault_Localization_Using_Model-domain_Synthesized_Failing_Test_Generation.pdf)
- [2] [N.V.Chawla, K.W.Bowyer, L.O.Hall, and W.P.Kegelmeyer Smote: Synthetic minority over-sampling technique, 2002.](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/master/artigos/SMOTE-Synthetic%20Minority%20Over-sampling%20Technique.pdf) 

# Autores da Pesquisa
- Reinaldo de Souza Júnior: reinaldo.junior@discente.ufg.br
- Plínio Sa Leitão Júnior: plinio.sa.leitao.junior@ufg.br
