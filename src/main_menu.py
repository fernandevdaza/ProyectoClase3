from src.add_empleado import add_empleado
from src.remove_empleado import remove_empleado
from src.show_all_empleados import show_all_empleados
def main_menu():

    while True:
        try:
            print("=====================")
            print("Gestión de Empleados")
            print("=====================")
            print("\n")   
            print("1. Agregar empleado")
            print("2. Eliminar empleado")
            print("3. Mostrar empleados")
            print("4. Salir")
            option = int(input("Ingresa una opción: "))
            if option == 1:
                add_empleado()
            elif option == 2:
                remove_empleado()
            elif option == 3:
                show_all_empleados()
            elif option == 4:
                exit()
            else:
                print("Main Ingrese una opción válida")
        except ValueError:
            print("Error, por favor escriba un número")