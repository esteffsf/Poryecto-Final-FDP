producto_archivo = open("producto.txt", "w")
producto_archivo.close

while True:
    print("-----------")
    print(" - Menú principal - ")
    print("1.- Agregar producto.")
    print("2.- Consultar inventario.")
    print("3.- Vender producto.")
    print("4.- Buscar producto.")
    print("5.- Stock bajo.")
    print("6.- Ventas del día.")
    print("7.- Total vendido del día.")
    print("8.- Salir.")
    print("")
    try: 
        seleccion1 = int(input("Escoje una de las anteriores opciones: "))
        if seleccion1 not in range(1,9):
            print("")
            print("Error, por favor solo escribe una opción disponible.")
            print("")
            continue
        elif seleccion1 == 1:
            nuevo_producto = input("Escribe un nuevo producto: ")
            cantidad_productos = int(input("¿Cuántos productos quieres agregar?: "))
            nuevo_precio = float(input("Escribe el precio del producto unitario (si ya existe, se actualiza): "))
            comprobacion = nuevo_producto.replace(" ", "")
            if comprobacion == "":
                print("")
                print("Error, por favor vuelve a intentarlo y escribe algo en producto.")
                print("")
                continue
            elif cantidad_productos < 0:
                print("")
                print("Error, por favor escribe un numero mayor o igual a 0 en cantidad de productos.")
                print("")
                continue
            elif nuevo_precio <= 0:
                print("")
                print("Error, por favor escribe un numero mayor a 0 en el precio.")
                print("")
                continue

            productos = []

            try:
                with open("producto_archivo.txt", "r") as archivo:
                    for linea in archivo:
                        datos = [dato.strip() for dato in linea.strip().split("|") if dato.strip() != ""]
                        if len(datos) >= 3:
                            nombre = datos[0].replace("Nombre del producto: ", "")
                            cantidad = int(datos[1].replace("Cantidad de productos: ", ""))
                            precio = float(datos[2].replace("Precio del producto unitario: $", ""))
                            productos.append([nombre, cantidad, precio])
                        
            except FileNotFoundError:
                pass

            producto_encontrado = False

            for producto in productos:
                if producto[0].lower() == nuevo_producto.lower():
                    producto[1] += cantidad_productos
                    producto[2] = nuevo_precio
                    producto_encontrado = True

            if producto_encontrado == False:
                productos.append([nuevo_producto, cantidad_productos, nuevo_precio])

            with open("producto_archivo.txt", "w") as archivo:
                for producto in productos:
                    archivo.write(f"|Nombre del producto: {producto[0]} |")
                    archivo.write(f"|Cantidad de productos: {producto[1]}|")
                    archivo.write(f"|Precio del producto unitario: ${producto[2]}|\n")

        elif seleccion1 == 2:
            with open("producto_archivo.txt","r") as archivo:
                leer = archivo.readlines()
                contador = 1
                for i in leer:
                    print(f"{contador}.- {i}")
                    contador += 1

        elif seleccion1 == 3:
            continue
            #
        elif seleccion1 == 4:
            continue
            #
        elif seleccion1 == 5:
            continue
            #
        elif seleccion1 == 6:
            continue
            #
        elif seleccion1 == 7:
            continue
            #
        elif seleccion1 == 8:
            continue
            #
            
    except:
        print("")
        print("Error, por favor solo escribe un numero antes mencionado.")
        print("")

