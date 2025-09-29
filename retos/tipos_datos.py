# tipos de datos numéricos
age = 20
height = 1.80
price = 4.99
print(price)


# tipos de datos texto
nombre = 'Alan'
apellido = "Sastre"
telefono_movil = '666555444'
print(nombre + apellido)
print(nombre + " " + apellido)

# tipos de datos boolean
is_student = True
is_eligible = False

calificacion = 9

# Convenciones de nomenclatura:
# no empiecen por número
# formato snake_case
# no tenga espacios
# evitar caracteres especiales: ñ, acentos, símbolos
# si es constante lo solemos poner en MAYUSCULAS
DESCUENTO = 10
PI = 3.14
IVA = 21
DEFAULT_USERNAME = 'User'

calificacion = 9

telefono_movil = '666555444'



# Crear variables con diferentes tipos de datos en Python 
# y realizar conversiones entre ellos.

#Se pueden declarar las variables directamente sin especificar el tipo de dato
# Python es un lenguaje de tipado dinámico

nombre = "Paco"
apellido = "Gutiérrez"
edad = 47
estatura = 1.72
es_programador = True

print("Nombre:", nombre + " " + apellido)
print("Edad:", edad)
print("Estatura:", estatura)        
print("¿Es programador?:", es_programador)


#Tambien se pueden usar las funciones de conversión de tipos de datos
# Convertir a cadena de texto (str) o simplemente definir la variable como texto
#Aqui se define saludo como texto(string) y se concatena con las variables nombre y apellido

saludo = str("Hola, " + nombre + " " + apellido)
print(saludo)


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
