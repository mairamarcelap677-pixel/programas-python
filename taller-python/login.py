# 4 septiempre  2026
# Developer: Mayra perdomo - sofia garcia

pin = "123456"
intentos = 0
Bloqueado = False


while intentos < 3:
    ingreso = input("Ingrese su pin:")
    if ingreso == pin: 
        print (" Acceso concedido. Muy bien!😒")
        break #rompe el ciclo 
    else:
        #intentos = intentos + 1 
        intentos += 1
        print(f" PIN incorrecto 😬 Te quedan (3 - intentos) intentos ")

if intentos == 3:
    print("cuantas bloqueada por seguridad")
