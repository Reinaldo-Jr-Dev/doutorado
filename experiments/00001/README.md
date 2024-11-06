<h1 align="center"> DESCRIÇÃO - EXPERIMENTO 00001 </h1>

# Dados gerais do experimento
  - Benchmark: Defects4j
  - Projeto Chart (versão 1)
  - Heurísticas: Ochiai e Tarantula
  - Métrica: Top-N

# Artefatos do experimento
  - config.ini: arquivo de configuração, utilizado pelo algoritmo implementado.
  - informacoes_ochiai.log: informações de log da heurística Ochiai.
  - informacoes_tarantula.log: informações de log da heurística Tarantula.
  - matriz_Chart_v1.txt: matriz de espectro de cobertura.

# Dados da matriz de espectro de cobertura
  - 428 Casos de Teste (quantidade de linhas)
    - 1 Caso de Test Negativo
    - 427 Casos de Teste Positivos
  - 7057 Elementos (quantidade de colunas)

# Quantidade de componentes com defeito
  - 1 componente

# Resultados
  - Ochiai (sem tratamento da matriz): Top-33
  - Tarantula (sem tratamento da matriz): Top-33
  - Ao aplicar o tratamento da matriz utilizando a técnica de balanceamento de dados Smote, o algoritmo apresentou um erro dizendo que não havia encontrado a quantidade mínima de vizinhos para geração de novas linhas na matriz. Esse erro ocorreu, pois a matriz possui apenas um caso de teste defeituoso (uma linha na matriz).