"""
Una clase es una plantilla o plano, el ADN de los objetos.    

* Las características (atributos): color, precio, raza, ID.

* Los comportamientos (métodos): arrancar, ladrar, iniciar sesión
    
"""

class Coche:
    #definimos atributos y métodos
    pass

mi_coche = Coche()
coche_de_amigo = Coche()


"""
Constructor: método especial que se ejecuta automáticamente cuando
creamos un nuevo objeto

El método __init__ se ejecuta automáticamente al crear el objeto
y sirve para dejar el objeto con datos iniciales

"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Carla", 50)

"""
El parámetro self es una referencia al objeto 
que se está creando o manipulando        
"""


class Libro:
    # atributos: titulo, autor, numero de paginas
    # metodos: abrir, leer, cerrar, subrayar
    def __init__(self, titulo, autor, numero_paginas=None):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.abierto = False
        
    def abrir(self):
        self.abierto = True
        print(f"Se ha abierto el {self.titulo}")
        
        
    def cerrar(self):
        self.abierto = False
        print(f"Se ha cerrado el {self.titulo}")

#libro_python = Libro()

libro_ficcion = Libro("El Hobbit", "J.R.R Tolkien", 322)

otro_libro = Libro("Cartomagia fundamental", "Vicente Canuto")

#Crear la clase Producto
class Producto:
    def __init__(self, nombre, precio=None, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

#Crear objetos Producto
laptop = Producto("Laptop HP Core-i7", 1200) #El stock será 0

teclado = Producto("Teclado mecánico Logitech", 80, 24)

print(laptop.stock)
print(teclado.stock)

#Crear clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = base * altura
        self.perimetro = 2 * (base + altura)
 
#Crear objeto rectangulo        
rectangulo = Rectangulo(5, 3)

print(rectangulo.area)
print(rectangulo.perimetro)

#Clase cuenta bancaria
class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        
        #Validación para que el saldo inicial sea como
        #mínimo 0 (no sea negativo)
        
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        
        self.saldo = saldo_inicial #Si pasa el if, puede inicializar
        
#crear objetos cuenta
cuenta_ana =Cuenta("Ana", 1000)

#Esto lanzará un ValueError
try:
    cuenta_problematica = Cuenta("Juan", -500)
except ValueError as e:
    print(f"ERROR: {e}")