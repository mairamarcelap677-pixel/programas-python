peso = 70.5
altura = 1.75

# 1. completa la formula matematica del IMC (peso divido por el cuadrado de la altura)
imc = peso / (altura ** 2)
print("Tu IMC es:", imc)

# Encuentra los 3 errores en esta estructura:

if imc < 18.5:
    print("Diagnostico: Bajo peso")
elif imc >= 24.9 and imc < 30.0:                  # Error 1: Se debe usar '==' para comparación, no '='
    print("Diagnostico: peso normal") 
elif imc >= 30.0:                 # Error 2: El rango de obesidad debería ser >= 30.0
    print("Diagnostico: sobre peso")
else :
    print("Diagnostico: Obesidad")