#proyecto: presentador virtual 
# autor: maira marcela 
# fecha: 12 de diciembre de 2008

#solicitamos datos de la persona 
nombre  = input("¿como es tu nombre? |¿what is your name: ?")
edad  = input ("¿cuantos años tienes? | ¿how old are you?")
Ciudad  = input("¿en que ciudad vives? | ¿which city do you live in?")
color = input("¿cual es tu color favorito? | ¿what is your favorite color?")
pasatiempo = input("¿cual es tu pasatiempo favorito? | ¿what is your favorite hobby?")
redesocial = input("¿cual es tu red social favorita? | ¿what is your favorite social network?")



#Mostramos el saludo como un presentador de TV
print("\n--------------------------")
print(f" Buenad tardes {nombre} Good affernoon, {nombre}!")
print(f" Hoy, desde la ciudad de {Ciudad}, presentamos a una persona increíble de {edad} años le gusta el color {color} y le gusta {pasatiempo} y utiliza {redesocial}.today, from the city of {Ciudad }, We have an incredible person from {edad } de age who likes the color { color} and the hobby {pasatiempo}")
print(f"¡Gracias por estar con nosotros!{nombre} ¡thank you for being with us!{nombre}")
print("-----------------------")