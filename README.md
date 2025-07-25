# 📚 Painel de Estudos - Doutorado
Este repositório tem como objetivo documentar os principais artigos científicos estudados ao longo dessa pesquisa. Para cada artigo, estão disponíveis:

- 📌 Título
- 🔗 DOI
- 📥 Link para o artigo
- 📝 Breve descrição
- 📖 Descrição detalhada
---
## 🧭 Resumo Geral da Pesquisa

A localização de defeitos baseada no espectro utiliza informações de cobertura de código obtidas durante a execução dos testes para abstrair padrões que auxiliem na identificação de statements defeituosos. Como, tipicamente, o número de casos de teste que revelam a presença de defeitos é inferior àqueles que não revelam, esse desbalanceamento dificulta a descoberta de padrões relevantes e, consequentemente, aumenta o custo da localização de defeitos. O foco central desta pesquisa é explorar técnicas de melhoria de um determinado conjunto de casos de teste (balanceamento, etc), de modo a melhorar a efetividade das heurísticas utilizadas na localização de defeitos em software.

🔍 **Áreas de interesse**:
- Localização de defeitos em software
- Geração de dados de teste
- Balanceamento de casos de teste
- Cobertura de casos de teste

📅 **Status atual**: Pesquisa em andamento, com atualizações constantes à medida que novos artigos são estudados.

---
## 👥 Autores da Pesquisa

- **Reinaldo de Souza Júnior** – reinaldo.junior@discente.ufg.br
- **Plínio de Sá Leitão Júnior** – plinio@inf.ufg.br  
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
