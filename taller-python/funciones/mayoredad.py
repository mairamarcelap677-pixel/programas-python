#Programa para saber si una persona es mayor de edad
#Developer: Yo 
edad = int(input("\ningrese su edad: "))

def mayor(edad):
    hijos = 0 
    if edad >= 18:
        return"Es mayor de edad"
        hijos = int(print("cuantos hijos tienes: "))
    else:
        return"NO , NO es mayor de edad"

#Llamo la funcion 
#print(mayor(15))


print ( mayor (edad))
#hijos = hijos + 2 
