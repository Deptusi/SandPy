from Sand_classes import *
from Sand_interactions import *
from Sand_coupons import ingresar_cupon
from Sand_inventory_control import *

def print_Tittle():
    print("*"*27)
    print("*     SANDWICHES UCAB     *")
    print("*"*27)

def ordenar_sandwich(orden_N):
    numero_descuento = ingresar_cupon()
    contador_ingredientes = devolver_diccionario(orden_N)
    control_inventario(contador_ingredientes)
    print(f"Sandwich número {orden_N}")
    Sandwich_temporal=Sandwich()
    Sandwich_temporal.set_contador_ingredientes(contador_ingredientes)
    Sandwich_temporal.definir_tamano()
    imprimir_ingredientes(Sandwich_temporal)
    while not Sandwich_temporal.sandwich_terminado:
        Sandwich_temporal.agregar_ingrediente()
    guardar_contador_ingrediente(Sandwich_temporal.get_contador_ingredientes())
    Sandwich_temporal.imprimir_seleccion(numero_descuento)
    return Sandwich_temporal

def realizar_orden():
    numero_de_orden = 1
    lista_de_ordenes = []
    lista_de_ordenes.append(ordenar_sandwich(numero_de_orden))
    while  input_continue():
        numero_de_orden+=1
        lista_de_ordenes.append(ordenar_sandwich(numero_de_orden))
    
    return lista_de_ordenes

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

