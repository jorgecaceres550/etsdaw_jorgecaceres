from carrito import calcular_subtotal
#carrito con productos
def test_carrito_lleno():
        assert calcular_subtotal([
 {"nombre":"teclado","precio":30,"cantidad":2},
 {"nombre":"raton","precio":10,"cantidad":1}
])==70
#carrito con un solo producto
def test_carrito_simple():
        assert calcular_subtotal([
 {"nombre":"teclado","precio":30,"cantidad":2}

])==60 
#carrito vacio
def carrito_vacio():
        assert calcular_subtotal([]) ==0  
        
from carrito import aplicar_descuento

def test_sin_descuento():
        assert aplicar_descuento(500,0)==500

def test_descuento_valido():
        assert aplicar_descuento(500,50)==250

def descuento_100():
        assert aplicar_descuento(500,100)==0

def test_descuento_no_valido():
        assert aplicar_descuento(500,200)

from carrito import calcular_envio

def test_sub_total_menor_100():
        assert calcular_envio(80)==5
def test_sub_total_mayor_100():
        assert calcular_envio(120)==0
def test_sub_total_igual_100():
        assert calcular_envio(100) ==5

from carrito import calcular_total

def test_total_sin_desciento():
        assert calcular_total([
 {"nombre":"teclado","precio":30,"cantidad":2},
 {"nombre":"raton","precio":10,"cantidad":1}
],0)==75

def test_total_con_desciento():
        assert calcular_total([
 {"nombre":"teclado","precio":30,"cantidad":2},
 {"nombre":"raton","precio":10,"cantidad":1}
],50)==40
        
def test_total_con_envio_gratis():
        assert calcular_total([
 {"nombre":"teclado","precio":30,"cantidad":3},
 {"nombre":"raton","precio":10,"cantidad":1}
],0)==105