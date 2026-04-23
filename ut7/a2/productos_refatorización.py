class Producto:
    def __init__(self, nombre, precio, cantidad, cantidad_minima_descuento=2):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.cantidad_minima_descuento = cantidad_minima_descuento

    @property
    def subtotal_base(self):
        subtotal = self.precio * self.cantidad
        # Aplicamos descuento si supera la cantidad mínima
        if self.cantidad > self.cantidad_minima_descuento:
            subtotal -= (subtotal * 0.1)
        return subtotal

    def __repr__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class Carrito:
    SUBTOTAL_MINIMO_ENVIO_GRATIS = 100
    COSTE_ENVIO = 5
    TOTAL_VIP_UMBRAL = 500

    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        self.productos.append(producto)

    def calcular_envio(self, subtotal_carrito):
        return 0 if subtotal_carrito > self.SUBTOTAL_MINIMO_ENVIO_GRATIS else self.COSTE_ENVIO

    def calcular_total(self):
        subtotal_carrito = sum(p.subtotal_base for p in self.productos)
        
        envio = self.calcular_envio(subtotal_carrito)
        
       
        
        print(f"Envío: {'Gratis' if envio == 0 else f'{envio} euros'}")
        
        return subtotal_carrito + envio

    def es_cliente_vip(self, total):
        return total > self.TOTAL_VIP_UMBRAL

# --- Ejecución del programa ---

mi_carrito = Carrito()
mi_carrito.añadir_producto(Producto("Teclado", 30, 2))
#mi_carrito.añadir_producto(Producto("Raton", 15, 3))
mi_carrito.añadir_producto(Producto("Monitor", 200, 1))

total_pedido = mi_carrito.calcular_total()

print(f"TOTAL PEDIDO: {total_pedido}€")

if mi_carrito.es_cliente_vip(total_pedido):
    print("Estado: Cliente VIP")
