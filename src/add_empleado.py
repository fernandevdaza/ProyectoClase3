from src.empleado import Empleado
from src.empleado_por_horas import EmpleadoPorHoras

PATH_EMPLEADO_CSV = "./data/Empleados.csv"
PATH_EMPLEADO_POR_HORA_CSV = "./data/EmpleadosPorHora.csv"

def add_empleado():
    while True:
        try:
            print("\n")
            print("¿Qué tipo de empleado quieres crear?")
            print("1. Fijo")
            print("2. Por hora")
            print("3. Regresar")
            option = int(input("Seleccione una opción: "))
            if option != 1 and option != 2 and option != 3:
                print("Selecciona una opción válida")
                continue
            print("\n")
            nombre = input("Ingrese el nombre del empleado: ")
            edad = int(input("Ingresa la edad del empleado: "))
            dni = int(input("Ingresa el dni del empleado: "))
            if option == 1:
                codigo_empleado = int(input("Ingresa el código del empleado: "))
                salario = int(input("Ingresa el salario del empleado: "))
                nuevo_empleado = Empleado(nombre, edad, dni, codigo_empleado, salario)
                nuevo_empleado.guardar_empleado_csv(PATH_EMPLEADO_CSV)
            elif option == 2:
                horas_trabajadas = int(input("Ingresa las horas trabajadas: "))
                tarifa_por_hora = int(input("Ingresa la tarifa por hora: "))
                nuevo_empleado_por_hora = EmpleadoPorHoras(nombre, edad, dni, horas_trabajadas, tarifa_por_hora)
                nuevo_empleado_por_hora.guardar_empleado_csv(PATH_EMPLEADO_POR_HORA_CSV)
            elif option == 3:
                return
            return
        except ValueError:
            print("Error, por favor escriba un número")
            continue  