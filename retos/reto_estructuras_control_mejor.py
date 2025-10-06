edad_usuario = input("Dame la edad del usuario: ")


# Convertir la entrada a entero
edad = int(edad_usuario)

# Evaluar la edad usando if-elif-else
if edad >= 65:
 mensaje = "adulto mayor"
elif edad >= 18:
 mensaje = "adulto"
elif edad >= 13:
 mensaje = "adolescente"
elif edad > 0:
 mensaje = "niño"
else:
 mensaje = "error. Por favor, escriba un número positivo"

# Mostrar el mensaje correspondiente
print(f"Eres un {mensaje}" if edad > 0 else f"Es un {mensaje}")

