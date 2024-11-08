import numpy as np
def calcular_semejanza(a: np.ndarray, b: np.ndarray, metodo: str = "distancia_euclidiana") -> float:
    if metodo == "distancia_euclidiana":
        return np.linalg.norm(a - b)
    elif metodo == "producto_punto":
        return np.dot(a, b)
    else:
        print("Método de semejanza no reconocido.")
        return float("inf")