saldo = 2000
print("1. Ingreso de dinero.")
print("2. Retirar dinero.")
print("3. Mostrar dinero.")
print("4. Salir.")

opcion = int(input("Ingrese la opcion: "))

if opcion == 1:
    ingreso = int(input("Ingrese la cantidad a ingresar: "))
    saldo = saldo + ingreso
    print(f"Su saldo es {saldo}")
elif opcion == 2:
    retiro = int(input("Ingrese la cantidad a retirar: "))

    if retiro > saldo:
        print("No puede retirar")
        
    else:
        saldo = saldo - retiro
        print(f"Su saldo es {saldo}")
  

elif opcion == 3:
    print(f"Su saldo es {saldo}")
elif opcion == 4:
    print("Adiós.")

