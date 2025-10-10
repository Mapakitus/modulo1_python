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
   
        
    
"""

nombres = ["Ana", "Luis", "Carlos", "María"]
print(nombres)