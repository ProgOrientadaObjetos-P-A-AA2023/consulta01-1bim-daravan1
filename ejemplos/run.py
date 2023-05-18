"""
Nombre: Dara Van Gijsel
Fecha: 18-05-23
"""
# Crear dos objetos de la clase 01
from mis_clases import Alumno
# objeto 01
# crear
alunmo1 = Alumno()
alunmo1.nombre = "Juan"
alunmo1.apellido = "Alvarez"
alunmo1.calificacion1 = 7.8
alunmo1.calificacion2 = 8.9
alunmo1.calcular_promedio()
# Presentar objeto; usar el método __st__
print(alunmo1)

# objeto 02
# crear ingresando valores por teclado
alunmo2 = Alumno()
print("Ingrese su nombre:")
alunmo2.nombre= input()
print("Ingrese su apellido:")
alunmo2.apellido = input()
print("Ingrese su primera calificacion:")
alunmo2.calificacion1= float(input())
print("Ingrese su segunda calificacion:")
alunmo2.calificacion2= float(input())
alunmo2.calcular_promedio()

# Presentar objeto; usar el método __st__
print(alunmo2)
