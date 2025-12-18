# 🔬 Detalhamento da Proposta de Exploração VIII

## Características do ambiente de execução
- Projeto: Defects4J.
- Programas: Chart.
- Versão: 16.
- Quantidade mínima de casos de teste: 4.
- Quantidade mínima de casos de teste "+": 2.
- Quantidade mínima de casos de teste "-": 2.

## Descrição dos experimento
Este experimento propõe uma investigação comparativa entre a técnica de balanceamento SMOTE, em sua versão canônica, e técnicas de balanceamento derivadas do Smote, tais como: Smotenc, Smoten, Adasyn, BorderlineSmote, KMeansSmote e SVMSmote.

- **Smote**
  - O algoritmo base que cria amostras sintéticas através da interpolação linear entre vizinhos próximos da classe minoritária.
- **Smotenc**
  - (Nominal and Continuous). Projetado para datasets mistos. Ele identifica quais colunas são categóricas e aplica um tratamento diferenciado nelas durante a geração.
- **Smoten**
  - (Nominal). Uma variação dedicada exclusivamente a datasets onde todos os atributos são categóricos, utilizando métricas de distância apropriadas para categorias.
- **Adasyn**
  - (Adaptive Synthetic). Similar ao SMOTE, mas foca em gerar mais dados para exemplos da classe minoritária que são "difíceis de aprender" (aqueles cercados por muitos pontos da classe majoritária).
- **BorderlineSmote**
  - Foca a geração de dados apenas na "fronteira" (borderline) entre as classes, evitando criar amostras em áreas onde a classe minoritária já está bem representada.
- **KMeansSmote**
  - Utiliza o algoritmo K-Means para agrupar os dados antes do over-sampling, gerando amostras apenas em clusters onde a classe minoritária é predominante, o que ajuda a evitar a criação de ruído.
- **SVMSmote**
  - Usa um classificador SVM para encontrar os vetores de suporte (os pontos mais próximos da fronteira de decisão) e gera novas amostras ao redor desses pontos críticos.
