import sys
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_consola()

empleados = []
nominas = []

calcular_salario_neto = lambda salario, salario_minimo: salario + 140000 if salario < 2 * salario_minimo else salario

def agregar_empleado(id_empleado, nombre, apellido, cargo, area, salario):
    empleado = {
        "id": id_empleado,
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "area": area,
        "salario": salario
    }
    empleados.append(empleado)

def listar_empleados():
    for empleado in empleados:
        print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']} {empleado['apellido']}, Cargo: {empleado['cargo']}")

# calcular los salarios netos y almacenar en la lista de nóminas
def calcular_salarios_netos():
    salario_minimo = 1160000
    for empleado in empleados:
        salario_neto = calcular_salario_neto(empleado['salario'], salario_minimo)
        empleado['salario_neto'] = salario_neto
        nominas.append((empleado, salario_neto))

def imprimir_nominas():
    for empleado, salario_neto in nominas:
        print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']} {empleado['apellido']}, Cargo: {empleado['cargo']}, Salario Neto: {salario_neto}")

def buscar_empleado_por_id(id_buscado):
    for empleado in empleados:
        if empleado['id'] == id_buscado:
            print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']} {empleado['apellido']}, Cargo: {empleado['cargo']}, Salario Neto: {empleado['salario_neto']}")
            return
    print("Empleado no encontrado")

def registrar_empleado():
    id_empleado = int(input("Ingrese el ID del empleado: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cargo = input("Ingrese el cargo: ")
    area = input("Ingrese el área: ")
    salario = float(input("Ingrese el salario: "))
    limpiar_consola()
    agregar_empleado(id_empleado, nombre, apellido, cargo, area, salario)
    print(f"Empleado {nombre} {apellido} fue registrado con éxito!")

def menu_listar_empleados():
    print("\nEmpleados:")
    listar_empleados()

def menu_calcular_salarios():
    calcular_salarios_netos()
    print("\nSalarios netos calculados.")

def menu_imprimir_nominas():
    print("\nNóminas:")
    imprimir_nominas()

def menu_buscar_empleado():
    id_buscado = int(input("Ingrese el ID del empleado que desea buscar: "))
    buscar_empleado_por_id(id_buscado)

def rol_analista():
    while True:
        print("\n  ⬇️   Menú ⬇️ \n ")
        print("-> 1. Registrar empleado <-")
        print("-> 2. Listado empleados  <-")
        print("-> 3. Calcular salarios netos <-")
        print("-> 4. Imprimir nóminas   <-")
        print("-> 5. Buscar empleado por ID  <-")
        print("-> 6. Cerrar sesión   <-")

        opcion = input("Seleccione una opción: ")
        limpiar_consola()

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            menu_listar_empleados()
        elif opcion == "3":
            menu_calcular_salarios()
        elif opcion == "4":
            menu_imprimir_nominas()
        elif opcion == "5":
            menu_buscar_empleado()
        elif opcion == "6":
            inicio_sesion()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def rol_empleado():
    while True:
        print("\n MENÚ ")
        print("1. Buscar nómina con tu ID")
        print("2. Cerrar sesión")

        opcion = input("Seleccione una opción: ")
        limpiar_consola()

        if opcion == "1":
            calcular_salarios_netos()
            id_buscado = int(input("Ingrese el ID del empleado a buscar: "))
            buscar_empleado_por_id(id_buscado)
        elif opcion == "2":
            inicio_sesion()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            inicio_sesion()

def inicio_sesion():
    print("\n" + "      ¡BIENVENIDO!" )
    print("\n" + "           AL     ")
    print("\n" + "    INICIO DE SESION")
    print("_________________________")
    print("                                    ")
    print("-> 1. Iniciar sesión como analista <- ")
    print("-> 2. Iniciar sesión como empleado <-")
    print("-> 3. Salir    <-")
    print("                                    ")

    modo = input("Ingrese la sesion deseada: ")

    if modo == "1":
        usuario_analista = "analista"
        contraseña_analista = "707"

        usuario_a = input("Nombre de usuario: ")
        contraseña_a = input("Contraseña: ")
        limpiar_consola()

        if usuario_a == usuario_analista and contraseña_a == contraseña_analista:
            print("\nInicio de sesión exitoso.\n")
            rol_analista()
        else:
            print("\nNombre de usuario o contraseña incorrectos.\n")
            inicio_sesion()

    elif modo == "2":
        usuario_empleado = "empleado"
        contraseña_empleado = "202"

        usuario_e = input("Nombre de usuario: ")
        contraseña_e = input("Contraseña: ")
        limpiar_consola()

        if usuario_e == usuario_empleado and contraseña_e == contraseña_empleado:
            print("\nInicio de sesión exitoso.\n")
            rol_empleado()
        else:
            print("\nNombre de usuario o contraseña incorrectos.\n")
            inicio_sesion()
    else:
        print("\nSaliendo del programa... Hasta Luego!\n")
        sys.exit()

inicio_sesion()