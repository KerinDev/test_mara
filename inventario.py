class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar(self, nombre, cantidad):
     if nombre in self.productos:
        raise ValueError("El producto ya existe")
     self.productos[nombre] = {
        "nombre": nombre,
        "cantidad": cantidad
    }
    
    def consultar(self, nombre):
     if nombre not in self.productos:
        raise ValueError("El producto no existe")
     return self.productos[nombre]
    
    def actualizar(self, nombre, cantidad):
     if nombre not in self.productos:
        raise ValueError("El producto no existe")

     if self.productos[nombre]["cantidad"] + cantidad < 0:
        raise ValueError("Stock insuficiente")

     self.productos[nombre]["cantidad"] += cantidad

    def listar(self):
     return sorted(self.productos.values(), key=lambda p: p["nombre"])