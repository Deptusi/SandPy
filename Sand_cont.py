num_ordenes_tot = 0
total_vendido = 0
total_triple = 0
total_doble = 0
total_sencilla = 0

## Esta funcion se encarga de abrir el archivo, leerlo y modificar los coantadores para tener una contabildiad de lo vendido en el sistema e imprimirlo
## Fernando Gonzalez
## version 1.1 - 30/05/2021 cambios por Fernando Gonzalez: correcion de errores
## -version1.0 - 26/05/2021
def abrir_contabilidad():
    global num_ordenes_tot
    global total_vendido

    ## Cambiar la direccion del archivo de contabilidad
    with open('d:\\Documents\\Universidad\\Python\\Proyecto2\\SandPy\\contabilidad.txt', 'r') as reader:
       for line in reader:
            templine = line.split('|')
            print("Orden Numero: " + templine[0])
            if ';' in templine[1]:
                list_sandwich = templine[1].split(';')
                for sand in list_sandwich:
                    if('-' in sand):
                        size = sand.split('-')[0]
                    else:
                        size = sand .split('/')[0]
                    count_sandwich(size)
                    ingredientslist = sand.split('/')[0].split('-')
                    ingredientslist.pop(0)
                    ingredients = ","
                    ingredients = ingredients.join(ingredientslist)
                    total = sand.split('/')[1]
                    print(f"Sandwich tamano: {size}, con los ingredientes: {ingredients}, con un total de: {total}")
            else:
                if('-' in templine[1]):
                    size = templine[1].split('-')[0]
                else:
                    size = templine[1].split('/')[0]
                count_sandwich(size)
                ingredientslist = templine[1].split('/')[0].split('-')
                ingredientslist.pop(0)
                ingredients = ","
                ingredients = ingredients.join(ingredientslist)
                total = templine[1].split('/')[1]
                print(f"Sandwich tamano: {size}, con los ingredientes: {ingredients}, con un total de: {total}")
            print(f"Total de orden: {templine[2]}")
            print("*"*28,)
            num_ordenes_tot = num_ordenes_tot + 1
            total_vendido = total_vendido + float(templine[2])
    print("")
    print("*"*28,)
    print("Total de Ordenes Vendidas: " + str(num_ordenes_tot))
    print("Total Vendido: " + str(total_vendido))
    print("*"*28,)
    print("Ventas por sandwiches")
    print("Triple: " + str(total_triple))
    print("Doble: " + str(total_doble))
    print("Individual: " + str(total_sencilla))

## Esta funcion cambia la variable que sea del tamano del sandwich
## Parametro que recibe sanwich, tiene la informacion del sandwich
## Fernando Gonzalez
## version 1.0 - 26/05/2021
def count_sandwich(sandwich):
    if(sandwich == "Triple"):
        global total_triple
        total_triple = total_triple +  1
    elif (sandwich == "Doble"):
        global total_doble
        total_doble = total_doble + 1
    elif (sandwich == "Individual"):
        global total_sencilla
        total_sencilla = total_sencilla + 1

## Funcion necesaria para borrar las variables guardadas
## Fernando Gonzalez
## version 1.0 - 26/05/2021
def borrar_info():
    global num_ordenes_tot
    global total_vendido
    global total_triple
    global total_doble
    global total_sencilla 
    num_ordenes_tot = 0
    total_vendido = 0
    total_triple = 0
    total_doble = 0
    total_sencilla = 0

## Inicia la contabilidad y borra las variables
## Fernando Gonzalez
## version 1.0 - 26/05/2021
def start_cont():
    abrir_contabilidad()
    borrar_info()