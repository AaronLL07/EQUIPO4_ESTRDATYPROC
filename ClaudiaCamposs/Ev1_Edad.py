# Soloicitar la edad y definir si es mayor o menor de edad

edad=int(input("Ingrese su edad: "))
if edad<0:
    print("Dato incorrecto. Ingrese una edad vailida.")
elif edad>=18:
    print("Es mayor de edad.")
else:
    print('Es menor de edad.')