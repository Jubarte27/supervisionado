import numpy as np

def make_h_theta(b, w):
    return lambda x : ((x * w) + b)

def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    h_theta = make_h_theta(b, w)

    x = data[:,0]
    y = data[:,1]
    
    m = x.size
    
    err = h_theta(x) - y

    return np.sum(err * err) / m

def compute_mse_deriv(b, w, data):
    """
    Calcula a derivada da função do erro quadratico medio em relação a b e w
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float,float - derivada em relação a b, derivada em relação a w
    """
    h_theta = make_h_theta(b, w)

    x = data[:,0]
    y = data[:,1]

    m = x.size
    
    err = h_theta(x) - y

    b_ = (np.sum(err) * 2) / m
    w_ = (np.sum(err * x) * 2) / m

    return b_, w_

def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """

    b_, w_ = compute_mse_deriv(b, w, data)

    return b - (alpha * b_), w - (alpha * w_)


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    bs = [b]
    ws = [w]
    for _ in range(num_iterations):
        b, w = step_gradient(b, w, data, alpha)
        bs.append(b)
        ws.append(w)

    return bs, ws
