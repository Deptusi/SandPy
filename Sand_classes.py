# -*- coding: cp1252 -*-

class Sandwich():

    def __init__(self,número_de_sandwich=1):
        self.número_de_sandwich=número_de_sandwich
        self.precio=0
        self.lista_de_tamaños={
            "t":[580,"Triple"],
            "d":[430, "Doble"],
            "i":[280, "Individual"],
        }
        self.tamaño=""
        self.lista_de_ingredientes={
            "ja":[40, "Jamón"],
            "ch":[35, "Champiñones"],
            "pi":[30, "Pimentón"],
            "dq":[40, "Doble Queso"],
            "ac":[57.5, "Aceitunas"],
            "pp":[38.5, "Pepperoni"],
            "sa":[62.5, "Salchichón"]
        }
        self.sandwich_terminado=False # Variable Boolean que indica cuando se terminan 
        # de agregar ingredientes
        self.lista_descriptiva=[] # Variable que almacena el tamaño e ingredientes del Sandwich
    
    def definir_tamaño(self, tamaño=False):
        print("Opciones:")
        if tamaño!=False:
            while True:
                opción_seleccionada=input("Tamaños: Triple ( t ) Doble ( d ) Individual ( i ): ")
                if opción_seleccionada in self.lista_de_tamaños:
                    break
                else:
                    print("=> Debe seleccionar el tamaño correcto!!")
            self.tamaño=(self.lista_de_tamaños[opción_seleccionada])
        else:
            self.tamaño=(self.lista_de_tamaños[tamaño])

    def agregar_ingrediente(self,ingredientes=[]):
        if len(ingredientes)==0:
            while True:

                if len(self.lista_de_ingredientes)>0: # si no hay más ingredientes, no tiene sentido continuar
                    opción_seleccionada=input("Indique ingrediente (enter para terminar): ")
                else: 
                    self.sandwich_terminado=True
                    break

                if opción_seleccionada in self.lista_de_ingredientes:
                    # Al agregar un ingrediente, utilizo pop para que ya no se pueda agregar
                    self.lista_descriptiva.append(
                        self.lista_de_ingredientes.pop(opción_seleccionada)
                    )
                    break
                elif opción_seleccionada=="":
                    self.sandwich_terminado=True
                    break
                else:
                    print("=> Debe seleccionar un ingrediente de la lista!!")
        else:
            self.lista_descriptiva=ingredientes
            self.sandwich_terminado=True

    def actualizar_precio(self):
        self.precio=self.tamaño[0]
        for ingrediente in self.lista_descriptiva:
            self.precio+=ingrediente[0]

    def imprimir_selección(self):
        self.actualizar_precio()
        txt=f"Usted seleccionó un sándwich {self.tamaño[1]} con "
        if len(self.lista_descriptiva)>0:
            for ingrediente in self.lista_descriptiva:
                txt=txt+ingrediente[1]+", "
            txt=txt[:-2] # Elimina la última ", "
        else:
            txt=txt+"Queso"
        print(txt)
        print("")
        print(f"Subtotal a pagar por un sándwich {self.tamaño[1]}: {self.precio}")




