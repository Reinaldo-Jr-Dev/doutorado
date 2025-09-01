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

### 2. **A Theoretical Analysis on Cloning the Failed Test Cases to Improve Spectrum-based Fault Localization**
- **DOI**: [10.1016/j.jss.2017.04.017](https://doi.org/10.1016/j.jss.2017.04.017)
- **Link para o artigo**: [A Theoretical Analysis on Cloning the Failed Test Cases to Improve Spectrum-based Fault Localization](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/A%20Theoretical%20Analysis%20on%20Cloning%20the%20Failed%20Test%20Cases%20to%20Improve%20Spectrum-based%20Fault%20Localization.pdf)
- **Breve descrição**: Realizar a investigação se a clonagem de casos de teste com defeito pode melhorar a eficácia das heurísticas de localização de defeitos baseadas em espectro de fluxo de controle (SBFL – Spectrum-Based Fault Localization), especialmente em cenários em que há poucos testes com defeito.
<details>
  <summary><strong>Descrição detalhada</strong></summary>

  - Contribuições
    - A proposta de clonagem dos casos de teste com defeito melhorou a precisão das principais heurísticas SBFL (de 33 heurísticas avaliadas, 22 heurísticas no cenário de um defeito, 21 em dois defeitos e 23 em três defeitos obtiveram melhores resultados), com base na métrica AVG Expense (quanto esforço é necessário para localizar o defeito na lista de suspeitos).
    - É apresentado de maneira empírica que a clonagem dos testes com defeito pode melhorar as heurísticas de localização de defeitos.
    - A proposta apresentada é uma abordagem simples e eficiente (em termos computacionais) para lidar com amostras desbalanceadas.
  - Importância do artigo para a pesquisa
    - Demonstra que a clonagem de casos de testes com defeito é uma estratégia eficaz e de baixo custo computacional para melhorar a eficácia das heurísticas de localização de defeitos, especialmente quando há poucos testes com defeito disponíveis.
</details>

---

### 3. **Noise Reduction for Spectrum-based Fault Localization**
- **DOI**: [10.14257/ijca.2013.6.5.11](http://dx.doi.org/10.14257/ijca.2013.6.5.11)
- **Link para o artigo**: [Noise Reduction for Spectrum-based Fault Localization](https://github.com/Reinaldo-Jr-Dev/doutorado/blob/article/Noise_Reduction_for_Spectrum_based_Fault_Localization.pdf)
- **Breve descrição**: Spectrum-based Fault Localization (SBFL) provou ser uma técnica eficaz para localizar declarações defeituosas no código do programa. As heurísticas SBFL exploram os registros de execução de instruções (espectros) independente se os casos de teste forem aprovados ou reprovados para classificar a probabilidade de uma instrução ser defeituosa. No entanto, em alguns casos, estes espectros contêm informações ou ruído duplicados e ambíguos que podem deteriorar o desempenho das heurísticas SBFL. Esse artigo propoem sete esquemas de redução de ruído para eliminar casos de teste que fornecem informações duplicadas e ambíguas e avaliar as melhorias de desempenho resultantes nas métricas SBFL. Com base nessas explorações, é fornecido um guia para os profissionais de SBFL selecionarem o esquema de redução de ruído com melhor desempenho para determinadas heurísticas SBFL.
<details>
  <summary><strong>Descrição detalhada</strong></summary>

  - Contribuições
    - A partir da análise realizada nos espectros de programas defeituosos no Siemens Test Suite, observou-se que, em muitas versões dos programas, existem casos de teste com espectros idênticos (registro de cobertura de execução de instruções), embora as entradas de teste sejam diferentes. Estas observações em casos de teste com espectros idênticos podem ser divididas em três categorias.
	    - Um caso de teste com defeito e um caso de teste aprovado compartilham o mesmo espectro.
	    - Mais de um caso de teste com defeito compartilha o mesmo espectro.
	    - Mais de um caso de teste aprovado compartilha o mesmo espectro.
    - É proposto sete esquemas de redução de ruído para remover e eliminar casos de teste que forneçam informações duplicadas e ambíguas e avaliar as melhorias de desempenho resultantes em mais de 30 heurísticas SBFL estudadas.
      - Noise Reduction Scheme 1 (NRS1): para cada caso de teste reprovado, todos os casos de teste aprovados com espectros idênticos ao caso de teste com defeito serão removidos.
      - Noise Reduction Scheme 2 (NRS2): para cada caso de teste aprovado, todos os casos de teste reprovados com espectros idênticos ao caso de teste aprovado serão removidos.
      - Noise Reduction Scheme 3 (NRS3): para cada conjunto de casos de teste aprovados e reprovados com espectros idênticos, todos os casos de teste do conjunto serão removidos. 
      - Noise Reduction Scheme 4 (NRS4): Para cada conjunto de casos de teste aprovados com espectros idênticos, todos, exceto um caso de teste, serão removidos.
      - Noise Reduction Scheme 5 (NRS5): Este esquema de redução de ruído é uma combinação de NRS4 e NRS1. 
      - Noise Reduction Scheme 6 (NRS6): Este esquema de redução de ruído é uma combinação de NRS4 e NRS2.
      - Noise Reduction Scheme 7 (NRS7): Este esquema de redução de ruído é uma combinação de NRS4 e NRS3.	
    - A partir dos experimentos realizados em 62 versões defeituosas de programas no Siemens Test Suite, foi descoberto que os casos de teste com espectros idênticos podem chegar a 27% no Siemens Test Suite.
    - A percentagem significativa elevada de casos de teste com espectros idênticos é essencialmente ruído para as heurísticas SBFL, o que podem deteriorar o seu desempenho.
  - Importância do artigo para a pesquisa
    - Foi demonstrado que o procedimento de eliminação dos ruídos da matriz de espectro poderá contribuir de forma significativa com a eficácia das heurísticas SBFL. 

</details>
