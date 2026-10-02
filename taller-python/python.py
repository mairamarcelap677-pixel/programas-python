#python

numero = 1 
suma_pares = 0

#1. completa la condicion para que llegue hasta el 20 (incluido)
while numero <= 20:

    #2. completa la logica para saber si el numero es par (residuo de 2)
    if numero % 2 == 0 :
        suma_pares = suma_pares + numero

 #¡CUIDADO! Hay un error logico grave en este bucle que colapsará tu terminal.
 #¿Qué línea falta agregar aquí abajo para que el ciclo avance y no sea infinito 

numero = numero + 1
print("La suma de los numeros pares del 1 al 20 es:", suma_pares)