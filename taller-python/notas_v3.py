#programa de notas 
#deleloper: jeronimo p. 
#date:21-08-26

print()
print("="*50)
print("---PROMOCION SOCIAL---")
print("="*50)

nombre = input("\n ¿cual es tu nombre:? ")
nota = int(input("\n escribe tu nota"))

if nota >= 100:
    print("la nota  ",nota,"es invalida")
elif nota >= 90:
    print("✅Excelente nivel  ")
elif nota >= 70:
    print("👌Aprobado, buen desempeño")
else:
    print("💪 Debes repasar los conceptos,tu puedes" ) 
