 # 🔬 Detalhamento da Proposta de Exploração II

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Chart, Lang, Math, Mockito e Time.
- Métricas: ???.
- Heurísticas: ochiai, tarantula, jaccard, op2, barinel e dstar.
- Quantidade mínima de casos de teste: ??.
- Quantidade mínima de casos de teste "+": ??.
- Quantidade mínima de casos de teste "-": ??.

![Total de Testes Repetidos](img/Tab_1_Proposta_Exploracao_II.png "Total de Testes Repetidos")

**Figura 1:** Total de Testes Repetidos (mesma cobertura)

## Descrição dos Experimentos
- **e002_smote_euclidian**
  - A execução das heurísticas foi realizada com a aplicação da técnica de balanceamento de dados SMOTE, adotando como métrica de proximidade a distância Euclidiana. Ressalta-se que tal implementação foi conduzida por meio da biblioteca imblearn.over_sampling. Ademais, o procedimento foi aplicado diretamente sobre a matriz de espectro em sua forma original.
- **e007_smote_euclidian_NRS7**
  - A execução das heurísticas foi realizada por meio da aplicação da técnica de balanceamento de dados SMOTE, utilizando a distância Euclidiana como métrica de proximidade. O procedimento foi implementado com o suporte da biblioteca imblearn.over_sampling e aplicado à matriz de espectro em um formato pré-processado, no qual foi adotado a técnica NRS7 (Noise Reduction Scheme 7) para redução de linhas de casos de teste redundantes, conforme artigo [Improving Fault Localization Using Model-domain Synthesized Failing Test Generation](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/IEEE-Improving_Fault_Localization_Using_Model-domain_Synthesized_Failing_Test_Generation.pdf).
   - Noise Reduction Scheme 7 (NRS7): Este esquema de redução de ruído é uma combinação da aplicação do NRS3 (Noise Reduction Scheme 3) e posteriormente o NRS4 (Noise Reduction Scheme 4).
     - Noise Reduction Scheme 3 (NRS3): para cada conjunto de casos de teste aprovados e reprovados com espectros idênticos, todos os casos de teste do conjunto serão removidos.
     - Noise Reduction Scheme 4 (NRS4): Para cada conjunto de casos de teste aprovados com espectros idênticos, todos, exceto um caso de teste, serão removidos.

