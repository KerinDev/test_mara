class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar(self, nombre, cantidad):
        self.productos[nombre] = {"nombre": nombre, "cantidad": cantidad}

    def consultar(self, nombre):
        return self.productos.get(nombre)

    def actualizar(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre]["cantidad"] += cantidad

    def listar(self):
        return list(self.productos.values())