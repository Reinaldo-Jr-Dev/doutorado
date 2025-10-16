# 🔍 Detalhamento dos Tópicos de Estudo

Este documento irá abordar os detalhes dos tópicos de estudo.

---

## Testes Estatísticos

Um teste estatístico é um método formal e sistemático utilizado para tomar decisões sobre uma população com base em dados de uma amostra. Em sua essência, ele nos permite avaliar a probabilidade de que os resultados observados em um experimento ou estudo sejam devidos ao acaso ou se realmente representam uma relação real entre variáveis.
Imagine que se esteja desenvolvendo uma nova metodologia para um software e quer saber se ela realmente melhora o desempenho em comparação com a metodologia anterior. Um teste estatístico pode te ajudar a determinar se a diferença observada no desempenho é estatisticamente significativa, e não apenas uma variação aleatória.

Conceitos Fundamentais:
  - Hipótese Nula (H₀): É a afirmação a ser testada, que geralmente assume que não há efeito, não há diferença ou não há relação entre as variáveis na população. Exemplo: Considerando o cenário do evento de software, H₀ poderia representar que não há diferença significativa no desempenho entre a nova metodologia e a antiga.
  - Hipótese Alternativa (H₁ ou Hₐ): É a afirmação que se espera que seja verdadeira ou que está tentando ser provada. Ela contradiz a hipótese nula. Exemplo: Há uma diferença significativa no desempenho entre a nova metodologia e a antiga ou a nova metodologia melhora o desempenho. O objetivo do teste estatístico é determinar se há evidência suficiente para rejeitar a H₀ em favor da H₁.
  - Nível de Significância (α): Também conhecido como alfa, é um limiar de probabilidade pré-definido (comumente 0.05 ou 5%) que representa o risco máximo que você está disposto a aceitar de cometer um erro.
  - Valor-p (p-value): O p-value é a probabilidade de observar resultados tão extremos (ou mais extremos) quanto aos dados coletados, assumindo que a hipótese nula (H₀) é verdadeira. Se (p-value < α), possui evidências suficientes para rejeitar a hipótese nula. Se (p-value ≥ α), não tem evidências suficientes para rejeitar a hipótese nula. Isso significa que os dados não fornecem suporte forte o suficiente para hipótese de H₁.
    
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

![Explicação - Wilcoxon Signed Rank](img/Explicacao_Wilcoxon_Signed__Rank.png "Explicação - Wilcoxon Signed Rank")

**Imagem 1** - Explicação do Teste Estatístico Wilcoxon Signed Rank

Conclusão
  - Se p-value < @, significa que a hipótese nula foi rejeitada, ou seja, com base nos dados do experimento, há evidências estatisticamente significativas de que existe uma diferença real, e não é apenas resultado do acaso.

## Teste Estatístico Wilcoxon Signed Rank aplicado ao cenario da pesquisa

  - Proposta: Comparar os formatos I e II da matriz de espectro para cada projeto, agrupando pelas heurísticas.

Formato dos dados:
```csv
Projeto,Heuristica,Tipo da Matriz,MFR_Valor
Chart,Ochiai,e001_original,480.42
Chart,Ochiai,e007_NRS3,98.85
Chart,Tarantula,e001_original,234.42
Chart,Tarantula,e007_NRS3,217.00
Chart,Jaccard,e001_original,481.57
Chart,Jaccard,e007_NRS3,133.00
Chart,Op2,e001_original,557.28
Chart,Op2,e007_NRS3,133.14
Chart,Barinel,e001_original,234.42
Chart,Barinel,e007_NRS3,219.14
Chart,Dstar,e001_original,509.14
Chart,Dstar,e007_NRS3,1602.00
Math,Ochiai,e001_original,206.28
Math,Ochiai,e007_NRS3,596.85
Math,Tarantula,e001_original,268.85
Math,Tarantula,e007_NRS3,658.85
Math,Jaccard,e001_original,191.57
Math,Jaccard,e007_NRS3,313.57
Math,Op2,e001_original,101.28
Math,Op2,e007_NRS3,469.42
Math,Barinel,e001_original,268.85
Math,Barinel,e007_NRS3,362.00
Math,Dstar,e001_original,320.71
Math,Dstar,e007_NRS3,421.71
Time,Ochiai,e001_original,1158.57
Time,Ochiai,e007_NRS3,1145.14
Time,Tarantula,e001_original,1193.85
Time,Tarantula,e007_NRS3,1188.71
Time,Jaccard,e001_original,1186.14
Time,Jaccard,e007_NRS3,1188.85
Time,Op2,e001_original,1034.00
Time,Op2,e007_NRS3,1050.00
Time,Barinel,e001_original,1193.85
Time,Barinel,e007_NRS3,1188.71
Time,Dstar,e001_original,1156.14
Time,Dstar,e007_NRS3,1143.14
Lang,Ochiai,e001_original,36.00
Lang,Ochiai,e007_NRS3,37.50
Lang,Tarantula,e001_original,87.00
Lang,Tarantula,e007_NRS3,79.00
Lang,Jaccard,e001_original,37.50
Lang,Jaccard,e007_NRS3,37.50
Lang,Op2,e001_original,19.00
Lang,Op2,e007_NRS3,19.00
Lang,Barinel,e001_original,87.00
Lang,Barinel,e007_NRS3,79.00
Lang,Dstar,e001_original,32.00
Lang,Dstar,e007_NRS3,32.50
Mockito,Ochiai,e001_original,422.45
Mockito,Ochiai,e007_NRS3,493.81
Mockito,Tarantula,e001_original,438.63
Mockito,Tarantula,e007_NRS3,497.09
Mockito,Jaccard,e001_original,456.54
Mockito,Jaccard,e007_NRS3,595.72
Mockito,Op2,e001_original,373.90
Mockito,Op2,e007_NRS3,511.09
Mockito,Barinel,e001_original,438.63
Mockito,Barinel,e007_NRS3,497.36
Mockito,Dstar,e001_original,696.18
Mockito,Dstar,e007_NRS3,849.27
```
**Arquivo CSV**

```python
import pandas as pd
import numpy as np
from scipy import stats

# --- Configurações ---
CSV_FILE_NAME = "experimento-1.csv"
ALPHA = 0.05 # Nível de significância

print(f"Análise estatística para o arquivo: {CSV_FILE_NAME}")
print(f"Nível de significância (α): {ALPHA}\n")

try:
    # --- 1. Leitura dos Dados ---
    df = pd.read_csv(CSV_FILE_NAME)

    # --- 2. Identificar Projetos Únicos ---
    projects = df['Projeto'].unique()

    # --- 3. Iterar por cada Projeto e Aplicar o Teste ---
    print("--- Resultados do Teste de Wilcoxon Signed-Rank por Projeto ---\n")
    for project in projects:
        print(f"### Projeto: {project} ###")

        # Filtrar dados para o projeto atual
        df_project = df[df['Projeto'] == project].copy()

        # Garantir que os dados para e001_original e e007_NRS3 estão alinhados pela heurística
        # Sort by Heuristica ensures correct pairing
        mfr_format_i = df_project[df_project['Tipo da Matriz'] == 'e001_original'].sort_values(by='Heuristica')['MFR_Valor'].values
        mfr_format_ii = df_project[df_project['Tipo da Matriz'] == 'e007_NRS3'].sort_values(by='Heuristica')['MFR_Valor'].values

        # Verificar se há dados suficientes para o teste
        if len(mfr_format_i) < 2 or len(mfr_format_ii) < 2:
            print(f"  Não há dados suficientes para realizar o Teste de Wilcoxon para o Projeto {project}. Pelo menos 2 pares são necessários.")
            print("-" * 40)
            continue
        
        # --- Aplicação do Teste de Wilcoxon Signed-Rank ---
        # alternative='two-sided' para um teste bicaudal (H1: diferença em qualquer direção)
        wilcoxon_statistic, p_value = stats.wilcoxon(mfr_format_i, mfr_format_ii, alternative='two-sided')

        # --- Resultados e Interpretação ---
        print(f"  Estatística W: {wilcoxon_statistic}")
        print(f"  P-valor: {p_value:.5f}")

        # Verificação da Hipótese Nula
        if p_value < ALPHA:
            print(f"  Hipótese Nula (H₀): REJEITADA (p-valor < α)")
            print(f"  Conclusão: Há evidências estatísticas significativas de uma diferença na mediana dos MFRs entre os tipos de matriz para o Projeto {project}.")
            # Determinar a direção da diferença (qual é 'melhor' MFR)
            mean_f1 = np.mean(mfr_format_i)
            mean_f2 = np.mean(mfr_format_ii)
            # Média_e007_NRS3 < Média_e001_original
            if mean_f2 < mean_f1:
                print(f"  O e007_NRS3 (Média MFR: {mean_f2:.3f}) tende a apresentar melhor desempenho que o e001_original (Média MFR: {mean_f1:.3f}).")
            else:
                print(f"  O e001_original (Média MFR: {mean_f1:.3f}) tende a apresentar melhor desempenho que o e007_NRS3 (Média MFR: {mean_f2:.3f}).")
        else:
            print(f"  Hipótese Nula (H₀): NÃO REJEITADA (p-valor ≥ α)")
            print(f"  Conclusão: Não há evidências estatísticas significativas de uma diferença na mediana dos MFRs entre os tipos de matriz para o Projeto {project}.")
            print(f"  (Média MFR e001_original: {np.mean(mfr_format_i):.3f}, Média MFR e007_NRS3: {np.mean(mfr_format_ii):.3f})")
        print("-" * 40)

except FileNotFoundError:
    print(f"Erro: O arquivo '{CSV_FILE_NAME}' não foi encontrado. Certifique-se de que ele está no mesmo diretório do script.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```
**Código - Teste Estatístico Wilcoxon Signed Rank**

```
Análise estatística para o arquivo: experimento-1.csv
Nível de significância (α): 0.05

--- Resultados do Teste de Wilcoxon Signed-Rank por Projeto ---

### Projeto: Chart ###
  Estatística W: 6.0
  P-valor: 0.43750
  Hipótese Nula (H₀): NÃO REJEITADA (p-valor ≥ α)
  Conclusão: Não há evidências estatísticas significativas de uma diferença na mediana dos MFRs entre os tipos de matriz para o Projeto Chart.
  (Média MFR e001_original: 416.208, Média MFR e007_NRS3: 400.522)
----------------------------------------
### Projeto: Math ###
  Estatística W: 0.0
  P-valor: 0.03125
  Hipótese Nula (H₀): REJEITADA (p-valor < α)
  Conclusão: Há evidências estatísticas significativas de uma diferença na mediana dos MFRs entre os tipos de matriz para o Projeto Math.
  O e001_original (Média MFR: 226.257) tende a apresentar melhor desempenho que o e007_NRS3 (Média MFR: 470.400).
----------------------------------------
### Projeto: Time ###
  Estatística W: 7.0
  P-valor: 0.50000
  Hipótese Nula (H₀): NÃO REJEITADA (p-valor ≥ α)
  Conclusão: Não há evidências estatísticas significativas de uma diferença na mediana dos MFRs entre os tipos de matriz para o Projeto Time.
  (Média MFR e001_original: 1153.758, Média MFR e007_NRS3: 1150.758)
----------------------------------------
### Projeto: Lang ###
  Estatística W: 3.0
  P-valor: 0.50000
  Hipótese Nula (H₀): NÃO REJEITADA (p-valor ≥ α)
  Conclusão: Não há evidências estatísticas significativas de uma diferença na mediana dos MFRs entre os tipos de matriz para o Projeto Lang.
  (Média MFR e001_original: 49.750, Média MFR e007_NRS3: 47.417)
----------------------------------------
### Projeto: Mockito ###
  Estatística W: 0.0
  P-valor: 0.03125
  Hipótese Nula (H₀): REJEITADA (p-valor < α)
  Conclusão: Há evidências estatísticas significativas de uma diferença na mediana dos MFRs entre os tipos de matriz para o Projeto Mockito.
  O e001_original (Média MFR: 471.055) tende a apresentar melhor desempenho que o e007_NRS3 (Média MFR: 574.057).
----------------------------------------
```
**Saída do Código**

Fontes:
  - A theoretical analysis on cloning the failed test cases to improve spectrum-based fault localization (Long Zhang, Lanfei Yan, Zhenyu Zhang, Jian Zhang, W.K. Chand, Zheng Zheng).
  - MathWorld, W., The web’s most extensive mathematics resource, 2010Access on: http://mathworld.wolfram.com.
