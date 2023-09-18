agrupaciones = []
def registrar_agrupacion():
    id = input("Ingrese el ID de la agrupación: ")
    nombre = input("Ingrese el nombre de la agrupación: ")
    genero = input("Ingrese el género de la agrupación: ")
    hora_presentacion = input("Ingrese la hora de presentación: ")
    pago = float(input("Ingrese el pago que se le dará a la agrupación: "))
    estado = input("¿Ya se presentó la agrupación? (True/False): ").lower() == 'true'
    
    agrupacion = {
        'id': id,
        'nombre': nombre,
        'genero': genero,
        'hora_presentacion': hora_presentacion,
        'pago': pago,
        'estado': estado
    }
    
    agrupaciones.append(agrupacion)
    print("Agrupación registrada con éxito.")

def mostrar_bandas_no_presentadas():
    no_presentadas = [agrupacion for agrupacion in agrupaciones if not agrupacion['estado']]
    if no_presentadas:
        print("Agrupaciones que no se han presentado:")
        for agrupacion in no_presentadas:
            print(f"ID: {agrupacion['id']}, Nombre: {agrupacion['nombre']}, Hora de presentación: {agrupacion['hora_presentacion']}")
    else:
        print("Todas las agrupaciones se han presentado.")

def cambiar_hora_presentacion():
    id_buscar = input("Ingrese el ID de la agrupación que desea cambiar la hora de presentación: ")
    
    for agrupacion in agrupaciones:
        if agrupacion['id'] == id_buscar and not agrupacion['estado']:
            nueva_hora = input("Ingrese la nueva hora de presentación: ")
            agrupacion['hora_presentacion'] = nueva_hora
            print("Hora de presentación actualizada con éxito.")
            return
    
    print("No se encontró la agrupación con el ID especificado o ya se ha presentado.")

def retirar_agrupacion():
    id_retirar = input("Ingrese el ID de la agrupación que desea retirar del festival: ")
    
    for agrupacion in agrupaciones:
        if agrupacion['id'] == id_retirar and not agrupacion['estado']:
            agrupaciones.remove(agrupacion)
            print("Agrupación retirada con éxito.")
            return
    
    print("No se encontró la agrupación con el ID especificado o ya se ha presentado.")

while True:
    print("\nMenú del Festival de Musica")
    print("1. Registrar una agrupacion musical")
    print("2. Mostrar agrupaciones que no se han presentado")
    print("3. Cambiar hora de presentacion")
    print("4. Retirar una agrupacion del festival")
    print("5. Mostrar agrupaciones que se han presentado")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion =='1':
        registrar_agrupacion()
    elif opcion =='2':
        mostrar_bandas_no_presentadas()
    elif opcion =='3':
        cambiar_hora_presentacion()
    elif opcion =='4':
        retirar_agrupacion() 
    elif opcion == '5':
        presentadas = [agrupacion for agrupacion in agrupaciones if agrupacion['estado']]
        if presentadas:
            print("Agrupaciones que se han presentado:")
            for agrupacion in presentadas:
                print(f"ID: {agrupacion['id']}, Nombre: {agrupacion['nombre']}, Hora de presentación: {agrupacion['hora_presentacion']}")
        else:
            print("No hay agrupaciones que se hayan presentado.")
    elif opcion == '6':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

