import numpy as np

def definir_variables():
    variables = []

    #A
    num_variables = int(input("Ingrese la cantidad de variables a utilizar: "))
    
    for i in range(num_variables):
        print(f"\nDefina la variable {i+1}:")
        
        #B Tipo de variable
        tipo = input("Seleccione el tipo (booleana, k-valente, real): ").lower()
        
        #C Valores admisibles
        if tipo == "booleana":
            while True:
                valores_admisibles = input(f"Ingrese el valor booleano (1 para True, 0 para False): ")
                if valores_admisibles == "1":
                    valores_admisibles = True
                    break
                elif valores_admisibles == "0":
                    valores_admisibles = False
                    break
                else:
                    print("Entrada inválida. Por favor, ingrese 1 para True o 0 para False.")
        elif tipo == "k-valente":
            num_valores = int(input("Ingrese la cantidad de valores posibles: "))
            valores_admisibles = [input(f"Valor {j+1}: ") for j in range(num_valores)]
        elif tipo == "real":
            min_val = float(input("Ingrese el valor mínimo: "))
            max_val = float(input("Ingrese el valor máximo: "))
            valores_admisibles = [min_val, max_val]
        else:
            print("Tipo de variable no reconocido.")
            continue

        #D Criterio de comparación
        print("Seleccione el criterio de comparación para esta variable:")
        criterio = input("1. Igualdad\n2. Diferencia\nSeleccione la opción (1 o 2): ")

        variable = {
            "tipo": tipo,
            "valores_admisibles": valores_admisibles,
            "criterio_comparacion": "igualdad" if criterio == "1" else "diferencia"
        }
        variables.append(variable)
    
    return variables