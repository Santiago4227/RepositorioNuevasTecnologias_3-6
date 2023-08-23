import random
import os

# Definir una lista para almacenar usuarios registrados
usuarios = []

# Definir la función mostrar_menu()
def mostrar_menu():
    """
    Esta función muestra el menú principal en la consola.
    """
    print("\n ----- MENÚ ----- ")
    print("|  1. Juego      |")
    print("|  2. Tarjeta    |")
    print("|  3. Salir      |")
    print(" ----- ---- ----- " + "\n")

# Definir la función registrar_usuario()
def registrar_usuario():
    """
    Esta función permite al usuario registrar un nuevo nombre de usuario y contraseña.
    Los datos del usuario se almacenan en la lista usuarios.
    """
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    usuarios.append({"nombre": nombre, "contrasena": contrasena})
    print("Registro exitoso. Puede iniciar sesión ahora.")

# Definir la función iniciar_sesion()
def iniciar_sesion():
    """
    Esta función permite al usuario iniciar sesión y verifica si las credenciales son correctas.
    """
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    for usuario in usuarios:
        if usuario["nombre"] == nombre and usuario["contrasena"] == contrasena:
            print(f"\n ¡BIENVENIDO!, {nombre}!")
            return True
    print("Nombre de usuario o contraseña incorrectos.")
    return False

opcion = 0
usuario_autenticado = False
cupo_total = 100000 # Definir el cupo total disponible

# Inicia un bucle principal que muestra el menú principal y gestiona las opciones
while opcion != 3:
    # Si el usuario no está autenticado, muestra el menú de inicio de sesión/registro
    if not usuario_autenticado:
        print("\n ------- ¡BIENVENIDO! ------- ")
        print("\n ----- INICIO DE SESIÓN ----- ")
        print("|  1. Registrarse           |")
        print("|  2. Iniciar sesión        |")
        print("|  3. Salir                 |")
        print(" ----- ---- ----- ----- ----" + "\n")

        seleccion = int(input("Seleccione una opción: "))

        if seleccion == 1:
            registrar_usuario()
        elif seleccion == 2:
            usuario_autenticado = iniciar_sesion()
        elif seleccion == 3:
            print("Hasta luego...| Cerrando programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    else:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("\n - Juego de Puntaje y Vidas")

            vidas = 5
            puntos = 0

            while vidas != 0:
                num = random.randint(0, 9)

                if num == 0:
                    vidas -= 1
                    print(f"Te quedan {vidas} vidas")
                else:
                    puntos += 1
                    print(f"Has ganado {puntos} puntos")

        elif opcion == 2:
            # Limpiar la consola antes de mostrar la tarjeta de crédito (compatible con varios sistemas)
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n - Tarjeta de crédito")
            print (f"\n Cupo disponible: ${cupo_total:.2f}")  # Mostrar el cupo disponible al inicio

            nombre = input("\n Ingrese su nombre: ")
            compra = int(input("\n Ingrese el valor de la compra: "))
            cuotas = int(input("\n Ingrese número de cuotas: "))

            if compra <= cupo_total:
                deuda = compra
                separacion = compra / cuotas
                total_pagos = 0
                print(f"\n Detalle de pagos de {nombre}")
                i = 1

                while deuda > 1 and i <= cuotas:
                    if deuda - separacion < 0:
                        cuota_actual = deuda
                        total_pagos += cuota_actual
                        deuda -= cuota_actual
                    else:
                        cuota_actual = separacion
                        total_pagos += cuota_actual
                        deuda -= cuota_actual

                    print(f"\n Cuota {i}: ${cuota_actual:.2f} - Deuda restante: ${deuda:.2f} - Total de pagos: ${total_pagos:.2f} \n")

                    i += 1 
              
                else:
                  print("\n No se puede hacer la compra")
        elif opcion == 3:
            print("Hasta luego.... ;D")
