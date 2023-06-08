marca_vehi = []
patente_vehi = []
modelo_vehi = []
ano_fabri = []
tipo_vehi = []
registro_vehi = []
consultar_auto = []
i = 1



while True:
    print("""
Bienvenido a ServiExpress:
1.- Registrar Automóvil
2.- Registro Mantenimiento
3.- Consultar Automóvil
4.- Salir
    """)
    opc = int(input("ingrese una opción: "))
    if opc == 1:
        for i in range(1,10000):
            patente = input("ingrese patente del vehiculo: ")
            if len(patente) < 6:
                print("la patente ingresada es incorrecta, porfavor reintente")
            else:
                patente_vehi.append(patente)
            marca = input("ingrese la marca del vehiculo: ")
            marca_vehi.append(marca)
            modelo = input("ingrese el modelo del vehiculo: ")
            modelo_vehi.append(modelo)
            ano_fabricacion = int(input("ingrese el año de fabricación: "))
            if ano_fabricacion > 1900 and ano_fabricacion < 2021:
                ano_fabri.append(ano_fabricacion)
            else:
                print("el vehiculo ingresado es muy antiguo (bajo el año 1900) o superior al 2021")
                break
            tipo_vehiculo = str(input("""
ingrese el tipo de vehiculo
bencina = b, diesel = d, electrico = e, hibrido = h
            """))
            if tipo_vehi == "b" or "B" or "d" or "D" or "e" or "E" or "h" or "H":
                tipo_vehi.append(tipo_vehiculo)
            else:
                print("el tipo de vehiculo ingresado es invalido")
                break
            auto_num = print(f"su vehiculo fue ingresado correctamente, su ID es: {i}")
            i = i + 1

    
