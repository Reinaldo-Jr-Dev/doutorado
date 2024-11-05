<h1 align="center"> DESCRIÇÃO - EXPERIMENTO 00001 </h1>

# Dados gerais do experimento
  - Projeto Chart (versão 1)
  - Heurísticas: Ochiai e Tarantula
  - Métrica: Top-N

# Dados da matriz de espectro de cobertura
  - 428 Casos de Teste
  - 7057 Elementos

# Quantidade de componentes com defeito
  - 1 componente

# Resultados
  - Ochiai (sem tratamento da matriz): Top-33
  - Tarantula (sem tratamento da matriz): Top-33
  - Ao aplicar o tratamento da matriz, utilizando a técnica de balanceamento de dados Smote, o algoritmo apresentou um erro dizendo que não havia encontrado a quantidade mínima de vizinhos para geração de novas linhas na matriz. Esse erro ocorreu, pois a matriz possui apenas um caso de teste (uma linha na matriz) defeituoso.
