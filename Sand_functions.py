# autor: German Bermudez
# Coautores:
#           Christian Neira
#           Jesus Requena
#           Fernando Gomes
from os import system,name
from Sand_classes import *
from Sand_interactions import *
from Sand_coupons import *
from Sand_inventory_control import *

def imprimir_titulo():
    """Imprime en el terminal el titulo del proyecto"""
    if name == "nt":
        system("cls")
    else:
        system("clear")
    
    print("*"*35)
    print("*         SANDWICHES UCAB         *")
    print("*"*35)

def ordenar_sandwich(orden_N):
    imprimir_titulo()
    """Realiza todas las operaciones para hacer un pedido"""
    # Crea el inventario de ingredientes
    contador_ingredientes = devolver_diccionario(orden_N) 
    # Revisa si hay existencia de todos los inventarios
    control_inventario(contador_ingredientes) 
    # Imprime el número de sandwich a ordenar
    print(f"Sandwich número {orden_N}") 
    # Crea la orden
    Sandwich_temporal=Sandwich() 
    #Asocia el inventario de ingredientes al objeto Sandwich
    Sandwich_temporal.set_contador_ingredientes(contador_ingredientes) 
    # Solicita al usuario ingresar el tamaño del sandwich
    Sandwich_temporal.definir_tamano() 
    # Imprime la lista de ingredientes, su leyenda y disponibilidad
    imprimir_ingredientes(Sandwich_temporal) 
    # Mientras el usuario no termine la orden, seguir agregando ingredientes
    while not Sandwich_temporal.sandwich_terminado: 
        Sandwich_temporal.seleccionar_ingredientes()
    guardar_contador_ingrediente(Sandwich_temporal.get_contador_ingredientes())
    # Solicita si el usuario tiene un cupon y cual es
    numero_descuento = ingresar_cupon() 
    # Imprime el resumen del pedido
    Sandwich_temporal.imprimir_seleccion(numero_descuento) 
    # Devuelve como resultado el objeto Sandwich
    return Sandwich_temporal 


def imprimir_ingredientes(Sandwich):
    """Imprime la lista de ingredientes con su leyenda y su cantidad en inventario"""
    print("\nIngredientes\n")
    for ingrediente in Sandwich.lista_de_ingredientes:
        print(
            #Imprime el nombre del ingrediente
            Sandwich.lista_de_ingredientes[ingrediente][1], 
            #Deja un espacio para que quede alineada la leyenda
            " "*(15-len(Sandwich.lista_de_ingredientes[ingrediente][1])),
            #Imprime la leyenda del ingrediente
            "(",ingrediente,")",
            #Imprime la disponibilidad de inventario
            " (Disponibles: "+ str((Sandwich.get_contador_ingredientes()[ingrediente]))+")")
        print('')

def input_continue():
    """Retorna un valor true o false dependiendo de la 
    entrada del usuario al preguntar si desea continuar"""
    print("*"*35,)
    temp=input("¿Desea continuar? [s/n]: ")
    while temp!="s" and temp!="n":
        temp=input("¿Desea continuar? [s/n]: ")
    if temp=="s":
        return True
    else:
        return False

def realizar_ordenes():
    """Empieza el ciclo de pedidos hasta que el usuario no desee continuar"""
    numero_de_orden = 1
    lista_de_ordenes = []
    lista_de_ordenes.append(ordenar_sandwich(numero_de_orden)) #Realiza el primer pedido
    while input_continue(): #Pregunta al usuario si desea continuar
        numero_de_orden += 1
        lista_de_ordenes.append(ordenar_sandwich(numero_de_orden)) #Realiza un pedido
    return lista_de_ordenes #Devuelve la lista de pedidos

