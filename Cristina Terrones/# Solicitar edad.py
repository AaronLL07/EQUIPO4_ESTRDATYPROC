# Solicitar edad

edad = int(input("Buen dia. Escribe la edad: "))
if edad < 0:
    print("Error: edad no aceptada.")
elif edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad")