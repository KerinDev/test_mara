import pytest
from inventario import Inventario

@pytest.fixture
def inv():
    return Inventario()

def test_registrar_producto(inv):
    inv.registrar("Camisa", 50)
    assert "Camisa" in inv.productos

def test_consultar_producto(inv):
    inv.registrar("Camisa", 50)
    producto = inv.consultar("Camisa")
    assert producto["nombre"] == "Camisa"
    assert producto["cantidad"] == 50

def test_actualizar_stock(inv):
    inv.registrar("Pantalón", 20)
    inv.actualizar("Pantalón", 10)
    assert inv.consultar("Pantalón")["cantidad"] == 30

def test_listar_inventario(inv):
    inv.registrar("A", 1)
    inv.registrar("B", 2)
    assert len(inv.listar()) == 2