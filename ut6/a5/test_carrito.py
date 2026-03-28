import pytest
from carrito import calcular_subtotal

@pytest.mark.parametrize("carrito, resultado_esperado", [
    ([{"nombre": "teclado", "precio": 30, "cantidad": 2}, {"nombre": "raton", "precio": 10, "cantidad": 1}], 70),
    ([{"nombre": "teclado", "precio": 30, "cantidad": 2}], 60)
])
def test_calcular_subtotal_varios(carrito, resultado_esperado):
    assert calcular_subtotal(carrito) == resultado_esperado


def test_carrito_vacio():
    with pytest.raises(ValueError, match="El carrito no puede estar vacio"):
        calcular_subtotal([])




def test_carrito_valores_invalidos():
    assert calcular_subtotal([{"nombre":"teclado","precio":-8,"cantidad":-20}])

from carrito import aplicar_descuento

@pytest.mark.parametrize("subtotal, descuento, resultado_esperado", [
    (60, 0, 60),   
    (60, 50, 30),   
    (100, 100, 0)   
])
def test_descuentos_validos(subtotal, descuento, resultado_esperado):
    assert aplicar_descuento(subtotal, descuento) == resultado_esperado

def test_descuento_invalido():
    assert aplicar_descuento(90,-50)

from carrito import aplicar_cupon

def test_cupon_WELCOME10():
    assert aplicar_cupon(100,"WELCOME10")==90

def test_cupon_FREESHIP():
    assert aplicar_cupon(70,"FREESHIP")==70

def test_cupon_invalido():
    assert aplicar_cupon(120,"CUPONVALIDO")

from carrito import calcular_impuestos

def test_impuestos_correctos():
    assert calcular_impuestos(100)==7

def test_impuestos_redondeados():
    assert calcular_impuestos(100.50)==7.04

from carrito import calcular_total
import pytest

@pytest.mark.parametrize("carrito, descuento, cupon, resultado_esperado", [
    #Sin descuento
    ([{"nombre":"teclado","precio":30,"cantidad":2}, {"nombre":"raton","precio":10,"cantidad":1}], 0, None, 79.9),
    
    #Descuento del 50%
    ([{"nombre":"teclado","precio":30,"cantidad":2}, {"nombre":"raton","precio":15,"cantidad":1}], 50, None, 45.13),
    
    # Cupón WELCOME10
    ([{"nombre":"teclado","precio":30,"cantidad":2}, {"nombre":"raton","precio":15,"cantidad":1}], 0, "WELCOME10", 77.23),
    
    # Cupón FREESHIP
    ([{"nombre":"teclado","precio":30,"cantidad":2}, {"nombre":"raton","precio":15,"cantidad":3}], 0, "FREESHIP", 112.35),
    
    # Con descuento y cupón
    ([{"nombre":"teclado","precio":30,"cantidad":6}, {"nombre":"raton","precio":15,"cantidad":3}], 10, "WELCOME10", 195.01)
])
def test_pedidos(carrito, descuento, cupon, resultado_esperado):
    assert calcular_total(carrito, descuento, cupon) == resultado_esperado
