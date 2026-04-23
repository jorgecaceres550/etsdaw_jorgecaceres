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