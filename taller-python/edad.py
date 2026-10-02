edad = int(input("Por favor, ingrese la edad del asistente: "))
tiene_identificacion = True  # Suponiendo que el asistente tiene identificación

# Nivel 1: if/else basico
if edad >= 18 :
    print("Acceso permitido al area general.")
else:
    print("Acceso denegado. Es menor de edad.")

# Nivel 2: Agregando elif y operadores logicos (and)

if edad >= 18 and tiene_identificacion:
    print("Acceso completo autorizado.")
elif edad >= 18 and not tiene_identificacion:
    print("Ve a la taquilla para verificar tu identificación.")
elif edad >= 13:
    print("Acceso permitido solo a la zona familiar .")
else:
    print("Acceso denegado. No cumple con los requisitos.")