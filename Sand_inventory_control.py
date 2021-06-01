# autor: Christian Neira
# Coautores:
#           Germán Bermúdez

cont_ingred = {}
lista_de_ingredientes={
    "ja":"Jamón",
    "ch":"Champiñones",
    "pi":"Pimentón",
    "dq":"Doble Queso",
    "ac":"Aceitunas",
    "pp":"Pepperoni",
    "sa":"Salchichón"
}

def devolver_diccionario(numero_orden):
    """Crea un inventario de ingredientes al iniciar la primera orden"""
    if (numero_orden == 1):
        contador_ingredientes = {
            "ja":5,
            "ch":5,
            "pi":5,
            "dq":5,
            "ac":5,
            "pp":5,
            "sa":5
        }
        return contador_ingredientes
    else:
        return cont_ingred

def guardar_contador_ingrediente(diccionario_contador):
    global cont_ingred
    cont_ingred = diccionario_contador

def control_inventario( dicc_contador_ingredientes ):
    global cont_ingred
    for ingrediente, cantidad in dicc_contador_ingredientes.items():
        # if (ingrediente == "ja"):
        #     print(f"Jamón\t\t({ingrediente}) tiene la cantidad: {cantidad}")
        # elif (ingrediente == "ch"):
        #     print(f"Champiñones\t({ingrediente}) tiene la cantidad: {cantidad}")
        # elif (ingrediente == "pi"):
        #     print(f"Pimentón\t({ingrediente}) tiene la cantidad: {cantidad}")
        # elif (ingrediente == "dq"):
        #     print(f"Doble Queso\t({ingrediente}) tiene la cantidad: {cantidad}")
        # elif (ingrediente == "ac"):
        #     print(f"Aceitunas\t({ingrediente}) tiene la cantidad: {cantidad}")
        # elif (ingrediente == "pp"):
        #     print(f"Pepperoni\t({ingrediente}) tiene la cantidad: {cantidad}")
        # elif (ingrediente == "sa"):
        #     print(f"Salchichón\t({ingrediente}) tiene la cantidad: {cantidad}")
        # if (cantidad == 0):
        #     print(f"Se agoto la existencia de este ingrediente {ingrediente}")
        #     cantidad_recargar = int(input("Ingrese la cantidad que sea recargar en el ingrediente: "))
        if (cantidad == 0):
            print(f"Se agoto la existencia de {lista_de_ingredientes[ingrediente]}")
            while True:
                try:
                    cantidad_recargar = int(input("Ingrese la cantidad que sea recargar en el ingrediente: "))
                    if cantidad_recargar>0:
                        break
                except:
                    print("Ingrese un número entero")
            dicc_contador_ingredientes[ingrediente] = cantidad_recargar
    cont_ingred = dicc_contador_ingredientes
