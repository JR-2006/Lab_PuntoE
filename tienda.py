print("Bienvenidos a nuestra tienda online \nDonde encontrara oportunudades para descuentos")
print()
print("Los clientes pueden obtener un descuento de 20% si su compra es mayor a $100.")
print("Si el cliente es un miembro VIP, siempre obtiene un descuento adicional de 10%, sin importar el monto de la compra.")
print("Si el cliente tiene un código de descuento especial, se le aplica un descuento extra de 5% adicional sobre el total.")
print()

compra = float(input("Digite el valor a pagar de su compra: "))

descuentoC = 0
descuento = 0
descuentoVIP = 0

#Descuento para usuario VIP
usuario = input("Usted es usuario VIP? Si/NO ")
if usuario == "Si":
    contraseña = input("Digite la contraseña si es un usuario VIP (SOLO TIENE UN INTENTO): ")
    if contraseña == "ElChuloRomeroCuervo":
        print("Contraseña correcta")
        descuentoVIP = 10
    else:
        print("Comtraseña invalida")

#Descuento superior a 100$ 
if compra > 100:
    descuento = 20 

#Codigo de descuentos del 5%
codigoD = input("Usted tiene un codigo de descuento? Si/NO  ")
if codigoD == "Si":
    digitCodigo = int(input("Por favor, digite su codigo (5 caracteres): "))
    descuentoC = 0

    if digitCodigo == 21554:
        descuentoC = 5
        print("Codigo aceptado")
    elif digitCodigo == 45487:
        descuentoC = 5
        print("Codigo aceptado")
    elif digitCodigo == 89522:
        descuentoC = 5
        print("Codigo aceptado")
    elif digitCodigo == 48987:
        descuentoC = 5
        print("Codigo aceptado")
    elif digitCodigo == 32165:
        descuentoC = 5
        print("Codigo aceptado")
    elif digitCodigo == 94891:
        descuentoC = 5
        print("Codigo aceptado")
    else:
        print("CODIGO NO VALIDO")

#Descuentos totales
descuentos = descuentoVIP + descuentoC + descuento
if descuentos > 1:
    descuentosPorcentaje = 0
    descuentosPorcentaje = (100 - descuentos)/100
    descuentoCompra = compra*descuentosPorcentaje

#Resultados
print()
print(f"valor de la compra: {compra}")
print(f"Recibe un descuento del {descuentos}%")
if descuentos == 0:
    print(f"El valor a pagar de su compra es: {compra}")
else:
    print(f"El valor a pagar de su compra es: {descuentoCompra}")