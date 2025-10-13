"""
Listas: [] o list()

* Una lista es una colección ordenada y mutable de elementos.
* Se definen usando corchetes [] o la función list().
* Pueden contener elementos de diferentes tipos de datos.
* Soportan operaciones como agregar, eliminar, y modificar elementos.
* Se accede a los elementos mediante índices (comenzando en 0).

Métodos relevantes:

* Longitud: len(): Devuelve el número de elementos en la lista.
* Acceso a elementos: 
    * Primero: nombres[0]
    * Último: nombres[-1]
    * IndexError: list index out of range. (Si ponemos un índice fuera del rango)
* Slicing: 
    * nombres[1:3] (desde el índice 1 hasta el 3, sin incluir el 3)
* Mutar un elemento mediante asignación:
    * precios[0] = precios[0] * 1.21 (modifica el primer elemento)
    
CRUD: (Create, Read, Update, Delete)
    
* Añadir o combinar:
    * append(): Añade un elemento al final de la lista.
        nombres.append("Lucía")
    * extend(): Añade múltiples elementos al final de la lista.
        nombres.extend(["Lucía", "Sofía"])
    * insert(): Inserta un elemento en una posición específica.
        nombres.insert(1, "Lucía") (inserta "Lucía" en la posición 1)
    * +: Combina dos listas.
        nombres = nombres + ["Lucía", "Sofía"]
    * *=: Repite la lista un número específico de veces.
        nombres *= 2 (duplica la lista)

* Eliminar:
    * pop(): Elimina y devuelve el último elemento
    * pop(0): Elimina y devuelve el primer elemento
        
    * remove(): Elimina la primera aparición de un valor específico.
        nombres = ["Ana", "Luis", "Carlos", "María", "Luis"]
        nombres.remove("Luis") (elimina el primer "Luis", pero sigue el segundo)
    * del: Elimina un elemento en una posición específica.
        del nombres[1] (elimina el elemento en la posición 1)
    * clear(): Elimina todos los elementos de la lista.
        nombres.clear() (deja la lista vacía, pero sigue existiendo)

* Recorrer:
    * for nombre in nombres: print(nombre)
    * enumerate(): Proporciona el índice y el valor al recorrer.
        for i, nombre in enumerate(nombres): print(i, nombre)
    * for i in range(len(nombres)): print(nombres[i])

* Buscar:
    * in: Verifica si un elemento está en la lista.
        if "Ana" in nombres: print("Ana está en la lista")
    * index(): Devuelve el índice de la primera aparición de un valor.
        indice = nombres.index("Carlos") (si no existe, lanza ValueError)
   
* Clonar:
    * lista_clon = nombres.copy()
    * lista_clon = nombres[:]
    * lista_clon = list(nombres)

* Ordenar:
    * sort(): Ordena la lista en su lugar.
        nombres.sort() (ordena alfabéticamente)
    * sorted(): Devuelve una nueva lista ordenada.
        nombres_ordenados = sorted(nombres) (no modifica la lista original)
    * reverse(): Invierte el orden de los elementos en la lista.
        nombres.reverse() (invierte la lista en su lugar)

* count(): Cuenta cuántas veces aparece un elemento en la lista.
    nombres.count("Luis") (devuelve 2 si "Luis" aparece dos veces)

        
    
"""
print("\n")
print("=" * 20)
print("DUPLICAR LISTA")
print("=" * 20)
nombres1 = ["Ana", "Luis", "Carlos", "María"]
nombres2 = ["Ana", "Luis", "Carlos", "María", "Paco"]
print(nombres1 * 2)

print()
print("\n")
print("=" * 20)
print("ACCEDER AL ÚLTIMO VALOR DE LISTA")
print("=" * 20)

ultimo_nombre = nombres1[-1]
print(ultimo_nombre)

print()

print("\n")
print("=" * 20)
print("ACCEDER A CIERTOS ÍNDICES LISTAS")
print("=" * 20)
numeros = [10, 20, 30, 40, 50, 60, 70]
primeros_tres = numeros[0:3]
print(primeros_tres)

print()

print("\n")
print("=" * 20)
print("ESTRUCTURAS DE CONTROL CONDICIONAL CON LISTAS")
print("=" * 20)
compras = ["leche", "pan", "huevos", "frutas"]

if "pan" in compras:
    print("Pan está en la lista de compras")
    
if "queso" not in compras:
    print("Necesito añadir queso a la lista")
    
print()

print("\n")
print("=" * 20)
print("LONGITUD DE LA LISTA")
print("=" * 20)
tareas = ["estudiar", "hacer ejercicio", "programar", "descansar"]

cantidad_tareas = len(tareas) #4
print(cantidad_tareas)

print("\n")
print("=" * 20)
print("POSICIÓN DENTRO DE LISTA")
print("=" * 20)
posicion = tareas.index("programar") #2

print()
print("\n")
print("=" * 20)
print("BUSCAR OCURRENCIAS EN LISTAS")
print("=" * 20)
letras = ["a", "b", "c", "a", "d", "a"]
ocurrencias_a = letras.count("a") #3
print(f"{ocurrencias_a} veces está la letra 'a'")

print()
print("\n")
print("=" * 20)
print("AÑADIR UN ELEMENTO AL FINAL DE UNA LISTA")
print("=" * 20)
tareas = ["estudiar", "ejercicio"]
tareas.append("programar")
print(tareas)

print("\n")
print("=" * 20)
print("AÑADIR UN ELEMENTO EN UNA POSICIÓN DE UNA LISTA")
print("=" * 20)
compras = ["pan", "huevos"]
compras.insert(1, "leche")
print(compras)

print()
print("\n")
print("=" * 20)
print("AÑADE ELEMENTOS DE OTRA LISTA AL FINAL")
print("=" * 20)

frutas = ["manzana", "plátano"]
mas_frutas = ["naranja", "uva"]
frutas.extend(mas_frutas)
print(frutas)  # ["manzana", "plátano", "naranja", "uva"]

print()

print("\n")
print("=" * 20)
print("AÑADE ELEMENTOS INDIVIDUALMENTE EN UNA LISTA")
print("=" * 20)

lista1 = [1, 2, 3]
lista2 = [4, 5]

# Con append, añade la lista completa como un único elemento
lista1.append(lista2)
print(lista1)  # [1, 2, 3, [4, 5]]

# Con extend, añade cada elemento individualmente
lista1 = [1, 2, 3]  # Reiniciamos la lista
lista1.extend(lista2)
print(lista1)  # [1, 2, 3, 4, 5]

print()

print("\n")
print("=" * 20)
print("ELIMINA LA PRIMERA OCURRENCIA")
print("=" * 20)

colores = ["rojo", "verde", "azul", "verde"]
colores.remove("verde")  # Elimina solo el primer "verde"
print(colores)  # ["rojo", "azul", "verde"]

print()

print("\n")
print("=" * 20)
print("ELIMINA Y DEVUELVE EL VALOR ELIMINADO DE UNA LISTA")
print("=" * 20)

numeros = [10, 20, 30, 40]
ultimo = numeros.pop()  # Elimina y devuelve 40
print(ultimo)  # 40
print(numeros)  # [10, 20, 30]

segundo = numeros.pop(1)  # Elimina y devuelve 20
print(segundo)  # 20
print(numeros)  # [10, 30]

print()

print("\n")
print("=" * 20)
print("VACÍA EL CONTENIDO DE UNA LISTA")
print("=" * 20)

mi_lista = [1, 2, 3, 4]
mi_lista.clear()
print(mi_lista)  # []

print()

print("\n")
print("=" * 20)
print("ELIMINA UN ELEMENTO O SECCIONES DE UNA LISTA")
print("=" * 20)

letras = ["a", "b", "c", "d"]
del letras[1]  # Elimina "b"
print(letras)  # ["a", "c", "d"]

# También puede eliminar secciones
numeros = [1, 2, 3, 4, 5]
del numeros[1:3]  # Elimina elementos en posiciones 1 y 2
print(numeros)  # [1, 4, 5]

print()

print("\n")
print("=" * 20)
print("ORDENAR LISTAS")
print("=" * 20)

numeros = [3, 1, 4, 2]
numeros.sort()
print(numeros)  # [1, 2, 3, 4]

# Orden descendente
numeros.sort(reverse=True)
print(numeros)  # [4, 3, 2, 1]

# Ordenar cadenas
palabras = ["zebra", "avión", "casa"]
palabras.sort()
print(palabras)  # ["avión", "casa", "zebra"]

print()

letras = ["a", "b", "c"]
letras.reverse()
print(letras)  # ["c", "b", "a"]

print("\n")
print("=" * 20)
print("COPIAR LISTAS")
print("=" * 20)

original = [1, 2, 3]
copia = original.copy()
copia.append(4)
print(original)  # [1, 2, 3] - No se modifica
print(copia)     # [1, 2, 3, 4]

print("\n")
print("=" * 20)
print("CONTAR O BUSCAR EN LISTAS")
print("=" * 20)

numeros = [1, 2, 2, 3, 2, 4]
ocurrencias = numeros.count(2)
print(ocurrencias)  # 3

print()

frutas = ["manzana", "plátano", "naranja", "plátano"]
posicion = frutas.index("plátano")
print(posicion)  # 1 (primera ocurrencia)

# Podemos especificar desde dónde empezar a buscar
posicion = frutas.index("plátano", 2)  # Busca desde posición 2
print(posicion)  # 3 (segunda ocurrencia)

print()

print("\n")
print("=" * 20)
print("RECORRER LISTAS")
print("=" * 20)

frutas = ["manzana", "plátano", "naranja", "uva"]

for fruta in frutas:
    print(f"Me gusta comer {fruta}")

tareas = ["estudiar", "hacer ejercicio", "programar"]

print("\n")
print("=" * 20)
print("RECORRER LISTAS SI NECESITAS LA POSICIÓN")
print("=" * 20)

#Empezaria en "tarea 0"
for indice, tarea in enumerate(tareas):
    print(f"Tarea {indice}: {tarea}")
print()
# Si queremos empezar en "tarea 1"
for indice, tarea in enumerate(tareas):
    print(f"Tarea {indice + 1}: {tarea}")
print()    
# Otra forma de comenzando desde 1 
# para una numeración más natural
for num, tarea in enumerate(tareas, 1):
    print(f"Tarea {num}: {tarea}")
print()

print("\n")
print("=" * 20)
print("RECORRER LISTAS AL REVÉS (REVERSE)")
print("=" * 20)

colores = ["rojo", "verde", "azul", "amarillo"]

# Opción 1: usando reversed()
for color in reversed(colores):
    print(color)

# Opción 2: usando índices negativos con range
for i in range(len(colores)-1, -1, -1):
    print(colores[i])

print("\n")
print("=" * 20)
print("RECORRER LISTAS CON COMPRENSIÓN")
print("=" * 20)

numeros = [1, 2, 3, 4, 5]

# Crear una nueva lista con los cuadrados
cuadrados = [num * num for num in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Filtrar solo los números pares
pares = [num for num in numeros if num % 2 == 0]
print(pares)  # [2, 4]

print()

print("\n")
print("=" * 20)
print("RECORRER VARIAS LISTAS A LA VEZ")
print("=" * 20)

nombres = ["Ana", "Carlos", "Elena"]
edades = [28, 32, 25]
ciudades = ["Madrid", "Barcelona", "Sevilla"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
