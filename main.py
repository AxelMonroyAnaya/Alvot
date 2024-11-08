from A import definir_variables
#from E import 
from F import leer_matriz
from G import construir_matriz_semejanza
import os,time
#A-D
variables = definir_variables()
print("datos guardados:")    
num =1
for i in range(0, len(variables)):
    print(f"variable {num}:" + str(variables[i])+'\n')
    num += 1
time.sleep(5)
os.system('cls')
# Paso E
print("\nSeleccione la función de semejanza:")
funcion_semejanza = input("1. Distancia Euclidiana\n2. Producto Punto\nSelecciona (1 o 2): ")
funcion_semejanza = "distancia_euclidiana" if funcion_semejanza == "1" else "producto_punto"
#F    
matriz = leer_matriz()
if matriz is None:
    print("Error al leer la matriz.")
    pass
# Paso G: 
matriz_semejanza = construir_matriz_semejanza(matriz, funcion_semejanza)