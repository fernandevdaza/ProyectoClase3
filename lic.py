import pandas as pd
import os

class Persona:
    def _init_(self, nombre, edad, dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
        self._pd=pd
        self._listaPersonas =[]
       

class Empleado(Persona):
    def _init_(self, nombre, edad, dni, codigo_empleado, salario):
        super()._init_(nombre, edad, dni)
        self.__codigo_empleado = codigo_empleado
        self.__salario = salario
        self.__archivo="empleado.csv"
    
    def calcular_salario(self):
        return self.__salario

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre}, Edad: {self._edad}, DNI: {self._dni}, Código: {self.codigo_empleado}, Salario: {self._salario}"
    
    def guardar_empleado(self,nombre,edad,dni,codigo_empleado,salario):
        self._nombre=nombre
        self._edad=edad
        self._dni=dni
        self.__codigo_empleado=codigo_empleado
        self.__salario=salario
        data = {
            'nombre': self._nombre,
            'edad': self._edad,
            'dni': self._dni,
            'codigo_empleado': self.__codigo_empleado,
            'salario': self.__salario
        }
        if not os.path.exists(self.__archivo):
            with open(self.__archivo, 'w') as f:
                f.write('nombre,edad,dni,codigo_empleado,salario\n')  # Escribir el encabezado
        df = self._pd.DataFrame([data])
        df.to_csv(self._archivo, index=False, mode='a', header=not os.path.exists(self._archivo))

   
    def cargar_empleados(self):
        df = self.pd.read_csv(self._archivo)
        empleados = []
        for index, row in df.iterrows():
            empleados.append(Empleado(row['nombre'], row['edad'], row['dni'], row['codigo_empleado'], row['salario']))
        self._listaPersonas=empleados
        return empleados

class EmpleadoPorHoras(Persona):
    def _init_(self, nombre, edad, dni, horas_trabajadas, tarifa_por_hora):
        super()._init_(nombre, edad, dni)
        self.__horas_trabajadas = horas_trabajadas
        self.__tarifa_por_hora = tarifa_por_hora
        self.__archivo="empleadosporhora.csv"

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def mostrar_informacion(self):
        return f"Empleado por Horas: {self.nombre}, Edad: {self._edad}, DNI: {self._dni}, Horas Trabajadas: {self.horas_trabajadas}, Tarifa por Hora: {self._tarifa_por_hora}"

   
    def guardar_empleado(self,nombre,edad,dni,horas_trabajadas,tarifa_por_hora):  # Cambiado a método de clase
       
        self._nombre=nombre
        self._edad=edad
        self._dni=dni
        self.__horas_trabajadas = horas_trabajadas
        self.__tarifa_por_hora = tarifa_por_hora
        data = {
            'nombre': self._nombre,
            'edad': self._edad,
            'dni': self._dni,
            'horas_trabajadas': self.__horas_trabajadas,
            'tarifa_por_hora': self.__tarifa_por_hora
        }
        if not os.path.exists(self.__archivo):
            with open(self.__archivo, 'w') as f:
                f.write('nombre,edad,dni,horas_trabajadas,tarifa_por_hora\n')  # Escribir el encabezado
        df = self._pd.DataFrame([data])
        df.to_csv(self._archivo, index=False, mode='a', header=not os.path.exists(self._archivo))
    
   
    def cargar_empleado(self):
       #Esta funcion es para mostrar el ultimo empleado cargado.
        df = self.pd.read_csv(self._archivo)
        empleado_data = df.iloc[-1]  # Tomamos el último empleado agregado
        return EmpleadoPorHoras(empleado_data['nombre'], empleado_data['edad'], empleado_data['dni'], empleado_data['horas_trabajadas'], empleado_data['tarifa_por_hora'])
    
    def cargar_empleados(self):
        #Esta funcion es para todos los empleados por hora.
            df = self.pd.read_csv(self._archivo)
            empleados = []
            for index, row in df.iterrows():
                empleados.append(Empleado(row['nombre'], row['edad'], row['dni'], row['horas_trabajadas'], row['tarifa_por_hora']))
            self._listaPersonas=empleados
            return empleados

# Crear instancias de empleados
empleado1 = Empleado("", 0, 0, "", 0.0)
empleado2 = EmpleadoPorHoras("",0,0,0,0.0)

# Guardar empleados en el archivo CSV
empleado1.guardar_empleado("Ale", 0, 1097534, "44xd", 1000.0)

lista=[]
lista=empleado1.cargar_empleados()
#mostrar todos los empleados
for list in lista:
    print(list.mostrar_informacion())

empleado2.guardar_empleado("Pedro",22,"15151515",150,150)
#print(empleado2.mostrar_informacion())
#mostrar el ultimo empleado
print(empleado2.cargar_empleado().mostrar_informacion())
#mostrar todos los empleados
lista2=empleado2.cargar_empleados()
for list2 in lista2:
    print(list2.mostrar_informacion())