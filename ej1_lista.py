asignaturas = []
flag = True

while flag == True:
    asignatura = input("Ingrese 6 asignaturas: ")
    asignaturas.append(asignatura)
    print(asignaturas)
    if len(asignaturas) > 5:
        flag = False

