# 🔍 Detalhamento dos Tópicos de Estudo

Este documento irá abordar os detalhes dos tópicos de estudo.

---

## SMOTE (Synthetic Minority Over-sampling Technique)

A técnica SMOTE propõe uma abordagem de sobreamostragem em que a classe minoritária é sobreamostrada através da criação de exemplos “sintéticos” em vez de sobreamostragem com substituição. Esta abordagem é inspirada em uma técnica que provou ser bem-sucedida no reconhecimento de caracteres manuscritos.

Pseudo código SMOTE

![Pseudo Código SMOTE](img/Pseudo-Codigo-SMOTE.png "Pseudo Código SMOTE")

### Código do método - Definição de quantidade de amostras a serem geradas (N)
Quando é chamado o método fit_resample(X, y), o algoritmo analisa o vetor de rótulos y, deforma a saber qual é a classe minoritária.

A quantidade de amostras sintéticas (n_samples) depende do parâmetro sampling_strategy (tipo de estratégia de geração dos novos casos de teste) configurado nos atributos de inicialicação do SMOTE.
- Estratégia "auto" (Padrão): O SMOTE calcula a diferença entre a classe majoritária e cada classe minoritária. 
- Estratégia por Proporção (Float): Se você definir 0.5, o algoritmo gerará amostras até que a classe minoritária tenha 50% do tamanho da majoritária.
- Estratégia por Dicionário: Você pode passar manualmente quais classes quer aumentar e quanto, como {'classe_A': 500}.
```python
    class BaseSMOTE(BaseOverSampler):
        # ( ... )
        def __init__(
            self,
            sampling_strategy="auto", # <-- ** LINHA IMPORTANTE **
            random_state=None,
            k_neighbors=5,
        ):
            super().__init__(sampling_strategy=sampling_strategy) # <-- ** LINHA IMPORTANTE **
            self.random_state = random_state
            self.k_neighbors = k_neighbors
        # ( ... )

    def _fit_resample(self, X, y):
        # ( ... )
        # n_samples: número de amostras da classe minoritaria a ser gerado
        # class_sample: classe minoritária (Ex: "-")
        for class_sample, n_samples in self.sampling_strategy_.items(): # <-- ** LINHA IMPORTANTE **
        # ( ... )        
```
Fragmento de Código - Definição de quantidade de amostras a serem geradas (N)

### Bloco de código - Cálculo dos k vizinhos (nnarray)
```python
def _make_samples(
    self, X, y_dtype, y_type, nn_data, nn_num, n_samples, step_size=1.0, y=None):

    # Serve para transformar self.random_state em um objeto gerador de números aleatórios
    random_state = check_random_state(self.random_state)

    # Geração de n_samples, números aleatórios
    samples_indices = random_state.randint(low=0, high=nn_num.size, size=n_samples) # <-- ** LINHA IMPORTANTE **

    # gera uma matriz 2D de tamanho n_samples, preenchidos por numeros aleatórios entre 0 e 1.     
    steps = step_size * random_state.uniform(size=n_samples)[:, np.newaxis] # <-- ** LINHA IMPORTANTE **

    # (samples_indices // qtde de colunas de nn_num) (divisão inteira)
    # obtem um vetor com as linhas da amostra de vizinhos
    rows = np.floor_divide(samples_indices, nn_num.shape[1]) # <-- ** LINHA IMPORTANTE **
                                                             
    # resto da divisão de samples_indices pelo número de colunas de nn_num
    # obtem um vetor com as colunas da amostra de vizinhos, ou seja, o vizinho a ser selecionado para cada amostra
    cols = np.mod(samples_indices, nn_num.shape[1]) # <-- ** LINHA IMPORTANTE **
                                                
    X_new = self._generate_samples(X, nn_data, nn_num, rows, cols, steps, y_type, y)

    # realiza o preenchimento de um array (tamanho n_samples) com um valor (fill_value=y_type) e tipo (dtype=y_dtype) constante.
    #  y_new: vetor preenchido com os valores de "0" (valores da classe minoritaria, classe a ser balanceada)
    y_new = np.full(n_samples, fill_value=y_type, dtype=y_dtype)
    return X_new, y_new
```
Fragmento de Código - Cálculo dos k vizinhos (nnarray)

### Bloco de código - Interpolação e Realização do Trunc
```python
def _generate_samples(
    self, X, nn_data, nn_num, rows, cols, steps, y_type=None, y=None):

    # Cálculo da diferença entre vizinho e amostra        
    diffs = nn_data[nn_num[rows, cols]] - X[rows]

    if y is not None:  # only entering for BorderlineSMOTE-2
        random_state = check_random_state(self.random_state)
        mask_pair_samples = y[nn_num[rows, cols]] != y_type
        diffs[mask_pair_samples] *= random_state.uniform(
            low=0.0, high=0.5, size=(mask_pair_samples.sum(), 1)
        )

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
        X_new = X[rows] + steps * diffs  # <-- ** LINHA IMPORTANTE **

    # Converte a matriz X_new para o tipo (X.dtype) que é inteiro. Assim os valores são truncados (Ex: 0.84398136 = 0)        
    return X_new.astype(X.dtype) # <-- ** LINHA IMPORTANTE **
```
Fragmento de Código - Interpolação e Realização do Trunc

[Documento com passo a passo do SMOTE](https://docs.google.com/document/d/e/2PACX-1vSVdjDTV00Ljt_XRSERzDLBPyZ-RXYZCrhOQdp9kuqND2zhc_icN4GG1IVHbkLcTEIW4GDoI7FXLiRl/pub)

Fontes:
  - [N. V. CHAWLA, K. W. BOWYER, L. O. H. W. P. K. Smote: Synthetic minority over-sampling technique. Journal of Artificial Intelligence Research, 2002.](https://arxiv.org/abs/1106.1813)
