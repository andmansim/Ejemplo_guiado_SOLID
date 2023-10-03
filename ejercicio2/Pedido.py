class Pedido:
    def __init__(self, id, cliente, tipo_pizza, ingredientes, precio, fecha, estado):
        self.id = id
        self.cliente = cliente
        self.tipo_pizza = tipo_pizza
        self.ingredientes = ingredientes
        self.precio = precio
        self.fecha = fecha
        self.estado = estado    

    def __str__(self):
        return f"Pedido: {self.id} - Cliente: {self.cliente} - Productos: {self.productos}"


if __name__ == "__main__":
    pass