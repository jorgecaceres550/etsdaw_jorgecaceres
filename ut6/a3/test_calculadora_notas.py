from calculadora_notas import calcular_media

def test_media_simple():
    assert calcular_media([6,7,8]) == 7

def test_media_decimal():
    assert calcular_media([10,9,8,7]) == 8.5

## Debajo de esta línea debes añadir los tests que hagan que la cobertura suba al 90%
def test_media_lista_vacia():
    assert calcular_media([])

def test_media_fuera_rango():
    assert calcular_media([100,100]) == 100

def test_media_no_numero():
    assert calcular_media(['nota=10'])

