vehiculos = {}

def registrar_vehiculo():
    patente = input("Ingrese la patente del vehículo: ")
    while len(patente) < 6 or len(patente) > 8:
        patente = input("La patente debe tener entre 6 y 8 caracteres. Ingrese nuevamente: ")
    marca = input("Ingrese la marca del vehículo: ")
    while marca == "":
        marca = input("La marca no puede estar vacía. Ingrese nuevamente: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    while modelo == "":
        modelo = input("El modelo no puede estar vacío. Ingrese nuevamente: ")   
    año = int(input("Ingrese el año de fabricación del vehículo (entre 1900 y 2021): "))
    while año < 1900 or año > 2021:
        año = int(input("El año debe ser un número entre 1900 y 2021 en valor numerico. Ingrese nuevamente: "))   
    tipo = input("Ingrese el tipo de vehículo (B, D, E, H): ")
    while tipo not in ["B", "D", "E", "H", "b", "d", "e", "h"]:
        tipo = input("El tipo de vehículo debe ser B, D, E o H. Ingrese nuevamente: ")
    vehiculos[patente] = {"marca": marca, "modelo": modelo, "año": año, "tipo": tipo}
    print(f"Vehículo con patente {patente} registrado correctamente.")

def registrar_mantenimiento():
    patente = input("Ingrese la patente del vehículo: ")
    while patente not in vehiculos:
        patente = input("La patente no se encuentra registrada. Ingrese nuevamente: ")
    fecha = input("Ingrese la fecha del mantenimiento (dd/mm/aaaa): ")
    observaciones = input("Ingrese las observaciones del mecánico: ")
    if "mantenimientos" not in vehiculos[patente]:
        vehiculos[patente]["mantenimientos"] = []
    vehiculos[patente]["mantenimientos"].append({"fecha": fecha, "observaciones": observaciones})
    print("Mantenimiento registrado correctamente.")

def consultar_vehiculo():
    patente = input("Ingrese la patente del vehículo: ")
    while patente not in vehiculos:
        patente = input("La patente no se encuentra registrada. Ingrese nuevamente: ")
    vehiculo = vehiculos[patente]
    print(f"Patente: {patente}\nMarca: {vehiculo['marca']}\nModelo: {vehiculo['modelo']}\nAño: {vehiculo['año']}\nTipo: {vehiculo['tipo']}")
    if "mantenimientos" in vehiculo:
        print("Mantenimientos:")
        for mantenimiento in vehiculo["mantenimientos"]:
            print(f"- Fecha: {mantenimiento['fecha']}\n  Observaciones: {mantenimiento['observaciones']}")

while True:
    print("\n-- MENÚ --")
    print("1. Registrar vehículo")
    print("2. Registrar mantenimiento")
    print("3. Consultar vehículo")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_vehiculo()
    elif opcion == "2":
        registrar_mantenimiento()
    elif opcion == "3":
        consultar_vehiculo()
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Ingrese nuevamente.")