# 📝 Artigos Importantes
Este repositório tem como objetivo documentar os principais artigos científicos estudados ao longo dessa pesquisa. Para cada artigo, estão disponíveis:

- 📌 Título
- 🔗 DOI
- 📥 Link para o artigo
- 📝 Breve descrição
- 📖 Descrição detalhada
---
## 📄 Lista de Artigos

### 1. **Improving Fault Localization Using Model-domain Synthesized Failing Test Generation**
- **DOI**: [10.1109/ICSME55016.2022.00026](https://doi.org/10.1109/ICSME55016.2022.00026)
- **Link para o artigo**: [Improving Fault Localization Using Model-domain Synthesized Failing Test Generation](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/IEEE-Improving_Fault_Localization_Using_Model-domain_Synthesized_Failing_Test_Generation.pdf)

- **Breve descrição**: É proposto uma abordagem para a geração de casos de teste, a partir de amostras defeituosas com o objetivo de aprimorar a precisão das heurísticas utilizadas na localização de defeitos.
<details>
  <summary><strong>Descrição detalhada</strong></summary>
  
  - Contribuições
    - É proposto uma abordagem (técnica de over-sampling SMOTE) para a geração de casos de teste com defeitos sintetizados, a partir de amostras defeituosas extraídas do modelo de domínio (matriz de espectro de fluxo de controle). O objetivo é aprimorar a precisão das heurísticas utilizadas na localização de defeitos.
    - Os experimentos de criação das amostras de testes com defeitos, melhorou significamente as heurísticas de localização de defeitos.
  - Importância do artigo para a pesquisa
    - Foi demonstrado que o procedimento de geração de casos de teste com defeitos sintetizados representa uma estratégia eficaz para aprimorar os dados originais do modelo de domínio. Essa melhoria contribui diretamente para o aumento da precisão das heurísticas de localização de defeitos.
    - As métricas utilizadas foram: Mean Average Rank (MAR), Mean First Rank (MFR) e Relative Improvement (RImp).
</details>

---

### 2. <mark>**Noise Reduction for Spectrum-based Fault Localization**</mark>
- **DOI**: [10.14257/ijca.2013.6.5.11](http://dx.doi.org/10.14257/ijca.2013.6.5.11)
- **Link para o artigo**: [Noise Reduction for Spectrum-based Fault Localization](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/Noise_Reduction_for_Spectrum_based_Fault_Localization.pdf)
- **Breve descrição**: Spectrum-based Fault Localization (SBFL) provou ser uma técnica eficaz para localizar declarações defeituosas no código do programa. As heurísticas SBFL exploram os registros de execução de instruções (espectros) independente se os casos de teste forem aprovados ou reprovados para classificar a probabilidade de uma instrução ser defeituosa. No entanto, em alguns casos, estes espectros contêm informações ou ruído duplicados e ambíguos que podem deteriorar o desempenho das heurísticas SBFL. Esse artigo propoem sete esquemas de redução de ruído para eliminar casos de teste que fornecem informações duplicadas e ambíguas e avaliar as melhorias de desempenho resultantes nas métricas SBFL. Com base nessas explorações, é fornecido um guia para os profissionais de SBFL selecionarem o esquema de redução de ruído com melhor desempenho para determinadas heurísticas SBFL.
<details>
  <summary><strong>Descrição detalhada</strong></summary>

  - Contribuições
    - <mark>A partir da análise realizada nos espectros de programas defeituosos no Siemens Test Suite, observou-se que, em muitas versões dos programas, existem casos de teste com espectros idênticos (registro de cobertura de execução de instruções), embora as entradas de teste sejam diferentes.</mark> Estas observações em casos de teste com espectros idênticos podem ser divididas em três categorias.
	    - Um caso de teste com defeito e um caso de teste aprovado compartilham o mesmo espectro.
	    - Mais de um caso de teste com defeito compartilha o mesmo espectro.
	    - Mais de um caso de teste aprovado compartilha o mesmo espectro.
    - É proposto sete esquemas de redução de ruído para remover e eliminar casos de teste que forneçam informações duplicadas e ambíguas e avaliar as melhorias de desempenho resultantes em mais de 30 heurísticas SBFL estudadas.<mark>
      - <mark>Noise Reduction Scheme 1 (NRS1): para cada caso de teste reprovado, todos os casos de teste aprovados com espectros idênticos ao caso de teste com defeito serão removidos.</mark>
      - <mark>Noise Reduction Scheme 2 (NRS2): para cada caso de teste aprovado, todos os casos de teste reprovados com espectros idênticos ao caso de teste aprovado serão removidos.</mark>
      - <mark>Noise Reduction Scheme 3 (NRS3): para cada conjunto de casos de teste aprovados e reprovados com espectros idênticos, todos os casos de teste do conjunto serão removidos.</mark>
      - <mark>Noise Reduction Scheme 4 (NRS4): Para cada conjunto de casos de teste aprovados com espectros idênticos, todos, exceto um caso de teste, serão removidos.</mark>
      - <mark>Noise Reduction Scheme 5 (NRS5): Este esquema de redução de ruído é uma combinação de NRS4 e NRS1.</mark>
      - <mark>Noise Reduction Scheme 6 (NRS6): Este esquema de redução de ruído é uma combinação de NRS4 e NRS2.</mark>
      - <mark>Noise Reduction Scheme 7 (NRS7): Este esquema de redução de ruído é uma combinação de NRS4 e NRS3.</mark>
    - A partir dos experimentos realizados em 62 versões defeituosas de programas no Siemens Test Suite, foi descoberto que os casos de teste com espectros idênticos podem chegar a 27% no Siemens Test Suite.
    - A percentagem significativa elevada de casos de teste com espectros idênticos é essencialmente ruído para as heurísticas SBFL, o que podem deteriorar o seu desempenho.
  - Importância do artigo para a pesquisa
    - <mark>Foi demonstrado que o procedimento de eliminação dos ruídos da matriz de espectro poderá contribuir de forma significativa com a eficácia das heurísticas SBFL.</mark> 

</details>

---

### 3. <mark>**A Theoretical Analysis on Cloning the Failed Test Cases to Improve Spectrum-based Fault Localization**</mark>
- **DOI**: [10.1016/j.jss.2017.04.017](https://doi.org/10.1016/j.jss.2017.04.017)
- **Link para o artigo**: [A Theoretical Analysis on Cloning the Failed Test Cases to Improve Spectrum-based Fault Localization](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/A%20Theoretical%20Analysis%20on%20Cloning%20the%20Failed%20Test%20Cases%20to%20Improve%20Spectrum-based%20Fault%20Localization.pdf)
- **Breve descrição**: Apesar de trabalhos anteriores terem mostrado empiricamente que a eficácia das técnicas SBFL podem ser melhoradas com mais execuções de casos de teste com defeito, a realidade da depuração frequentemente apresenta um cenário inverso: um número muito reduzido de casos de teste com defeito em comparação com os casos de teste bem-sucedidos. Esse cenário de desequilibrio de classes pode diminuir a precisão das fórmulas SBFL. <mark>Esse artigo, realiza a investigação se a clonagem de casos de teste com defeito pode melhorar a eficácia das heurísticas de localização de defeitos baseadas em espectro de fluxo de controle (SBFL – Spectrum-Based Fault Localization).</mark>
<details>
  <summary><strong>Descrição detalhada</strong></summary>	
	
  - Solução Proposta
  	- <mark>Para mitigar o problema do desequilíbrio de classes sem perder informações valiosas dos testes existentes, os autores propõem uma **estratégia de clonagem**. A ideia é replicar o conjunto de casos de teste falhos até que seu tamanho se aproxime ou se iguale ao número de casos de teste bem-sucedidos.</mark>
  - Experimento produzido:
	- 33 fórmulas SBFL avaliadas.
	- 12 programas como benchmark foram utilizados.
	- O experimento considerou os seguintes cenários de defeito: Single-fault (versões de programa com um único defeito conhecido), Double-fault (versões de programa com dois defeitos sintetizados), Triple-fault (versões de programas com três defeitos sintetizados).
  - Análise Estatística
  	- Para determinar a significância dos resultados empíricos, foi empregado o teste de Wilcoxon Signed Rank, com um nível de significância de 0.05.
  - Detalhes do Processo de Clonagem
	- <mark>A abordagem dos autores é uma estratégia baseada em adição. Eles optaram por adicionar "cópias" dos testes com defeito existentes. É importante notar que essa clonagem é conceitual e matemática, não implicando na criação de inúmeras cópias físicas dos casos de teste e sua reexecução. O artigo enfatiza que o benefício é a manipulação das fórmulas das técnicas SBFL.</mark>
	- A fórmula para o fator de clonagem c é: c = (P / F) Onde: P (é o número de casos de teste bem-sucedidos) e F (é o número de casos de teste falhos). Isso significa que cada um dos F casos de teste falhos serão clonados c vezes.
	- As fórmulas SBFL dependem de parâmetros como aef (número de casos de teste falhos que executam uma entidade de programa), anf (número de casos de teste falhos que não executam uma entidade de programa), aep (número de casos de teste passados que executam uma entidade de programa) e anp (número de casos de teste passados que não executam uma entidade de programa) e após a clonagem esses parâmatros ficam da seguinte forma: aef, anf, (c * aep) e (c * anp).
  - Por que essa abordagem foi utilizada?
	- <mark>Eficiência Computacional: É uma operação matemática simples (fator de clonagem * valor da variável) que tem um custo computacional muito baixo. Reexecutar testes ou manipular matrizes gigantescas não seria interessante.</mark>
	- <mark>Foco na Análise: Permite uma análise matemática mais direta do impacto nas fórmulas SBFL, já que a mudança é essencialmente uma ponderação dos argumentos das fórmulas.</mark>
	- <mark>Viabilidade: Permite que a técnica seja aplicada mesmo em grandes projetos de software onde o custo de geração de mais testes falhos ou a alteração da matriz de cobertura seria impraticável.</mark>
  - Métricas utilizadas
	- Avg expense: Custo médio para localizar um defeito.
	- Max expense: Similar ao Avg, mas considera o defeito como o último a ser encontrado em caso de empate.
	- Top-5 e Top-5‰: Avaliam se o defeito foi localizada dentro das 5 primeiras posições ou dos 5‰ das entidades com maior suspeita.
  - Contribuições:
	- <mark>O estudo demonstra de forma robusta, que a estratégia de clonagem de casos de teste com defeito é uma abordagem eficaz e benéfica para melhorar (ou, no mínimo, 	preservar) a precisão das fórmulas de localização de defeitos baseada em espectro para a maioria das fórmulas analisadas. Esta técnica oferece um método de baixo custo computacional para lidar com o problema de desequilíbrio de classes em conjuntos de testes.	</mark>	
  - Importância do artigo para a pesquisa
    - Demonstra que a clonagem de casos de testes com defeito é uma estratégia eficaz e de baixo custo computacional para melhorar a eficácia das heurísticas de localização de defeitos.
		
</details>
