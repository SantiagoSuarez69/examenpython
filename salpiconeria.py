frutas = []

def ingresar_fruta():
    id = input("Ingrese el ID de la fruta: ")
    nombre = input("Ingrese el nombre de la fruta: ")
    precio_unitario = float(input("Ingrese el precio unitario de la fruta: "))
    cantidad = int(input("Ingrese la cantidad de la fruta: "))
    
    fruta = {
        'id': id,
        'nombre': nombre,
        'precio_unitario': precio_unitario,
        'cantidad': cantidad
    }
    
    frutas.append(fruta)
    print("Fruta ingresada con éxito.")

def costo_total_salpicon():
    costo_total = sum(fruta['precio_unitario'] * fruta['cantidad'] for fruta in frutas)
    print(f"El costo total del salpicón es: ${costo_total:.2f}")

def mostrar_frutas_ordenadas():
    frutas_ordenadas = sorted(frutas, key=lambda x: x['precio_unitario'], reverse=True)
    
    print("Frutas ordenadas de mayor a menor costo:")
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio Unitario: ${fruta['precio_unitario']:.2f}, Cantidad: {fruta['cantidad']}")

def mostrar_frutas_extremas():
    frutas_ordenadas = sorted(frutas, key=lambda x: x['precio_unitario'])
    
    fruta_mas_barata = frutas_ordenadas[0]
    fruta_mas_cara = frutas_ordenadas[-1]
    
    print(f"La fruta más barata es: {fruta_mas_barata['nombre']} (${fruta_mas_barata['precio_unitario']:.2f})")
    print(f"La fruta más cara es: {fruta_mas_cara['nombre']} (${fruta_mas_cara['precio_unitario']:.2f})")

while True:
    print("\nMenú del Salpicón de Frutas")
    print("1. Ingresar información de una fruta")
    print("2. Calcular el costo total del salpicón")
    print("3. Mostrar frutas ordenadas por costo")
    print("4. Mostrar la fruta más barata y más cara")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        ingresar_fruta()
    elif opcion == '2':
        costo_total_salpicon()
    elif opcion == '3':
        mostrar_frutas_ordenadas()
    elif opcion == '4':
        mostrar_frutas_extremas()
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
