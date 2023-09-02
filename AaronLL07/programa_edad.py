# Primero se solicita la edad
edad = int(input("Ingrese su edad: "))  # En esta linea se solicitó la edad
# Ahora se evalua la edad con una condición, si cumple con los parámetros
# se imprime que es mayor de edad, sino, que no es menor
if edad <= 0 :
    print("Edad no válida, ingresar una edad correcta")

elif edad >= 18:
    print("Eres mayor de edad")

elif edad < 18:                  
    print("Eres menor de edad")  


