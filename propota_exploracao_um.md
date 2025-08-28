# 🔬 Detalhamento da Proposta de Exploração I

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Chart, Lang, Math, Mockito e Time.
- Métricas: ACC@N.
- Heurísticas: ochiai, tarantula, jaccard, op2, barinel e dstar.
- Quantidade mínima de casos de teste: 22.
- Quantidade mínima de casos de teste "+": 11.
- Quantidade mínima de casos de teste "-": 11.

![Resumo geral dos casos de teste](img/Tab_1_Proposta_Exploracao_I.png "Resumo geral dos casos de teste")

**Figura 1:** Resumo geral dos casos de teste

![Resumo geral dos casos de teste negativos](img/Tab_Resumo_Casos_Teste_Negativos.png "Resumo geral dos casos de teste negativos")

**Figura 2:** Resumo geral dos casos de teste negativos

## Descrição dos Experimentos
- **e001_original**
  - Execução das heurísticas sem a aplicação de qualquer tipo de balanceamento de dados.
- **e002_smote_euclidian**
  - Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância Euclidiana. É importante destacar que essa execução foi realizada com o uso da biblioteca "imblearn.over_sampling".
- **e003_smote_interpolation**
  - Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância Euclidiana. É importante destacar que essa execução foi realizada com o algoritmo original do Smote (sem uso da biblioteca "imblearn.over_sampling") e a geração das novas amostras sintéticas incluiu o arredondamento dos valores dos atributos, em vez do truncamento.
      
```python
#return X_new.astype(X.dtype)        
return np.round(X_new).astype(X.dtype)
```    
- **e004_smote_jaccard**
  - Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância de Jaccard. É importante destacar que essa execução foi realizada com o algoritmo original do Smote (sem uso da biblioteca "imblearn.over_sampling").
- **e005_smote_hamming**
  - Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância de Hamming. É importante destacar que essa execução foi realizada com o algoritmo original do Smote (sem uso da biblioteca "imblearn.over_sampling").
- **e006_smote_cosine**
  - Execução das heurísticas com a aplicação da técnica de balanceamento de dados SMOTE, utilizando o cálculo de distância de Cosine. É importante destacar que essa execução foi realizada com o algoritmo original do Smote (sem uso da biblioteca "imblearn.over_sampling").
  
## Resultados

![Resultado do Experimento da Proposta de Exploração I](img/Tab_2_Proposta_Exploracao_I.png "Resultado do Experimento da Proposta de Exploração I")

**Figura 3:** Resultado do Experimento da Proposta de Exploração I

## Análise dos Resultados
- Observou-se que os valores de cada heurística exibiram uniformidade ao longo de todos os experimentos simulados. Presume-se que tal ocorrência esteja diretamente relacionada à limitada quantidade de casos de teste remanescentes após a aplicação dos critérios de seleção, que precederam a fase de simulação. Como próximas etapas, propõe-se:
  - Aumentar a quantidade de casos de teste remanescentes através da alteração dos critérios de seleção (Quantidade mínima de casos de teste: 10, Quantidade mínima de casos de teste "+": 5 e Quantidade mínima de casos de teste "-": 5), a fim de investigar se a uniformidade dos dados será atenuada.
  - Avaliar para cada experimento, o volume de casos de teste não duplicados gerados pelo balanceador. Acredita-se que a geração de um maior número de casos de teste não duplicados promoverá um melhor desempenho das heurísticas."

