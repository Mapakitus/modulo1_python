"""
    Diccionarios, equivalentes a mapas de claves con valores:
    
    Creación: {} o dict()
        diccionario = {"clave1": valor1, "clave2": valor2}

"""

customer = {
    "id": 1,
    "name": "John Doe", 
    "age": 30,
    "is_verified": True,
    "balance": 100.5,
    "tags": ["premium", "active"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip": "12345"
    }
    }

customer.update({"age": 31})  # Actualiza el valor de "age" a 31