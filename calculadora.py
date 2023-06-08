
def suma(num1,num2):
    return num1 + num2

def resta(num1,num2):
    return num1 - num2

def multiplicacion(num1,num2):
    return num1 * num2

def sobrante(num1,num2):
    return num1 % num2

def division(num1,num2):
    if num2 == 0:
        return "No se puede dividir por cero"
    else:
        return num1 / num2

def calculadora():
        print("Bienvenido a la calculadora básica en Python")
        opcion = True
        while opcion:

            print("""
Seleccione la operación que desea realizar:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Sobrante de una División
6. Salir
            """)    
            opcion = int(input("Ingrese el número de la operación que desea realizar: "))
            if opcion < 7:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))

                if opcion == 1:
                    resultado = suma(num1, num2)
                    print("El resultado de la suma es:", resultado)
                    print("")
                    volver = str(input("volver al menu? s/n: "))
                    if volver == "s":
                        print("volviendo al menu...")
                    else:
                        break    
                elif opcion == 2:              
                    resultado = resta(num1, num2)
                    print("El resultado de la resta es:", resultado)
                    volver = str(input("volver al menu? s/n: "))            
                    if volver == "s":
                        print("volviendo al menu...")
                    else:
                        break                
                elif opcion == 3:           
                    resultado = multiplicacion(num1, num2)
                    print("El resultado de la multiplicación es:", resultado)
                    volver = str(input("volver al menu? s/n: "))            
                    if volver == "s":
                        print("volviendo al menu...")
                    else:
                        break                
                elif opcion == 4:            
                    resultado = division(num1, num2)
                    print("El resultado de la división es:", resultado)
                    volver = str(input("volver al menu? s/n: "))            
                    if volver == "s":
                        print("volviendo al menu...")
                    else:
                        break
                elif opcion == 5:                
                    resultado = sobrante(num1, num2)
                    print("El resultado sobrante de la división es:", resultado)
                    volver = str(input("volver al menu? s/n: "))            
                    if volver == "s":
                        print("volviendo al menu...")
                    else:
                        break
                elif opcion == 6:               
                    break                                     
            else:
                print("")
                print("Porfavor ingrese una opción válida del menú")        
calculadora()