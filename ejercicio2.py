'''
Ejercicio 2(7 Puntos): La pizzería
Estás creando un sistema de gestión de pedidos de pizza en línea utilizando Python. 
Este sistema consta de varios componentes que interactúan entre sí. Los componentes principales son:

CLASE: DataBaseManager: Esta clase es responsable de manejar la conexión con la base de datos y realizar 
operaciones CRUD. 

CLASE: Authenticator: Esta clase se utiliza para manejar la autenticación de usuarios, posiblemente utilizando un 
servicio externo o una base de datos local. 

CLASE: OrderManager: Esta clase se encarga de la gestión de los pedidos, incluyendo la creación, actualización, y 
eliminación de los pedidos de los usuarios. 

CLASE: PaymentProcessor: Esta clase es responsable de manejar las transacciones de pago, utilizando un servicio de 
procesamiento de pagos externo.
'''
#DataBase debe de tener get, put, delete  y otra cosa
#Authenticator: nombre, email, telefono, apellidos, pagos. Es la base del modelo. Métodos: login y registrer. 
#Esto tiene que apuntar al DataBase
#OrderManager: gestiona pedidos
#Payment: maneja los pagos
'''
Estos componentes no deben crearse ni gestionarse dentro de cada clase que los utiliza, sino que deben ser 
creados en algún lugar centralizado y "inyectados" en las clases que los necesitan.
'''
#hacer al menos 4 APIS que hacen cosas y apuntan a las base de datos, apis tienen métodos que hacen cositas. 
#Organizar cosas: definir clase, atributos, métodos todo en una clase y hacer de quien hereda o a quien se lo paso
'''
Tu tarea es implementar este sistema utilizando el concepto de inyección de dependencias. 
Debes definir cada clase y sus dependencias, luego inyectar las dependencias a través de los constructores de 
las clases. Por ejemplo, la clase OrderManager debería recibir instancias de DataBaseManager, Authenticator, y 
PaymentProcessor a través de su constructor.
'''
#Clase A depende de B por tanto A tiene en su constructor B. Ejemplo: clase persona, clase carnet --> (self, persona)
#Todo esto para modificar todo de 1
'''
Al implementar este sistema, considera los siguientes aspectos:
Desacoplamiento de las clases: Las clases no deben crear sus propias dependencias. En lugar de eso, 
deben recibir las dependencias ya creadas. Esto promueve un código más limpio y modular.

Pruebas: La inyección de dependencias debe facilitar las pruebas de las clases. Deberías poder crear "mocks" o 
"stubs" de las dependencias para probar las clases de manera aislada.

Reutilización de código: Si varias clases necesitan la misma dependencia, no debes crear una nueva instancia 
para cada una. En lugar de eso, crea una instancia de la dependencia y pásala a todas las clases que la necesiten.

Para concluir, debes demostrar cómo crearías las instancias de las dependencias y cómo las inyectarías en las 
clases que las necesitan. Asegúrate de que tu implementación sea robusta, fácil de entender y fácil de mantener.

'''