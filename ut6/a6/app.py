class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return a / b


def es_par(numero):
    return numero % 2 == 0


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b


def validar_password(password):
    if len(password) < 8:
        raise ValueError("Password demasiado corta")
    if not any(c.isupper() for c in password):
        raise ValueError("Debe contener mayúsculas")
    if not any(c.isdigit() for c in password):
        raise ValueError("Debe contener números")
    return True


def clasificar_edad(edad):
    if edad < 12:
        return "niño"
    elif edad < 18:
        return "adolescente"
    elif edad < 65:
        return "adulto"
    else:
        return "mayor"


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


class Carrito:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p[0] != nombre]

    def calcular_total(self):
        return sum(precio for _, precio in self.productos)


def eliminar_duplicados(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def calcular_media(notas):
    if len(notas) == 0:
        raise ValueError("Lista vacía")
    return sum(notas) / len(notas)


def login(usuario, password):
    if usuario != "admin":
        return False
    if password != "1234":
        return False
    return True