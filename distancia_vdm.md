# 🔍 Detalhamento dos Tópicos de Estudo

Este documento irá abordar os detalhes dos tópicos de estudo.

---

## Distância de VDM (Value Difference Metric)

A técnica Smoten (Synthetic Minority Over-sampling Technique for Nominal) é uma variante do SMOTE desenvolvida especificamente para lidar com conjuntos de dados onde todas as variáveis são categóricas (nominais). Os vizinhos mais próximos, são identificados pelo uso da métrica Value Difference Metric (VDM).

O VDM responde a seguinte pergunta: “Azul e Verde são parecidos… em relação ao que acontece com a classe (0 ou 1)”. Imagine que você olhou o seu histórico e viu isso: 

Quando a cor é Azul
  - De cada 10 casos com Azul:
    - 8 são classe 0
    - 2 são classe 1
      
Azul → (classe 0: 0,8) e (classe 1: 0,2)

Então:

Quando a cor é Verde
  - De cada 10 casos com Verde:
    - 6 são classe 0
    - 4 são classe 1

Verde → (classe 0: 0,6) e (classe 1: 0,4)

Como o VDM calcula a “distância” entre Azul e Verde. Ele faz duas comparações e soma:
  - Comparação na classe 0
    - Azul tem 0,8 de classe 0
    - Verde tem 0,6 de classe 0
    - Diferença: 0,8 - 0,6 = 0,2

Comparação na classe 1
  - Azul tem 0,2 de classe 1
  - Verde tem 0,4 de classe 1
  - Diferença: 0,2 - 0,4 = -0,2 (como distância é sempre positiva, vira 0,2)

Agora soma as duas diferenças:
  - Distância = 0,2 + 0,2 = 0,4
    
✅ Então o VDM diz: a distância entre Azul e Verde é 0,4.

Como interpretar esse 0,4 (do jeito mais intuitivo)
  - Se Azul e Verde fossem muito parecidos, eles teriam quase a mesma “mistura” de classe 0 e 1. A distância ficaria perto de 0.
  - Se Azul fosse quase sempre classe 0 e Verde quase sempre classe 1, as diferenças seriam grandes e a distância ficaria bem maior.

Após a definição dos vizinhos, como os novos vizinhos são gerados?
  - Como não dá para “interpolar” categorias (como o SMOTE faz com números), o SMOTEN monta uma nova linha escolhendo, em cada coluna, a categoria mais comum (moda) entre a amostra base e seus vizinhos.
