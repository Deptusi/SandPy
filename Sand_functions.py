from Sand_classes import *

def print_Tittle():
    print("*"*27)
    print("*     SANDWICHES UCAB     *")
    print("*"*27)

def ordenar_sandwich(orden_N):
    print(f"Sandwich número {orden_N}")
    Sandwich_temporal=Sandwich()
    Sandwich_temporal.definir_tamano()
    imprimir_ingredientes(Sandwich_temporal)
    while not Sandwich_temporal.sandwich_terminado:
        Sandwich_temporal.agregar_ingrediente()
    Sandwich_temporal.imprimir_seleccion()
    return Sandwich_temporal

def imprimir_ingredientes(Sandwich):
    # Aquí no encuentro la forma para que quede alineada la leyenda
    print("Ingredientes" ,"\n")
    for ingrediente in Sandwich.lista_de_ingredientes:
        print(
            Sandwich.lista_de_ingredientes[ingrediente][1], " "*5,
            "(",ingrediente,")")

def input_continue():
    print("*"*28,)
    temp=input("¿Desea continuar [s/n]?: ")
    while temp!="s" and temp!="n":
        temp=input("¿Desea continuar [s/n]?: ")
    if temp=="s":
        return True
    else:
        return False

def realizar_ordenes():
    numero_de_orden = 1
    lista_de_ordenes = []
    lista_de_ordenes.append(ordenar_sandwich(numero_de_orden))
    while input_continue():
        numero_de_orden+=1
        lista_de_ordenes.append(ordenar_sandwich(numero_de_orden))
    
    return lista_de_ordenes

def imprimit_total(lista_de_ordenes):
    print("*"*28,)
    print(f"El pedido tiene un total de {len(lista_de_ordenes)} \
sándwich(es) por un monto de {sum([sandwich.precio for sandwich in lista_de_ordenes])}")
    
    # aquí podréamos agregar una opción para dar un resumen detallado de los 
    # pedidos, y preguntar si quiere eliminar un pedido, o duplicar otro
    print("\nGracias por su compra, regrese pronto")

