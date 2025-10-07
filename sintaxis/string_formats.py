print("\n")
print("=" * 20)
print("MÉTODOS DE FORMATEO DE STRINGS")
print("=" * 20)
print("\n")
#Muy útil para aplicaciones de consola y Logs. 

#Con una variable
precio = 50
descripcion = "El producto vale {} €"

print(descripcion.format(precio))
print("\n")
print("=" * 20)

#Con varias variables
cantidad = 3
id_producto = 236
precio = 54
descripcion = "El producto con ID: {} tiene un precio de {:.2f} € y hay {} unidades en stock"
print(descripcion.format(id_producto, precio, cantidad))
print("\n")
print("=" * 20)

#f-string es la forma moderna o rápida de formatear textos:
print("\n")
print(f"El producto con ID: {id_producto} tiene un precio de {precio:.2f} € y hay {cantidad} unidades en stock")