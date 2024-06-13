from src.persona import Persona
import pandas as pd
import os

class Empleado(Persona):
    def __init__(self, nombre, edad, dni, codigo_empleado, salario):
        super().__init__(nombre, edad, dni)
        self.__codigo_empleado = codigo_empleado
        self.__salario = salario

    def get_codigo_empleado(self):
        return self.__codigo_empleado

    def calcular_salario(self):
        return self.__salario
    
    def mostrar_informacion(self):
        return f"""
        Empleado: {self.get_nombre()}
        Edad: {self.get_edad()}
        DNI: {self.get_dni()}
        Codigo: {self.get_codigo_empleado()}
        Salario: {self.calcular_salario()}
        """
    
    def generar_dict_empleado(self):
        return {
            "nombre": self.get_nombre(),
            "edad": self.get_edad(),
            "dni": self.get_dni(),
            "codigo_empleado": self.get_codigo_empleado(),
            "salario": self.calcular_salario()
        }

    @staticmethod
    def leer_csv(path):
        df = pd.read_csv(path)
        lista_empleados = []
        for _, row in df.iterrows():
            lista_empleados.append(Empleado(row['nombre'], row['edad'], row['dni'], row['codigo_empleado'], row['salario']))
        return lista_empleados
    
    def guardar_empleado_csv(self, path):
        try:
            dict_empleado = self.generar_dict_empleado()
            df = pd.DataFrame([dict_empleado])
            if not os.path.exists(path):
                df.to_csv(path, index=False)
            else:
                df.to_csv(path, mode="a", header=False, index=False)
            return True
        except Exception as e:
            print(f"Hubo un error al intentar guardar el empleado: {e}")
            return False

    @staticmethod
    def guardar_empleados(lista_empleados, path):
        if lista_empleados:
            lista_df = [empleado.generar_dict_empleado() for empleado in lista_empleados]
            df = pd.DataFrame(lista_df)
        else:
            df = pd.DataFrame(columns=["nombre", "edad", "dni", "codigo_empleado", "salario"])
        df.to_csv(path, index=False)

    @staticmethod
    def eliminar_empleado(lista_empleados, codigo_empleado, path):
        found = False
        original_length = len(lista_empleados)
        lista_empleados = [emp for emp in lista_empleados if emp.get_codigo_empleado() != codigo_empleado]
        if len(lista_empleados) < original_length:
            found = True
        Empleado.guardar_empleados(lista_empleados, path)
        return found