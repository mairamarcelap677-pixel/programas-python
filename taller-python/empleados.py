# ====================================================================
# Registro de Empleados 
# Tecnico en Programacion de Software
# ===================================================================

print ("\n======= REGISTRO DE EMPLEADOS =======")

nombre = input("Nombre del empleados:  ")

edad = int(input("Edad: "))
cargo = input ("Cargo: ").upper()
salarioMensual = float (input("salario Mensual: "))
activo = input("¿El empleado esta activo?(True / False): ").upper()

#Conversion a datos booleano
#activo = activo == "True"

if activo == "True":
    activo = "True"
    

print("\n ==== INFORMACION REGISTRADA ====")
print("Nombre:", nombre.upper())
print(f"Edad: {edad}")
print(f"cargo: {cargo}")
print(f" salario Mensual: {salarioMensual} ")
print("Empleado Activo: ", activo.upper())

