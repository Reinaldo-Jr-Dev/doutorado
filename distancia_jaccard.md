# 🔍 Detalhamento dos Tópicos de Estudo

Este documento irá abordar os detalhes dos tópicos de estudo.

---

## Distância de Jaccard

- Objetivo: Distância de Jaccard (ou o Coeficiente de Similaridade de Jaccard, do qual a distância é 1 menos a similaridade) mede a dissimilaridade entre dois conjuntos.
- Artigo de origem: [Nouvelles recherches sur la distribution florale](https://www.researchgate.net/publication/242013831_Nouvelles_Recherches_Sur_la_Distribution_Florale)
- Algumas propostas práticas de solução:
	- [Measurement of Text Similarity: A Survey](https://www.mdpi.com/2078-2489/11/9/421)
 		- O artigo se propõe a fazer uma análise sistemática do estado da arte na medição de similaridade textual, detalhando os pontos fortes e fracos dos métodos existentes, e propondo um sistema de classificação mais abrangente para os algoritmos de similaridade de texto. AO longo do artigo, é citado a Similaridade de Jaccard, como técnica para comparação de Strings. 
	- [Introducing mothur: Open-Source, Platform-Independent, Community-Supported Software for Describing and Comparing Microbial Communities](https://journals.asm.org/doi/full/10.1128/aem.01541-09)
	- [An efficient recommendation generation using relevant Jaccard similarity](https://www.sciencedirect.com/science/article/pii/S0020025519300325?casa_token=oyDh6iiMD0wAAAAA:fMzC3zXAJnLShafvs_grbrFy1G5fvrA3FgSGJylHUGspMaVxWwwSW6a7LdWx5jrsu-oDOKRYmUs)
- É utilizado em quais estruturas de dados?
	- Vetores binários: Onde um '1' indica a presença de um item em um conjunto e '0' a ausência.
	- Bags de palavras - "Bag Words" (em processamento de linguagem natural): Conjuntos de palavras únicas de um documento.
	- Listas de atributos: Onde cada lista representa um conjunto de características.

![Exemplo de cálculo da distância de Jaccard](img/explicacao_distancia_jaccard.png "Calculo da distância")
