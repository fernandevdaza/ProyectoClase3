from src.empleado_por_horas import EmpleadoPorHoras
from src.empleado import Empleado

PATH_EMPLEADO_CSV = "./data/Empleados.csv"
PATH_EMPLEADO_POR_HORA_CSV = "./data/EmpleadosPorHora.csv"

def show_all_empleados():
    while True:
        try:
            print("\n")
            print("1. Empleados Fijos")
            print("2. Empleados por Horas")
            print("3. Regresar")
            option = int(input("Seleccione una opción: "))
            if option != 1 and option != 2 and option != 3:
                print("Selecciona una opción válida")
                continue
            if option == 1:
                empleados = Empleado.leer_csv(PATH_EMPLEADO_CSV)
                if empleados:
                    for empleado in empleados:
                        print(empleado.mostrar_informacion())
                else:
                    print("No hay empleados fijos registrados")
            elif option == 2:
                empleados = EmpleadoPorHoras.leer_csv(PATH_EMPLEADO_POR_HORA_CSV)
                if empleados:
                    for empleado in empleados:
                        print(empleado.mostrar_informacion())
                else:
                    print("No hay empleados por horas registrados")
            elif option == 3:
                return
            return
        except ValueError:
            print("Error, por favor escriba un número")
            continue