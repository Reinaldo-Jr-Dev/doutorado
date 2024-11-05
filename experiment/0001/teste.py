import numpy as np

# Definimos o vetor de resultados da heurística Ochiai
ochiai_scores = np.array([0.25, 0.40, 0.67, 0.80])
print(ochiai_scores)

# Linha com defeito real (índice 1 representa a linha 2)
defect_line_index = 1

# Classificamos as linhas em ordem decrescente com base nos resultados da heurística retornando seus índices
sorted_indices = np.argsort(ochiai_scores)[::-1]
print(sorted_indices)

# Função para calcular o TOP-N
def calculate_top_n(sorted_indices, defect_line_index):
    # Encontrar a posição da linha defeituosa na classificação
    position = np.where(sorted_indices == defect_line_index)[0][0] + 1  # +1 porque queremos TOP-1, TOP-2, etc.
    return position

# Calculamos o TOP-N para a heurística Ochiai
top_n_ochiai = calculate_top_n(sorted_indices, defect_line_index)
print(top_n_ochiai)
