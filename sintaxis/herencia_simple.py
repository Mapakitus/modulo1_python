"""
La herencia permite que una clase (llamada clase hija o subclase)
adquiera los atributos y métodos de otra clase (llamada clase padre o superclase).
"""



# clase Padre o Superclase
class Animal:
    def __init__(self, edad):
        self.edad = edad

#Clase hija o subclase de Animal y es también clases padre de Gato       
class Felino(Animal):
    def __init__(self, edad, ronrroneo):
        super().__init__(edad)
        pass
 
 #Clase hija o subclase de Felino    
class Gato(Felino):
    def __init__(self, edad, ronrroneo, nombre):
       pass

#Clase hija o subclase de Animal    
class Tigre(Felino):
    def __init__(self, edad, ronrroneo, rayas):
       pass

#Clase hija o subclase de Animal
class Ave(Animal):
    def __init__(self, edad, plumas):
        super().__init__(edad)
        self.plumas = plumas
    pass

#Clase hija o subclase de Ave 
class Mirlo(Ave):
    def __init__(self, edad, plumas, canto):
        pass
