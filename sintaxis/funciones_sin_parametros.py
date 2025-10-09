print("\n")
print("=" * 20)
print("FUNCIONES SIN PARÁMETROS")
print("=" * 20)
#Las funciones son una forma de crear bloques de código reutilizables varias veces.
#Las funciones sin parámetros son aquellas que no reciben ningún valor de entrada.
#Se definen con la palabra reservada "def", seguida del nombre de la función y paréntesis.
#El código de la función va indentado (sangrado) dentro del bloque de la función.
#"pass" indica que no hay código todavia, se suele escribir cuanto estamos diseñando
#la función pero no hemos implementado el código todavía.
#Sin "pass" te obliga a escribir código dentro de la función ya que no puede estar vacía.
#Intentar que el nombre de la función sea descriptivo de lo que hace.

#Convención: nombres en minúsculas y palabras separadas por guiones bajos.
#is_x si devuelve boolean
#calculate_x si procesa o calcula algo
#get_x si obtiene o recupera algo
#set_x si establece o asigna algo
#print_x si imprime o muestra algo
#show_x si muestra o imprime algo
#find_x si busca o encuentra algo
#insert_x si inserta o añade algo
#update_x si actualiza o modifica algo
#save_x si guarda o almacena algo
#remove_x si elimina o borra algo
#add_x si añade o agrega algo
#delete_x si elimina o suprime algo


def is_adult():
    edad = int(input("Introduce tu edad: "))
    if edad >= 18:
        return True
    else:
        return False

print(is_adult())  # Llama a la función y muestra el resultado
print(is_adult())
print