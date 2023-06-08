'''
na emprendedora comenzó a vender tablas de madera con entrega a domicilio. Estas, son de diversas formas y tamaños. 
Para ello creó una tienda online donde los clientes solicitan los productos y la grabación de la tabla si así lo desea.  
Cada tabla tiene un precio según el tamaño ella:  
Pequeña: $15.000
Mediana: $25.000
Grande:   $35.000

Determine el total a pagar por un cliente que requiere una cantidad X de tablas de distintos tamaños y la cantidad de cada una de las tablas solicitadas.
Ejemplo:
Pequeña: 2 	$30.000
Mediana: 1 	$25.000
Grande:   0 	$0
Total.         $55.000
'''

tabla_pequena = 0
tabla_grande = 0                      
tabla_mediana = 0

cont_pequena = 0
cont_mediana = 0
cont_grande = 0

menu = True

print(f"""
    Precios de tablas:
    1.- Tabla Pequeña = 15000
    2.- Tabla Mediana = 35000
    3.- Tabla Grande = 25000
    4.- Total
    # """)

while menu == True:
    try:
        opc = int(input("Seleccione una opción: "))
    except:
        print("el valor ingresado no es un numero, intente nuevamente")

    if opc == 1:
        tabla_pequena = tabla_pequena + 15000
        cont_pequena = cont_pequena + 1
        print(f"Tabla pequeña ingresada correctamente, llevas un total de {cont_pequena} tablas pequeñas")


    elif opc == 2:
        tabla_mediana = tabla_mediana + 35000
        cont_mediana = cont_mediana + 1
        print(f"Tabla medianas ingresada correctamente, llevas un total de {cont_mediana} tablas medianas")
        opc = opc - 2  

    elif opc == 3:
        tabla_grande = tabla_grande + 25000
        cont_grande = cont_grande + 1
        print(f"Tabla grandes ingresada correctamente, llevas un total de {cont_grande} tablas grandes")
        opc = opc - 3

    elif opc == 4:     
        cont_total = cont_mediana + cont_grande + cont_pequena
        total = tabla_grande + tabla_mediana + tabla_pequena
        print(f"""
        sus totales son:
        total de tablas pequeñas: {cont_pequena} = {tabla_pequena}
        total de tablas medianas: {cont_mediana} = {tabla_mediana}
        total de tablas grandes: {cont_grande} = {tabla_grande}
        total de todas las tablas: {cont_total} = {total}
        """)
        opc = opc - 4

    elif opc >= 5:
        print("la opcion no es valida, intente nuevamente") 
        opc = opc - opc   

 
