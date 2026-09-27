import datetime
import time

while True:
    fecha_ingresada = input("Ingrese la fecha (DD/MM/YYYY): ").strip()
    try:
        fecha_inicial = datetime.datetime.strptime(fecha_ingresada, "%d/%m/%Y")
        fecha = fecha_inicial.strftime("%d/%m/%Y")
        break
    except ValueError:
        print("Fecha no válida. Intente de nuevo.")

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
                archivo.write(f'|Nombre del producto: {producto["Nombre"].title()} |')
                archivo.write(f'|Cantidad de productos: {producto["Cantidad"]}|')
                archivo.write(f'|Precio del producto unitario: ${producto["Precio"]:.2f}|\n')

def lista_simple():
    print("--------------------------")
    print("Productos disponibles:")
    hay_productos=False
    for producto in productos:
        if producto["Cantidad"] >=1:
            print(f"-{producto["Nombre"].title()}")
            hay_productos=True
    if not hay_productos:
        print("No hay productos aún.")
    print("--------------------------")
    return hay_productos

def buscar_existencia(producto_buscado):
    #Busca que el nombre exista en algún diccionario
    for producto in productos:
        if producto["Nombre"]==producto_buscado:
            producto_encontrado=producto
            return producto_encontrado

def registrar_venta(producto,cantidad,precio,total,fecha):
    with open("ventas.txt", "r") as archivo:
        lineas=archivo.readlines()

        fecha_linea= f"Fecha: {fecha}\n"
        nueva_venta=f"-Producto: {producto}, Precio por unidad: ${precio:.2f}, Cantidad: {cantidad}, Total: ${total:.2f}"
        if fecha_linea in lineas:
            donde_esta=lineas.index(fecha_linea)
            lineas.insert(donde_esta + 1, nueva_venta)
            with open("ventas.txt", "w") as archivo:
                for linea in lineas:
                    archivo.write(linea)
        else:
            with open("ventas.txt","a") as archivo:
                archivo.write("\n\n" + fecha_linea)
                archivo.write(nueva_venta)


def stock_bajo():
    print("----- Stock Bajo -----")
    hay_stock_bajo = False

    for producto in productos:
        if producto["Cantidad"] <= 5 and producto["Cantidad"] > 0:
            print(f"{producto['Nombre'].title()} tiene stock bajo.\nUnidades: {producto['Cantidad']}")
            hay_stock_bajo = True

    if not hay_stock_bajo:
        print("No hay productos con stock bajo.")

    return hay_stock_bajo



def ventas_dia():
    venta_dia = []
    
    with open("ventas.txt", "r") as archivo:
        lineas = archivo.readlines()

    fecha_linea = f"Fecha: {fecha}"
    
    agregar_linea = False
    for linea in lineas:
        if linea.strip() == fecha_linea:
            agregar_linea = True
            continue
        
        if "Fecha:" in linea and linea.strip() != fecha_linea:
            agregar_linea = False
        elif agregar_linea:
            if linea.strip()=="":
                continue
            venta_dia.append(linea.strip())

    print(f"Fecha: {fecha}")
    for venta in venta_dia:
        print(venta)
    return venta_dia


def total_ventas_dia():
    total_final=0
    
    for venta in venta_dia:
        if venta=="":
            continue
        partes=venta.split(",")
        total=float(partes[3].split("$")[1])
        total_final+=total
    return total_final


while True:
    #Abre los archivos y los crea si no existen
    try:
        producto_archivo = open("producto_archivo.txt", "r")
        producto_archivo.close()
    except FileNotFoundError:
        producto_archivo = open("producto_archivo.txt", "w")
        producto_archivo.close()

    try:
        archivo=open("ventas.txt","r")
        archivo.close()
    except FileNotFoundError:
        with open("ventas.txt","w") as archivo:
            archivo.write("-----Registro de Ventas-----")
        

    #Mete el contenido del inventario a una lista de diccionarios
    productos=[]
    with open("producto_archivo.txt", "r") as archivo:
        for linea in archivo:
            datos = [dato.strip() for dato in linea.strip().split("|") if dato.strip() != ""]
            if len(datos) >= 3:
                nombre = datos[0].replace("Nombre del producto: ", "")
                cantidad = int(datos[1].replace("Cantidad de productos: ", ""))
                precio = float(datos[2].replace("Precio del producto unitario: $", ""))
                productos.append({"Nombre": nombre.title(), "Cantidad": cantidad, "Precio": precio})
    
    print("\n-----------------------")
    print(" - Menú principal - \n")
    print("1.- Agregar producto.")
    print("2.- Consultar inventario.")
    print("3.- Vender producto.")
    print("4.- Buscar producto.")
    print("5.- Stock bajo.")
    print("6.- Ventas del día.")
    print("7.- Total vendido del día.")
    print("8.- Salir.\n")
  
    opcion = input("Elije una opción (Sólo el número): ").strip()
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
            if producto["Nombre"] == nuevo_producto.title():
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
            producto_buscado=input("Escriba el nombre del producto que desea vender: ").strip().title()
            producto_encontrado=buscar_existencia(producto_buscado)

            if producto_encontrado is None:
                print("Este producto no existe.\n")
                continue

            try:
                cantidad_a_vender=int(input("Ingrese la cantidad de productos que desea vender: "))
                if cantidad_a_vender<=0:
                    print("Cantidad no válida. Intente de nuevo.\n")
                    continue

                if cantidad_a_vender <=producto_encontrado["Cantidad"]:
                    producto_encontrado["Cantidad"]-=cantidad_a_vender
                    total_vendido=producto_encontrado["Precio"]*cantidad_a_vender
                    print("\nVenta realizada!")
                    print(f"|Unidad| {producto_encontrado["Nombre"]} - ${producto_encontrado["Precio"]:.2f}\n|Cantidad| x{cantidad_a_vender}\n----------------\n|Total| ${total_vendido:.2f}")
                    reescribir_archivo()
                    registrar_venta(producto_encontrado["Nombre"], cantidad_a_vender, producto_encontrado["Precio"],total_vendido,fecha)
                    break
                else:
                    print("No hay suficiente stock de este producto. Revise inventario para ver el stock.")
                    break

            except ValueError:
                print("Respuesta no válida.\n")
                continue

                
    elif opcion == "4":
        print("-----Buscar Productos-----")
        hay_productos=lista_simple()
        if not hay_productos:
            continue

        while True:
            producto_buscado=input("Escriba el nombre de un producto para ver más información: ").strip().title()
            producto_encontrado=buscar_existencia(producto_buscado)
            if producto_encontrado is None:
                continue
            
            precio_total=producto_encontrado["Cantidad"]*producto_encontrado["Precio"]

            print("\nInformación del producto:")
            print(f"|Nombre| {producto_encontrado["Nombre"]}\n|Cantidad| {producto_encontrado["Cantidad"]}\n|Precio unitario| {producto_encontrado["Precio"]}\n|Precio total| {precio_total:.2f}")
            break
        
    elif opcion == "5":
        hay_stock_bajo=stock_bajo()
        
    elif opcion == "6":
        print("----- Ventas del día -----")
        venta_dia=ventas_dia()
        if len(venta_dia)==0:
            print("No han habido ventas este día.")
            continue

        
    elif opcion == "7":
        print("----- Total vendido del día -----")
        print("Ventas:")
        venta_dia=ventas_dia()
        if len(venta_dia)==0:
            print("No han habido ventas este día.")
            continue

        total_final=total_ventas_dia()
        print(f"--------------------------\nTotal vendido: ${total_final}")
    
    elif opcion == "8":
        print("Saliendo, no apague el dispositivo.")
        for i in range(3):
            print("...")
            time.sleep(1)
        print("Guardado correctamente, apagando.")
        break
        
    else:
        print("Opción no válida. Escriba solo un número disponible")