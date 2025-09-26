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

## Testes Estatísticos aplicado a SBFL

Importância de se trabalhar com Teste Estatíticos em SBFL
  - Permitem que as descobertas sejam generalizadas.
  - Ajudam a realizar a comparação entre as variáveis independentes e a análise de sua relevância.
    
Cenário de dados da proposta de pesquisa:
  - Variável Dependente: MFR (Mean First Rank).
  - Fatores Fixos (de Interesse) ou Variáveis Independentes:
    - Heurísticas (6 níveis): Você quer comparar o desempenho médio das 6 heurísticas.
    - Formatos da Matriz de Espectro (N formatos).
  - Unidades Experimentais: Defects4J (Projetos + Versões).

## Teste Estatístico Wilcoxon Signed Rank
Por que o Teste de Wilcoxon Signed-Rank é Ideal para o cenário da nossa pesquisa?
  - Dados Emparelhados/Dependentes:
    - Podemos comparar dois formatos da matriz de espectro de controle para a mesma versão de projeto e mesma heurística. Isso significa que as observações são naturalmente emparelhadas.
  - Natureza Não-Paramétrica:
    - Métricas como o MFR (Mean First Rank) não seguem uma distribuição normal.
  - Comparações de Medianas:
    - O teste avalia se existe uma diferença estatisticamente significativa nas medianas das diferenças entre os pares. Essa medida de tendência central é utilizada pelo dato dos dados serem não-paramétricos.

### Exemplo de aplicação (Teste Estatístico Wilcoxon Signed Rank)
Cenário: Uma empresa de desenvolvimento de software está testando duas ferramentas de análise estática de código (Ferramenta A e Ferramenta B) para identificar vulnerabilidades. Eles aplicam ambas as ferramentas em 7 projetos diferentes e registram o "número de vulnerabilidades críticas não detectadas" por cada ferramenta (um valor menor é melhor).

![Explicação - Wilcoxon Signed Rank](img/Explicacao_Wilcoxon_Signed_Rank.png "Explicação - Wilcoxon Signed Rank")

**Imagem 1** - Explicação do Teste Estatístico Wilcoxon Signed Rank

```python
  import numpy as np
  from scipy import stats
  
  # Dados do nosso exemplo didático:
  # Número de vulnerabilidades críticas não detectadas
  ferramenta_a = [12, 8, 15, 10, 9, 13, 11]
  ferramenta_b = [10, 7, 12, 11, 6, 10, 9]
  n = len(ferramenta_a) # Número de pares
  
  print(f"## Cenário: Comparando Ferramenta A vs. Ferramenta B (n={n} pares) ##\n")
  
  print("--- Implementação Manual do Wilcoxon Signed-Rank Test (Para fins didáticos) ---\n")
  
  # Passo 1: Calcular a Diferença (dᵢ) entre cada par (Ferramenta B - Ferramenta A)
  diferencas = np.array(ferramenta_b) - np.array(ferramenta_a)
  print(f"1. Diferenças (B - A): {diferencas}")
  
  # Passo 2: Calcular o Valor Absoluto das Diferenças
  abs_diferencas = np.abs(diferencas)
  print(f"2. Valores Absolutos das Diferenças: {abs_diferencas}")
  
  # Filtrar diferenças zero (se houvesse) - no nosso exemplo não há
  # A função wilcoxon da scipy lida com isso. Para a manual, vamos considerar que não há zeros.
  # Se houvesse zeros, eles seriam removidos antes de ranquear e 'n' seria ajustado.
  # Por clareza, no nosso exemplo, não há diferenças zero.
  
  # Passo 3: Ordenar os Valores Absolutos e Atribuir Ranks (tratando empates)
  # Usaremos stats.rankdata para atribuir ranks médios para empates, conforme explicado.
  ranks_abs = stats.rankdata(abs_diferencas)
  print(f"3. Ranks dos Valores Absolutos: {ranks_abs}")
  
  # Passo 4: Reatribuir os Sinais Originais aos Ranks (Ranks Sinalizados)
  # Multiplicamos o rank pelo sinal da diferença original (1 para positivo, -1 para negativo)
  signed_ranks = ranks_abs * np.sign(diferencas)
  print(f"4. Ranks Sinalizados: {signed_ranks}")
  
  # Passo 5: Calcular a Soma dos Ranks Positivos (W⁺) e a Soma dos Ranks Negativos (W⁻)
  W_plus_manual = np.sum(signed_ranks[signed_ranks > 0])
  W_minus_manual = np.sum(signed_ranks[signed_ranks < 0])
  print(f"5. Soma dos Ranks Positivos (W⁺): {W_plus_manual}")
  print(f"   Soma dos Ranks Negativos (W⁻): {W_minus_manual} (considerando o sinal)")
  
  # Passo 6: Determinar o Valor da Estatística de Teste (W)
  # W é o menor valor absoluto entre W⁺ e W⁻ (ou T+ e |T-|, dependendo da convenção)
  # Usaremos o menor entre a soma dos ranks positivos e o valor absoluto da soma dos ranks negativos.
  W_statistic_manual = min(W_plus_manual, abs(W_minus_manual))
  print(f"6. Estatística W calculada manualmente: {W_statistic_manual}")
  
  print("\n--- Utilizando a biblioteca scipy.stats para o Wilcoxon Signed-Rank Test ---\n")
  
  # Utilizando scipy.stats.wilcoxon
  # Por padrão, é um teste bicaudal (two-sided)
  # `zero_method='wilcox'` (padrão) exclui as diferenças zero.
  # `alternative='two-sided'` (padrão) indica teste bicaudal.
  statistic_scipy, p_value_scipy = stats.wilcoxon(ferramenta_a, ferramenta_b, alternative='two-sided')
  
  print(f"Estatística W (Scipy): {statistic_scipy}")
  print(f"P-valor (Scipy): {p_value_scipy:.5f}") # Formato para melhor leitura
  
  # Interpretação dos Resultados
  alpha = 0.05
  print(f"\nNível de Significância (alpha) escolhido: {alpha}")
  
  print(f"\nComparação com o Valor Crítico (Tabela):")
  print(f"   Para n={n} e alpha={alpha} (bicaudal), o valor crítico da tabela é 2.")
  print(f"   Nossa estatística W manual é {W_statistic_manual}.")
  if W_statistic_manual <= 2:
      print(f"   Como {W_statistic_manual} é MENOR ou IGUAL ao valor crítico 2, REJEITAMOS a hipótese nula.")
  else:
      print(f"   Como {W_statistic_manual} é MAIOR que o valor crítico 2, NÃO REJEITAMOS a hipótese nula.")
  
  print(f"\nComparação com o P-valor (Scipy):")
  if p_value_scipy < alpha:
      print(f"   Como o P-valor ({p_value_scipy:.5f}) é MENOR que alpha ({alpha}), REJEITAMOS a hipótese nula.")
      print("   **Conclusão:** Há evidências estatísticas significativas de uma diferença na mediana do número de vulnerabilidades críticas não detectadas entre as Ferramentas A e B.")
  else:
      print(f"   Como o P-valor ({p_value_scipy:.5f}) é MAIOR ou IGUAL a alpha ({alpha}), NÃO REJEITAMOS a hipótese nula.")
      print("   **Conclusão:** Não há evidências estatísticas significativas de uma diferença na mediana do número de vulnerabilidades críticas não detectadas entre as Ferramentas A e B.")
```

**Código 1** - Implementação do Teste Estatístico Wilcoxon Signed Rank

Conclusão
  - Como o valor de W calculado de 1,5 é menor ou igual ao valor crítico 2, rejeitamos a hipótese nula (é a afirmação a ser testada, que geralmente assume que não há efeito, não há diferença ou não há relação entre as variáveis na população).
  - Com base neste exemplo, e considerando um nível de significância de 0.05, há evidências estatísticas significativas para rejeitar a hipótese nula. Isso significa que há uma diferença significativa na mediana do número de vulnerabilidades críticas não detectadas entre a Ferramenta A e a Ferramenta B.
