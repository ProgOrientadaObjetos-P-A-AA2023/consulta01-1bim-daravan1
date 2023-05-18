"""
Nombre: Dara Van Gijsel
Fecha: 18-05-23
"""
from mis_clases import Profesor

# Crear dos objetos de la clase 02

# objeto 01
profesor1 = Profesor()
profesor1.nombre = "Juan"
profesor1.apellido = "Alvarez"
profesor1.num_estudiantes = 20
profesor1.num_pruebas = 3
profesor1.calcularPruebasTotal()
# Presentar objeto; usar el método __st__
print(profesor1)

# objeto 02

profesor2 = Profesor()
print("Ingrese su nombre:")
profesor2.nombre= input()
print("Ingrese su apellido:")
profesor2.apellido = input()
print("Ingrese el  numero de alumnos en clase:")
profesor2.num_estudiantes= int(input())
print("Ingrese el numero de pruebas a calificar por alumno:")
profesor2.num_pruebas= int(input())
profesor2.calcularPruebasTotal()

# Presentar objeto; usar el método __st__
print(profesor2)