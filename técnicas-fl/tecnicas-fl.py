import math
import configparser
import numpy as np

# - TRANSFORMAR ARQUIVO TXT EM MATRIZ DE ESPECTRO E VETOR DE RESULTADOS  ------------------------------------------------------------------------------
def transformar_arquivo_txt_matriz(arquivo):
    # Inicializa a matriz e o vetor
    matriz = []
    vetor = []

    # Abre o arquivo para leitura
    with open(arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Remove espaços em branco e divide a linha em valores
            valores = linha.strip().split()
            
            # Adiciona o valor da última coluna ao vetor
            vetor.append(valores[-1])
            
            # Adiciona os valores da linha (exceto a última coluna) à matriz
            matriz.append(list(map(int, valores[:-1])))

    # Exibe a matriz e o vetor
    #print("Matriz:")
    #print(np.array(matriz))
    #print("Vetor:")
    #print(vetor)

    return np.array(matriz), vetor

# - OCHIAI --------------------------------------------------------------------------------------------------------------------------------------------
def calcular_ochiai(matriz_cobertura, resultados_testes):
    num_linhas = matriz_cobertura.shape[1]
    resultados = {}
    # Leitura de todos os Statements (Colunas) [1 até N]
    for linha in range(num_linhas):
        # A: Número de testes que falharam e cobriram a linha (defeito).
        # Leitura de todas as linhas para cada coluna da matriz para realizar o cálculo por coluna que seria o statement (elemento analisado / linha)
        A = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '-' and matriz_cobertura[i][linha] == 1)
        # B: Número de testes que passaram e cobriram a linha.
        B = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '+' and matriz_cobertura[i][linha] == 1)
        # C: Número de testes que falharam e não cobriram a linha.
        C = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '-' and matriz_cobertura[i][linha] == 0)
        
        # Aplicar a Fórmula
        denom = math.sqrt((A + B) * (A + C))
        if denom == 0:
            resultados[linha] = 0
        else:
            resultados[linha] = A / denom

    return resultados

# - TARANTULA --------------------------------------------------------------------------------------------------------------------------------------------
def calcular_tarantula(matriz_cobertura, resultados_testes):
    num_linhas = matriz_cobertura.shape[1]
    resultados = {}
    # Leitura de todos os Statements (Colunas) [1 até N]
    for linha in range(num_linhas):
        # A: Número de testes que falharam e cobriram a linha.
        # Leitura de todas as linhas para cada coluna da matriz para realizar o cálculo por coluna que seria o statement (elemento analisado / linha)
        A = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '-' and matriz_cobertura[i][linha] == 1)
        # B: Número de testes que passaram e cobriram a linha.
        B = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '+' and matriz_cobertura[i][linha] == 1)
        # C: Número de testes que falharam e não cobriram a linha.
        C = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '-' and matriz_cobertura[i][linha] == 0)
        # D: Número de testes que passaram e não cobriram a linha.
        D = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '+' and matriz_cobertura[i][linha] == 0)

        # Cálculo da métrica Tarantula
        if (A + C) == 0:
            p1 = 0  # evita divisão por zero
        else:
            p1 = A / (A + C)
        
        if (B + D) == 0:
            p2 = 0  # evita divisão por zero
        else:
            p2 = B / (B + D)

        if (p1 + p2) == 0:
            resultados[linha] = 0  # evita divisão por zero
        else:
            resultados[linha] = p1 / (p1 + p2)

    return resultados

# - Mostrar Resultados ---------------------------------------------------------------------------------------------------------------------------------------
def mostrar_resultados(tecnica, resultados):
    print(f"Técnica Aplicada: {tecnica}")
    for linha, resultado in resultados.items():
        print(f"Resultado para a linha {linha + 1}: {resultado:.2f}")

# - Inicialização da Matriz de Espectro ----------------------------------------------------------------------------------------------------------------------
#matriz_cobertura = np.array([
#    [1, 0, 1],  # Teste 1
#    [1, 1, 0],  # Teste 2
#   [0, 1, 1],  # Teste 3
#    [0, 0, 1],  # Teste 4
#    [1, 0, 1],  # Teste 5
#])

# Resultados dos testes (P = Passou, F = Falhou)
#resultados_testes = ['F', 'P', 'F', 'F', 'P']

# - SETUP (Leitura de Arquivo de Configuração) ----------------------------------------------------------------------------------------------------------------
# Criar um objeto ConfigParser
config = configparser.ConfigParser()

# Ler o arquivo de configuração
config.read('config.ini')

# Acessar os dados (metadados)
# Técnica
tecnica = config['tecnica']['nome']
# Nome do arquivo TXT que possui a matriz de espectro de cobertura
arquivo_matriz_cobertura = config['matriz_espectro']['nome_arquivo']

matriz_cobertura, resultados_testes = transformar_arquivo_txt_matriz(arquivo_matriz_cobertura)
print(matriz_cobertura)
print(resultados_testes)

# - Chamada das Técnicas --------------------------------------------------------------------------------------------------------------------------------------
if tecnica == 'ochiai':
    resultados = calcular_ochiai(matriz_cobertura, resultados_testes)
    mostrar_resultados(tecnica, resultados)
elif tecnica == 'tarantula':
    resultados = calcular_tarantula(matriz_cobertura, resultados_testes)
    mostrar_resultados(tecnica, resultados)
else:
    print(f"A técnica {tecnica} não foi implementada!")

