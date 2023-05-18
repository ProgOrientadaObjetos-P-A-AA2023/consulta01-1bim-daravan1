"""
Nombre: Dara Van Gijsel
Fecha: 18-05-23
"""


# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Alumno:
    def __int__(self, nombre, apellido, calificacion1, calificacion2):
        self.nombre = nombre
        self.apellido = apellido
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
    def calcular_promedio(self):
        return (self.calificacion1 + self.calificacion2) / 2
    def __str__(self):
        promedio = self.calcular_promedio()
        return f"El alunmo {self.nombre} {self.apellido} tiene un primera calificacion de {self.calificacion1}, " \
               f"una segunda calificacion de {self.calificacion2} y un promedio: {promedio}"


# clase 02
class Profesor:
    def __int__(self, nombre, apellido, num_estudiantes, num_pruebas):
        self.nombre = nombre
        self.apellido = apellido
        self.num_estudiantes = num_estudiantes
        self.num_pruebas = num_pruebas


    def calcularPruebasTotal(self):
        return self.num_estudiantes * self.num_pruebas

    def __str__(self):
        pruebas_total = self.calcularPruebasTotal()
        return f"El profesor {self.nombre} {self.apellido} con {self.num_estudiantes} alumnos y" \
               f" {self.num_pruebas} pruebas por alunmo tiene {pruebas_total} pruebas a calificar"

