# 🔍 Detalhamento dos Tópicos de Estudo

Este documento irá abordar os detalhes dos tópicos de estudo.

---

## Distância de Hamming

- Objetivo: A distância de Hamming mede o número de posições em que dois vetores (ou cadeias de caracteres) são diferentes.
- Artigo de origem: [Error Detecting and Error Correcting Codes](https://ieeexplore.ieee.org/document/6772729)
- Algumas propostas práticas de solução:
	- [Comparison of genomic sequences using the Hamming distance](https://www.sciencedirect.com/science/article/abs/pii/S037837580400268X)
 		- Objetivo Geral: Este artigo se debruça sobre o problema da homogeneidade entre grupos, especificamente através da comparação de sequências genômicas. O cerne da questão é determinar se diferentes grupos de sequências genômicas são semelhantes ou diferentes. A técnica proposta utiliza a distância de Hamming para determinar a similaridade ou dissimilaridade entre as sequências genômicas.
	- [Fingerprint - Iris Fusion Based Identification System Using a Single Hamming Distance Matcher](https://ieeexplore.ieee.org/abstract/document/5376876)
	- [Hamming distance based approximate similarity text search algorithm](https://ieeexplore.ieee.org/abstract/document/7184772?casa_token=owHLjvbsgGMAAAAA:ASPc-NJa4u9XsrGbfOdo3RAF3VSeWPMmg_evoBfM8NBa3mW25ABwS3xHnHKPyTiaiYbUiG6FpA)
- É utilizado em quais estruturas de dados?
	- Sequências binárias (strings de 0s e 1s) que podem representar presença/ausência.
	- Sequências de caracteres de comprimento fixo para comparação de palavras ou cadeias de texto de mesmo tamanho.
	- Sequências de DNA/RNA: Representadas como sequências de nucleotídeos (A, T, C, G).
	- Vetores de características (feature vectors) de tamanho fixo, onde cada posição representa uma característica específica e o valor pode ser binário (presença/ausência).

 ![Exemplo de cálculo da distância de Hamming](img/explicacao_distancia_hamming.png "Calculo da distância")
