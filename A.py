class a:
    def __init__(self, cantidad):
        self.cantidad = cantidad    
        self.resultado=[]
        for i in range(self.cantidad):
            self.opciones_validas = {"booleana", "k-valente", "real"}
            self.nombre = input(f"Ingrese el nombre de la variable {i+1}: ")
            while True:    
                tipo = input(f"Ingrese el tipo de la variable '{self.nombre}'{self.opciones_validas}: ")
                if tipo in self.opciones_validas:
                    self.tipo=tipo
                    break
                else:
                    print("teclea una opcion valida")
            while True:
                var = input("Ingrese un valor: ")
                if self.tipo == "real":
                    try:
                        var = int(var)
                        self.variables = var
                        break
                    except ValueError:
                        print("Ingresa un valor válido para tipo real (debe ser un entero).")
                elif self.tipo == "k-valente":
                    if isinstance(var, str):
                        self.variables = var
                        break
                    else:
                        print("Ingresa un valor válido para tipo k-valente (debe ser una cadena).")
                elif self.tipo == "booleana":
                    if var.lower() in ["true", "false"]:
                        self.variables = var.lower() == "true"
                        break
                    else:
                        print("Ingresa un valor válido para tipo booleana (debe ser true o false).")
                else:
                    print("Tipo no reconocido. Por favor, inténtalo de nuevo.")
            self.resultado.append([self.nombre, self.tipo, self.variables])
    def getA(self):    
        return self.resultado