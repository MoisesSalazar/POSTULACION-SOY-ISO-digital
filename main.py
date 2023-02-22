# Definir los diccionarios
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

# Función para mostrar la lista de productos
def mostrar_productos():
    print("="*80)
    print("{:<10s}{:<30s}{:<20s}{:<10s}".format("ID", "Producto", "Precio", "Stock"))
    print("="*80)
    for id, producto in Productos.items():
        precio = Precios[id]
        stock = Stock[id]
        print("{:<10d}{:<30s}{:<20.2f}{:<10d}".format(id, producto, precio, stock))
    print("="*80)
  
# Función para agregar un producto
def agregar_producto():
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad de stock del producto: "))
    id = max(Productos.keys()) + 1
    Productos[id] = producto
    Precios[id] = precio
    Stock[id] = stock
    print(f"El producto {producto} ha sido agregado correctamente.")

# Función para eliminar un producto
def eliminar_producto():
    id = int(input("Ingrese el ID del producto que desea eliminar: "))
    if id in Productos:
        del Productos[id]
        del Precios[id]
        del Stock[id]
        print("El producto ha sido eliminado correctamente.")
    else:
        print("El ID ingresado no corresponde a ningún producto.")

# Función para actualizar un producto
def actualizar_producto():
    id = int(input("Ingrese el ID del producto que desea actualizar: "))
    if id in Productos:
        producto = input("Ingrese el nuevo nombre del producto (deje vacío si no desea cambiarlo): ")
        precio = input("Ingrese el nuevo precio del producto (deje vacío si no desea cambiarlo): ")
        stock = input("Ingrese la nueva cantidad de stock del producto (deje vacío si no desea cambiarlo): ")
        if producto != '':
            Productos[id] = producto
        if precio != '':
            Precios[id] = float(precio)
        if stock != '':
            Stock[id] = int(stock)
        print("El producto ha sido actualizado correctamente.")
    else:
        print("El ID ingresado no corresponde a ningún producto.")

# Programa principal
while True:
    mostrar_productos()
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
    opcion = input("Elija opción: ")
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        eliminar_producto()
    elif opcion == '3':
        actualizar_producto()
    elif opcion == '4':
        break
    else:
        print("Opción inválida. Intente de nuevo.")
