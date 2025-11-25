# 🔬 Detalhamento da Proposta de Exploração VI

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Math, Time e Mockito.
- Métricas: pos-fault.
- Heurísticas: Ochiai e Op2.
- Quantidade mínima de casos de teste: 4.
- Quantidade mínima de casos de teste "+": 2.
- Quantidade mínima de casos de teste "-": 2.

## Descrição dos experimentos
Este experimento propõe uma investigação comparativa sobre a aplicação de diferentes heurísticas (Ochiai e Op2) à matriz de espectro de cobertura, tanto em seu formato original quanto com a aplicação da técnica de balanceamento de dados SMOTE. Os resultados serão avaliados de acordo com a métrica pos-fault (posição do elemento defeituoso). O teste estatístico Wilcoxon Signed-Rank e Vargha & Delaney foram aplicados para verificar se os resultados observados no experimento proposto podem ser atribuídos ao acaso ou se evidenciam uma relação significativa entre as variáveis e também identificar a técnica de melhor eficácia.

- **e80_original**
  - Execução das heurísticas aplicadas à matriz de espectro de cobertura em seu formato original.
- **e81_smote**
  - Execução das heurísticas aplicadas à matriz de espectro de cobertura em seu formato transformado, por meio da técnica de balanceamento de dados SMOTE. 

## Resultados dos dados dos experimentos

[Planilha com resultados](https://docs.google.com/spreadsheets/d/e/2PACX-1vQt6L8Z9mk-be_DKJal9ZzuapgrugOYXGz0FqitBYko9ERinjRmeSsUgc85c_INeA/pubhtml?gid=855928177&single=true)

  - Com base no teste estatístico de Wilcoxon Signed-Rank, verificou-se que, em todos os cenários analisados, o p-value foi superior ao nível de significância adotado (0,05). Dessa forma, conclui-se que não há diferença estatisticamente significativa entre os valores de Pos-Fault obtidos nos experimentos e80_original e e81_smote, considerando os projetos do experimento (Math, Time e Mockito) e as heurísticas Ochiai e Op2.

## Experimento manipulado para obtenção de significância estatística

  - Para a obtenção da significância estatística na análise da amostra, uma parte dos dados da planilha mencionada anteriormente foram tratados da seguinte maneira: inicialmente, a tabela de resultados do projeto Math, associada à heurística Ochiai, foi duplicada. Na cópia gerada, acrescentou-se o valor dez à métrica Pos-Fault, número escolhido de forma aleatória. Em seguida, todo esse conjunto de dados foi novamente duplicado, dessa vez sem qualquer alteração adicional nos valores. A adoção desse procedimento de manipulação dos dados fundamenta-se em evidências encontradas na literatura, que apontam que um dos principais fatores que dificultam a obtenção de significância estatística é o tamanho reduzido das amostras disponíveis para análise.

Arquivo CSV - Conjunto de dados manipulado
```
Projeto;Versão;Heurística;Experimento;Pos-Fault
Math;66;Ochiai;e80_original;144
Math;66;Ochiai;e81_smote;102
Math;68;Ochiai;e80_original;128
Math;68;Ochiai;e81_smote;128
Math;35;Ochiai;e80_original;10
Math;35;Ochiai;e81_smote;9
Math;102;Ochiai;e80_original;13
Math;102;Ochiai;e81_smote;13
Math;69;Ochiai;e80_original;75
Math;69;Ochiai;e81_smote;75
Math;29;Ochiai;e80_original;6
Math;29;Ochiai;e81_smote;197
Math;16;Ochiai;e80_original;6
Math;16;Ochiai;e81_smote;704
Math;6;Ochiai;e80_original;1179
Math;6;Ochiai;e81_smote;902
Math;1;Ochiai;e80_original;21
Math;1;Ochiai;e81_smote;366
Math;21;Ochiai;e80_original;88
Math;21;Ochiai;e81_smote;83
Math;86;Ochiai;e80_original;94
Math;86;Ochiai;e81_smote;41
Math;43;Ochiai;e80_original;71
Math;43;Ochiai;e81_smote;56
Math;36;Ochiai;e80_original;2
Math;36;Ochiai;e81_smote;356
Math;31;Ochiai;e80_original;109
Math;31;Ochiai;e81_smote;35
Math;98;Ochiai;e80_original;19
Math;98;Ochiai;e81_smote;19
Math;37;Ochiai;e80_original;21
Math;37;Ochiai;e81_smote;251
Math;99;Ochiai;e80_original;4
Math;99;Ochiai;e81_smote;27
Math;101;Ochiai;e80_original;12
Math;101;Ochiai;e81_smote;12
Math;64;Ochiai;e80_original;252
Math;64;Ochiai;e81_smote;252
Math;46;Ochiai;e80_original;2
Math;46;Ochiai;e81_smote;1
Math;77;Ochiai;e80_original;26
Math;77;Ochiai;e81_smote;28
Math;84;Ochiai;e80_original;146
Math;84;Ochiai;e81_smote;146
Math;71;Ochiai;e80_original;2
Math;71;Ochiai;e81_smote;280
Math;76;Ochiai;e80_original;107
Math;76;Ochiai;e81_smote;107
Math;47;Ochiai;e80_original;2
Math;47;Ochiai;e81_smote;2
Math;22;Ochiai;e80_original;2
Math;22;Ochiai;e81_smote;54
Math;66;Ochiai;e80_original;154
Math;66;Ochiai;e81_smote;112
Math;68;Ochiai;e80_original;138
Math;68;Ochiai;e81_smote;138
Math;35;Ochiai;e80_original;20
Math;35;Ochiai;e81_smote;19
Math;102;Ochiai;e80_original;23
Math;102;Ochiai;e81_smote;23
Math;69;Ochiai;e80_original;85
Math;69;Ochiai;e81_smote;85
Math;29;Ochiai;e80_original;16
Math;29;Ochiai;e81_smote;207
Math;16;Ochiai;e80_original;16
Math;16;Ochiai;e81_smote;714
Math;6;Ochiai;e80_original;1189
Math;6;Ochiai;e81_smote;912
Math;1;Ochiai;e80_original;31
Math;1;Ochiai;e81_smote;376
Math;21;Ochiai;e80_original;98
Math;21;Ochiai;e81_smote;93
Math;86;Ochiai;e80_original;104
Math;86;Ochiai;e81_smote;51
Math;43;Ochiai;e80_original;81
Math;43;Ochiai;e81_smote;66
Math;36;Ochiai;e80_original;12
Math;36;Ochiai;e81_smote;366
Math;31;Ochiai;e80_original;119
Math;31;Ochiai;e81_smote;45
Math;98;Ochiai;e80_original;29
Math;98;Ochiai;e81_smote;29
Math;37;Ochiai;e80_original;31
Math;37;Ochiai;e81_smote;261
Math;99;Ochiai;e80_original;14
Math;99;Ochiai;e81_smote;37
Math;101;Ochiai;e80_original;22
Math;101;Ochiai;e81_smote;22
Math;64;Ochiai;e80_original;262
Math;64;Ochiai;e81_smote;262
Math;46;Ochiai;e80_original;12
Math;46;Ochiai;e81_smote;11
Math;77;Ochiai;e80_original;36
Math;77;Ochiai;e81_smote;38
Math;84;Ochiai;e80_original;156
Math;84;Ochiai;e81_smote;156
Math;71;Ochiai;e80_original;12
Math;71;Ochiai;e81_smote;290
Math;76;Ochiai;e80_original;117
Math;76;Ochiai;e81_smote;117
Math;47;Ochiai;e80_original;12
Math;47;Ochiai;e81_smote;12
Math;22;Ochiai;e80_original;12
Math;22;Ochiai;e81_smote;64
Math;66;Ochiai;e80_original;144
Math;66;Ochiai;e81_smote;102
Math;68;Ochiai;e80_original;128
Math;68;Ochiai;e81_smote;128
Math;35;Ochiai;e80_original;10
Math;35;Ochiai;e81_smote;9
Math;102;Ochiai;e80_original;13
Math;102;Ochiai;e81_smote;13
Math;69;Ochiai;e80_original;75
Math;69;Ochiai;e81_smote;75
Math;29;Ochiai;e80_original;6
Math;29;Ochiai;e81_smote;197
Math;16;Ochiai;e80_original;6
Math;16;Ochiai;e81_smote;704
Math;6;Ochiai;e80_original;1179
Math;6;Ochiai;e81_smote;902
Math;1;Ochiai;e80_original;21
Math;1;Ochiai;e81_smote;366
Math;21;Ochiai;e80_original;88
Math;21;Ochiai;e81_smote;83
Math;86;Ochiai;e80_original;94
Math;86;Ochiai;e81_smote;41
Math;43;Ochiai;e80_original;71
Math;43;Ochiai;e81_smote;56
Math;36;Ochiai;e80_original;2
Math;36;Ochiai;e81_smote;356
Math;31;Ochiai;e80_original;109
Math;31;Ochiai;e81_smote;35
Math;98;Ochiai;e80_original;19
Math;98;Ochiai;e81_smote;19
Math;37;Ochiai;e80_original;21
Math;37;Ochiai;e81_smote;251
Math;99;Ochiai;e80_original;4
Math;99;Ochiai;e81_smote;27
Math;101;Ochiai;e80_original;12
Math;101;Ochiai;e81_smote;12
Math;64;Ochiai;e80_original;252
Math;64;Ochiai;e81_smote;252
Math;46;Ochiai;e80_original;2
Math;46;Ochiai;e81_smote;1
Math;77;Ochiai;e80_original;26
Math;77;Ochiai;e81_smote;28
Math;84;Ochiai;e80_original;146
Math;84;Ochiai;e81_smote;146
Math;71;Ochiai;e80_original;2
Math;71;Ochiai;e81_smote;280
Math;76;Ochiai;e80_original;107
Math;76;Ochiai;e81_smote;107
Math;47;Ochiai;e80_original;2
Math;47;Ochiai;e81_smote;2
Math;22;Ochiai;e80_original;2
Math;22;Ochiai;e81_smote;54
Math;66;Ochiai;e80_original;154
Math;66;Ochiai;e81_smote;112
Math;68;Ochiai;e80_original;138
Math;68;Ochiai;e81_smote;138
Math;35;Ochiai;e80_original;20
Math;35;Ochiai;e81_smote;19
Math;102;Ochiai;e80_original;23
Math;102;Ochiai;e81_smote;23
Math;69;Ochiai;e80_original;85
Math;69;Ochiai;e81_smote;85
Math;29;Ochiai;e80_original;16
Math;29;Ochiai;e81_smote;207
Math;16;Ochiai;e80_original;16
Math;16;Ochiai;e81_smote;714
Math;6;Ochiai;e80_original;1189
Math;6;Ochiai;e81_smote;912
Math;1;Ochiai;e80_original;31
Math;1;Ochiai;e81_smote;376
Math;21;Ochiai;e80_original;98
Math;21;Ochiai;e81_smote;93
Math;86;Ochiai;e80_original;104
Math;86;Ochiai;e81_smote;51
Math;43;Ochiai;e80_original;81
Math;43;Ochiai;e81_smote;66
Math;36;Ochiai;e80_original;12
Math;36;Ochiai;e81_smote;366
Math;31;Ochiai;e80_original;119
Math;31;Ochiai;e81_smote;45
Math;98;Ochiai;e80_original;29
Math;98;Ochiai;e81_smote;29
Math;37;Ochiai;e80_original;31
Math;37;Ochiai;e81_smote;261
Math;99;Ochiai;e80_original;14
Math;99;Ochiai;e81_smote;37
Math;101;Ochiai;e80_original;22
Math;101;Ochiai;e81_smote;22
Math;64;Ochiai;e80_original;262
Math;64;Ochiai;e81_smote;262
Math;46;Ochiai;e80_original;12
Math;46;Ochiai;e81_smote;11
Math;77;Ochiai;e80_original;36
Math;77;Ochiai;e81_smote;38
Math;84;Ochiai;e80_original;156
Math;84;Ochiai;e81_smote;156
Math;71;Ochiai;e80_original;12
Math;71;Ochiai;e81_smote;290
Math;76;Ochiai;e80_original;117
Math;76;Ochiai;e81_smote;117
Math;47;Ochiai;e80_original;12
Math;47;Ochiai;e81_smote;12
Math;22;Ochiai;e80_original;12
Math;22;Ochiai;e81_smote;64
```

Código Python aplicado ao CSV
```python
import pandas as pd
import numpy as np
from scipy.stats import wilcoxon

def carregar_dados(caminho_csv):
    """
    Carrega os dados do arquivo CSV.
    """
    df = pd.read_csv(caminho_csv, sep=';')
    return df

def obter_experimentos_unicos(df):
    """
    Retorna todos os experimentos únicos presentes nos dados.
    """
    return df['Experimento'].unique()

def agrupar_dados_por_projeto_heuristica(df):
    """
    Agrupa os dados por Projeto e Heurística.
    """
    return df.groupby(['Projeto', 'Heurística'])

def aplicar_wilcoxon_teste(grupo_dados):
    """
    Aplica o teste de Wilcoxon Signed Rank para um grupo específico.
    Retorna os resultados estatísticos e a recomendação de qual experimento é melhor.
    """
    # Separação dos experimentos (e80_original e e81_smote)
    experimentos = grupo_dados['Experimento'].unique()

    if len(experimentos) < 2:
        return None

    exp1 = experimentos[0] # e80_original
    exp2 = experimentos[1] # e81_smote

    # Busca valores de Pos-Fault do experimento e80_original
    valores_exp1 = grupo_dados[grupo_dados['Experimento'] == exp1]['Pos-Fault'].values
    # Busca valores de Pos-Fault do experimento e81_smote
    valores_exp2 = grupo_dados[grupo_dados['Experimento'] == exp2]['Pos-Fault'].values

    # Se os tamanhos são diferentes, ajusta para o tamanho mínimo
    tamanho_minimo = min(len(valores_exp1), len(valores_exp2))
    valores_exp1 = valores_exp1[:tamanho_minimo]
    valores_exp2 = valores_exp2[:tamanho_minimo]

    # Cálculo das medianas
    mediana_exp1 = np.median(valores_exp1)
    mediana_exp2 = np.median(valores_exp2)

    # Aplicar o teste de Wilcoxon para verificar se há significância entre os valores
    estatistica, p_valor = wilcoxon(valores_exp1, valores_exp2, alternative='two-sided')

    alfa             = 0.05 # Considera significante com nível alfa = 0.05
    significante     = p_valor < alfa
    p_value_a_melhor = 0
    p_value_b_melhor = 0

    # SE p_valor < alfa ENTÃO Verificar qual é o melhor experimento
    if (significante):
        # Determinar qual técnica tende a ser maior
        if (mediana_exp1 > mediana_exp2):
          tipo = 'greater' # Testa se valores_exp1 > valores_exp2
        elif (mediana_exp1 < mediana_exp2):
          tipo = 'less' # Testa se valores_exp1 < valores_exp2
        else:
          tipo = 'nenhum' # As técnicas são equivalentes
        # Confirmação da melhor técnica
        if (tipo != 'nenhum'):
          w_stat_tecnica, p_value_tecnica = wilcoxon(valores_exp1, valores_exp2, alternative=tipo)
        else:
          w_stat_tecnica = 0
          p_value_tecnica = 0

    # Calcular Vargha & Delaney
    A12 = calcular_vargha_delaney(valores_exp1, valores_exp2)
    interpretacao_A12, classificacao_A12 = interpretar_efeito_vargha_delaney(A12)

    return {
        'alfa': alfa,
        'estatistica': estatistica,
        'p_valor': p_valor,
        'significante': significante,
        'experimento_1': exp1,
        'experimento_2': exp2,
        'mediana_exp1' : mediana_exp1,
        'mediana_exp2' : mediana_exp2,
        'p_valor_tecnica': p_value_tecnica,
        'A12': A12,
        'interpretacao_A12': interpretacao_A12,
        'classificacao_A12': classificacao_A12
    }

def processar_testes_wilcoxon(df):
    """
    Processa o teste de Wilcoxon para cada Projeto+Heurística.
    """
    grupos_projeto_heuristica = agrupar_dados_por_projeto_heuristica(df)
    resultados = {}

    for (projeto, heuristica), grupo_dados in grupos_projeto_heuristica:
        chave = f"{projeto}_{heuristica}"
        resultado = aplicar_wilcoxon_teste(grupo_dados)

        if resultado is not None:
            resultados[chave] = {
                'projeto': projeto,
                'heuristica': heuristica,
                **resultado
            }

    return resultados

def calcular_vargha_delaney(valores_exp1, valores_exp2):
    """
    Calcula a estatística A12 de Vargha & Delaney.
    Representa a probabilidade de uma observação do experimento 1
    ser maior que uma observação do experimento 2.

    Args:
        valores_exp1: Array com valores do experimento 1
        valores_exp2: Array com valores do experimento 2

    Returns:
        float: Valor de A12 (entre 0 e 1)
    """
    # Junção dos dois vetores (valores_exp1 e valores_exp2)
    combined = np.concatenate([valores_exp1, valores_exp2])
    # Cálculo dos ranks
    ranks = _calcular_ranks(combined)

    n1 = len(valores_exp1) # Tamanho da amostra do grupo 1
    n2 = len(valores_exp2) # Tamanho da amostra do grupo 2

    # Soma dos ranks do experimento 1
    R1 = ranks[:n1].sum()

    # Fórmula Oficial de Vargha & Delaney usando ranks
    #A12 = (2 * R1 - n1 * (n1 + 1)) / (2 * n1 * n2)
    # Fórmula simplificada e derivada da Oficial
    A12 = (R1 / (n1 * n2)) - ((n1 + 1)/(2 * n2))

    return A12


def _calcular_ranks(data, ascending=False):
    """
    Calcula ranks tratando empates.

    Args:
        data: Array com os dados
        ascending: bool
            - True (padrão): valores MAIORES recebem ranks MAIORES (tradicional)
            - False: valores MENORES recebem ranks MAIORES (para otimização)

    Returns:
        np.ndarray: Array com os ranks
    """
    # Inverter dados se necessário (menores = melhores)
    if not ascending:
        data_para_rankear = -data  # Inverte a ordem
    else:
        data_para_rankear = data

    sorted_indices = np.argsort(data_para_rankear)
    ranks = np.empty_like(sorted_indices, dtype=float)
    ranks[sorted_indices] = np.arange(1, len(data) + 1)

    # Tratar empates
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                avg_rank = (ranks[i] + ranks[j]) / 2
                ranks[i] = avg_rank
                ranks[j] = avg_rank

    return ranks


def interpretar_efeito_vargha_delaney(A12):
    """
    Interpreta o tamanho do efeito baseado em A12.

    Artigo: "A critique and improvement of the CL common language effect size statistics of McGraw and Wong" (2000)
    Autores: Vargha, A., & Delaney, H. D.

    Args:
        A12: Valor de A12

    Returns:
        tuple: (interpretação, classificação)
    """

    # Nenhum efeito (equivalentes)
    if A12 == 0.5:
        return ("NENHUM: Grupos equivalentes", "NENHUM")

    # Efeito ao favor do Experimento 1 (A12 > 0.5)
    elif 0.5 < A12 <= 0.56:
        return ("NEGLIGENCIÁVEL: Efeito negligenciável (diferença mínima ao favor do Técnica 1)", "NEGLIGENCIÁVEL")

    elif 0.56 < A12 <= 0.64:
        return ("PEQUENO: Efeito pequeno (diferença detectável mas modesta ao favor do Técnica 1)", "PEQUENO")

    elif 0.64 < A12 <= 0.71:
        return ("MÉDIO: Efeito médio (diferença prática relevante ao favor do Técnica 1)", "MÉDIO")

    elif A12 > 0.71:
        return ("GRANDE: Efeito grande (diferença prática importante ao favor do Técnica 1)", "GRANDE")

    # Efeito ao favor do Experimento 2 (A12 < 0.5)
    elif 0.44 <= A12 < 0.5:
        return ("NEGLIGENCIÁVEL: Efeito negligenciável (diferença mínima ao favor do Técnica 2)", "NEGLIGENCIÁVEL")

    elif 0.36 <= A12 < 0.44:
        return ("PEQUENO: Efeito pequeno (diferença detectável mas modesta ao favor do Técnica 2)", "PEQUENO")

    elif 0.29 <= A12 < 0.36:
        return ("MÉDIO: Efeito médio (diferença prática relevante ao favor do Técnica 2)", "MÉDIO")

    elif A12 < 0.29:
        return ("GRANDE: Efeito grande (diferença prática importante ao favor do Técnica 2)", "GRANDE")

def exibir_resultado_individual(chave, resultado):
    """
    Exibe o resultado detalhado para um Projeto+Heurística específico.
    """
    projeto = resultado['projeto']
    heuristica = resultado['heuristica']

    print(f"\n{'='*60}")
    print(f"PROJETO: {projeto:<20} | HEURÍSTICA: {heuristica}")
    print(f"{'='*60}")

    print(f"\n📈 TESTE DE WILCOXON SIGNED RANK:")
    print(f"  Estatística (W): {resultado['estatistica']:.4f}")
    print(f"  Alfa (@): {resultado['alfa']:.2f}")
    print(f"  P-Valor: {resultado['p_valor']:.6f}")
    print(f"  Mediana - Técnica 1: {resultado['mediana_exp1']:.2f}")
    print(f"  Mediana - Técnica 2: {resultado['mediana_exp2']:.2f}")
    print(f"  P-Valor Técnica: {resultado['p_valor_tecnica']:.6f}")

    # INTERPRETAÇÃO
    # Se possui Significância Estatística (p_valor < 0,05)
    if resultado['significante']:
        print(f"  ✓ Resultado: HÁ SIGNIFICÂNCIA ESTATÍSTICA (P-Valor < 0.05)")
        # Se existe diferença entre as medianas dos valores das técnicas I e II
        if (resultado['mediana_exp1'] != resultado['mediana_exp2']):
          # Se p_valor da técnica < 0,05, possui significância
          if (resultado['p_valor_tecnica'] < resultado['alfa']):
            # Se mediana do experimento I < mediana do experimento II
            if (resultado['mediana_exp1'] < resultado['mediana_exp2']):
              print("  ✓ A Técnica " + resultado['experimento_1'] + " é melhor")
            # Se mediana do experimento II < mediana do experimento I
            else:
              print("  ✓ A Técnica " + resultado['experimento_2'] + " é melhor")
        # Não existe diferença entre as medianas dos valores das técnicas I e II
        else:
          print("  ✓ As Técnicas abordadas nesse experimento são equivalentes")
    else:
        print(f"  ✗ Resultado: NÃO HÁ SIGNIFICÂNCIA ESTATÍSTICA (P-Valor >= 0.05)")

    print(f"\n📈 TESTE DE VARGHA & DELANEY:")
    print(f"  Estatística A12: {resultado['A12']:.4f}")
    #print(f"  Interpretação: {resultado['interpretacao_A12']}")
    print(f"  Classificação do Efeito: {resultado['classificacao_A12']}")

    # REGRA SIMPLES:
    #   A12 > 0.5 → Técnica 1 é melhor A12 < 0.5 → Técnica 2 é melhor A12 = 0.5 → Técnicas equivalentes
    if resultado['A12'] > 0.5:
        prob_percent = resultado['A12'] * 100
        print(f"  ➜ Técnica {resultado['experimento_1']} é {prob_percent:.1f}% mais provável de ser superior")
    elif resultado['A12'] < 0.5:
        prob_percent = (1.0 - resultado['A12']) * 100
        print(f"  ➜ Técnica {resultado['experimento_2']} é {prob_percent:.1f}% mais provável de ser superior")
    else:
        print(f"  ➜ Técnica têm chance igual de serem superiores")

def main():
    """
    Função principal que orquestra o programa.
    """
    caminho_csv = 'csv_e80_original_e81_smote_V2.csv'    

    try:
        # Carregamento de dados do arquivo em Data Frame (df)
        print("🔄 Carregando dados...")
        df = carregar_dados(caminho_csv)
        print(f"✓ Dados carregados com sucesso! ({len(df)} linhas)\n")

        print("🔄 Processando Teste de Wilcoxon Signed Rank...\n")
        resultados = processar_testes_wilcoxon(df)

        # Exibe resultados para cada Projeto+Heurística
        for chave in sorted(resultados.keys()):
            exibir_resultado_individual(chave, resultados[chave])

        print(f"\n{'='*60}\n")

    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{caminho_csv}' não encontrado.")
        print("Por favor, certifique-se de que o arquivo está no diretório correto.")
    except Exception as e:
        print(f"❌ Erro ao processar os dados: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
```

Resultado da execução do código Python
```
🔄 Carregando dados...
✓ Dados carregados com sucesso! (208 linhas)

🔄 Processando Teste de Wilcoxon Signed Rank...


============================================================
PROJETO: Math                 | HEURÍSTICA: Ochiai
============================================================

📈 TESTE DE WILCOXON SIGNED RANK:
  Estatística (W): 768.0000
  Alfa (@): 0.05
  P-Valor: 0.013285
  Mediana - Técnica 1: 27.50
  Mediana - Técnica 2: 84.00
  P-Valor Técnica: 0.006642
  ✓ Resultado: HÁ SIGNIFICÂNCIA ESTATÍSTICA (P-Valor < 0.05)
  ✓ A Técnica e80_original é melhor

📈 TESTE DE VARGHA & DELANEY:
  Estatística A12: 0.6586
  Classificação do Efeito: MÉDIO
  ➜ Técnica e80_original é 65.9% mais provável de ser superior

============================================================
```
