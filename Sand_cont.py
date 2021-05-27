num_ordenes_tot = 0
total_vendido = 0
total_triple = 0
total_doble = 0
total_sencilla = 0

def open_file_cont():
    global num_ordenes_tot
    global total_vendido
    with open('contabilidad.txt', 'r') as reader:
       for line in reader:
            templine = line.split('|')
            print("Orden Numero: " + templine[0])
            if ';' in templine[1]:
                list_sand = templine[1].split(';')
                for sand in list_sand:
                    size = sand.split('-')[0]
                    count_sand(size)
                    ingredientslist = sand.split('/')[0].split('-')
                    ingredientslist.pop(0)
                    ingredients = ","
                    ingredients = ingredients.join(ingredientslist)
                    print(ingredients)
                    total = sand.split('/')[1]
                    print(f"Sandwich tamano: {size}, con los ingredientes: {ingredients}, con un total de: {total}")
            else:
                size = templine[1].split('-')[0]
                count_sand(size)
                ingredientslist = templine[1].split('/')[0].split('-')
                ingredientslist.pop(0)
                ingredients = ","
                ingredients = ingredients.join(ingredientslist)
                total = templine[1].split('/')[1]
                print(f"Sandwich tamano: {size}, con los ingredientes: {ingredients} con un total de: {total}")
            print("*"*28,)
            num_ordenes_tot = num_ordenes_tot + 1
            total_vendido = total_vendido + int(templine[2])
    print("")
    print("*"*28,)
    print("Total de Ordenes Vendidas: " + str(num_ordenes_tot))
    print("Total Vendido: " + str(total_vendido))
    print("*"*28,)
    print("Ventas por sandwiches")
    print("Triple: " + str(total_triple))
    print("Doble: " + str(total_doble))
    print("Individual: " + str(total_sencilla))


def count_sand(sand):
    if(sand == "Triple"):
        global total_triple
        total_triple = total_triple +  1
    elif (sand == "Doble"):
        global total_doble
        total_doble = total_doble + 1
    elif (sand == "Individual"):
        global total_sencilla
        total_sencilla = total_sencilla + 1

def delete_info():
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

def start_cont():
    open_file_cont()
    delete_info()