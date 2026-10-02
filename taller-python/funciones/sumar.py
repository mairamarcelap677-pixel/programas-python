#programar para restar,multiplicar y dividir 


def sumar ():
    return num1 + num2
    

def restar():
    return num1 - num2


def multiplicar():
    return num1 * num2

def dividir():
    return num1 / num2 

    

num1 =int(input("\n Digite el primer numero: "))
num2 = int(input("\n Digite el segundo numero: ")) 

resultado = restar()
print(f"\n el resultado de la recta es:{resultado}")

resultado = multiplicar()
print(f"\n el resultado de la multiplicar es:{resultado}")

if num2 ==0:
    print("\n Error, no se puede dividir entre 0")
else:
    resultado = dividir()
    print(f"\n El resultado de la division es: {resultado}")
