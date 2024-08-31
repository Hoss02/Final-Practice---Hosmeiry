menu = [{'id': 20, 'nombre': 'Arroz', 'precio': 50},
        {'id': 21, 'nombre': 'Habichuelas', 'precio': 80},
        {'id': 22, 'nombre': 'Aceite', 'precio': 300},
        {'id': 23, 'nombre': 'Pollo', 'precio': 85},
        {'id': 24, 'nombre': 'Lechuga', 'precio': 80}]

carrito = []

def imprimir_menu(menu):
    tammax = 0
    for item in menu:
        tamactual = len(str(item['id'])) + len(item['nombre']) + len(str(item['precio']))
        if tamactual > tammax:
            tammax = tamactual
    print('-' * (int(tammax / 2 + 2)) + 'Menú' + '-' * (int(tammax / 2 + 2)))
    for item in menu:
        print(f"{item['id']}. {item['nombre']} -> RD${item['precio']}")

def imprimir_factura(carrito):
    tamid = 1
    tamnombre = 1
    tamprecio = 1
    for item in carrito:
        tamidact = len(str(item['id']))
        tamnombreact = len(item['nombre'])
        tamprecioact = len(str(item['precio']))
        if tamidact > tamid:
            tamid = tamidact
        if tamnombreact > tamnombre:
            tamnombre = tamnombreact
        if tamprecioact > tamprecio:
            tamprecio = tamprecioact
    if tamid - 2 < 0:
        tamid = 1
    else:
        tamid -= 2
    if tamnombre - 6 < 0:
        tamnombre = 1
    else:
        tamnombre -= 6
    if tamprecio - 6 < 0:
        tamprecio = 1
    else:
        tamprecio -= 6
    print('ID' + ' ' * (tamid + 2) + 'Nombre' + ' ' * (tamnombre + 1) + 'Precio' + ' ' * (tamprecio) + 'Cantidad' + ' ' * 8 + 'Total')
    subtotal = 0
    for item in carrito:
        total = item['precio'] * item['cantidad']
        subtotal += total
        print(str(item['id']) + ' ' * (tamid + 4 - len(str(item['id']))) + item['nombre'] + ' ' * (tamnombre + 7 - len(item['nombre'])) + str(item['precio']) + ' ' * (tamprecio + 8 - len(str(item['precio']))) + str(item['cantidad']) + ' ' * 8 + str(total))
    impuestos = subtotal * 0.18
    total_final = subtotal + impuestos
    print(f"\nSubtotal: RD${subtotal}")
    print(f"Impuestos (18%): RD${impuestos:.2f}")
    print(f"Total: RD${total_final:.2f}")

def agregar_al_carrito():
    while True:
        try:
            id_producto = int(input("Ingrese el ID del producto: "))
            producto_valido = False
            for item in menu:
                if item['id'] == id_producto:
                    producto_valido = True
                    break
            if not producto_valido:
                print("ID de producto no es válido. Intente de nuevo.")
                continue

            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo. Intente de nuevo.")
                continue

            encontrado = False
            for item in carrito:
                if item["id"] == id_producto:
                    item["cantidad"] += cantidad
                    encontrado = True
                    break
            if not encontrado:
                for item in menu:
                    if item['id'] == id_producto:
                        carrito.append({"id": id_producto, "nombre": item["nombre"], "precio": item["precio"], "cantidad": cantidad})
                        break

            break
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

# Código principal
while True:
    imprimir_menu(menu)
    agregar_al_carrito()
    continuar = input("¿Desea agregar otro producto? (s/n): ")
    if continuar != 's' and continuar != 'S':
        imprimir_factura(carrito)
        break
    print("\033[H\033[J")  # Limpiar pantalla