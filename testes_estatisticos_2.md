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

```python
import numpy as np
from scipy import stats

alg_a = np.array([120, 130, 110, 140, 125, 118, 135, 122, 128, 115, 132, 127, 119, 138, 126, 123, 131, 116, 129, 124])
alg_b = np.array([115, 125, 108, 135, 120, 112, 130, 118, 122, 110, 128, 123, 114, 133, 121, 120, 127, 113, 124, 119])

# Realizar o Teste t de Student Pareado
t_statistic, p_value = stats.ttest_rel(alg_a, alg_b)

print(f"Média Algoritmo A: {np.mean(alg_a):.2f} ms")
print(f"Média Algoritmo B: {np.mean(alg_b):.2f} ms")
print(f"Estatística t: {t_statistic:.3f}")
print(f"Valor p: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"Com p-value ({p_value:.4f}) < {alpha}, rejeitamos a hipótese nula.")
    print("Há uma diferença estatisticamente significativa no tempo de execução.")
    if np.mean(alg_b) < np.mean(alg_a):
        print(f"O Algoritmo B (Média={np.mean(alg_b):.2f}) é significativamente mais rápido que o Algoritmo A (Média={np.mean(alg_a):.2f}).")
    else:
        print(f"O Algoritmo A é significativamente mais rápido que o Algoritmo B.")
else:
    print(f"Com p-value ({p_value:.4f}) >= {alpha}, não rejeitamos a hipótese nula.")
    print("Não há evidência estatística suficiente para afirmar que há uma diferença significativa no tempo de execução entre os algoritmos.")
    print("A diferença observada de {np.mean(alg_a) - np.mean(alg_b):.2f} ms pode ser devido ao acaso.")

```
**Fragmento de Código 1** - Teste Estatítico (Teste t Pareado)



