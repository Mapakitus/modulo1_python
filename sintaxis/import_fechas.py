print("\n")
print("=" * 20)
print("OPERACIONES CON FECHAS")
print("=" * 20)

import datetime 

#date para fechas sin tiempo
fecha_actual = datetime.date.today()
print(f"Fecha actual: {fecha_actual}")

# datetime para fecha con tiempo:
ahora = datetime.datetime.now()
print(f"Hora actual: {ahora}")

#time solo tiempo:
tiempo = datetime.time(10, 30)
print(f"Hora actual: {tiempo}")