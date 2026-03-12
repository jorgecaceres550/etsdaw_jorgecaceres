# UT6-A3 Cobertura de código en Python 

### Objetivo de la práctica

El objetivo de esta práctica es comprender el concepto de cobertura de código y analizar qué partes de un programa están siendo ejecutadas durante las pruebas.

Mediante esta práctica aprenderás a:

+ ejecutar tests automatizados

+ medir la cobertura de código

+ identificar partes del programa que no están siendo probadas

+ mejorar los tests para aumentar la cobertura

### Descripción del programa

Se proporciona el programa `calculadora_notas.py` el cual contiene el siguiente código:

```python
def calcular_media(notas):

    if len(notas) == 0:
        raise ValueError("Lista vacía")

    suma = 0

    for nota in notas:

        if not isinstance(nota,(int,float)):
            raise ValueError("Nota no numérica")

        if nota < 0 or nota > 10:
            raise ValueError("Nota fuera de rango")

        suma += nota

    return suma / len(notas)
```

Los test iniciales se encuentran en al archivo `test_calculadora_notas.py` el cual incluye el código siguiente:

```python
from calculadora_notas import calcular_media

def test_media_simple():
    assert calcular_media([6,7,8]) == 7

def test_media_decimal():
    assert calcular_media([10,9,8,7]) == 8.5
```

Vamos a instalar las herramientas necesarias para medir la cobertura de código:

```bash
pip install pytest pytest-cov
```

Para medir la cobertura ejecutamos el comando `pytest --cov`  el cual nos da como ejemplo de salida:

```
Name                     Stmts   Miss  Cover
--------------------------------------------
calculadora_notas.py       12      4    67%
```

Esto indica que **sólo el 67% del código está cubierto por tests**.


### Actividad

Debes analizar qué partes del código no están siendo ejecutadas por los tests actuales.

Posteriormente debes crear **nuevos tests** para comprobar también los siguientes casos:

- lista vacía

- nota fuera de rango

- valor no numérico

Adjunta en la siguiente caja de código el archivo completo con los nuevos tests que haz añadido:

```python
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
```



Tras añadir los nuevos tests debes volver a ejecutar `pytest --cov` e intentar conseguir una **cobertura mínima del 90%.**

Adjunta a continuación una captura de pantalla de la covertura alcanzada después de incluir los nuevos test:

![Cobertura de tests](/img/001.png)

## Entrega

Debes subir a tu repositorio de GitHub:

- El archivo `calculadora_notas.py`

- El archivo `ntest_calculadora_notas.py` con los test que has incluido

- Este archivo `README.md` con las evidencias que se piden.





