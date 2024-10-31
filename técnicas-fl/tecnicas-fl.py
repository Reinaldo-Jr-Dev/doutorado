from imblearn.over_sampling import SMOTE
import math
import configparser
import numpy as np
import logging

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

    return np.array(matriz), vetor

# - OCHIAI --------------------------------------------------------------------------------------------------------------------------------------------
def calcular_ochiai(matriz_cobertura, resultados_testes):
    logging.info("Aplicando a técnica Ochiai ...")
    # Definição da quantidade de elementos(linhas) a ser analisado
    num_linhas = matriz_cobertura.shape[1]
    resultados = {}
    # Leitura de todos os elementos [1 até N]
    for linha in range(num_linhas):
        # A: Número de testes que falharam e cobriram a linha (defeito).
        # Leitura de todas as linhas para cada coluna da matriz para realizar o cálculo por coluna que seria o statement (elemento analisado / linha)
        A = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '-' and matriz_cobertura[i][linha] == 1)
        # B: Número de testes que passaram e cobriram a linha.
        B = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '+' and matriz_cobertura[i][linha] == 1)
        # C: Número de testes que falharam e não cobriram a linha.
        C = sum(1 for i in range(len(resultados_testes)) if resultados_testes[i] == '-' and matriz_cobertura[i][linha] == 0)
        
        # Aplicar a Fórmula
        denom = math.sqrt((A + C) * (A + B))
        if denom == 0:
            resultados[linha] = 0
        else:
            resultados[linha] = A / denom

    return resultados

# - TARANTULA --------------------------------------------------------------------------------------------------------------------------------------------
def calcular_tarantula(matriz_cobertura, resultados_testes):
    logging.info("Aplicando a técnica Tarantula ...")
    # Definição da quantidade de elementos(linhas) a ser analisado
    num_linhas = matriz_cobertura.shape[1]
    resultados = {}
    # Leitura de todos os elementos [1 até N]
    for linha in range(num_linhas):
        logging.info("Lendo Elemento {0} ".format(linha + 1))
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
    logging.info("Tabela de Scores {0} ".format(tecnica))
    for linha, resultado in resultados.items():
        logging.info(" Elemento {0}: {1} ".format(linha + 1, resultado))

# - Calcular Métrica TOP-N -----------------------------------------------------------------------------------------------------------------------------------
def calcular_metrica_top_n(resultados, linhas_defeituosas):
    logging.info(" Calculando a métrica TOP-N ... ")
    # Alimenta vetor de resultados
    vetor_resultados = []
    for linha, resultado in resultados.items():
        vetor_resultados.append(resultado)
    # Transforma vetor em numpy para a aplicação da ordenação    
    np_vetor_resultados = np.array(vetor_resultados)    
    # Classificamos as linhas em ordem decrescente com base nos resultados da heurística retornando seus índices ordenados
    vetor_classificado_indices = np.argsort(vetor_resultados)[::-1]
    logging.info(resultados)
    logging.info(vetor_classificado_indices)    
    # Encontrar a posição da linha defeituosa na classificação e add e vetor_posicoes
    vetor_posicoes = []    
    for posicao_i in range(len(linhas_defeituosas)):        
        posicao = np.where(vetor_classificado_indices == linhas_defeituosas[posicao_i])[0][0] + 1  # +1 porque queremos TOP-1, TOP-2, etc.
        vetor_posicoes.append(posicao)

    return max(vetor_posicoes) # considerar a maior posição (TOP-N)

def balanceamento_dados_smote(k, matriz_cobertura, resultados_testes):
    # Exemplo de matriz de dados (features) e rótulos (labels)
    X = matriz_cobertura
    # definição de rótulos da matriz de dados: 1 (minoritaria - 2 amostras) e 0 (majoritaria - 3 amostras)
    y = np.array(resultados_testes)  
    # Criar uma instância do SMOTE com um vizinho (k = 1)
    smote = SMOTE(k_neighbors=k)
    # Aplicar SMOTE
    X_resampled, y_resampled = smote.fit_resample(X, y)
    # Mostrar dados Balanceados
    # Observe que no resultado final (X_resampled) é criado um novo vetor duplicando a amostra de equilíbrio ([0 0 0 1])
    #print("-----------------------------")
    #print("Matriz não balanceada:")
    #print(X)
    #print("Rótulos não balanceados:")
    #print(y)
    #print("-----------------------------")
    #print("Matriz de dados balanceada:")
    #print(X_resampled)
    #print("Rótulos balanceados:")
    #print(y_resampled)
    #print("-----------------------------")
    return X_resampled, y_resampled

# - SETUP (Leitura de Arquivo de Configuração) ----------------------------------------------------------------------------------------------------------------
# Criar um objeto ConfigParser
print('Iniciando ...')
config = configparser.ConfigParser()

# Ler o arquivo de configuração
config.read('config.ini')

# Acessar os dados (metadados)
# Técnica
tecnica = config['tecnica']['nome']

# Acessar os dados (metadados)
# Técnica
tecnica_balanceamento = config['tecnica_tratamento_matriz']['nome']

# Configurando o logging
logging.basicConfig(filename='informacoes_'+tecnica+'.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Nome do arquivo TXT que possui a matriz de espectro de cobertura
arquivo_matriz_cobertura = config['matriz_espectro']['nome_arquivo']
matriz_cobertura, resultados_testes = transformar_arquivo_txt_matriz(arquivo_matriz_cobertura)

# Elementos com defeito
elementos_com_defeito = config['defeito']['lista_elementos']
vetor_elementos_com_defeito = [int(value) for value in elementos_com_defeito.split(',')]

# - Balanceamento dos Dados -----------------------------------------------------------------------------------------------------------------------------------
if tecnica_balanceamento == 'smote':  
    logging.info("(SMOTE) Iniciando balanceamento dos dados")
    matriz_cobertura, resultados_testes = balanceamento_dados_smote(1, matriz_cobertura, resultados_testes)
    logging.info("(SMOTE) Finalizando balanceamento dos dados")

# - Chamada das Técnicas --------------------------------------------------------------------------------------------------------------------------------------
if tecnica == 'ochiai':
    # Chamar a técnica
    resultados = calcular_ochiai(matriz_cobertura, resultados_testes)
    # Mostrar resultados (Tabelas de Scores)
    mostrar_resultados(tecnica, resultados)
    # Mostrar resultado da métrica (TOP-N)
    logging.info("Métricas ")
    logging.info(" Top-{0}".format(calcular_metrica_top_n(resultados, vetor_elementos_com_defeito)))  
elif tecnica == 'tarantula':    
    # Chamar a técnica
    resultados = calcular_tarantula(matriz_cobertura, resultados_testes)
    # Mostrar resultados (Tabelas de Scores)
    mostrar_resultados(tecnica, resultados)
    # Mostrar resultado da métrica (TOP-N)
    logging.info("Métricas ")
    logging.info(" Top-{0}".format(calcular_metrica_top_n(resultados, vetor_elementos_com_defeito)))
else:
    logging.info("A técnica {0} não foi implementada!".format(tecnica))

print('O processamento finalizou! Avalie o arquivo informacoes_'+tecnica+'.log')