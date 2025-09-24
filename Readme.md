# Aprendizado supervisionado

* Nomes, cartões de matrícula e turma (turma da manhã é A, e turma da tarde é B) dos integrantes do
grupo

    | Nome                  | Matrícula | Turma |
    |:----------------------|:---------:|:------|
    | Lucas Giron           | 00577244  | B     |
    | Matheus Machado Cezar | 00597894  | B     |
    | Rodrigo Brock         |           |       |

* Valores iniciais de b, w, valores de alpha e num_iterations que resultem na melhor execução da sua regressão linear. Especifique também o melhor erro quadrático médio obtido na sua implementação da regressão linear

    ``` python
        b = 0 # não importa muito
        w = 0 # não importa muito
        alpha = 0.6
        num_iterations = 1070
        EQM = 8.555850536716767
    ```

* Sua análise dos datasets (quantas classes, quantas amostras, qual o tamanho das imagens (altura x largura x canais de cor)).

    | Nome             | Classes | Am. Treino | Am. Teste | Dimensões    |
    |:-----------------|:--------|:-----------|:----------|:-------------|
    | mnist            | 10      | 60,000     | 10,000    | 28 x 28 x 1  |
    | fashion_mnist    | 10      | 60,000     | 10,000    | 28 x 28 x 1  |
    | cifar10          | 10      | 50,000     | 10,000    | 32 x 32 x 32 |
    | cifar100         | 100     | 50,000     | 10,000    | 32 x 32 x 32 |

* Suas conclusões considerando as questões do Exercício 1.
  * Normalização dos dados permite uma taxa de aprendizado muito maior
  * ...
* Suas conclusões considerando as questões do Exercício 2.
* Documentação do(s) extra(s) implementado(s), se aplicável.
