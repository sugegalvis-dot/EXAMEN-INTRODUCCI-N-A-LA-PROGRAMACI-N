
saldo = 1000

def mostrarmenu():
    print ("==== CAJERO AUTOMÁTICO====")
    print ("====MOSTRAR MENU====")
    print ("a. Consultar Saldo")
    print ("b. Depositar dinero")
    print ("c. Retirar dinero")
    print ("0. Salir")


def consutar_saldo():
    print ("Su saldo actual es: ", "$", saldo)

def depositar():
    global saldo
    monto = float(input("Ingrese monto a depositar: $",))
    if  monto <= 0:
        print ("Deposito rechazado. El deposito debe ser mayor o que 0")
    else:
        saldo = saldo + monto
        print ("Deposito aceptado. Su saldo actual es: ", saldo)


def retirar():
    global saldo
    monto = float(input("Ingrese monto a retirar: "))
    if monto <= 0:
        print ("Error. Retiro rechazado. El retiro debe ser mayor que 0")
    elif monto > saldo:
        print ("Saldo Insuficiente. Ingrese otro valor")
    else: 
        saldo = (saldo - monto)
        print ("Retiro exitoso.")
        print ("Saldo disponible: ", saldo)




opcion = -1


while opcion != 0:
    mostrarmenu()
    opcion = str(input("Elija una opción: "))
    if opcion == "a":
        consutar_saldo()
    elif opcion == "b": 
        depositar()
    elif opcion == "c":
        retirar()
    elif opcion == "0":
        print ("Sesión finalizada, Gracias por usar el cajero.")
    else:
        print ("Opción inválida. Marque otra opción")    


