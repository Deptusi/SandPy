# -*- coding: cp1252 -*-
from Sand_classes import *

def print_Tittle():
    print("*"*26)
    print("*     SANDWICHES UCAB    *")
    print("*"*26)

def ordenar_sándwich(orden_N):
    print(f"Sandwich número {orden_N}")
    Sandwich_temporal=Sandwich()
    Sandwich_temporal.definir_tamaño()
    imprimir_ingredientes(Sandwich_temporal)
    while not Sandwich_temporal.sandwich_terminado:
        Sandwich_temporal.agregar_ingrediente()
    Sandwich_temporal.imprimir_selección()
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
    número_de_orden=1
    lista_de_ordenes=[]
    lista_de_ordenes.append(ordenar_sándwich(número_de_orden))
    while input_continue():
        número_de_orden+=1
        lista_de_ordenes.append(ordenar_sándwich(número_de_orden))
    
    return lista_de_ordenes

def imprimit_total(lista_de_ordenes):
    print("*"*28,)
    print(f"El pedido tiene un total de {len(lista_de_ordenes)} \
sándwich(es) por un monto de {sum([sandwich.precio for sandwich in lista_de_ordenes])}")
    print("")
    # aquí podríamos agregar una opción para dar un resumen detallado de los 
    # pedidos, y preguntar si quiere eliminar un pedido, o duplicar otro
    print("Gracias por su compra, regrese pronto")

