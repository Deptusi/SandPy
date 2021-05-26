from Sand_classes import *

def print_Tittle():
    print("*"*27)
    print("*     SANDWICHES UCAB     *")
    print("*"*27)

def ingresar_cupon():
    salir = False
    descuento = 0
    while not salir:
        respuesta = input("¿Usted tiene un cupon [s/n]? ")
        if (respuesta == "s"):
            codigo_cupon= input("Ingrese el codigo del cupón: ")
            archivo = open("codigos_cupones.txt", "r")
            cupones = []
            for linea in archivo:
                linea = linea.replace("\n", "")
                cupones.append(linea)
            archivo.close()
            buscar = False
            for cupon in cupones:
                codigo = cupon.split()[0]
                if (codigo_cupon == codigo):
                    archivo = open("codigos_cupones.txt", "r")
                    lineas = archivo.readlines()
                    archivo.close()
                    archivo_nuevo = open("codigos_cupones.txt", "w")
                    for linea in lineas:
                        if (linea.strip("\n") != cupon):
                            archivo_nuevo.write(linea)
                    archivo_nuevo.close()
                    buscar = True
                    descuento = int(cupon.split()[1])
                    return descuento
            if (not buscar):
                print("No existe este codigo de cupon en el sistema")
        elif (respuesta == "n"):
            salir = True
            return descuento
        else:
            print("Ingrese una opción valida")

def ordenar_sandwich(orden_N):
    numero_descuento = ingresar_cupon()
    print(f"Sandwich número {orden_N}")
    Sandwich_temporal=Sandwich()
    Sandwich_temporal.definir_tamano()
    imprimir_ingredientes(Sandwich_temporal)
    while not Sandwich_temporal.sandwich_terminado:
        Sandwich_temporal.agregar_ingrediente()
    Sandwich_temporal.imprimir_seleccion(numero_descuento)
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

