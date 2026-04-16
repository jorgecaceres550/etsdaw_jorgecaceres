# UT7A1 – Identificación de “malos olores” en el código


### Objetivo de la práctica

El objetivo de esta práctica es **analizar un programa que funciona correctamente pero cuya calidad de código es mejorable**.

Durante la sesión se realizará un **análisis colectivo del código para detectar “malos olores” (code smells)**. Estos son indicios de que el diseño del programa podría mejorarse mediante técnicas de refactorización.

- En esta práctica **no se debe modificar el código**.  
- El trabajo consiste únicamente en **analizarlo y debatir sobre su calidad**.


### Instrucciones de la práctica

Se proporciona un programa sencillo que simula un **sistema básico de gestión de pedidos**.

El programa realiza varias operaciones:

- almacena una lista de productos
- calcula el precio de cada producto en función de su cantidad
- aplica un descuento en algunos casos
- calcula el coste de envío
- calcula el total del pedido

Aunque el programa funciona correctamente, su código presenta **diversos problemas de diseño y calidad**.

El objetivo de la práctica es **analizar el código para identificar esos problemas**.

### Trabajo en clase

1. Lee el código detenidamente.
2. Analiza cómo está organizado.
3. Detecta posibles problemas de diseño o calidad del código.
4. Anota todos los problemas que encuentres.

Durante la sesión se realizará un **debate en clase**, donde cada grupo expondrá los problemas detectados.

### Preguntas que pueden ayudarte en el análisis

Para identificar posibles problemas puedes plantearte las siguientes cuestiones:

- ¿Hay **métodos demasiado largos**?
      En el código mezcla distintas responsabilidades, una de ellas podría ser calcular el costo del envio.
- ¿Las **variables tienen nombres claros y descriptivos**?

1. Los nombres de las variables no son descriptivos lo que dificulta la compresión del código.
la variable n se podría llamar nombre_producto,p producto_precio y c producto_cantidad.

2. En el bucle for cambiar la p por producto.

3. En el subtotal efectuar el cambio anteriormente mencionado en el punto 1.

4. Añadir al constructor de la clase el atributo que para poder aplicar un descuento sea 2.

5. se podría crear una variable denominada "cantidad_mínima" para que sea el minimo de productos para que pueda recibir el descuento del 10 %, también se podría crear variables que sean "SUBTOTAL_MINIMO" para que el valor sea 100, lo mismo se podría la variable "TOTAL_VIP_UMBRAL" y que su valor sea 500. Estas variables serán futuros atributos del constructor para otra clase que haga el calculo del total.
- ¿Se repite código en diferentes partes del programa?
    Se podría reducir la cantidad de "print" en el código.
- ¿Hay **números que aparecen directamente en el código sin explicación**?
    Los números que aparecen sin explicación son el 100 y 500 aunque se pueden llegar a interpretar por el contexto, sería mejor que tengan una variable para que tengan un contexto en el código.
- ¿El código mezcla distintas responsabilidades?
    Para poder mejorar la calidad del código sugerimos estos cambios:
    1. subtotal = subtotal - (subtotal * 0.1) cambiarla por subtotal- =  (subtotal * 0.1),en el constructor crear una lista vacia

    2. Se podría crear un método que se llame añadir_produto cuya función sería agregar el producto en la lista productos.

    3. Se podría crear un método mágico __repr__ para poder hacer la represacion del producto y quitar los print para que el código quede más limpio.

    4. Se podría crear un método llamado calcular_envio que evalue, si es mayor que 100 no sumarle nada, si es menor sumarle una variable llamada "coste_envio" y su valor sea 5.

    5. Se podría crear un método denominado "calcular_total" que haga los calculos del bucle, facilitando así la comprensión del código.
    6.Se podria crear un metodo denominado subtotal_base siendo una propertu, luego otro método que verifique si la cantidad de producto es mayor que 2. Estos métodos podrían estar en la clase producto

    7. Se podría añadir un método denominado "cliente_vip" que calcule si es un cliente vip o no.
    Las anteriores sugerencias se podrían estar dentro de otra clase distinta a producto.

- ¿El programa sería fácil de modificar o ampliar?
   El estado actual del código no es optimo ya que a pesar de ser funcional la legibilidad es baja lo que dificultaría en futuras actualizaciones o ampliaciones

- ¿Falta documentación o comentarios que expliquen el funcionamiento?
    Si.
    

### Entregable

Cada grupo deberá entregar un documento que incluya:

- una lista de los problemas detectados en el código
- una breve explicación de cada problema
- una posible mejora para cada caso


### Código a analizar

El código a analizar es el siguiente:

```python
class Producto:

    def __init__(self, n, p, c):
        self.n = n
        self.p = p
        self.c = c


productos = []

productos.append(Producto("Teclado", 30, 2))
productos.append(Producto("Raton", 15, 3))
productos.append(Producto("Monitor", 200, 1))

total = 0

for p in productos:

    subtotal = p.p * p.c

    if p.c > 2:
        subtotal = subtotal - (subtotal * 0.1)

    print("Producto:", p.n)
    print("Precio:", p.p)
    print("Cantidad:", p.c)
    print("Subtotal:", subtotal)

    if subtotal > 100:
        print("Envio gratis")
    else:
        print("Envio: 5 euros")
        subtotal = subtotal + 5

    total = total + subtotal

    print("-------------------")

print("TOTAL PEDIDO:", total)

if total > 500:
    print("Cliente VIP")
```
