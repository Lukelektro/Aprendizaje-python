datos = []

def agregar_datos():
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    datos.append((clave, valor))
    print("Datos agregados correctamente.")

def obtener_valor():
    clave = input("Ingrese la clave: ")
    for tupla in datos:
        if tupla[0] == clave:
            valor = tupla[1]
            print(f"El valor asociado a la clave '{clave}' es: {valor}")
            return
    print("La clave no se encuentra en los datos.")

while True:
    print("\n-- MENÚ --")
    print("1. Agregar datos")
    print("2. Obtener valor")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_datos()
    elif opcion == "2":
        obtener_valor()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Ingrese nuevamente.")
