# 🔍 Detalhamento dos Tópicos de Estudo

Este documento irá abordar os detalhes dos tópicos de estudo.

---

## Testes Estatísticos

O principal propósito de um teste estatístico é ajudar a inferir conclusões sobre uma população maior a partir de uma amostra limitada, quantificando a incerteza associada a essas inferências. Ele nos dá uma estrutura para:

  - Avaliar hipóteses: Confirmar ou refutar suposições sobre um parâmetro populacional ou a relação entre variáveis.
  - Tomar decisões informadas: Direcionar a escolha entre diferentes alternativas baseadas em evidências empíricas.
  - Quantificar a evidência: Fornecer um valor de probabilidade (p-value) que indica o quão forte é a evidência contra uma hipótese inicial.

As pesquisas em SBFL frequentemente empregam testes estatísticos formais para avaliar, comparar e validar o desempenho de diferentes algoritmos ou variações. Estes são testes de hipótese clássicos que permitem aos pesquisadores tirar conclusões robustas sobre a significância dos resultados.

Para que o teste estatístico possa analisar a variabilidade e a significância estatística das diferenças, ele precisa de múltiplas observações (ou repetições) para cada combinação única de suas variáveis independentes (projetos + versão, heurísticas e técnica de balanceamento).

<mark>Eu não tenho aleatoriedade</mark>

### Exemplo de Aplicação

Cenário: Uma equipe de desenvolvimento otimizou um algoritmo de busca (Algoritmo B) e acredita que ele é mais rápido que a versão atual (Algoritmo A). Você decide fazer um experimento para verificar isso. Foi selecionado 20 operações de busca representativas. Para cada operação, você mede o tempo de execução (em milissegundos) tanto com o Algoritmo A quanto com o Algoritmo B.

![Tabela de Simulações](img/Tabela_Simulacoes.png "Tabela de Simulações")

**Tabela 1:** Tabela de Simulações



