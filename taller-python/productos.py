# =====================================
# Venta de un Producto en Dolares
# registro de compra
# =====================================

print("=" * 100)
print("VENTA DE UN PRODUCTO")
print("=" * 100)

cliente = input("Nombre del cliente: ").upper()
identificacion = input ("numero de identificacion:")
producto = input("Ingrese el nombre del producto: ").upper()

precio = float(input("Ingrese el precio del producto en USD: "))
cantidad = int(input("Ingrese la cantidad a comprar: "))

total = precio * cantidad
total = round(total, 2)



print("=" * 100)
print("FACTURA DE COMPRA")
print("=" * 100)
print(f"Cliente: {cliente}")
print(f"identificacion:{identificacion}")
print(f"Producto: {producto}")
print(f"Precio unitario: {precio} USD")
print(f"Cantidad: {cantidad}")
print(f"Total a pagar: {total} USD")

if total > 20:
    print("¡Felicidades! Por tu compra mayores a $20 USD recibes un descuento o obsequio por tu compra.")
else:
    print("Gracias por tu compra. ¡NO VUELVA POR ACA!")
