"""
Crea un sistema de gestión de empleados con tarjetas corporativas que implemente una relación one-to-one en Python.

Pasos a realizar:
Crear la clase Empleado con los siguientes atributos:

id: identificador único (entero)
nombre: nombre del empleado (cadena)
cargo: puesto de trabajo (cadena)
salario: salario anual (entero)
tarjeta: referencia a la tarjeta corporativa (inicializar como None)
Crear la clase TarjetaCorporativa con los siguientes atributos:

id: identificador único (entero)
numero: número de la tarjeta (cadena)
fecha_emision: fecha de emisión (cadena)
empleado_id: ID del empleado propietario (entero)
Crear objetos:

Un empleado: con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 4500
Una tarjeta: con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
Establecer la relación one-to-one:

Asignar la tarjeta al empleado
Verificar que cada empleado tiene una sola tarjeta y cada tarjeta pertenece a un solo empleado
Mostrar la información de ambos objetos y confirmar que la relación funciona correctamente.    

"""

print("=== EJERCICIO: RELACIÓN EMPLEADO-TARJETA CORPORATIVA ===\n")

# 1. Crear la clase Empleado con los atributos: id, nombre, cargo, salario
# El atributo 'tarjeta' debe inicializarse como None
class Empleado:
    def __init__(self, id, nombre, cargo, salario):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.tarjeta = None
        
print("=== CREANDO OBJETOS ===")

# 2. Crear la clase TarjetaCorporativa con los atributos: id, numero, fecha_emision, empleado_id

class TarjetaCorporativa:
    def __init__(self, id, numero, fecha_emision, empleado_id):
        self.id = id
        self.numero = numero
        self.fecha_emision = fecha_emision
        self.empleado_id = empleado_id
        
print("=== CREANDO OBJETOS ===")

# 3. Crear un empleado con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 45000
empleado1 = Empleado(1, "Alba Motacilla", "Desarrolladora", 45000)


# 4. Crear una tarjeta corporativa con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
tarjeta1 = TarjetaCorporativa(1, "TC001", "2025-01-15", 1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Asignar la tarjeta al empleado (relación one-to-one)
empleado1.tarjeta = tarjeta1


print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del empleado y su tarjeta
# Hay para mostrar:
# - Nombre del empleado
print(f"Nombre del empleado: {empleado1.nombre}")

# - Número de tarjeta
print(f"Número de tarjeta: {empleado1.tarjeta.numero}")

# - Fecha de emisión de la tarjeta
print(f"Fecha de emisión de la tarjeta: {empleado1.tarjeta.fecha_emision}")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-one
"""
Crea un sistema de gestión de empleados con tarjetas corporativas que implemente una relación one-to-one en Python.

Pasos a realizar:
Crear la clase Empleado con los siguientes atributos:

id: identificador único (entero)
nombre: nombre del empleado (cadena)
cargo: puesto de trabajo (cadena)
salario: salario anual (entero)
tarjeta: referencia a la tarjeta corporativa (inicializar como None)
Crear la clase TarjetaCorporativa con los siguientes atributos:

id: identificador único (entero)
numero: número de la tarjeta (cadena)
fecha_emision: fecha de emisión (cadena)
empleado_id: ID del empleado propietario (entero)
Crear objetos:

Un empleado: con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 4500
Una tarjeta: con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
Establecer la relación one-to-one:

Asignar la tarjeta al empleado
Verificar que cada empleado tiene una sola tarjeta y cada tarjeta pertenece a un solo empleado
Mostrar la información de ambos objetos y confirmar que la relación funciona correctamente.    

"""

print("=== EJERCICIO: RELACIÓN EMPLEADO-TARJETA CORPORATIVA ===\n")

# 1. Crear la clase Empleado con los atributos: id, nombre, cargo, salario
# El atributo 'tarjeta' debe inicializarse como None
class Empleado:
    def __init__(self, id, nombre, cargo, salario):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.tarjeta = None
        
print("=== CREANDO OBJETOS ===")

# 2. Crear la clase TarjetaCorporativa con los atributos: id, numero, fecha_emision, empleado_id

class TarjetaCorporativa:
    def __init__(self, id, numero, fecha_emision, empleado_id):
        self.id = id
        self.numero = numero
        self.fecha_emision = fecha_emision
        self.empleado_id = empleado_id
        
print("=== CREANDO OBJETOS ===")

# 3. Crear un empleado con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 45000
empleado1 = Empleado(1, "Alba Motacilla", "Desarrolladora", 45000)


# 4. Crear una tarjeta corporativa con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
tarjeta1 = TarjetaCorporativa(1, "TC001", "2025-01-15", 1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Asignar la tarjeta al empleado (relación one-to-one)
empleado1.tarjeta = tarjeta1


print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del empleado y su tarjeta
# Hay para mostrar:
# - Nombre del empleado
print(f"Nombre del empleado: {empleado1.nombre}")

# - Número de tarjeta
print(f"Número de tarjeta: {empleado1.tarjeta.numero}")

# - Fecha de emisión de la tarjeta
print(f"Fecha de emisión de la tarjeta: {empleado1.tarjeta.fecha_emision}")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-one
"""
Crea un sistema de gestión de empleados con tarjetas corporativas que implemente una relación one-to-one en Python.

Pasos a realizar:
Crear la clase Empleado con los siguientes atributos:

id: identificador único (entero)
nombre: nombre del empleado (cadena)
cargo: puesto de trabajo (cadena)
salario: salario anual (entero)
tarjeta: referencia a la tarjeta corporativa (inicializar como None)
Crear la clase TarjetaCorporativa con los siguientes atributos:

id: identificador único (entero)
numero: número de la tarjeta (cadena)
fecha_emision: fecha de emisión (cadena)
empleado_id: ID del empleado propietario (entero)
Crear objetos:

Un empleado: con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 4500
Una tarjeta: con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
Establecer la relación one-to-one:

Asignar la tarjeta al empleado
Verificar que cada empleado tiene una sola tarjeta y cada tarjeta pertenece a un solo empleado
Mostrar la información de ambos objetos y confirmar que la relación funciona correctamente.    

"""

print("=== EJERCICIO: RELACIÓN EMPLEADO-TARJETA CORPORATIVA ===\n")

# 1. Crear la clase Empleado con los atributos: id, nombre, cargo, salario
# El atributo 'tarjeta' debe inicializarse como None
class Empleado:
    def __init__(self, id, nombre, cargo, salario):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.tarjeta = None
        
print("=== CREANDO OBJETOS ===")

# 2. Crear la clase TarjetaCorporativa con los atributos: id, numero, fecha_emision, empleado_id

class TarjetaCorporativa:
    def __init__(self, id, numero, fecha_emision, empleado_id):
        self.id = id
        self.numero = numero
        self.fecha_emision = fecha_emision
        self.empleado_id = empleado_id
        
print("=== CREANDO OBJETOS ===")

# 3. Crear un empleado con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 45000
empleado1 = Empleado(1, "Alba Motacilla", "Desarrolladora", 45000)


# 4. Crear una tarjeta corporativa con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
tarjeta1 = TarjetaCorporativa(1, "TC001", "2025-01-15", 1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Asignar la tarjeta al empleado (relación one-to-one)
empleado1.tarjeta = tarjeta1


print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del empleado y su tarjeta
# Hay para mostrar:
# - Nombre del empleado
print(f"Nombre del empleado: {empleado1.nombre}")

# - Número de tarjeta
print(f"Número de tarjeta: {empleado1.tarjeta.numero}")

# - Fecha de emisión de la tarjeta
print(f"Fecha de emisión de la tarjeta: {empleado1.tarjeta.fecha_emision}")

print("\n=== RESULTADO FINAL ===")
print()
# 7. Verificar la relación one-to-one
# 7. Mostrar un mensaje confirmando la relación one-to-one
if empleado1.tarjeta is not None and empleado1.tarjeta.empleado_id == empleado1.id:
    print("✅ Relación one-to-one establecida correctamente.")
    print(f"El empleado {empleado1.nombre} posee la tarjeta {empleado1.tarjeta.numero}.")
else:
    print("❌ Error: la relación entre empleado y tarjeta no es válida.")
print("\n=== RESULTADO FINAL ===")






