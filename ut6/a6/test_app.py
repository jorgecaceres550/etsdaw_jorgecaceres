import pytest

from app import Calculadora

calc=Calculadora()

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),      
    (10, -2, 8),    
    (0, 0, 0),
    (20,33,53)      
])
def test_suma(a, b, esperado):
    assert calc.sumar(a, b) == esperado

@pytest.mark.parametrize("a, b, esperado", [
    (50, 3, 47),      
    (-10, -2, -8),    
    (0, 0, 0),
    (-20,21,-41)      
])
def test_resta(a, b, esperado):
    assert calc.restar(a, b) == esperado

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 6),      
    (10, -2, -20),    
    (0, 0, 0),
    (-20,-20,400)     
])
def test_multiplicacion(a, b, esperado):
    assert calc.multiplicar(a, b) == esperado

@pytest.mark.parametrize("a, b, esperado", [
    (10, -2, -5),
    (20, 5, 4),
    (7, 2, 3.5),
    (-20,-10,2)
])
def test_division(a, b, esperado):
    assert calc.dividir(a, b) == esperado

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        calc.dividir(10, 0)

from app import es_par

def test_par():
    assert es_par(20)==True

def test_no_par():
    assert es_par(19)==False

def test_par_negativo():
    assert es_par(-40)==True

def test_no_par_negativo():
    assert es_par(-99)==False

from app import dividir

def test_division_correcta():
    assert dividir(20,2)==10

def test_division_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(92,0)

from app import validar_password

@pytest.mark.parametrize("password, bool", [
    ("Contraseñacorrecta1234",True),
    ("vAlida12345678",True)

])
def test_validar_password_correctas(password,bool):
    assert validar_password(password) == bool

@pytest.mark.parametrize("password, mensaje_error", [
    ("hola23", "Password demasiado corta"),      
    ("contraseña07", "Debe contener mayúsculas"), 
    ("Contraseña", "Debe contener números")
])
def test_validar_password_errores(password, mensaje_error):
    with pytest.raises(ValueError) as excinfo:
        validar_password(password)
    assert str(excinfo.value) == mensaje_error

from app import clasificar_edad

@pytest.mark.parametrize("edad, esperado", [
    (0, "niño"),          
    (11, "niño"),         
    (17, "adolescente"),
    (18, "adulto"),
    (64, "adulto"),  
    (65, "mayor")      
])
def test_clasificar_edad(edad, esperado):
    assert clasificar_edad(edad) == esperado

from app import es_primo
def test_numero_primo():
    assert es_primo(2)==True

def test_numero_no_primo():
    assert es_primo(4)==False
from app import Carrito

def test_numero_menor_2():
    assert es_primo(1)==False
from app import Carrito

def test_añadir_un_producto():
    c = Carrito()
    c.agregar_producto("Monitor", 200)
    assert len(c.productos) == 1
    assert c.productos[0] == ("Monitor", 200)

def test_calcular_total_varios_productos():
    c = Carrito()
    c.agregar_producto("Teclado", 50)
    c.agregar_producto("Mouse", 25)
    assert c.calcular_total() == 75

def test_eliminar_un_producto():
    c = Carrito()
    c.agregar_producto("Libro", 10)
    c.agregar_producto("Goma", 2)
    c.eliminar_producto("Libro")
    assert len(c.productos) == 1
    assert c.productos[0][0] == "Goma"

def test_eliminar_en_carrito_vacio():
    c = Carrito()
    c.eliminar_producto("Sinproducto")
    assert len(c.productos) == 0


from app import eliminar_duplicados

def test_lista_con_duplicados():
    entrada = [("A", 1), ("A", 1), ("B", 2)]
    esperado = [("A", 1), ("B", 2)]
    assert eliminar_duplicados(entrada) == esperado

def test_lista_sin_duplicados():
    entrada = [("A", 1), ("B", 2)]
    assert eliminar_duplicados(entrada) == entrada

def test_lista_vacia():
    assert eliminar_duplicados([]) == []

def test_mantener_orden_original():
    entrada = [("C", 3), ("A", 1), ("C", 3), ("B", 2)]
    esperado = [("C", 3), ("A", 1), ("B", 2)]
    assert eliminar_duplicados(entrada) == esperado

from app import calcular_media

def test_lista_vacia():
    with pytest.raises(ValueError):
        calcular_media([])

def test_media_correcta():
    numeros = [10, 20, 30, 40]
    assert calcular_media(numeros) == 25

def test_media_valores_extremos():
    
    numeros = [1000, -1000, 0]
    assert calcular_media(numeros) == 0

from app import login

def test_login_correcto():
    assert login("admin", "1234") is True

def test_usuario_incorrecto():
    assert login("jorge", "1234") is False

def test_password_incorrecto():
    assert login("admin", "abcd") is False

def test_ambos_incorrectos():
    
    assert login("root", "admin123") is False