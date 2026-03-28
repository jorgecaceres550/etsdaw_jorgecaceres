def calcular_subtotal(carrito):
    subtotal = 0
    if len(carrito) == 0:
        raise ValueError("El carrito no puede estar vacio")
    
    for producto in carrito:
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        subtotal += precio * cantidad
    return subtotal


def aplicar_descuento(subtotal, descuento):
    
    if descuento < 0 or descuento > 100:
        return subtotal  
    return subtotal - (subtotal * descuento / 100)


def aplicar_cupon(subtotal, cupon):
    if cupon == "WELCOME10":
        return subtotal * 0.9
    elif cupon == "FREESHIP":
        return subtotal 
    else:
        return subtotal 


def calcular_envio(subtotal):
    if subtotal > 100: 
        return 0
    return 5


def calcular_impuestos(subtotal):
    return round(subtotal * 0.07, 2)


def calcular_total(carrito, descuento=0, cupon=None):
    subtotal = calcular_subtotal(carrito)
    subtotal = aplicar_descuento(subtotal, descuento)

    if cupon:
        subtotal = aplicar_cupon(subtotal, cupon)

    envio = calcular_envio(subtotal)
    impuestos = calcular_impuestos(subtotal)

    total = subtotal + envio + impuestos
    return total