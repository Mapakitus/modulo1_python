"""
Usaremos try except para capturar errores y gestionarlos.

"""
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("No se ha podido hacer la división")


print("Fin del programa")
