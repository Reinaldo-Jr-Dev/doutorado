import random
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Função para exibir a matriz
def exibir_matriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna, end=' ')
        print() 

# Função para gerar amostras sintéticas com SMOTE
# k: Número de vizinhos
def smote(k):
    # Exemplo de matriz de dados (features) e rótulos (labels)
    matriz_features = np.array([
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 0]
    ])
    print("Matriz Original")
    exibir_matriz(matriz_features)
    # definição de rótulos da matriz de dados: 1 (minoritaria - 2 amostras) e 0 (majoritaria - 3 amostras)
    matriz_labels = np.array([1, 1, 0, 0, 0]) 
    # busca em indices_matriz_labels_defeito, elementos de minoria com defeito (label == 1)
    indices_matriz_labels_defeito = [i for i, x in enumerate(matriz_labels) if x == 1]
    # busca em indices_matriz_labels_defeito, elementos de maioria sem defeito (label == 0)
    indices_matriz_labels_sem_defeito = [i for i, x in enumerate(matriz_labels) if x == 0]

    # criação de matriz TOrigF que possui as linhas com o label == 1
    TOrigF = [];
    # Varredura de indices_matriz_labels_defeito, para criação de TOrigF
    for i in range(len(indices_matriz_labels_defeito)):
        TOrigF.append(matriz_features[indices_matriz_labels_defeito[i]]);
    print("Linhas da matriz com defeito")
    exibir_matriz(TOrigF)

    # Matriz original
    TOrig = matriz_features
    # Nova Matriz a ser incluída as novas amostras
    TNew = TOrig
    # Tamanho da Matriz com testes sem defeito
    Pnum = len(indices_matriz_labels_sem_defeito)
    # Tamanho da Matriz com as linhas que correspondem os elementos de minoria (label == 1)
    Fnum = len(indices_matriz_labels_defeito)

    # Criar uma instância do NearestNeighbors
    # K+1 para considerar sempre um vizinho a mais, uma vez, que o algoritmo NearestNeighbors() considera o próprio ponto, como um vizinho
    nn = NearestNeighbors(n_neighbors=k+1)
    # Ajustar o modelo com os dados
    nn.fit(TOrigF)
    # Encontrar os vizinhos mais próximos para cada ponto
    distances, nnarray = nn.kneighbors(TOrigF)
    # distances: distância dos k vizinhos
    print("Distancias")
    print(distances)
    # nnarray: índice dos k vizinhos
    print("Indices dos k vizinhos (nnarray)")
    print(nnarray)
    # Quantidade de amostras a serem geradas para igualar a quantidade entre label == 1 e label == 2
    FNewnum = Pnum - Fnum
    print("Quantidade de amostras a ser gerada")
    print(FNewnum)

    # Avaliar se existem dados a serem gerados para a efetivação do balanceamento (Pnum > Fnum)
    if (FNewnum > 0):
        # Regra: A quantidade de amostras a serem geradas deve ser <= a quantidade total de possibilidades de vizinhos
        if (FNewnum > (Fnum * Fnum)):
            print(f"A quantidade de amostras a serem geradas {FNewnum} é maior que a quantidade de possibilidades de vizinhos {(Fnum * Fnum)}")
            return

        # Vetor de amostras sintetizadas
        TAmostrasSintetizadas = [];
        index = 0; # Garantia para leitura somente da quantidade das linhas da matriz TOrigF  
        for i in range(FNewnum):
            # Garantia para leitura somente da quantidade das linhas da matriz TOrigF  
            if ( (index % Fnum) == 0):
                index = 0;
            # Calcula randomicamente um nummero entre 1 (para não considerar o próprio ponto como seu vizinho) e (k). 
            nn = random.randint(1, k)
            # Busca o indice do vizinho (escolhido randomicamente)
            TNearest = TOrigF[(nnarray[index])[nn]]
            print("Indice do vizinho escolhido")
            print(f"index: {index}, nn: {nn}, TNeares: {TNearest}")
            # Realiza a composição da nova amostra
            numRandom = random.randint(0, 1)
            # Se nn = 1, i = 1 e numRamdom = 1, tNew será [ 2 2 2 1]
            # Seria interessante aplicar uma normalização desses dados, ou seja, [ 2 2 2 1] será [ 1 1 1 0]
            tNew = TOrigF[index] + (numRandom * abs(TNearest - TOrigF[index]))
            print("Cálculo de tNew")
            print(f"TOrigF[index]: {TOrigF[index]}, numRandom: {numRandom}, abs(TNearest - TOrigF[index]): {abs(TNearest - TOrigF[index])}")
            print(f"tNew: {tNew}")
            # Adicionando o vetor como nova linha
            TAmostrasSintetizadas.append(tNew)
            index += 1 # Garantia para leitura somente da quantidade das linhas da matriz TOrigF  
        # Matriz Final = TNew (amostra original) + TAmostrasSintetizadas (amostras sintetizadas)
        print("Matriz de Amostras Sintetizadas")
        exibir_matriz(TAmostrasSintetizadas)
        nova_matriz = np.append(TNew, TAmostrasSintetizadas, axis=0)
        print("Matriz Final")
        exibir_matriz(nova_matriz)
    else:
        print("Os testes com defeito são maiores que os testes sem defeito, portanto a simulação não será aplicada")

# Exibindo a matriz
smote(1)