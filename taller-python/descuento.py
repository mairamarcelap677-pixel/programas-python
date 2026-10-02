#descuento por compras

compra = 100
compra = float(input("Ingrese el monto de la compra: "))

if compra >= 100:
    descuento = 0.1 * compra
    print("Descuento aplicado:", descuento)
if compra <100:
    print("No hay descuento disponible.")
elif compra >= 200:
        descuento = 0.2 * compra
        print("Descuento aplicado:", descuento)
else:
        print("No hay descuento disponible.")

