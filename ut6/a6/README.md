# UT6-A6 — Diseño de tests unitarios en Python con pytest y cobertura

### Objetivo

El objetivo de esta práctica es diseñar y ejecutar pruebas unitarias utilizando `pytest` para validar el comportamiento de un conjunto de funciones ya implementadas, así como medir la **cobertura de código** utilizando `pytest-cov`.

 **IMPORTANTE:**  
- NO debes modificar el código proporcionado (`app.py`)  
- Tu trabajo consiste exclusivamente en **diseñar tests**  
- Debes intentar cubrir el mayor número de casos posibles, incluidos errores y casos límite  



### Requisitos

- Python 3
- pytest
- pytest-cov

Instalación:

```bash
pip install pytest pytest-cov
```

Ejecución de tests:

```bash
pytest
```

Ejecución con cobertura:

```bash
pytest --cov
```

Informe detallado:

```bash
pytest --cov=app --cov-report=term-missing
```
Debes crear un fichero llamado test_app.py donde implementarás todos los tests.

**Tests básicos — Calculadora**

Diseña tests que verifiquen:

+ Suma correcta
+ Resta correcta
+ Multiplicación correcta
+ División correcta
+ División por cero (debe lanzar excepción)

**2. Función es_par**

+ Números pares
+ Números impares
+ Números negativos
  
**1. Función dividir**

+ División correcta
+ División por cero (excepción)

**Validación de contraseña**

Casos a probar:

+ Contraseña válida
+ Menos de 8 caracteres
+ Sin mayúsculas
+ Sin números

Debes comprobar que se lanzan excepciones cuando corresponda.

**Tests parametrizados — clasificar_edad**

Debes utilizar:

```bash
@pytest.mark.parametrize
```

Casos a cubrir:

+ Niño
+ Adolescente
+ Adulto
+ Mayor
  
**Tests parametrizados — es_primo**

+ Números primos
+ Números no primos
+ Casos límite (0, 1)
  
**Clase Carrito**

Diseña tests que validen:

+ Añadir productos
+ Calcular total correctamente
+ Eliminar productos
+ Comportamiento con carrito vacío
. 
**Función eliminar_duplicados**

+ Lista con duplicados
+ Lista sin duplicados
+ Lista vacía
+ Mantener el orden original

**Función calcular_media**

+ Media correcta
+ Lista vacía → excepción
+ Valores extremos

**Función login**

+ Login correcto
+ Usuario incorrecto
+ Password incorrecto

**Cobertura de código**

Debes medir la cobertura de tus tests utilizando ``pytest-cov``.

Ejecuta: ``pytest --cov=app --cov-report=term-missing``

Objetivo de cobertura:

+ Alcanzar al menos un 80% de cobertura
+ Identificar líneas no cubiertas
+ Añadir tests para mejorar la cobertura

**Entrega**

Debes entregar:

+ ``app.py``
+ ``test_app.py``