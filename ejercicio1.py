'''
Ejercicio práctico1 (3Puntos): Creación de una clase en Python que representa una matriz.
Para este ejercicio, deberás crear una clase que representa una matriz. 
Las operaciones que esta clase debe permitir son la creación de una matriz a partir de una lista 
de listas, la impresión de la matriz en una forma legible, y el cálculo de la 
transpuesta de la matriz. Asegúrate de que cada método tenga una única responsabilidad.

'''
class Matriz:
    def __init__(self, elementos): #crea matriz en listas de listas
        self.elementos = elementos

    #Esto de abajo en otra clase hereda de matriz
    def imprimir(self):
        for fila in self.elementos:
            print(fila)

    def transpuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])
'''
operaciones son acciones --> métodos
operaciones en otra clase, la matriz colo tenemos una clase estática 
elementos son la lista de listas
class ej: matriz --> estructura
otras clases son las que hacen las cosas (MVC)
Este código no cumple el método SOLID
Si queremos meter otra función se hace en otra clase (otro to do) no tocamos el código que ya está hecho. 
Hacemos otra clase y heredamos :)
En el main hay q definir la matriz, imprimir y que cumpla SOLID
'''