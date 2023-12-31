from __future__ import annotations #importamos anotaciones
from abc import ABC, abstractmethod #abs para crear clases abstractas


class Creator(ABC):
    '''
    Declara el metodo factory que retorna un objeto de la clase producto.
    Las subclases de Creator usualmente proveen la implementacion de este metodo.
    '''
   
    @abstractmethod #para indicar a la memoria que nos guarde un espacio para esto y así que no se sobreescriba
    def factory_method(self):
        '''
        El método de la clase que hace cositas
        '''
        pass

    def some_operation(self) -> str:
        '''
        Crea el objeto producto y lo usa
        '''
        #llamamos al metodo factory_method para que nos cree el objeto producto
        product = self.factory_method()

        #usamos el producto
        result = f"Creator:{product.pedido()}"

        return result



'''
las clases concretas heredan de la creadora para cambiar el tipo de producto dependiendo del caso
'''

class ConcreteCreator1(Creator):
    '''
    Cambiamos el método factory a nuestro gusto dependiendo del caso concreto que queramos. 
    Podemos tener tantos casos concretos y productos como queramos
    '''
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()

'''
Producto: id, tamaño, ingredientes, precio, estado_producto, alergias, cliente (dependerá si lo ponemos en cliente o en producto)
'''
class Product(ABC):
    '''
    Declaramos la operación general de todos los productos
    '''
    def __init__(self, id, tamanio, ingredientes, precio, estado_producto, alergias, cliente):
        self.tamanio = tamanio
        self.ingredientes = ingredientes
        self.precio = precio
        self.estado_producto = estado_producto
        self.alergias = alergias
        self.cliente = cliente
        self.id = id
   
    @abstractmethod
    def pedido(self) -> str:
        pass



'''
Casos concretos de los productos
'''

class ConcreteProduct1(Product):
    def pedido(self) -> str:
        return f'Producto: {self.id}, Precio: {self.precio}, Estado: {self.estado_producto}, Cliente: {self.cliente}, Tamaño: {self.tamanio}, Ingredientes: {self.ingredientes}, Alergia: {self.alergias},  '

#De momento no creo que haga falta hacer otro caso
class ConcreteProduct2(Product):
    def pedido(self) -> str:
        return "{Result of the ConcreteProduct2}"


'''
Cliente:nombre, apellido, DNI o gmail, contraseña, pedido, estado_pago, direción 
'''
def client_code(creator: Creator) -> None:
    '''
    Nos muestra el pedido del cliente
    '''
    print(f"Pedido Cliente.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("Cliente1: Con caso concreto1")
    client_code(ConcreteCreator1())
    print("\n")

    print("Cliente2: Con caso concreto2")
    client_code(ConcreteCreator2())