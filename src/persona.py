class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    def get_nombre(self):
        return self._nombre
    def get_edad(self):
        return self._edad
    def get_dni(self):
        return self._dni
    
