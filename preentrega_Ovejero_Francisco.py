productos = [
    ["pera", "fruta", 10],
    ["escoba", "limpieza", 50],
    ["banana", "fruta", 15]
]

while True:
    print("MENÚ PRINCIPAL")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("0. Salir")
    
    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1: 
            print("----AGREGAR PRODUCTO-----")
            #este while me permite ingresar varios productos sin teners que regresar al menu
            while True:
                #le pido los datos al usuario y hago validaciones
                nombre = input("Ingrese el nombre del producto: ")
                while nombre == "" :
                    print("El nombre no puede quedar vacio. Intente otra vez.")
                    nombre = input("Ingrese el nombre del producto: ")

                categoria = input("Ingrese la categoria: ")
                while categoria == "" :
                    print("La categoria no puede quedar vacia. Intente otra vez.")
                    categoria = input("Ingrese la categoria: ")

                precio = int(input("Ingrese el precio: "))
                while precio <= 0 :
                    print("El precio no puede ser 0 ni negativo. Intente otra vez.")
                    precio = int(input("Ingrese el precio: "))

                #guardo lo ingresado en la lista productos[]
                nuevo_producto = [nombre, categoria, precio]
                productos.append(nuevo_producto)
                print("--Producto agregado con exito--")

                continuar = input("¿Desea añadir mas productos? (Si/No): ").lower()
                if continuar == "no" : 
                    break
        case 2: 
            print("----LISTA COMPLETA DE PRODUCTOS----")
            #uso el contador para numerar los productos al mostrarlos
            contador = 0
            for producto in productos : 
                contador += 1
                print(f"Producto {contador}")
                print(f"Nombre: {producto[0]}")
                print(f"Categoria: {producto[1]}")
                print(f"Precio: ${producto[2]}\n")
                #print(f"{producto[0]}\t{producto[1]}\t${producto[2]}") 
        case 3: 
            print("---BUSCAR PRODUCTO----")
            #pido producto a buscar y valido el ingreso
            encontrar_producto = input("Ingrese el producto que quiere buscar: ")
            while encontrar_producto == "" :
                print("El nombre no puede estar vacio. Intente otra vez.")
                encontrar_producto = input("Ingrese el producto que quiere buscar: ")

            encontrado = False

            #busco coincidencias y las muestro en caso de haberlas
            for producto in productos : 
                if encontrar_producto == producto[0] : 
                    print("---Coincidencias de busqueda---")
                    print(f"Nombre: {producto[0]}")
                    print(f"Categoria: {producto[1]}")
                    print(f"Precio: ${producto[2]}\n")
                    encontrado = True

            if encontrado == False :
                print("No hubo coincidencias de busqueda.")
        case 4: 
            print("---ELIMINAR PRODUCTO---")
            #pido la posicion del producto que quiero eliminar y valido lo ingresado
            indice = int(input("Ingrese el número del producto a eliminar: ")) - 1
            while indice < 0 or indice >= len(productos) :
                print("El numero ingresado no existe en la lista. Intente otra vez")
                indice = int(input("Ingrese el número del producto a eliminar: ")) - 1

            #elimino el producto 
            producto_eliminado = productos.pop(indice)

            print(f"El producto {producto_eliminado[0]} fue eliminado correctamente")
        case 0: 
            print("Programa terminado")
            break  #termino el bucle en caso de ingresar 0
        case _:
            print("Opción no válida. Por favor intenta de nuevo")
