print("\n")
print("=" * 20)
print("ESTRUCTURAS DE CONTROL ITERATIVO")
print("=" * 20)

print("\n")
print("=" * 20)
print("BUCLES FOR")
print("=" * 20)
print("\n")

frutas = ["manzana", "banana", "cereza"]
print(f"Lista de frutas: {frutas}")

for fruta in frutas:
    print(f"Fruta: {fruta}")
    
print("\n")
print("=" * 20)
print("RANGE")
print("=" * 20)
print("\n")

# Iterar de 0 a 4
for i in range(5):
    print(f"Número: {i}")
print("=" * 20)

# Iterar de 3 a 7 
for i in range(3,8):
    print(f"Número: {i}")
print("=" * 20)

# Iterar de 10 a 0 en pasos de -1   
for i in range(10,-1, -1): #Empieza en 10, con paso -1 y acaba en 0
    print(f"Número: {i}")
print("=" * 20)

print("\n")
print("=" * 20)
print("ITERAR SOBRE INDICES")
print("=" * 20)
print("\n")

nombres = ["Ana", "Luis", "Carlos"]
print(f"Lista de nombres: {nombres}")

for i in range(len(nombres)):
    print(f"Posición {i}: Nombre: {nombres[i]}")
    
print("\n")
print("=" * 20)
print("OTRA FORMA DE HACER LO MISMO")
print("=" * 20)
print("\n")
nombres = ["Valeria", "Paco", "Pedro"]
print(f"Lista de nombres: {nombres}")
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: Nombre: {nombre}")
    
print("\n")
print("=" * 20)
print("BUCLES WHILE")
print("=" * 20)
print("\n")
#Bucle indeterminado, porque se ejecuta en base a condiciones por lo que
#no sabemos cuántas veces se va a ejecutar.
#Ideal para crear aplicaciones de consola (CLI "Command Line Interface" apps.)

contador = 0
while contador < 10:
    print(f"Contador: {contador}")
    contador += 1  # Incrementar el contador para evitar un bucle infinito

print("=" * 20)
print("\n")
print("BUCLES WHILE INFINITO")
print("=" * 20)
print("\n")
#Ideal para crear aplicaciones de consola (CLI "Command Line Interface" apps.)
#Bucle infinito, porque la condición siempre es True.
#Salimos del bucle cuando el usuario escriba "salir"
#Es indeterminado porque no sabemos cuándo el usuario va a escribir "salir"

while True:
    print("""Welcome to the app
            1. Mostrar Todos los Productos
            2. Mostrar un Producto
            3. Salir - Salir de la aplicación
            """)
    opcion = input("Introduce una opción:").lower()
    print(f"Has elegido la opción: {opcion}")
        
    if opcion == "3" or opcion == "salir":
        print("Saliendo de la aplicación...")
        break
    
print ("Fuera del bucle")
