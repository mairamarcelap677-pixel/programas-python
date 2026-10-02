# 4 sep 26
# Developer: YO

#imprimiendo una serie de numeros
 
#Recorremos una COLECCION DE ELEMENTOS  como un rango o lista 
for  n in range (1,10):
    print (f"Generando reporte #{n}")


#------------------------------------------------------

print ("="* 30)
for num in range (10):
    print (num)

#----------------------------------------------------
print ("="* 30)
for palabra in "Hola":
    print (palabra)

#----------------------------------------------------
print ("="* 30)
#iteramos sobre una LISTA
frutas = ["manzana","pera","durazno","sandia","cereza","fresa",]
for fruta in frutas:
    print(fruta)
#-----------------------------------------------
print ("="* 30)
print ("Ahora viene la magia ✅")

for indice, fruta in enumerate(frutas):
    print (f"en la caja {indice}, tengo  {frutas}")

#-----------------------------------------------
print ("="* 30)
print("la granja de mi tio tiene los siguientes animales")
print ("="* 30)
animales = ["gallina","cerdo","vaca","oveja","caballo","perro","gato"]
for animal in animales:
    print (f"mi tio tiene un {animal}")


