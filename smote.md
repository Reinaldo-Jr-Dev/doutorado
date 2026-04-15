# 🔍 Detalhamento dos Tópicos de Estudo

Este documento irá abordar os detalhes dos tópicos de estudo.

---

## SMOTE (Synthetic Minority Over-sampling Technique)

A técnica SMOTE propõe uma abordagem de sobreamostragem em que a classe minoritária é sobreamostrada através da criação de exemplos “sintéticos” em vez de sobreamostragem com substituição. Esta abordagem é inspirada em uma técnica que provou ser bem-sucedida no reconhecimento de caracteres manuscritos.

Pseudo código SMOTE

![Pseudo Código SMOTE](img/Pseudo-Codigo-SMOTE.png "Pseudo Código SMOTE")

```python
    def _validate_estimator(self):
        self.nn_k_ = check_neighbors_object(
            "k_neighbors", self.k_neighbors, additional_neighbor=1, 
        )
        self.nn_k_.metric = "cosine"
        #self.nn_k_.metric = "jaccard"
        #self.nn_k_.metric = "hamming"
```
**Fragmento de Código 2** - Definição das métricas de cálculo dos vizinhos

[Documento com passo a passo do SMOTE](https://docs.google.com/document/d/e/2PACX-1vR-ke46OkleIwcab4f2c_QsVwc1P7unB7kYyrwkPw8J_Wrsrg3p0-E2r2a_WRek42Ek7NuFPzV_i8Ya/pub)

Fontes:
  - [N. V. CHAWLA, K. W. BOWYER, L. O. H. W. P. K. Smote: Synthetic minority over-sampling technique. Journal of Artificial Intelligence Research, 2002.](https://arxiv.org/abs/1106.1813)
