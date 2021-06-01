# autor: German Bermudez
# Coautores:
#           Christian Neira
#           Jesus Requena
#           Fernando Gomes

class Sandwich():
    def __init__(self,numero_de_sandwich=1,cont_ingred_sand={}):
        """Define las variables que contiene el objeto Sandwich"""
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
        self.contador_ingredientes = cont_ingred_sand
        self.sandwich_terminado=False # Variable Boolean que indica cuando se terminan 
        # de agregar ingredientes
        self.lista_descriptiva=[] # Variable que almacena el tamano e ingredientes del Sandwich
    
    def definir_tamano(self):
        """Solicita al usuario ingresar el tamaño del sandwich"""
        print("Opciones:")
        while True: 
            opcion_seleccionada=input("Tamaños: Triple ( t ) Doble ( d ) Individual ( i ): ")
            if opcion_seleccionada in self.lista_de_tamanos:
                break
            else:
                print("=> Debe seleccionar el tamaño correcto!!")
        self.tamano=(self.lista_de_tamanos[opcion_seleccionada])

    def seleccionar_ingredientes(self):
        """Solicita al usuario el ingrediente a agregar"""
        while True:
            if len(self.lista_de_ingredientes)>0: # Solo continua si quedan ingredientes por agregar
                opcion_seleccionada=input("Indique ingrediente (enter para terminar): ")
                if opcion_seleccionada in self.lista_de_ingredientes:
                    self.agregar_ingrediente(opcion_seleccionada)
                elif opcion_seleccionada=="":
                    self.sandwich_terminado=True
                    break
                else:
                    print("=> Debe seleccionar un ingrediente de la lista!!")
            else: # si no quedan ingredientes por agregar, se considera terminado el sandwhich
                self.sandwich_terminado=True
                break
                
    def agregar_ingrediente(self,opcion_seleccionada):            
        """Agrega un ingrediente seleccionado y elimina este ingrediente de la lista disponible"""
        self.lista_descriptiva.append(self.lista_de_ingredientes.pop(opcion_seleccionada))
        # Luego de agregar el ingrediente, se actualizan los ingredientes en inventario
        for ingrediente, contador in self.contador_ingredientes.items():
            if (ingrediente == opcion_seleccionada):
                contador -= 1
                self.contador_ingredientes[ingrediente] = contador

            

    def actualizar_precio(self, numero_descuento=0):
        """Calcula el precio del sandwich con base a su tamaño e ingredientes agregados"""
        self.precio=self.tamano[0]
        for ingrediente in self.lista_descriptiva:
            self.precio+=ingrediente[0]
        if (numero_descuento != 0):
            descuento_porcentaje = (100 - numero_descuento) / 100
            self.precio = self.precio * descuento_porcentaje   


    def imprimir_seleccion(self, numero_descuento):
        """Realiza un resumen de la orden al finalizar el pedido"""
        self.actualizar_precio(numero_descuento)
        txt=f"Usted seleccionó un sándwich {self.tamano[1]} con "
        if len(self.lista_descriptiva)>0:
            for ingrediente in self.lista_descriptiva:
                txt=txt+ingrediente[1]+", "
            txt=txt[:-2] # Elimina la última ", "
        else:
            txt=txt+"Queso"
        print(txt+"\n"+f"Subtotal a pagar por un sándwich {self.tamano[1]}: {self.precio}")

    def get_contador_ingredientes(self):
        return self.contador_ingredientes
    
    def set_contador_ingredientes(self,contador_ingredientes_nuevo):
        self.contador_ingredientes = contador_ingredientes_nuevo
