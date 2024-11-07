<h1 align="center"> DESCRIÇÃO - EXPERIMENTO 00003 </h1>

# Dados gerais do experimento
  - Benchmark: Defects4j
  - Projeto: Chart (versão 6)
  - Heurísticas: Ochiai e Tarantula
  - Técnica de Tratamento de Dados: SMOTE
  - Métrica: Top-N

# Artefatos do experimento
  - config.ini: arquivo de configuração, utilizado pelo algoritmo implementado.
  - sem_smote_informacoes_ochiai.log: informações de log da heurística Ochiai (sem a manipulação da matriz de espectro de cobertura).
  - com_smote_informacoes_ochiai.log: informações de log da heurística Ochiai (com a manipulação da matriz de espectro de cobertura)..
  - sem_smote_informacoes_tarantula.log: informações de log da heurística Tarantula (sem a manipulação da matriz de espectro de cobertura)..
  - com_smote_informacoes_tarantula.log: informações de log da heurística Tarantula (com a manipulação da matriz de espectro de cobertura)..
  - matriz_Chart_v6.txt: matriz de espectro de cobertura.

# Dados da matriz de espectro de cobertura
  - 479 Casos de Teste (quantidade de linhas)
    - 2 Casos de Teste Negativos
    - 477 Casos de Teste Positivos
  - 676 Elementos (quantidade de colunas)

# Quantidade de componentes com defeito real
  - 1 elemento

# Resultados
  - Percebeu-se que em ambas as heurísticas tiverem melhores resultados, depois que a matriz de espectro de cobertura foi manipulada.
    - Tarantula (sem manipulação da matriz): TOP-102
    - Tarantula (com manipulação da matriz): TOP-28
    - Ochiai (sem manipulação da matriz): TOP-57
    - Ochiai (com manipulação da matriz): TOP-16