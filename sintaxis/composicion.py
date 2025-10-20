"""
Uno a Uno (One to One):
    Un ciudadano español tiene UN DNI. Y ese DNI pertenece sólo a UN ciudadano español.
"""
#Crear las clases
class Ciudadano:
    def __init__(self, id, nombre, apellido, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = None
        
class DNI:
    def __init__(self, id, numero):
        self.id = id
        self.numero = numero
        
#Crear los objetos
ciudadano1 = Ciudadano(1, "Paco", "Gutiérrez", 47)
dni1 = DNI(1, "12345678A")

#Asignar la referencia
#asignar como atributo dni de ciudadano1 el valor de dni1
ciudadano1.dni = dni1

print(ciudadano1.id)
print(ciudadano1.nombre)
print(ciudadano1.apellido)
print(ciudadano1.edad)
print(ciudadano1.dni.numero)
        
"""
Uno a Muchos (One to Many):
    Una categoría puede tener MUCHOS productos. Y un producto sólo puede pertenecer a UNA categoría.
"""
#Crear las clases
class Categoria:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []
   
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        
        
#Crear los objetos
categoria1 = Categoria(1, "Electrónica", "Dispositivos electrónicos")
categoria2 = Categoria(2, "Ropa", "Ropa y accesorios")

producto1 = Producto(1, "Laptop", 1200)
producto2 = Producto(2, "Teclado", 75)
producto3 = Producto(3, "Monitor", 300)
producto4 = Producto(4, "Chaqueta", 80.00)

#Asignar la referencia
categoria1.productos.append(producto1)
categoria1.productos.append(producto2)
categoria1.productos.append(producto3)
categoria2.productos.append(producto4)

#Relación bidireccional, ambas conocen de la otra----
class Categoria:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = [] #Lista de productos
   
class Producto:
    def __init__(self, id, nombre, precio, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria #Agregamos referencia a categoria
        
categoria1 = Categoria(1, "Electrónica", "Dispositivos electrónicos")
categoria2 = Categoria(2, "Ropa", "Ropa y accesorios")

producto1 = Producto(1, "Laptop", 1200, categoria1)
producto2 = Producto(2, "Teclado", 75, categoria1)
producto3 = Producto(3, "Monitor", 300, categoria1)
producto4 = Producto(4, "Chaqueta", 80.00, categoria2)



"""
Muchos a Uno (Many to One):
    Un profesor trabaja en UN departamento. Y ese departamento puede tener MUCHOS profesores.
"""
#departamento: id, nombre, ubicacion

class Departamento:
    def __init__(self, id, nombre, ubicacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion

class Profesor:
    def __init__(self, id, nombre, especialidad, departamento):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.departamento = departamento
        
#Crear los objetos
departamento1 = Departamento(1, "Natemáticas", "Edificio A1")
profesor1 = Profesor(1, "Paco Gutiérrez", "Informática", departamento1)
profesor2 = Profesor(2, "Bacterio", "Biología", departamento1)


"""
Muchos a muchos (Many to Many):
    Un estudiante pueden tener MUCHAS asignaturas. Cada asignatura puede tener MUCHOS estudiantes.
"""

class Estudiante:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.asignaturas = [] #Lista de asignaturas
        
class Asignatura:
    def __init__(self, id, nombre, creditos):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.estudiantes = [] #Lista de estudiantes
        
#Crear tabla intermedia
class EstudianteAsignatura:
    def __init__(self, estudiante_id, asignatura_id, nota):
        self.estudiante = estudiante_id
        self.asignatura = asignatura_id
        self.nota = nota
        
#Crear los objetos
estudiante1 = Estudiante(1, "Paco", 47)
estudiante2 = Estudiante(2, "Ana", 30)

asignatura1 = Asignatura(1, "Matemáticas", 6)
asignatura2 = Asignatura(2, "Historia", 3)

#Relaciones
estudiante1.asignaturas = [asignatura1, asignatura2]
estudiante2.asignaturas = [asignatura1]

asignatura1.estudiantes = [estudiante1, estudiante2]
asignatura2.estudiantes = [estudiante1]

relaciones = [
    EstudianteAsignatura(1, 1, 8.5),
    EstudianteAsignatura(1, 2, 6.0),
    EstudianteAsignatura(2, 1, 7.5)
]
