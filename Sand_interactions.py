from Sand_functions import *
from Sand_cont import start_cont
def print_Tittle():
    print("*"*27)
    print("*     SANDWICHES UCAB     *")
    print("*"*27)


def imprimit_total(lista_de_ordenes):
    print("*"*28,)
    print(f"El pedido tiene un total de {len(lista_de_ordenes)} \
sándwich(es) por un monto de {sum([sandwich.precio for sandwich in lista_de_ordenes])}")
    
    # aquí podréamos agregar una opción para dar un resumen detallado de los 
    # pedidos, y preguntar si quiere eliminar un pedido, o duplicar otro
    print("\nGracias por su compra, regrese pronto")

def start_program():
    varglobal=True
    while(varglobal):
        case_selection()
        temp=""
        while(temp!="1" and temp!="0"):
            temp=input("Desea salir? Si(1) - No(0)")
            if temp== "1":
                print("Hasta Luego")
                varglobal = False
            else:
                if temp == "0":
                    temp==""
        print("*"*28,)
    print("")

def case_selection():
    print("Ver Contabilidad (1)")
    print("Realizar venta de sandwiches (2)")
    temp=""
    while(temp!="1" and temp!="2"):
        temp=input("Que desea hacer? ")
    print("*"*28,)
    print("")
    if temp=="1":
        start_conta()
    else: 
        if temp == "2":
            start_sale()
        else:
            print("Opcion incorrecta, Escoja nuevamente")

def start_conta():
    start_cont()

def start_sale():
    imprimit_total(realizar_orden())
