#hacer un programa donde diga excelente , aprobado o Reprobado 
# 90 > excelente 
# 60 < reprobado 
# 60> a <90 aprobado

print("======= notas2026========")

nombre = input("\n Digite su nombre⬅️")
nota = int(input("\n digite su nota: "))

if nota >= 90:
    print(f"{nombre}, excelente sigue asi✅")
elif nota < 60:
    print (f"{nombre} ,has reprobado necesitas recuperar😬")
elif nota > 60 or nota < 90:
    print (f"{nombre} aprobaste😊")
    