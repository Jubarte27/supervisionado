# Aprendizado supervisionado

## Nomes, cartões de matrícula e turma (turma da manhã é A, e turma da tarde é B) dos integrantes do grupo

| Nome                  | Matrícula | Turma |
|:----------------------|:---------:|:------|
| Lucas Giron           | 00577244  | B     |
| Matheus Machado Cezar | 00597894  | B     |
| Rodrigo Brock         | 00329957  | A     |

## Valores iniciais de b, w, valores de alpha e num_iterations que resultem na melhor execução da sua regressão linear. Especifique também o melhor erro quadrático médio obtido na sua implementação da regressão linear

``` python
    b = 0 # não importa muito
    w = 0 # não importa muito
    alpha = 0.6
    num_iterations = 1070
    EQM = 8.555850536716767
```

## Sua análise dos datasets (quantas classes, quantas amostras, qual o tamanho das imagens (altura x largura x canais de cor))

| Nome             | Classes | Am. Treino | Am. Teste | Dimensões    |
|:-----------------|:--------|:-----------|:----------|:-------------|
| mnist            | 10      | 60,000     | 10,000    | 28 x 28 x 1  |
| fashion_mnist    | 10      | 60,000     | 10,000    | 28 x 28 x 1  |
| cifar10          | 10      | 50,000     | 10,000    | 32 x 32 x 32 |
| cifar100         | 100     | 50,000     | 10,000    | 32 x 32 x 32 |

## Suas conclusões considerando as questões do Exercício 1

- Normalização dos dados permitiu uma taxa de aprendizado muito maior
- b e w importam pouco

## Suas conclusões considerando as questões do Exercício 2

As técnicas utilizadas foram mais ou menos as mesmas em todos os 3 datasets, já que todas elas apresentaram aumento na acurácia obtida. São elas:

- [x] Normalização periódica dos dados permitiu uma taxa de aprendizado maior no cifar100, melhorando a acurácia ao utilizar apenas 10 épocas
- [x] Dropout de uma porcentagem aleátoria dos dados permitiu que fosse utilizado mais camadas tanto de convoluções quanto de densamente conectadas sem causar overfitting
- [x] Utilizar a função de ativação 'gelu' causa um pequeno aumento na acurácia em comparação com a 'relu'
- [x] Utilizar o otimizador 'adamw' causa um pequeno aumento na acurácia em comparação com a 'adam'
- [x] Decaimento da taxa de aprendizagem também proporcionou uma acurácia levemente maior

A principal diferença entre os modelos está na quantidade de camadas e o tamanho de cada camada.

Os tempos de treinamento foram obtidos utilizando o Google Colab em um ambiente com "GPUs: T4".

### mnist

| Acurácia | Tempo de treinamento |
|:---------|:---------------------|
| 98.8%    | 102.2s               |

O mais fácil de se lidar dentre os 4. Já foi visto em aula, portanto não houveram muitos desafios para atingir uma acurácia ótima. De qualquer forma, foram utilizadas as "novas" técnicas, já que todas apresentaram um ganho na acurácia, mesmo que pequeno.

### fashion_mnist

| Acurácia | Tempo de treinamento |
|:---------|:---------------------|
| 91%      | 100.51               |

Possui muitas características iguais ao mnist, mas o nível de detalhe em cada imagem dificulta alcançar uma acurácia tão boa quanto a do mnist. Ajustes finos na quantidade de convoluções poderiam resultar em uma acurácia mais alta, mas para isso necessitaria de mais testes.

### cifar10

| Acurácia | Tempo de treinamento |
|:---------|:---------------------|
| 82%      | 130.8s               |

A existência de 2 dimensões extras de dados representa um salto considerável na complexidade necessária para que a rede consiga generalizar bem. Praticamente todas as técnicas "extras" foram encontradas na busca por melhorar a acurácia para este dataset.

### cifar100

| Acurácia | Tempo de treinamento |
|:---------|:---------------------|
| 54.2%    | 233.3s               |

10 vezes mais categorias aliado a 3 canais de cor torna este o dataset mais "difícil". O maior problema foi o tempo de treinamento, já que cada nova hipótese de melhora demorava muito para ser verificada.

## Documentação do(s) extra(s) implementado(s), se aplicável

### Questão 1

- [x] Normalização na redução linear

### Questão 2

- [x] Normalização utilizado tf.keras.layers.BatchNormalization
- [x] Dropout utilizando tf.keras.layers.GaussianDropout
- [x] Utilizar a função de ativação 'gelu'
- [x] Utilizar o otimizador 'adamw'
- [x] Decaimento da taxa de aprendizagem utilizando keras.optimizers.schedules.ExponentialDecay
