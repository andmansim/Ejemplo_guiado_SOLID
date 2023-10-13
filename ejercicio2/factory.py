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

    def some_operation(self) -> str: #el -> str es para indicar que el metodo retorna un string y hace de funión lambda para ahorrar tiempo
        '''
        Este contiene la lógica del código que depende de un objeto producto retornado por el método 
        factory.
        Las subclases pueden cambiar indirectamente esa lógica al sobreescribir el método factory y 
        retornar un tipo diferente de producto.
        '''
    
        #llamamos al metodo factory_method para que nos cree el objeto producto
        product = self.factory_method()

        #usamos el producto
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

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
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


'''
Cliente:nombre, apellido, DNI o gmail, contraseña, pedido, estado_pago, direción 
'''
def client_code(creator: Creator) -> None:
    '''
    Funciona con una instancia concreta de creador. El código del cliente debería funcionar con cualquier subclase de creador.
    '''
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())