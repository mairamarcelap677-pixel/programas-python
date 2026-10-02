import random


intentos = 10
numero = random.randint(1, 10)

print("\n=== Adivina el numero ===")
print("Estoy pensando en un numero del 1 al 10.")

for intento in range(1, intentos + 1):
	try:
		respuesta = int(input(f"\nIntento {intento}/{intentos}. Digite su numero: "))
	except ValueError:
		print("Escriba un numero entero.")
		continue

	if respuesta == numero:
		print(f"¡Felicitaciones! Adivinaste el numero en {intento} intento(s).")
		break
	elif respuesta < numero:
		print("El numero secreto es mayor.")
	else:
		print("El numero secreto es menor.")
else:
	print(f"Se acabaron los intentos. El numero secreto era {numero}.")

