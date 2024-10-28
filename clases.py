from A import a
cantidad = int(input("Ingrese la cantidad de variables a utilizar: "))
objeto_a = a(cantidad)
lis = objeto_a.getA()
for i in lis:
    print(f"objeto {i[0]}\n")
    print(f"tipo {i[1]}\n")
    print(f"valor {i[2]}\n")