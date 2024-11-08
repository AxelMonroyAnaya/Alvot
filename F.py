import  numpy as np

def leer_matriz() -> np.ndarray:
    #F Leer matriz desde archivo o teclado
    #LEER POR TECLADO
    fuente = input("¿Desea ingresar la matriz por teclado (1) o desde archivo (2)?: ")
    if fuente == "1":
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
        matriz = np.zeros((filas, columnas))
        print("Ingrese los datos de la matriz:")
        for i in range(filas):
            for j in range(columnas):
                matriz[i, j] = float(input(f"Elemento ({i+1},{j+1}): "))
    #LEER POR ARCHIVO
    elif fuente == "2":
        ruta = input("Ingrese la ruta del archivo: ")
        matriz = np.loadtxt(ruta)
    else:
        print("Opción no válida.")
        matriz = None
    
    return matriz