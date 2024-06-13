# Document Design para la Aplicación de Gestión de Empleados

## Objetivo

Desarrollar una aplicación en Python para gestionar información sobre empleados de una empresa utilizando la biblioteca Pandas y aplicando el concepto de herencia.

## Requisitos

### Clases

1. **Clase Base: Persona**
    - **Atributos:**
        - `nombre`: Nombre del empleado.
        - `edad`: Edad del empleado.
        - `dni`: Documento Nacional de Identidad del empleado.
    - **Métodos:**
        - `mostrar_informacion()`: Muestra la información básica de la persona.

2. **Clase Derivada: Empleado**
    - Hereda de `Persona`.
    - **Atributos:**
        - `codigo_empleado`: Código único del empleado.
        - `salario`: Salario mensual del empleado.
    - **Métodos:**
        - `calcular_salario()`: Calcula y retorna el salario del empleado.
        - `mostrar_informacion()`: Muestra la información del empleado incluyendo los atributos heredados de `Persona`.

3. **Clase Derivada: EmpleadoPorHoras**
    - Hereda de `Persona`.
    - **Atributos:**
        - `horas_trabajadas`: Número de horas trabajadas.
        - `tarifa_por_hora`: Tarifa por hora del empleado.
    - **Métodos:**
        - `calcular_salario()`: Calcula y retorna el salario basado en horas trabajadas y tarifa por hora.
        - `mostrar_informacion()`: Muestra la información del empleado incluyendo los atributos heredados de `Persona`.

### Persistencia de Datos

- Utilizar archivos CSV para almacenar la información de los empleados.
- Usar Pandas para manejar los DataFrames que representan la información de los empleados.

### Interfaz de Usuario

- Crear una interfaz de línea de comandos para interactuar con los empleados.
- Funcionalidades:
    - Añadir empleados.
    - Eliminar empleados.
    - Consultar información de los empleados.

### Pruebas

- Proporcionar un script de prueba que demuestre el uso de las clases `Empleado` y `EmpleadoPorHoras` y sus métodos.
- Funcionalidades del script de prueba:
    - Crear instancias de varios empleados.
    - Calcular el salario de cada empleado.
    - Mostrar la información de cada empleado.

## Estructura del Proyecto

```
gestion_empleados/
│
├── data/
│   ├── empleados.csv
│   ├── empleados_por_horas.csv
│
├── src/
│   ├── __init__.py
│   ├── persona.py
│   ├── empleado.py
│   ├── empleado_por_horas.py
│   ├── main.py
│
├── tests/
│   ├── test_script.py
│
├── README.md
└── requirements.txt
```

## Detalles de Implementación

### 1. Clase Base: Persona

- Atributos: `nombre`, `edad`, `dni`
- Método: `mostrar_informacion()`

### 2. Clase Derivada: Empleado

- Hereda de `Persona`
- Atributos: `codigo_empleado`, `salario`
- Métodos: `calcular_salario()`, `mostrar_informacion()`

### 3. Clase Derivada: EmpleadoPorHoras

- Hereda de `Persona`
- Atributos: `horas_trabajadas`, `tarifa_por_hora`
- Métodos: `calcular_salario()`, `mostrar_informacion()`

### 4. Interfaz de Usuario

- Funcionalidades:
    - Cargar empleados desde un archivo CSV.
    - Guardar empleados en un archivo CSV.
    - Añadir empleados.
    - Eliminar empleados.
    - Mostrar información de empleados.
    - Menú interactivo en la línea de comandos.

### 5. Pruebas

- Script de prueba que crea instancias de empleados y empleados por horas, calcula sus salarios y muestra su información.
- Asegurar que el script maneje correctamente la creación, actualización y eliminación de empleados en los archivos CSV.

## Requisitos Adicionales

### Archivos CSV

- **empleados.csv**
  ```csv
  nombre,edad,dni,codigo_empleado,salario
  ```

- **empleados_por_horas.csv**
  ```csv
  nombre,edad,dni,horas_trabajadas,tarifa_por_hora
  ```

### README.md

Incluir detalles sobre la instalación, uso y estructura del proyecto.

```
# Gestión de Empleados

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python src/main.py
```

## Estructura del Proyecto

```
gestion_empleados/
│
├── data/
│   ├── empleados.csv
│   ├── empleados_por_horas.csv
│
├── src/
│   ├── __init__.py
│   ├── persona.py
│   ├── empleado.py
│   ├── empleado_por_horas.py
│   ├── main.py
│
├── tests/
│   ├── test_script.py
│
├── README.md
└── requirements.txt
```