# 🔍 Detalhamento dos Tópicos de Estudo

Este documento irá abordar os detalhes dos tópicos de estudo.

---

## Testes Estatísticos

Um teste estatístico é um método formal e sistemático utilizado para tomar decisões sobre uma população com base em dados de uma amostra. **Em sua essência, ele nos permite avaliar a probabilidade de que os resultados observados em um experimento ou estudo sejam devidos ao acaso ou se realmente representam uma relação real entre variáveis**.
Imagine que se esteja desenvolvendo uma nova metodologia para um software e quer saber se ela realmente melhora o desempenho em comparação com a metodologia anterior. **Um teste estatístico pode te ajudar a determinar se a diferença observada entre os experimentos é estatisticamente significativa, e não apenas uma variação aleatória**.

Conceitos Fundamentais:
  - **Hipótese Nula (H₀): É a afirmação a ser testada, que geralmente assume que não há efeito, não há diferença ou não há relação entre as variáveis na população**. Exemplo: Considerando o cenário do evento de software, H₀ poderia representar que não há diferença significativa no desempenho entre a nova metodologia e a antiga.
  - Hipótese Alternativa (H₁ ou Hₐ): É a afirmação que se espera que seja verdadeira ou que está tentando ser provada. Ela contradiz a hipótese nula. Exemplo: Há uma diferença significativa no desempenho entre a nova metodologia e a antiga ou a nova metodologia melhora o desempenho. O objetivo do teste estatístico é determinar se há evidência suficiente para rejeitar a H₀ em favor da H₁.
  - Nível de Significância (α): Também conhecido como alfa, é um limiar de probabilidade pré-definido (comumente 0.05 ou 5%) que representa o risco máximo que você está disposto a aceitar de cometer um erro.
  - Valor-p (p-value): **O p-value é a probabilidade de observar resultados extremos quanto aos dados coletados. Se (p-value < α), possui evidências suficientes para rejeitar a hipótese nula (H₀). Se (p-value ≥ α), não tem evidências suficientes para rejeitar a hipótese nula. Isso significa que os dados não fornecem suporte forte o suficiente para hipótese de H₁**.
    
## Teste Estatístico Wilcoxon Signed Rank
Por que o Teste de Wilcoxon Signed-Rank é Ideal para o cenário da nossa pesquisa?
  - Dados Emparelhados/Dependentes:
    - Podemos comparar dois formatos da matriz de espectro de controle para a mesma versão de projeto e mesma heurística. Isso significa que as observações são naturalmente emparelhadas.
  - Natureza Não-Paramétrica:
    - Métricas como o MFR (Mean First Rank) não seguem uma distribuição normal.
  - Comparações de Medianas:
    - O teste avalia se existe uma diferença estatisticamente significativa nas medianas das diferenças entre os pares. Essa medida de tendência central é utilizada pelo fato dos dados serem não-paramétricos.

### Exemplo de aplicação (Teste Estatístico Wilcoxon Signed Rank)
Um teste estatístico é um método formal e sistemático utilizado para tomar decisões sobre uma população com base em dados de uma amostra. Em sua essência, ele nos permite avaliar a probabilidade de que os resultados observados em um experimento ou estudo sejam devidos ao acaso ou se realmente existe uma relação real entre as variáveis.

Cenário: Uma empresa de desenvolvimento de software está testando duas ferramentas de análise estática de código (Ferramenta A e Ferramenta B) para identificar vulnerabilidades. Eles aplicam ambas as ferramentas em 7 projetos diferentes e registram o "número de vulnerabilidades críticas não detectadas" por cada ferramenta (um valor menor é melhor).

  - Hipótese Nula (H₀): Não há diferença significativa no desempenho para identificar vulnerabilidades entre as ferramentas A e B.
  - Hipótese Alternativa (H₁): A hipótese de que a Ferramenta B é melhor que a Ferramenta A se confirma (os valores da Ferramenta B são menores que a Ferramenta A)?

![Explicação - Wilcoxon Signed Rank](img/Explicacao_Wilcoxon_Signed__Rank.png "Explicação - Wilcoxon Signed Rank")

Conclusões: 
  - Como **p-value (0,0468) < @ (0,05)**, há evidências estatísticas significativas para rejeitar a hipótese nula (H₀). Isso significa que há uma diferença significativa no número de vulnerabilidades críticas não detectadas entre a Ferramenta A e a Ferramenta B.
  - Com base no Teste de Wilcoxon Signed-Rank, a Ferramenta B é significativamente melhor que a Ferramenta A para detectar vulnerabilidades críticas (W = 2, p = 0.0234, unicaudal). A Ferramenta B deixa, em média, apenas 9.29 vulnerabilidades não detectadas, enquanto a Ferramenta A deixa 11.14, uma redução de aproximadamente 10% (9.916%).

## Teste Estatístico de Vargha & Delaney
O teste de Vargha e Delaney é um teste não paramétrico utilizado para medir o tamanho do efeito entre duas amostras independentes. Esse teste quantifica a magnitude da diferença observada entre as amostras, classificando-a em pequeno, médio, grande ou muito grande efeito. Em outras palavras, o teste não tem como objetivo verificar se existe uma diferença estatisticamente significativa entre as amostras, mas sim avaliar a relevância dessa diferença.
Para maior clareza, o teste estatístico será aplicado ao cenário previamente descrito de forma formal.

![Vargha & Delaney - Cálculo](img/Vargha&Delaney_Calculo.png)

![Vargha & Delaney - Efeito](img/Vargha&Delaney_Efeito.png)

Fontes:
  - A theoretical analysis on cloning the failed test cases to improve spectrum-based fault localization (Long Zhang, Lanfei Yan, Zhenyu Zhang, Jian Zhang, W.K. Chand, Zheng Zheng).
  - MathWorld, W., The web’s most extensive mathematics resource, 2010Access on: http://mathworld.wolfram.com.
