#python

numero = 1 
suma_pares = 0

while numero <= 20:

    if numero % 2 == 0:
        suma_pares = suma_pares + numero


    numero = numero + 1
print("La suma de los numeros pares del 1 al 20 es:", suma_pares)