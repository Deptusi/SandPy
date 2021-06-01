# autor: Christian Neira
def ingresar_cupon():
    salir = False
    descuento_porcentaje = 0
    while not salir:
        respuesta = input("¿Usted tiene un cupon [s/n]? ")
        if (respuesta == "s"):
            codigo_cupon= input("Ingrese el codigo del cupón: ")
            archivo_codigos = open("codigos_cupones.txt", "r")
            cupones = []
            for linea_cupon in archivo_codigos:
                linea_cupon = linea_cupon.replace("\n", "")
                cupones.append(linea_cupon)
            archivo_codigos.close()
            buscar_codigo = False
            for cupon in cupones:
                codigo = cupon.split()[0]
                if (codigo_cupon == codigo):
                    archivo_codigos = open("codigos_cupones.txt", "r")
                    lineas_cupones = archivo_codigos.readlines()
                    archivo_codigos.close()
                    archivo_codigos_nuevo = open("codigos_cupones.txt", "w")
                    for linea_cupon in lineas_cupones:
                        if (linea_cupon.strip("\n") != cupon):
                            archivo_codigos_nuevo.write(linea_cupon)
                    archivo_codigos_nuevo.close()
                    buscar_codigo = True
                    descuento_porcentaje = int(cupon.split()[1])
                    return descuento_porcentaje
            if (not buscar_codigo):
                print("No existe este codigo de cupon en el sistema")
        elif (respuesta == "n"):
            salir = True
            return descuento_porcentaje
        else:
            print("Ingrese una opción valida")