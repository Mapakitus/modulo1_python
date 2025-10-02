print("\n")
print("=" * 20)
print("VARIABLES")
print("=" * 20)
print("\n")

edad = 25
nombre = "Ana"
altura = 1.68
es_estudiante = False

x = y = z = 10  # Múltiples asignaciones
print(f"Variables x, y, z: {x}, {y}, {z}")

nombre, edad, altura = "Luis", 30, 1.75  # Asignación múltiple con diferentes valores
print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}")

a = 5
b = 10
print(f"Antes del intercambio - a: {a}, b: {b}")
a, b = b, a  # Intercambio de valores
print(f"Después del intercambio - a: {a}, b: {b}")

print("\n")
print("=" * 20)
print("ASIGNACIÓN DE OPERDORES")
print("=" * 20)
print("\n")

contador = 0
print(f"Contador inicial: {contador}")
# contador = contador + 1
contador += 1  # contador = contador + 1
print(f"Contador después de incrementar: {contador}")

contador -= 2  # contador = contador - 2
print(f"Contador después de decrementar: {contador}")

precio = 100
precio *= 1.21  # precio = precio * 1.21 (aplicar IVA)
print(f"Precio con IVA: {precio}")
precio /= 2  # precio = precio / 2 (descuento del 50%)
print(f"Precio después de descuento: {precio}")


print("\n")
print("=" * 20)
print("ÁMBITO LOCAL Y GLOBAL")
print("=" * 20)
print("\n")

mensaje = "Hola, mundo!"  # Variable global
print(f"Variable global antes de la función: {mensaje}")
 
def saludar():
    nombre = "Marta"  # Variable local
    print(f"{mensaje}, {nombre}!")
    
saludar()

contador_global = 100  # Variable global
print(f"Contador global antes de la función: {contador_global}")

def incrementar():
    global contador_global
    contador = 0  # Variable local
    print(f"Contador local al inicio de la función: {contador}")
    contador += 1
    print(f"Contador dentro de la función +1: {contador}")
    contador_global += 1
    
incrementar() #Imprime: "Contador local: 1"

print(f"Contador global después de la función: {contador_global}") #Imprime: 101

print("\n")
print("=" * 20)
print("FUNCIONES ANIDADAS")
print("=" * 20)
print("\n")

def funcion_principal():
    variable = 1  
    
    def funcion_secundaria():
        print(variable)  # Accede a la variable de la función principal
    funcion_secundaria()
          
funcion_principal()  # Imprime: 1
