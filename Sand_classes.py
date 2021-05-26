class Sandwich():

    def __init__(self,numero_de_sandwich=1):
        self.numero_de_sandwich = numero_de_sandwich
        self.precio = 0
        self.lista_de_tamanos={
            "t":(580,"Triple"),
            "d":(430, "Doble"),
            "i":(280, "Individual"),
        }
        self.tamano=""
        self.lista_de_ingredientes={
            "ja":(40, "Jamón"),
            "ch":(35, "Champiñones"),
            "pi":(30, "Pimentón"),
            "dq":(40, "Doble Queso"),
            "ac":(57.5, "Aceitunas"),
            "pp":(38.5, "Pepperoni"),
            "sa":(62.5, "Salchichón")
        }
        self.sandwich_terminado=False # Variable Boolean que indica cuando se terminan 
        # de agregar ingredientes
        self.lista_descriptiva=[] # Variable que almacena el tamano e ingredientes del Sandwich
    
    def definir_tamano(self):
        print("Opciones:")
        while True:
            opcion_seleccionada=input("Tamaños: Triple ( t ) Doble ( d ) Individual ( i ): ")
            if opcion_seleccionada in self.lista_de_tamanos:
                break
            else:
                print("=> Debe seleccionar el tamaño correcto!!")
        self.tamano=(self.lista_de_tamanos[opcion_seleccionada])

    def agregar_ingrediente(self):
        while True:

            if len(self.lista_de_ingredientes)>0: # si no hay más ingredientes, no tiene sentido continuar
                opcion_seleccionada=input("Indique ingrediente (enter para terminar): ")
            else: 
                self.sandwich_terminado=True
                break

            if opcion_seleccionada in self.lista_de_ingredientes:
                # Al agregar un ingrediente, utilizo pop para que ya no se pueda agregar
                self.lista_descriptiva.append(
                    self.lista_de_ingredientes.pop(opcion_seleccionada)
                )
                break
            elif opcion_seleccionada=="":
                self.sandwich_terminado=True
                break
            else:
                print("=> Debe seleccionar un ingrediente de la lista!!")

    def actualizar_precio(self, numero_descuento):
        if (numero_descuento == 0):
            self.precio=self.tamano[0]
            for ingrediente in self.lista_descriptiva:
                self.precio+=ingrediente[0]
        else:
            self.precio=self.tamano[0]
            for ingrediente in self.lista_descriptiva:
                self.precio+=ingrediente[0]
            descuento = (100 - numero_descuento) / 100
            self.precio = self.precio * descuento   

    def imprimir_seleccion(self, numero_descuento):
        self.actualizar_precio(numero_descuento)
        txt=f"Usted seleccionó un sándwich {self.tamano[1]} con "
        if len(self.lista_descriptiva)>0:
            for ingrediente in self.lista_descriptiva:
                txt=txt+ingrediente[1]+", "
            txt=txt[:-2] # Elimina la última ", "
        else:
            txt=txt+"Queso"
        print(txt+"\n")
        print(f"Subtotal a pagar por un sándwich {self.tamano[1]}: {self.precio}")
