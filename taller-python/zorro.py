# el pequeño zorro zip

print("¡Hola, soy el pequeño zorro zip!")
print("Estoy aquí para ayudarte a aprender Python de manera divertida y sencilla.")
print("ayudame en esta aventura de aprendizaje, juntos podemos explorar el mundo de la programación.")

energia = int(input("¿Cuánta energía tienes? (Ingresa un número): "))
monedas = int(input("¿Cuántas monedas tienes? (Ingresa un número): "))

if energia >= 50:
    print("¡Puede pasar el puente de inmediato sin pagar nada!")
if energia < 50:
    print("¡Necesitas pagar 10 monedas para pasar el puente!")
if monedas >= 10:
        monedas -= 10
        print("Has pagado 10 monedas. Te quedan", monedas, "monedas.")
else:
    print("No tienes suficientes monedas para pagar. ¡deberas quedarte en el bosque!")