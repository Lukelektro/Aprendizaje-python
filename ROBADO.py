#!/usr/bin/env python
# coding: utf-8

# In[ ]:


numero_clientes = int(input())
monto_final = 0
porcentaje_ventas_stgo = 0
porcentaje_ventas_norte = 0
porcentaje_ventas_sur = 0
monto_total_recaudado = 0
contador_debito = 0
contador_credito = 0
suma_debito = 0
suma_credito = 0
i = 0

while numero_clientes > 0:
    rut = str(input())
    monto_de_compra = float(input())
    forma_de_pago = int(input())
    zona_de_envio = int(input())
    descuento = int()
    i += 1
    print(f'Rut Cliente : {rut}')
    print(f'Monto Compra : {monto_de_compra}')
    
    if forma_de_pago == 1:
        print(f'Forma de Pago : TARJETA DÉBITO')
        contador_debito += 1
    elif forma_de_pago == 2:
        print(f'Forma de Pago : TARJETA CRÉDITO')
        contador_credito += 1
    
    if zona_de_envio == 1:
        print(f'Zona Destino : SANTIAGO')
        costo_de_envio = 3000
        porcentaje_ventas_stgo += 1
    elif zona_de_envio == 2:
        print(f'Zona Destino : NORTE')
        costo_de_envio = 6000
        porcentaje_ventas_norte += 1
    elif zona_de_envio == 3:
        print(f'Zona Destino : SUR')
        costo_de_envio = 8000
        porcentaje_ventas_sur += 1
    
    if forma_de_pago == 1:
        if monto_de_compra <= 50000:
            total_con_descuento = monto_de_compra
        if monto_de_compra > 50000 and monto_de_compra <= 100000:
            descuento = 10
            total_con_descuento = monto_de_compra * 0.9
        elif monto_de_compra > 100000 and monto_de_compra <= 500000:
            descuento = 20
            total_con_descuento = monto_de_compra * 0.8
        elif monto_de_compra > 500000 :
            descuento = 40
            total_con_descuento = monto_de_compra * 0.6
        suma_debito += total_con_descuento
    elif forma_de_pago == 2:
        if monto_de_compra <= 50000:
            total_con_descuento = monto_de_compra
        elif monto_de_compra > 50000 and monto_de_compra <= 100000:
            descuento = 5
            total_con_descuento = monto_de_compra * 0.95
        elif monto_de_compra > 100000 and monto_de_compra <= 500000:
            descuento = 10
            total_con_descuento = monto_de_compra * 0.9
        elif monto_de_compra > 500000 :
            descuento = 25
            total_con_descuento = monto_de_compra * 0.75
        suma_credito += total_con_descuento
            
    if total_con_descuento > 100000 and zona_de_envio == 1:
        costo_de_envio = 0
    elif total_con_descuento > 200000 and zona_de_envio == 2:
        costo_de_envio = 0
    elif total_con_descuento > 300000 and zona_de_envio == 3:
        costo_de_envio = 0
        
    monto_final = costo_de_envio + total_con_descuento
    monto_total_recaudado += monto_final         
    
    if descuento > 0:
        print(f'Porcentaje de descuento a aplicar = {descuento}%')
    else:
        print('No Tiene Descuento.')
    
    print(f'Monto total de la compra = {round(total_con_descuento)}')
    print(f'Costo Envío = {costo_de_envio}')
    print(f'Monto final a pagar por compra y envío = ${round(monto_final)}')
    
    print('')
    if i == numero_clientes:
        break
    
porcentaje_ventas_stgo = porcentaje_ventas_stgo * 100 / numero_clientes
porcentaje_ventas_norte = porcentaje_ventas_norte * 100 / numero_clientes
porcentaje_ventas_sur = porcentaje_ventas_sur * 100 / numero_clientes

print('')
print('REPORTE FINAL')
print('')
print(f'Monto total recaudado por concepto de ventas = ${round(monto_total_recaudado)}')
print(f'Porcentaje de ventas enviadas a Santiago = {round(porcentaje_ventas_stgo,1)}%')
print(f'Porcentaje de ventas enviadas a Zona Norte = {round(porcentaje_ventas_norte,1)}%')
print(f'Porcentaje de ventas enviadas a Zona Sur = {round(porcentaje_ventas_sur,1)}%')
print(f'Total de clientes que pagaron con tarjeta de débito = {contador_debito}')
print(f'Total de clientes que pagaron con tarjeta de crédito = {contador_credito}')
if contador_debito > 0:
    promedio_debito = suma_debito / (contador_debito)
    print(f'Promedio de ventas con tarjeta de débito = {round(promedio_debito)}')
else:
    print('No se procesaron compras con tarjeta de débito')
if contador_credito > 0:
    promedio_credito = suma_credito / (contador_credito)
    print(f'Promedio de ventas con tarjeta de crédito = {round(promedio_credito)}')
else:
    print('No se procesaron compras con tarjeta de crédito')

