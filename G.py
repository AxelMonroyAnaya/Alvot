import numpy as np
from H import calcular_semejanza

def construir_matriz_semejanza(matriz: np.ndarray, metodo: str):
    n = matriz.shape[0]
    matriz_semejanza = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            semejanza = calcular_semejanza(matriz[i], matriz[j], metodo)
            matriz_semejanza[i, j] = matriz_semejanza[j, i] = semejanza
    return matriz_semejanza
