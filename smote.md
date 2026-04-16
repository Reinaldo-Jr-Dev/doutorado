# 🔍 Detalhamento dos Tópicos de Estudo

Este documento irá abordar os detalhes dos tópicos de estudo.

---

## SMOTE (Synthetic Minority Over-sampling Technique)

A técnica SMOTE propõe uma abordagem de sobreamostragem em que a classe minoritária é sobreamostrada através da criação de exemplos “sintéticos” em vez de sobreamostragem com substituição. Esta abordagem é inspirada em uma técnica que provou ser bem-sucedida no reconhecimento de caracteres manuscritos.

Pseudo código SMOTE

![Pseudo Código SMOTE](img/Pseudo-Codigo-SMOTE.png "Pseudo Código SMOTE")

```python
        # Se matriz (X) for esparsa
        if sparse.issparse(X):
            sparse_func = type(X).__name__ # recebe o nome da função, de acordo com o tipo da matriz (csr_matrix, csc_matrix e coo_matrix)
            steps = getattr(sparse, sparse_func)(steps) # semelhante a "scipy.sparse.csr_matrix(steps)" 
                                                        #  converte o array steps em uma matriz esparsa de acordo com o seu tipo (csr_matrix, csc_matrix e coo_matrix)
                                                        #   para ficar do mesmo tipo que a matrix X, senão irá gerar um erro na multiplização steps.multiply(diffs).
            # Cálculo da nova amostra 
            #  X[rows]: amostra base ; steps: vetor com valores aleatórios ∈ [0, 1] ; diffs: cálculo da diferença entre vizinho e amostra 
            X_new = X[rows] + steps.multiply(diffs)
        else:
            # Cálculo da nova amostra 
            #  X[rows]: amostra base ; steps: vetor com valores aleatórios ∈ [0, 1] ; diffs: cálculo da diferença entre vizinho e amostra

            X_new = X[rows] + steps * diffs   

        # Converte a matriz X_new para o tipo (X.dtype) que é inteiro. Assim os valores são truncados (Ex: 0.84398136 = 0)        
        return X_new.astype(X.dtype)
```
**Fragmento de Código 2** - Definição das métricas de cálculo dos vizinhos

[Documento com passo a passo do SMOTE](https://docs.google.com/document/d/e/2PACX-1vR-ke46OkleIwcab4f2c_QsVwc1P7unB7kYyrwkPw8J_Wrsrg3p0-E2r2a_WRek42Ek7NuFPzV_i8Ya/pub)

Fontes:
  - [N. V. CHAWLA, K. W. BOWYER, L. O. H. W. P. K. Smote: Synthetic minority over-sampling technique. Journal of Artificial Intelligence Research, 2002.](https://arxiv.org/abs/1106.1813)
