# autor: Christian Neira
cont_ingred = {}

def devolver_diccionario(numero_orden):
    if (numero_orden == 1):
        contador_ingredientes = {
            "ja":5,
            "ch":5,
            "pi":5,
            "dq":2,
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

def control_inventario(dicc_contador_ingredientes):
    global cont_ingred
    for ingrediente, cantidad in dicc_contador_ingredientes.items():
        if (ingrediente == "ja"):
            print(f"Jamón {ingrediente} tiene la cantidad: {cantidad}")
        elif (ingrediente == "ch"):
            print(f"Champiñones {ingrediente} tiene la cantidad: {cantidad}")
        elif (ingrediente == "pi"):
            print(f"Pimentón {ingrediente} tiene la cantidad: {cantidad}")
        elif (ingrediente == "dq"):
            print(f"Doble Queso {ingrediente} tiene la cantidad: {cantidad}")
        elif (ingrediente == "ac"):
            print(f"Aceitunas {ingrediente} tiene la cantidad: {cantidad}")
        elif (ingrediente == "pp"):
            print(f"Pepperoni {ingrediente} tiene la cantidad: {cantidad}")
        elif (ingrediente == "sa"):
            print(f"Salchichón {ingrediente} tiene la cantidad: {cantidad}")
        if (cantidad == 0):
            print(f"Se agoto la existencia de este ingrediente {ingrediente}")
            cantidad_recargar = int(input("Ingrese la cantidad que sea recargar en el ingrediente: "))
            dicc_contador_ingredientes[ingrediente] = cantidad_recargar
    cont_ingred = dicc_contador_ingredientes
