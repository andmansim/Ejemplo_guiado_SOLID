class Matriz():
    def __init__(self, elementos):
        self.elementos= elementos
    

class Traspuesta(Matriz):
    def __init__(self, elementos):
        super().__init__(elementos)
    def traspuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range (len(self.elementos[0]))])#enlazar bucles for para elementos pequeños sí (15, 20 datos), para grandes hacerlo de manera (miles datos) recuersiva
    #función lamnda para que la borre una vez hecha y así optimizamos el código --> lo ha hecho chatGpt
class Imprimir(Matriz):
    def __init__(self, elementos):
        super().__init__(elementos)
    def imprimir(self):
        for fila in self.elementos:
            print(fila)


#Todo esto tiene que ir en una clase lanzador, hay que pedirselo al chat para que te lo haga bien. TODO LO HACE EL CHAT
m = Imprimir([[1,2], [3,4]])
m.imprimir()

t = Traspuesta(m.elementos)
print(t.traspuesta().elementos)

class Lanzador(Imprimir, Traspuesta):
    def __init__(self, elementos):
        super().__init__(elementos)
    
    def lanzar(self):
        self.imprimir()
        print(self.traspuesta().elementos)

class Main