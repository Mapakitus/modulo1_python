# Solicitar la edad al usuario
edad = input("Dime tu edad: ")

# Convertir la entrada a entero
edad = int(edad)

# Evaluar la edad usando if-elif-else
# Mostrar el mensaje correspondiente
if edad >=0 and edad < 13:
    print("Eres un niño")
elif 13 <= edad < 18:
    print("Eres un adolescente")
elif 18 <= edad < 65:
    print("Eres un adulto")
elif edad >= 65:
    print("Eres un adulto mayor")
else:
    print("Edad no válida")