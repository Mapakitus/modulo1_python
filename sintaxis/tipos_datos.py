# Convenciones de nomenclatura:
# no empiecen por número
# formato snake_case
# no tenga espacios
# evitar caracteres especiales: ñ, acentos, símbolos
# si es constante lo solemos poner en MAYUSCULAS


print("NÚMEROS ENTEROS")

edad = 20
temperatura_bajo_cero = -15
poblacion_mundial = 8_000_000_000

print(f"Edad: {edad}")
print(f"Temperatura bajo cero: {temperatura_bajo_cero}")
print(f"Población mundial: {poblacion_mundial}")

numeros_grande= 123456789012345678901234567890
print(f"Números grande: {numeros_grande}")
print(f"Números grande + 1: {numeros_grande +1}")

print("\n")
print("NÚMEROS DECIMALES (FLOAT)")
print("\n")

altura = 1.75
pi = 3.141592654
temperatura = 36.6

resultado_flotante = 0.1 + 0.2
print(f"Resultado flotante (0.1 + 0.2): {resultado_flotante}")
print(f"Resultado flotante redondeado: {round(resultado_flotante, 2)}")

import math
print(f"Resultado flotante usando math.isclose: {math.isclose(resultado_flotante, 0.3)}")

complejo = 3 + 4j
print(f"Número complejo: {complejo}")
print(f"Parte real: {complejo.real}")
print(f"Parte imaginaria: {complejo.imag}")
print(f"Módulo: {abs(complejo)}")

print("\n")
print("OPERACIONES BÁSICAS CON NÚMEROS")
print("\n")

suma = 5 + 3
resta = 5 - 3
multiplicacion = 5 * 3
division = 5 / 3
modulo = 5 % 3
exponente = 5 ** 3
division_entera = 5 // 3
valor_absoluto = abs(-7)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Módulo: {modulo}")
print(f"Exponente: {exponente}")
print(f"División entera: {division_entera}")
print(f"Valor absoluto: {valor_absoluto}")


redondeo_decimal = round(3.14159, 2)
print(f"Redondeo decimal: {redondeo_decimal}")

print("\n")
print("CONVERSIONES ENTRE TIPOS DE DATOS")
print("\n")

edad_aproximada = int(47.6)  # Convierte float a int (trunca)
print(f"Edad aproximada: {edad_aproximada}")

precio_exacto = float(20) # Convierte int a float
print(f"Precio exacto: {precio_exacto}")

cantidad = int("100") # Convierte str a int
medida = float("1.75") # Convierte str a float
print(f"Cantidad: {cantidad}") 
print(f"Medida: {medida}")  
 


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
