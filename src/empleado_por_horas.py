from src.persona import Persona
import pandas as pd
import os
class EmpleadoPorHoras(Persona):
    def __init__(self, nombre, edad, dni, horas_trabajadas, tarifa_por_hora):
        Persona.__init__(self, nombre, edad, dni)
        self.__horas_trabajadas = horas_trabajadas
        self.__tarifa_por_hora = tarifa_por_hora
    
    def get_horas_trabajadas(self):
        return self.__horas_trabajadas
    
    def get_tarifa_por_hora(self):
        return self.__tarifa_por_hora

    def calcular_salario(self):
        return self.__horas_trabajadas * self.__tarifa_por_hora
    
    def mostrar_informacion(self):
        return f"""
        Empleado: {self.get_nombre()}
        Edad: {self.get_edad()}
        DNI: {self.get_dni()}
        Horas Trabajadas: {self.get_horas_trabajadas()}
        Tarifa Por Hora: {self.get_tarifa_por_hora()}
        """
    
    def generar_dict_empleado(self):
        return {
            "nombre": self.get_nombre(),
            "edad": self.get_edad(),
            "dni": self.get_dni(),
            "horas_trabajadas": self.get_horas_trabajadas(),
            "tarifa_por_hora": self.get_tarifa_por_hora()
        }

    @staticmethod
    def leer_csv(path):
        df = pd.read_csv(path, header=0)
        lista_empleados = []
        for index, row in df.iterrows():
            lista_empleados.append(EmpleadoPorHoras(row['nombre'], row['edad'], row['dni'], row['horas_trabajadas'], row['tarifa_por_hora']))
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
    def eliminar_empleado(lista_empleados, dni, path):
        found = False
        original_length = len(lista_empleados)
        lista_empleados = [emp for emp in lista_empleados if emp.get_dni() != dni]
        if len(lista_empleados) < original_length:
            found = True
        EmpleadoPorHoras.guardar_empleados(lista_empleados, path)
        return found