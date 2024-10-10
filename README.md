<h1 align="center"> DOCUMENTAÇÃO - DOUTORADO </h1>

# Introdução
As técnicas de localização de defeitos baseada em espectro (SBFL - Spectrum-based Fault Localization) compõem uma das principais vertentes de pesquisa quanto à automatização do processo de localização de defeitos de software. Como parte essencial do teste de software, a qualidade dos dados de teste afeta diretamente a eficacia das técnicas de localização de defeitos de software. Dessa forma, existem algums estudos direcionados a melhorar a qualidade dos dados de teste, que é o foco principal dessa pesquisa.

# Implementações
- Um conjunto de dados está desbalanceado se as categorias de classificação não forem representadas de forma aproximadamente igual. Muitas vezes, os conjuntos de dados do mundo real são predominantemente compostos por exemplos “normais”, com apenas uma pequena percentagem de exemplos “anormais”. A técnica de balancemaento de dados Smote, propoem uma abordagem de sobreamostragem em que a classe minoritária é sobreamostrada através da criação de exemplos “sintéticos” em vez de sobreamostragem com substituição. Sendo assim, foi implementado dois formatos da técnica SMOTE, uma delas foi utilizado a técnica importada da biblioteca "imblearn.over_sampling" (SMOTE I), já a outra implementação todo o algoritmo foi codificado, conforme instruções do artigo [2] (SMOTE II).
  - [SMOTE I](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/master/smote/smote-v1.py)
  - [SMOTE II](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/master/smote/smote-v2.py)

# Baselines Utilizadas
- ( ... )

# Métricas Utilizadas
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
