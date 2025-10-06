print("\n")
print("=" * 20)
print("ESTRUCTURAS DE CONTROL CONDICIONAL")
print("=" * 20)

print("\n")
print("=" * 20)
print("IF")
print("=" * 20)
print("\n")
    
edad = 20
print(f"Edad: {edad}")

if edad >= 18:
    print("Eres mayor de edad")

print("=" * 20)

edad = 16
print(f"Edad: {edad}")

if edad >= 18:
    print("Eres mayor de edad")
    

print("=" * 20)

temperatura = 30
print(f"Temperatura: {temperatura}°C")

if temperatura > 25:
    print("Hace calor")

print("=" * 20)

hora = 10
if hora >= 6 and hora < 12:
    print("Buenos días.")


print("\n")
print("=" * 20)
print("OPERADORES COMPARACIÓN")
print("=" * 20)
print("\n")

numero = 15
print(f"Número: {numero}")

if numero == 15:
    print("== El número es igual a 15")
    
if numero != 10:
    print("!= El número es distinto de 10")
    
if numero > 10:
    print("> El número es mayor que 10")
    
if numero < 20:
    print("< El número es menor que 20")
    
if numero >= 15:
    print(">= El número es mayor o igual que 15")

if numero <= 20:
    print("<= El número es menor o igual que 20")
    
print("\n")
print("=" * 20)
print("IF - ELSE")
print("=" * 20)
print("\n")

edad = 17
print(f"Edad: {edad}")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    

print("=" * 20)

numero = 15
print(f"Número: {numero}")

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
print("\n")
print("=" * 20)
print("IF - ELIF - ELSE")
print("=" * 20)
print("\n")

numero = 0
print(f"Número: {numero}")

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
    
print("=" * 20)
nota = 7.5
print(f"Nota: {nota}")
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")
    
print("\n")
print("=" * 20)
print("MATCH-CASE")
print("=" * 20)
print("\n")

fruta = input("Introduzca una fruta: ").lower()
print(f"Fruta: {fruta}")

match fruta:
    case "manzana":
        print("Has elegido una manzana")
    case "plátano":
        print("Has elegido un plátano")
    case "naranja":
        print("Has elegido una naranja")    
    case _:
        print("Fruta no disponible")
    
print("\n")
print("=" * 20)
print("IF ANIDADOS")
print("=" * 20)
print("\n")   
        
edad = 30
estado_civil = "soltero"
print(f"Edad: {edad}, Estado civil: {estado_civil}")

if (edad >= 18):
    if (estado_civil == "casado"):
        print("Eres mayor de edad y casado")
    else:
        print("Eres mayor de edad y soltero")
else:
    print("Eres menor de edad")
print("\n")

print("\n")
print("=" * 20)
print("CONDICIONAL TERNARIO")
print("=" * 20)
print("\n") 

edad = 17
print(f"Edad: {edad}")

mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)