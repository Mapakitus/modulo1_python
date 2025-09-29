# Crear variables con diferentes tipos de datos en Python 
# y realizar conversiones entre ellos.


# Convertir a entero (int)
numero_entero = int(12.5)      # 12 (trunca la parte decimal)
texto_a_entero = int("10016")    # 10016
booleano_a_entero = int(True)  # 1

# Convertir a decimal (float)
decimal = float(12)            # 12.0
texto_a_decimal = float("12.5") # 12.5
booleano_a_decimal = float(False) # 0.0

# Convertir a texto (str)
entero_a_texto = str(12)       # "12"
decimal_a_texto = str(12.5)    # "12.5"
booleano_a_texto = str(True)   # "True"

# Convertir a booleano (bool)
numero_a_booleano = bool(12)   # True (cualquier número excepto 0 es True)
texto_a_booleano = bool("")    # False (cadena vacía es False)

print("Entero:", numero_entero)
print("Texto a entero:", texto_a_entero)
print("Booleano a entero:", booleano_a_entero)
print("Decimal:", decimal)
print("Texto a decimal:", texto_a_decimal)
print("Booleano a decimal:", booleano_a_decimal)
print("Entero a texto:", entero_a_texto)
print("Decimal a texto:", decimal_a_texto)
print("Booleano a texto:", booleano_a_texto)
print("Número a booleano:", numero_a_booleano)
print("Texto a booleano:", texto_a_booleano)
