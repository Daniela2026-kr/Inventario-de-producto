 # Inventario de maquillaje
#Base de datos y configuración inicial
#lista principal que almacena losproductos como claves
#y sus propiedades precio y disponibilidad
inventario = {
    "Labial": {"precio": 6.00, "disponibles": 20},
    "Base": {"precio": 12.50, "disponibles": 15},
    "Corrector": {"precio": 8.00, "disponibles": 10},
    "Rubor": {"precio": 7.50, "disponibles": 12},
    "Paleta": {"precio": 18.00, "disponibles": 8},
    "Delineador": {"precio": 4.50, "disponibles": 8},
    "Máscara de pestañas": {"precio": 10.00, "disponibles": 20},
    "Iluminador": {"precio": 7.25, "disponibles": 10},
    "Lápiz de cejas": {"precio": 3.99, "disponibles": 30},
    "Set de esponjas y brochas": {"precio": 15.00, "disponibles": 15}
}
#Lista vacia donde se guardaran las compras registradas por el usuario
carrito = []
#Bucle principal de el programa 
#ciclo infinito para que la tienda se mantenga activa hasta que el usuario quiera salir 
while True:
#despliegue del menu interactivo que se mostrara en consola
    print("\n===== TIENDA DE MAQUILLAJE =====")
    print("1. Ver productos")
    print("2. Comprar producto")
    print("3. Ver carrito / Pagar")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()
#Opcion 1 mostrar catalogo 
    if opcion == "1":
        print("\nProductos disponibles:")
        for producto, datos in inventario.items():
            print(f"• {producto} - Precio: ${datos['precio']:.2f} - Disponibles: {datos['disponibles']}")
#Opcion 2 agregar productos al carrito
    elif opcion == "2":
        
        nombre = input("Ingrese el nombre del producto: ").strip().title()
#validamos si el producto que ingreso existe en nuestro inventario
        if nombre in inventario:
#convierte la entrada en un numero entero 
            try:
                cantidad = int(input("¿Cuántos desea comprar? "))
#verifica si hay stock suficiente
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                elif cantidad <= inventario[nombre]["disponibles"]:
#calcula el costo parcial
                    subtotal = cantidad * inventario[nombre]["precio"]
                    carrito.append({
                        "producto": nombre,
                        "cantidad": cantidad,
                        "subtotal": subtotal
                    })
#descuenta las unidades vendidas del inventario actual 
                    inventario[nombre]["disponibles"] -= cantidad
                    print(f"✓ {cantidad}x '{nombre}' agregado(s) al carrito.")
                else:
                    print("No hay suficientes disponibles en stock.")
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
        else:
            print("Producto no encontrado. Verifique la ortografía.")

    elif opcion == "3":
        if not carrito:
            print("\nEl carrito está vacío.")
        else:
            total = 0
            print("\n===== CARRITO DE COMPRAS =====")
            for compra in carrito:
                print(f"{compra['producto']} - Cantidad: {compra['cantidad']} - Subtotal: ${compra['subtotal']:.2f}")
                total += compra["subtotal"]

            print("--------------------------------")
            print(f"TOTAL A PAGAR: ${total:.2f}")

            # Preguntar si desea finalizar la compra
            confirmar = input("\n¿Desea realizar el pago ahora? (s/n): ").strip().lower()

            if confirmar == 's':
                print("¡Pago procesado con éxito! Gracias por su compra.")
                carrito.clear()  # Vaciar el carrito tras pagar
            else:
                print("Puede seguir navegando o agregando más productos.")

    elif opcion == "4":
        print("Gracias por visitar la tienda. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")