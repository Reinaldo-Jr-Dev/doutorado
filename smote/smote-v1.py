from imblearn.over_sampling import SMOTE
import numpy as np

# Exemplo de matriz de dados (features) e rótulos (labels)
X = np.array([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 0]
])
# definição de rótulos da matriz de dados: 1 (minoritaria - 2 amostras) e 0 (majoritaria - 3 amostras)
y = np.array([1, 1, 0, 0, 0])  

# Criar uma instância do SMOTE com um vizinho (k = 1)
smote = SMOTE(k_neighbors=1)

# Aplicar SMOTE
X_resampled, y_resampled = smote.fit_resample(X, y)

# Mostrar dados Balanceados
# Observe que no resultado final (X_resampled) é criado um novo vetor duplicando a amostra de equilíbrio ([0 0 0 1])
print("-----------------------------")
print("Matriz não balanceada:")
print(X)
print("Rótulos não balanceados:")
print(y)
print("-----------------------------")
print("Matriz de dados balanceada:")
print(X_resampled)
print("Rótulos balanceados:")
print(y_resampled)
print("-----------------------------")
