import time
flag = True

total_integral = 0
total_baguette = 0
total_molde = 0
total_amasado = 0

cant_integral = 0
cant_baguette = 0
cant_molde = 0
cant_amasado = 0


while flag == True:
    print("""
Bienvenido a la panaderia, seleccione el tipo de pan que llevará:
1.- Amasado : 1500
2.- Molde : 1000
3.- Baguette : 2000
4.- Integral : 3000
5.- Total
6.- Salir
    """)
    opc = int(input("ingrese una opción porfavor"))    


    if opc == 1:
        cant_amasado = int(input("ingrese la cantidad de pan que llevará ó vuelva al menu con 0: "))
        if cant_amasado > 0:
            total_amasado = 1500 * cant_amasado
            print(f"entendido, la cantidad ingresada es {cant_amasado}, dando un total de {total_amasado}, se le redireccionará al menú.")
            time.sleep(1)
            print("volviendo al menu...")
            time.sleep(1)
        elif cant_amasado == 0:
            cant_amasado = 0
            print("volviendo al menu...")
            time.sleep(1)
        else:
            print("porfavor ingrese una cantidad de pan o vuelva al menú con el numero 0: ")

    elif opc == 2:
        cant_molde = int(input("ingrese la cantidad de pan que llevará ó vuelva al menu con 0: "))
        if cant_molde > 0:
            total_molde = 1000 * cant_molde
            print(f"entendido, la cantidad ingresada es {cant_molde}, dando un total de {total_molde}, se le redireccionará al menú")
            time.sleep(1)
            print ("volviendo al menu...")
            time.sleep(1)
        elif cant_molde == 0:
            print("volviendo al menu...")
            time.sleep(1)
        else:
            print("porfavor ingrese una cantidad de pan o vuelva al menú con el numero 0")

    elif opc == 3:
        cant_baguette = int(input("ingrese la cantidad de pan que llevará ó vuelva al menu con 0"))
        if cant_baguette > 0:
            total_baguette = 2000 * cant_baguette
            print(f"entendido, la cantidad ingresada es {cant_baguette}, dando un total de {total_baguette}, se le redireccionará al menú")
            time.sleep(1)
            print ("volviendo al menu...")
            time.sleep(1)
        elif cant_amasado == 0:
            print("volviendo al menu...")
            time.sleep(1)
        else:
            print("porfavor ingrese una cantidad de pan o vuelva al menú con el numero 0")

    elif opc == 4:
        cant_integral = int(input("ingrese la cantidad de pan que llevará ó vuelva al menu con 0"))
        if cant_integral > 0:
            total_integral = 3000 * cant_integral
            print(f"entendido, la cantidad ingresada es {cant_integral}, dando un total de {total_integral}, se le redireccionará al menú")
            time.sleep(1)
            print ("volviendo al menu...")
            time.sleep(1)
        elif cant_integral == 0:
            cant_integral = 0
            print("volviendo al menu...")
            time.sleep(1)
        else:
            print("porfavor ingrese una cantidad de pan o vuelva al menú con el numero 0")

    elif opc == 5:
        total_venta = total_amasado + total_molde + total_baguette + total_integral
        print(f"""
Total de la venta:
Cantidad de panes amasados = {cant_amasado} total = {total_amasado}
Cantidad de panes amasados = {cant_molde} total = {total_molde}
Cantidad de panes amasados = {cant_baguette} total = {total_baguette}
Cantidad de panes amasados = {cant_integral} total = {total_integral}
Total venta = {total_venta}
        """)
        deliv = input("delivery? = s/n")
        if deliv == "s":
            if total_venta > 5000:
                print("ya que su compra fue mayor a 5000, el envio es gratis!")
                time.sleep(1)
                print("imprimiendo comprobante...")
            else:
                print(f"el total a pagar con delivery incluido es: {total_venta * 0.10}")
        else:
            print(f"su total a pagar es: {total_venta}")
            time.sleep(1)
            print("imprimiendo comprobante...")
            break

    elif opc == 6:
            print("Tenga un buen dia")

    elif opc > 6:
            print("numero equivocado, reintente")