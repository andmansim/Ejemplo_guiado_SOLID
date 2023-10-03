class Usuario:
    def __init__(self, nombre, apellido, email, password, dinero, direccion, telefono, n_pedidos):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.n_pedidos = n_pedidos
        self.email = email
        self.password = password
        self.dinero = dinero
        self.direccion = direccion
    def __str__(self):
        return f"Usuario: {self.nombre}, Apellido: {self.apellido}, Telefono: {self.telefono}, Pedidos: {self.n_pedidos}, Email: {self.email}, Contraseña: {self.password}, Dinero: {self.dinero} y Dirección{self.direccion}"
   
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "n_pedidos": self.n_pedidos,
            "email": self.email,
            "password": self.password,
            "dinero": self.dinero,
            "direccion": self.direccion
        }