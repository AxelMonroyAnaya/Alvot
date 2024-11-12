import numpy as np
  
def criterio_bo_conexo(matriz_semejanza: np.ndarray, umbral: float):
    n = matriz_semejanza.shape[0]
    grupos = []
    asignados = set()

    for i in range(n):
        if i not in asignados:
            grupo = [i]
            asignados.add(i)
            for j in range(i + 1, n):
                if matriz_semejanza[i, j] <= umbral:
                    grupo.append(j)
                    asignados.add(j)
            grupos.append(grupo)

    return grupos