<h1 align="center"> DESCRIÇÃO - EXPERIMENTO 00003 </h1>

# Dados gerais do experimento
  - Benchmark: Defects4j
  - Projeto: Chart (versão 6)
  - Heurísticas: Ochiai e Tarantula
  - Técnica de Balanceamento de Dados: SMOTE
  - Métrica: Top-N

# Artefatos do experimento
  - [config.ini](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/master/experiments/00003/config.ini): arquivo de configuração.
  - arquivos de log (log_*.txt).
  - [matriz de espectro de cobertura](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/benchmark/benchmark/defects4j/Chart/6/matrix.txt).
  - [elementos da matriz](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/benchmark/benchmark/defects4j/Chart/6/spectra.tx).

# Dados da matriz de espectro de cobertura
  - 479 Casos de Teste (quantidade de linhas)
    - 2 Casos de Teste Negativos
    - 477 Casos de Teste Positivos
  - 676 Elementos (quantidade de colunas)

# Quantidade de componentes com defeito real
  - 1 elemento

# Resultados
  - Percebeu-se que em ambas as heurísticas houveram melhores resultados, depois que a matriz de espectro de cobertura foi manipulada pela técnica da balanceamento de dados SMOTE.
    - Tarantula (sem manipulação da matriz): TOP-102
    - Tarantula (com manipulação da matriz): TOP-28
    - Ochiai (sem manipulação da matriz): TOP-57
    - Ochiai (com manipulação da matriz): TOP-16
