import numpy as np
def calcular_semejanza(a: np.ndarray, b: np.ndarray, metodo: str = "distancia_euclidiana") -> float:
    if metodo == "distancia_euclidiana":
        return np.linalg.norm(a - b)
    elif metodo == "producto_punto":
        return np.dot(a, b)
    else:
        print("Método de semejanza no reconocido.")
        return float("inf")

def calcular_umbral(matriz_semejanza: np.ndarray) -> float:
    print("Seleccione el método para calcular el umbral:")
    metodo = input("1. Promedio de semejanza\n2. Mediana de semejanza\nSeleccione (1 o 2): ")
    if metodo == "1":
        return np.mean(matriz_semejanza)
    elif metodo == "2":
        return np.median(matriz_semejanza)
    else:
        print("Método no reconocido. Usando promedio por defecto.")
        return np.mean(matriz_semejanza) 