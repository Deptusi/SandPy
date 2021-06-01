from Sand_functions import *
from Sand_cont import start_cont
direccion_archivo = 'contabilidad.txt'
def print_Tittle():
    print("*"*27)
    print("*     SANDWICHES UCAB     *")
    print("*"*27)

## Esta funcion se encarga de generar el numero de orden para guardar en el archivo
## Fernando Gonzalez
## version 1.0 - 30/05/2021
def contar_ordenes():
    contador_ordenes = 0
    with open(direccion_archivo, 'r') as reader:
       for line in reader:
           contador_ordenes += 1
    return contador_ordenes

## Esta funciona se encarga de generar el string y guardarlo en el archivo
## Recibe como parametro lista_de_ordenes que tiene la lista de los sandwchices pedidos
## Fernando Gonzalez
## version 1.0 - 30/05/2021
def guardar_sandwiches(lista_de_ordenes):
    numero_de_orden = contar_ordenes() + 1
    orden_para_guardar = str(numero_de_orden) + "|"
    total = 0
    for sandwich in lista_de_ordenes:
        tamano_sandwich = sandwich.tamano[1]
        lista_de_ingredientes = ""
        for ingredientes in sandwich.lista_descriptiva:
            lista_de_ingredientes = lista_de_ingredientes + "-" + ingredientes[1]
        orden_para_guardar = orden_para_guardar + tamano_sandwich + lista_de_ingredientes + "/" + str(sandwich.precio) + ";"
        total += sandwich.precio
    
    orden_para_guardar = orden_para_guardar[:-1] + "|" + str(total)
    print(orden_para_guardar)
    with open(direccion_archivo, 'a+') as outfile:
        outfile.write("\n")
        outfile.write(orden_para_guardar)
    outfile.close()

def imprimit_total(lista_de_ordenes):
    guardar_sandwiches(lista_de_ordenes)
    print("*"*28,)
    print(f"El pedido tiene un total de {len(lista_de_ordenes)} \
sándwich(es) por un monto de {sum([sandwich.precio for sandwich in lista_de_ordenes])}")
    
    # aquí podréamos agregar una opción para dar un resumen detallado de los 
    # pedidos, y preguntar si quiere eliminar un pedido, o duplicar otro
    print("\nGracias por su compra, regrese pronto")

## Esta funcion es el ciclo de vida del programa
## Fernando Gonzalez
## -version 1.1 - 30/05/2021 cambios por Fernando Gonzalez: cambios para la salida de sistema 
## -version 1.0 - 26/05/2021
def start_program():
    ciclo_de_programa=True
    while(ciclo_de_programa):
        seleccion_caso()
        salir=""
        while(salir!="s" and salir!="n"):
            salir=input("Desea salir? Si(s) - No(n)")
            if salir== "s":
                print("Hasta Luego")
                ciclo_de_programa = False
            else:
                if salir == "n":
                    salir==""
        print("*"*28,)
    print("")

## Esta funcion es para dar al usuario la opcion de escoger que quiere hacer en el sistema
## Fernando Gonzalez
## version 1.0 - 26/05/2021
def seleccion_caso():
    print("Ver Contabilidad (1)")
    print("Realizar venta de sandwiches (2)")
    entrada_datos=""
    while(entrada_datos!="1" and entrada_datos!="2"):
        entrada_datos=input("Que desea hacer? ")
    print("*"*28,)
    print("")
    if entrada_datos=="1":
        start_conta()
    else: 
        if entrada_datos == "2":
            start_sale()
        else:
            print("Opcion incorrecta, Escoja nuevamente")

## Inicia la opcion de contabilidad
## Fernando Gonzalez
## version 1.0 - 26/05/2021
def start_conta():
    start_cont()

## Inicia la opcion de venta
## Fernando Gonzalez
## version 1.0 - 26/05/2021
def start_sale():
    imprimit_total(realizar_orden())
