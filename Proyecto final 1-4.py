def consultar_inventario():
    with open("producto_archivo.txt","r") as archivo:
        leer = archivo.readlines()
        if len(leer) ==0:
            print("No hay productos en el inventario.")
            return leer
        contador = 1
        for i in leer:
            print(f"{contador}.- {i}")
            contador += 1
        return leer

def reescribir_archivo():
    with open("producto_archivo.txt", "w") as archivo:
        for producto in productos:
            if producto["Cantidad"]>0:
                archivo.write(f"|Nombre del producto: {producto["Nombre"].title()} |")
                archivo.write(f"|Cantidad de productos: {producto["Cantidad"]}|")
                archivo.write(f"|Precio del producto unitario: ${producto["Precio"]:.2f}|\n")

def lista_simple():
    print("--------------------------")
    print("Productos disponibles:")
    hay_productos=False
    for producto in productos:
        if producto["cantidad"] >=1:
            print(f"-{producto["nombre"].title()}")
            hay_productos=True
    if not hay_productos:
        print("No hay productos aún.")
    print("--------------------------")
    return hay_productos

def buscar_existencia(producto_buscado):
    #Busca que el nombre exista en algún diccionario
    producto_existe=False
    for producto in productos:
        if producto["Nombre"]==producto_buscado:
            producto_encontrado=producto
            producto_existe=True
            return producto_encontrado
    if not producto_existe:
        print("Este producto no existe.")
        return producto_existe

while True:
    #Abre el archivo y lo crea si no existe
    try:
        producto_archivo = open("producto_archivo.txt", "r")
        producto_archivo.close
    except FileNotFoundError:
        producto_archivo = open("producto_archivo.txt", "w")
        producto_archivo.close()

    #Mete el contenido del archivo a una lista de diccionarios
    productos=[]
    with open("producto_archivo.txt", "r") as archivo:
        for linea in archivo:
            datos = [dato.strip() for dato in linea.strip().split("|") if dato.strip() != ""]
            if len(datos) >= 3:
                nombre = datos[0].replace("Nombre del producto: ", "")
                cantidad = int(datos[1].replace("Cantidad de productos: ", ""))
                precio = float(datos[2].replace("Precio del producto unitario: $", ""))
                productos.append({"Nombre": nombre.title(), "Cantidad": cantidad, "Precio": precio})
    print("\n",productos)
    
    print("-----------------------")
    print(" - Menú principal - \n")
    print("1.- Agregar producto.")
    print("2.- Consultar inventario.")
    print("3.- Vender producto.")
    print("4.- Buscar producto.")
    print("5.- Stock bajo.")
    print("6.- Ventas del día.")
    print("7.- Total vendido del día.")
    print("8.- Salir.\n")
  
    opcion = input("Elije una opción (Sólo el número): ")
    print("")

    if opcion == "1":
        while True:
            print("-----Agregar Producto-----")
            try:
                nuevo_producto = input("Escribe un nuevo producto: ")
                cantidad_productos = int(input("¿Cuántos productos quieres agregar?: "))
                nuevo_precio = float(input("Escribe el precio del producto unitario (si ya existe, se actualiza): "))
                comprobacion = nuevo_producto.replace(" ", "")
            
                if comprobacion == "":
                    print("")
                    print("Error, no se puede guardar un producto vacío.")
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
                break

            except ValueError:
                print("\nError, respuesta no válida.\n")
                continue

        #Checa si el producto ya existe
        producto_encontrado = False

        for producto in productos:
            if producto["Nombre"].lower() == nuevo_producto.lower():
                producto["Cantidad"] += cantidad_productos
                producto["Precio"] = nuevo_precio
                producto_encontrado = True

        #Si no existe, lo agrega a la lista
        if producto_encontrado == False:
            productos.append({"Nombre": nuevo_producto, "Cantidad": cantidad_productos, "Precio": nuevo_precio})

        reescribir_archivo()

    elif opcion == "2":
        print("-----Inventario-----")
        leer=consultar_inventario()
        if len(leer)==0:
            continue

    elif opcion == "3":
        print("-----Venta de Productos-----")
        hay_productos=lista_simple()
        if not hay_productos:
            continue

        while True:
            producto_buscado=input("Escriba el nombre del producto que desea vender: ").lower()

            producto_existe=False
            for producto in productos:
                if producto["Nombre"]==producto_buscado:
                    producto_encontrado=buscar_existencia(producto_buscado)
                    producto_existe=True
            if not producto_existe:
                producto_existe=buscar_existencia(producto_buscado)
                continue


            try:
                cantidad_a_vender=int(input("Ingrese la cantidad de productos que desea vender: "))
                if cantidad_a_vender<=0:
                    print("Cantidad no válida. Intente de nuevo.")
                    continue

                if cantidad_a_vender <=producto_encontrado["Cantidad"]:
                    producto_encontrado["Cantidad"]-=cantidad_a_vender
                    total_vendido=producto_encontrado["Precio"]*cantidad_a_vender
                    print(f"Venta realizada!\nSu total sería: ${total_vendido:.2f}")
                    break
                else:
                    print("No hay suficiente stock de este producto. Revise inventario para ver el stock.")
                    break

            except ValueError:
                print("Respuesta no válida.")

    elif opcion == "4":
        continue
        #
    elif opcion == "5":
        continue
        #
    elif opcion == "6":
        continue
        #
    elif opcion == "7":
        continue
        #
    elif opcion == "8":
        continue
        #
    else:
        print("Opción no válida. Escriba solo un número disponible")