def mostrar_menu():
    print("\n__________Cuenta__________")
    print("1. Registrar Ingreso")
    print("2. Registrar Deducción")
    print("3. Mostrar Balance")
    print("4. Salir")
   
saldo = 0

# Bucle infinito para mantener el programa en ejecución hasta que el usuario decida salir
while True:
    
    mostrar_menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        try:
            # Captura el monto del ingreso como un número decimal
            ingreso = float(input("\nIngrese el monto del ingreso: "))
            
            # Agrega el monto del ingreso al saldo actual
            saldo += ingreso
            
            # Muestra un mensaje de confirmación del registro del ingreso
            print(f"Ingreso registrado: ${ingreso:.2f}\n")

            #se utiliza para bloquear el try por si el value falla
        except ValueError:

            # Manejo de errores en caso de que se ingrese una entrada no válida
            print("Entrada inválida. Introduzca un número válido.")

    elif opcion == "2":
        try:
            # Captura el monto de la deducción como un número decimal
            deduccion = float(input("\nIngrese el monto de la deducción: "))
            
            # Resta el monto de la deducción al saldo actual
            saldo -= deduccion
            
           
            print(f"Deducción registrada: ${deduccion:.2f}\n")  # Muestra un mensaje de confirmación del registro de la deducción
            
        except ValueError:

            # Manejo de errores en caso de que se ingrese una entrada no válida
            print("\nEntrada inválida. Introduzca un número válido.")

    elif opcion == "3":
        # Verifica el saldo actual para determinar si hay ganancias, pérdidas o saldo sin cambios
        if saldo > 0:
            print(f"\nBalance total: ${saldo:.2f} (Ganancias)")
        elif saldo < 0:
            print(f"\nBalance total: ${saldo:.2f} (Pérdidas)")
        else:
            print("\nBalance total: $0.00 (Sin cambios en el saldo)")

    elif opcion == "4":
        print("\nSaliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
