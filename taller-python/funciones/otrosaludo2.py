#Funcion con argumentos 
def saludar_persona(nombre):
    print(f"Hola {nombre}")

#Llamamos la funcion 
saludar_persona("maira")
saludar_persona("sofia")

# otro ejemplo---------------------------
# utilizamos return
def suma(a,b):
    resultado = a+b
    return resultado

print(suma(5,8))

# otro ejemplo
def despedida(nombre="Amigo"):
    print(f"Adios {nombre}")

despedida("sofia")
despedida()



