#Usted debe escribir un programa, utilizando exclusivamente lo aprendido en las unidades 2 y 3de IWI-131, que permita atender las necesidades de la Superintendencia, calculando el costo real de una llamada particular. El programa debe solicitar el nombre del cliente que hace la llamada, para poder entregar una respuesta personalizada. Los valores finales deben redondearse al entero más cercano. No debe redondear resultados intermedios para evitar la pérdida innecesaria de decimales.
print("Bienvenido(a) al programa de calculación de cobro de la empresa BSTH Mobiles, porfavor ingrese su nombre y apellido para comenzar.")

nombre = input("Introduzca aquí su nombre y apellido:")

dia = int(input("Introduzca aquí el día en que se realizó la llamada, si su llamada fue realizada el día domingo, escriba 1. Si su llamada fue realizada otro día, escriba 2."))
diaesp = input("Porfavor, introduzca el nombre del día en que se realizó la llamada, en minúsculas:")
#diaesp = Día específico.
dhora = int(input("Introduzca la hora en la que se realizó la llamada, es decir [xx:yy] los números que se encuentran en xx:"))
#dhora = Hora específica del día.
dmins = int(input("Introduzca los minutos en la hora que se realizó la llamada, es decir [xx:yy] los números que se encuentran en yy:"))
#dmins = Minutos de la hora específica del día.

hora = input("Si la llamada se realizó entre las 5:00 AM y las 12:00 PM, introduzca 1, si se realizó entre las 12:01 PM y las 4:59 AM, introduzca 2:")

minutos = float(input("Introduzca aquì la cantidad de minutos que duró la llamada:"))
segundos = float(input("Introduzca aquí la cantidad de segundos que duró la llamada:"))
print("Nombre y apellido del cliente: ", nombre)
print("Dia en que se realizó la llamada:", diaesp)
print("Inicio de la llamada [Horas]:", dhora)
print("Inicio de la llamada [Minutos]:", dmins)
print("Duración de la llamada [Minutos]:", minutos)
print("Duración de la llamada [Segundos]:", segundos)
print("Muchas gracias por utilizar este programa, le deseamos lo mejor para su vida :D.")
if minutos <= 5:
    precio = minutos * 150 + (segundos * 2,5)
    false = print("El número ingresado es incorrecto.")
elif minutos <= 8:
    precio = minutos * 95 + 750 + (segundos * 1.583)
elif minutos <= 10:
    precio = minutos * 70 + 1035 + (segundos * 1.166)
elif minutos > 10:
    precio = minutos * 50 + 1320 + (segundos* 0.833)
if dia == 1 or dia == 2:
    if dia == 1:
        impd = round(precio * 0.03) #impd = impuesto de día domingo.
        result = round(precio + impd)
        print(f"El total a pagar por {minutos} minutos es: ${result}")
        print(" El impuesto que se aplicó es de $", impd)
    else:
            if hora == 1:
              impd = round(precio * 0.15)
            else:
                impd = round(precio * 0.10)
                result = round(precio + impd)
                print (f"El total a pagar por {minutos} minutos es: ${result}")
                print (f"El impuesto que se aplicó es de $", impd)