from src.empleado import Empleado
from src.empleado_por_horas import EmpleadoPorHoras

PATH_EMPLEADO_CSV = "./data/Empleados.csv"
PATH_EMPLEADO_POR_HORA_CSV = "./data/EmpleadosPorHora.csv"

def remove_empleado():
    while True:
        try:
            isRemoved = False
            print("\n")
            print("¿Qué tipo de empleado quieres borrar?")
            print("1. Fijo")
            print("2. Por hora")
            option = int(input("Seleccione una opción: "))
            if option != 1 and option != 2:
                print("Selecciona una opción válida: ")
                continue
            print("\n")
            if option == 1:
                codigo_empleado = int(input("Ingresa el código del empleado: "))
                isRemoved = Empleado.eliminar_empleado(Empleado.leer_csv(PATH_EMPLEADO_CSV), codigo_empleado, PATH_EMPLEADO_CSV)
            else:
                dni = int(input("Ingresa el DNI del empleado: "))
                isRemoved = EmpleadoPorHoras.eliminar_empleado(EmpleadoPorHoras.leer_csv(PATH_EMPLEADO_POR_HORA_CSV), dni, PATH_EMPLEADO_POR_HORA_CSV)
            if isRemoved:
                print("Empleado eliminado exitosamente")
            else:
                print("Hubo un error al eliminar al empleado")
            return
        except ValueError:
            print("Error, por favor escriba un número")
        except Exception as e:
            print(f"Hubo un error: {e}")