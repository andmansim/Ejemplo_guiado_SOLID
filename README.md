# Progra1

plant uml --> online server --> le pones el código o cosa que te da el chatGPT. 
Le ponemos en el chatGPT el enunciado de la tarea y q nos haga un diagrama UML cumpliendo los criterios SOLID. 
Lo volvemos a poner en el plant uml para comprobar cómo nos lo ha creado. 
Después nos vamos a nuestro repo y creamos una carpeta nombre: PlantUML. Añadimos la imagen que nos ha generado la web basándose en el chat y el código (.puml). En ejercicio1.puml le pegamos el código que nos da chat. 
#No va --> lo subimos como imagen. 

Montar un googlecolaps con gpu con .....
Hacer el diagrama uml con el chaty y comprobarlo. Tras tener todo el código y que vaya. Guardar el uml como .svg (vector gráfico que se adapta a todo)
PRINCIPIOS_GENERALES_Y_SOLID--> buscar repo
para ver el preview es control + d

El ejercicio 2 en otra carpeta
DatabaseManager --> dni, apellido y dinero
ENUNCIADO EJE 2
Estás creando un sistema de gestión de pedidos de pizza en línea utilizando Python. Este sistema consta de varios componentes que interactúan entre sí. Los componentes principales son:

DataBaseManager: Esta clase es responsable de manejar la conexión con la base de datos y realizar operaciones CRUD.

Authenticator: Esta clase se utiliza para manejar la autenticación de usuarios, posiblemente utilizando un servicio externo o una base de datos local.

OrderManager: Esta clase se encarga de la gestión de los pedidos, incluyendo la creación, actualización, y eliminación de los pedidos de los usuarios.

PaymentProcessor: Esta clase es responsable de manejar las transacciones de pago, utilizando un servicio de procesamiento de pagos externo.

Estos componentes no deben crearse ni gestionarse dentro de cada clase que los utiliza, sino que deben ser creados en algún lugar centralizado y "inyectados" en las clases que los necesitan.

Tu tarea es implementar este sistema utilizando el concepto de inyección de dependencias. Debes definir cada clase y sus dependencias, luego inyectar las dependencias a través de los constructores de las clases. Por ejemplo, la clase OrderManager debería recibir instancias de DataBaseManager, Authenticator, y PaymentProcessor a través de su constructor.

Al implementar este sistema, considera los siguientes aspectos:

Desacoplamiento de las clases: Las clases no deben crear sus propias dependencias. En lugar de eso, deben recibir las dependencias ya creadas. Esto promueve un código más limpio y modular.

Pruebas: La inyección de dependencias debe facilitar las pruebas de las clases. Deberías poder crear "mocks" o "stubs" de las dependencias para probar las clases de manera aislada.

Reutilización de código: Si varias clases necesitan la misma dependencia, no debes crear una nueva instancia para cada una. En lugar de eso, crea una instancia de la dependencia y pásala a todas las clases que la necesiten.

Para concluir, debes demostrar cómo crearías las instancias de las dependencias y cómo las inyectarías en las clases que las necesitan. Asegúrate de que tu implementación sea robusta, fácil de entender y fácil de mantener.

