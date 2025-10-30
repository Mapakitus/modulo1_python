


try:
    resultado = 10/0
    [].pop()
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except IndexError:
    print("La lista está vacía")
    
print("Fin del programa")


try:
    resultado = 10/0
    [].pop()
except Exception: #Esto captura todo
    print("Ha ocurrido un error")
    
