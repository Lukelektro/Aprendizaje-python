mascotas_r = {}

def registrar_mascota():
    chip_mascota = input("Ingrese el numero del chip de su mascota: ")
    while len(chip_mascota) < 16:
        chip_mascota = input("el numero ingresado es menor a 16, porfavor ingrese correctamente el numero de la mascota.")            
    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    while nombre_mascota == "":
        nombre_mascota = input("ingrese un nombre porfavor: ")
    especie_mascota = ("Ingrese que animal es su mascota: Perro, Gato, Otro")
    while especie_mascota.lower() not in ["perro" , "gato" ,"otro"]: 
        if especie_mascota == "otro":
            especie_mascota = input("ingrese porfavor el animal: ")
        elif especie_mascota == "perro":
            print("ingresado como perro")
        elif especie_mascota == "gato":
            print("ingresado como : gato")
        else:
            print("ingrese un animal valido porfavor.")
    raza_animal = input("ingrese la raza de la mascota: ")
    while raza_animal == "":
        raza_animal = input("la raza no puede ir en blanco, ingrese la raza porfavor.")
    edad_animal = int(input("ingrese el la edad de la mascota: "))
    while edad_animal < 0 and edad_animal > 20:
        edad_animal = input("la edad del animal no debe superar los 20 años ni menor a 0 años")
    peso_mascota = float(input("porfavor, ingrese el peso del animal"))
    while peso_mascota < 0 and peso_mascota > 100:
        peso_mascota = float(input("porfavor, ingrese un peso bajo los 100 y sobre el 0"))
    mascotas_r[chip_mascota] = {"nombre": nombre_mascota , "animal": especie_mascota , "raza": raza_animal , "edad": edad_animal , "peso": peso_mascota}
    print(f"el/la {especie_mascota} : {nombre_mascota} fue ingresado correctamente al chip: {chip_mascota}")         

def consultar_mascota():
    chip_mascota = input("ingrese el chip de la mascota: ")
    while chip_mascota not in mascotas_r:
        chip_mascota = print("el chip ingresado no esta en nuestra base de datos, ingrese nuevamente: ")
    mascota = mascotas_r[chip_mascota]
    print(f"chip: {mascota}\nEspecie: {mascota['especie_mascota']}\nRaza:{mascota['raza_animal']}\nEdad: {mascota['edad_animal']}\nPeso:{mascota['peso_mascota']}")
    if "consulta" in mascota:
        print("Consulta: ")
        for consulta in mascota["consulta"]:
            print(f"Fecha: {consulta['fecha']}\nMotivo Consulta: {consulta['motivo']}")    
        
def registrar_consulta():
    chip_mascota = input("ingrese el chip de la mascota: ")
    while chip_mascota not in mascotas_r:
        chip_mascota = input("el chip de la mascotas no esta ingresada en la base de datos, ingrese nuevamente: ")
    fecha = input("ingrese una fecha de la consulta (dd/mm/aaaa): ")
    motivo = input("ingrese el motivo de la consulta: ")
    if "consulta" not in mascotas_r[chip_mascota]:
        chip_mascota = mascotas_r[chip_mascota]["consulta"] = []
    mascotas_r[chip_mascota]["consulta"].append({"fecha": fecha , "motivo": motivo})
    print(f"consulta agregada al chip {chip_mascota} correctamente.")      

while True:
    print("""
---Sushi-Nikkey App---
1.- Registrar Mascota
2.- Consultar Datos Mascota
3.- Registrar Consulta
4.- Salir
    """)             
    opc = int(input("ingrese una opcion: "))
    if opc == 1:
        registrar_mascota()
    elif opc == 2:
        consultar_mascota()
    elif opc == 3:
        registrar_consulta()
    elif opc == 4:
        break
    else:
        input("el numero ingresado es incorrecto, porfavor reingrese un numero")    

