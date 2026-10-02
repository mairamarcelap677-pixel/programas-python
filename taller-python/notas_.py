print()
print("=" * 50)
print("-------------PROMOCION SOCIAL------------")
print("=" * 50)
nombre = input ("\nDigite su nombre: ")
nota = int(input("Digite su nota: "))

print(f"hola {nombre}")
if nota > 100 or nota < 0: 
    print("la Nota es incorrecta")
elif nota >= 90:
    print("✅ Excelente nivel")
elif nota >= 70:
    print(" Aprobado. Buen desempeño👍")
elif nota <= 60:
    print("💪Debes repasar los conceptos. Tu puedes!👌")