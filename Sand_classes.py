# -*- coding: cp1252 -*-

class Sandwich():

    def __init__(self,n�mero_de_sandwich=1):
        self.n�mero_de_sandwich=n�mero_de_sandwich
        self.precio=0
        self.lista_de_tama�os={
            "t":[580,"Triple"],
            "d":[430, "Doble"],
            "i":[280, "Individual"],
        }
        self.tama�o=""
        self.lista_de_ingredientes={
            "ja":[40, "Jam�n"],
            "ch":[35, "Champi�ones"],
            "pi":[30, "Piment�n"],
            "dq":[40, "Doble Queso"],
            "ac":[57.5, "Aceitunas"],
            "pp":[38.5, "Pepperoni"],
            "sa":[62.5, "Salchich�n"]
        }
        self.sandwich_terminado=False # Variable Boolean que indica cuando se terminan 
        # de agregar ingredientes
        self.lista_descriptiva=[] # Variable que almacena el tama�o e ingredientes del Sandwich
    
    def definir_tama�o(self):
        print("Opciones:")
        while True:
            opci�n_seleccionada=input("Tama�os: Triple ( t ) Doble ( d ) Individual ( i ): ")
            if opci�n_seleccionada in self.lista_de_tama�os:
                break
            else:
                print("=> Debe seleccionar el tama�o correcto!!")
        self.tama�o=(self.lista_de_tama�os[opci�n_seleccionada])

    def agregar_ingrediente(self):
        while True:

            if len(self.lista_de_ingredientes)>0: # si no hay m�s ingredientes, no tiene sentido continuar
                opci�n_seleccionada=input("Indique ingrediente (enter para terminar): ")
            else: 
                self.sandwich_terminado=True
                break

            if opci�n_seleccionada in self.lista_de_ingredientes:
                # Al agregar un ingrediente, utilizo pop para que ya no se pueda agregar
                self.lista_descriptiva.append(
                    self.lista_de_ingredientes.pop(opci�n_seleccionada)
                )
                break
            elif opci�n_seleccionada=="":
                self.sandwich_terminado=True
                break
            else:
                print("=> Debe seleccionar un ingrediente de la lista!!")

    def actualizar_precio(self):
        self.precio=self.tama�o[0]
        for ingrediente in self.lista_descriptiva:
            self.precio+=ingrediente[0]

    def imprimir_selecci�n(self):
        self.actualizar_precio()
        txt=f"Usted seleccion� un s�ndwich {self.tama�o[1]} con "
        if len(self.lista_descriptiva)>0:
            for ingrediente in self.lista_descriptiva:
                txt=txt+ingrediente[1]+", "
            txt=txt[:-2] # Elimina la �ltima ", "
        else:
            txt=txt+"Queso"
        print(txt)
        print("")
        print(f"Subtotal a pagar por un s�ndwich {self.tama�o[1]}: {self.precio}")




