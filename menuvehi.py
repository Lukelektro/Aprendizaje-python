registros_vehiculos = []
ID_registros = 0

def solicitar_patente():
    patente = input("Ingrese la patente del vehículo: ")
    return patente

def solicitar_marca():
    marca = input("Ingrese la marca del vehículo: ")
    return marca

def solicitar_modelo():
    modelo = input("Ingrese el modelo del vehículo: ")
    return modelo

def solicitar_anio_fabricacion():
    anio = int(input("Ingrese el año de fabricación del vehículo (entre 1900 y 2021): "))
    while anio < 1900 or anio > 2021:
        anio = int(input("Ingrese el año de fabricación del vehículo (entre 1900 y 2021): "))
    return anio

def solicitar_tipo_vehiculo():
    tipo_vehiculo = input("Ingrese el tipo de vehículo (b, d, e, h en minúsculas o mayúsculas): ")
    while tipo_vehiculo not in ["b", "B", "d", "D", "e", "E", "h", "H"]:
        tipo_vehiculo = input("Ingrese el tipo de vehículo (b, d, e, h en minúsculas o mayúsculas): ")
    return tipo_vehiculo

def buscar_vehiculo(patente):
    for vehiculo in registros_vehiculos:
        if vehiculo["patente"] == patente:
            return vehiculo
    return None

def registrar_vehiculo():
    global ID_registros
    ID_registros += 1
    patente = solicitar_patente()
    marca = solicitar_marca()
    modelo = solicitar_modelo()
    anio = solicitar_anio_fabricacion()
    tipo_vehiculo = solicitar_tipo_vehiculo()
    vehiculo = {
        "ID": ID_registros,
        "patente": patente,
        "marca": marca,
        "modelo": modelo,
        "anio_fabricacion": anio,
        "tipo_vehiculo": tipo_vehiculo
    }
    registros_vehiculos.append(vehiculo)
    print("Vehículo registrado exitosamente con el ID: {}".format(ID_registros))

def registro_mantenimiento():
    patente = solicitar_patente()
    vehiculo = registros_vehiculos(patente)
    if vehiculo:
        print("Mantenimiento registrado exitosamente para el vehículo con ID {}".format(vehiculo["ID"]))
    else:
        print("El vehículo con la patente {} no está registrado en la base de datos".format(patente))

def consulta_vehiculo():
    patente = solicitar_patente()
    vehiculo = buscar_vehiculo(patente)
    if vehiculo:
        print("ID: {}".format(vehiculo["ID"]))
        print("Patente: {}".format(vehiculo["patente"]))
        print("Marca: {}".format(vehiculo["marca"]))
        print("Modelo: {}".format(vehiculo["modelo"]))
        print("Año de fabricación: {}".format(vehiculo["anio_fabricacion"]))
        print("Tipo de vehículo: {}".format(vehiculo["tipo_vehiculo"]))
    else:
        print("El vehículo con la patente {} no está registrado en la base de datos".format(patente))