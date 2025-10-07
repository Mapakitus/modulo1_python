print("\n")
print("=" * 20)
print("OPERADORES ARITMÉTICOS")
print("=" * 20)
print("\n")

# Suma: Calculando el total de una compra
precio_manzanas = 3
precio_naranjas = 4
total_frutas = precio_manzanas + precio_naranjas
print(f"Total de la compra: {total_frutas} euros")  # Total de la compra: 7 euros

# Resta: Calculando el cambio a recibir
dinero_entregado = 20
precio_producto = 8
cambio = dinero_entregado - precio_producto
print(f"Su cambio es: {cambio} euros")  # Su cambio es: 7 euros

# Multiplicación: Calculando el precio total de varios artículos iguales
precio_unitario = 5
cantidad = 3
precio_total = precio_unitario * cantidad
print(f"Precio por {cantidad} unidades: {precio_total} euros")  # Precio por 3 unidades: 15 euros

# División normal: Siempre devuelve un float
pizza = 8 / 2
print(f"8 / 2 = {pizza}")  # 8 / 2 = 4.0

# División entre personas: Repartiendo una cuenta
cuenta_total = 85
personas = 4
pago_por_persona = cuenta_total / personas
print(f"Cada persona debe pagar: {pago_por_persona} euros")  # Cada persona debe pagar: 21.25 euros

# División entera: Útil cuando necesitamos solo la parte entera
horas_totales = 90
horas_por_dia = 24
dias_completos = horas_totales // horas_por_dia
print(f"Días completos: {dias_completos} días")  # Días completos: 3

# Módulo: Encontrando las horas restantes
horas_restantes = horas_totales % horas_por_dia
print(f"Horas restantes: {horas_restantes} horas")  # Horas restantes: 18

# Exponenciación: Calculando el área de un cuadrado
lado = 4
area = lado ** 2
print(f"El área del cuadrado es: {area} unidades cuadradas")  # El área del cuadrado es: 16 unidades cuadradas

# Calculando el volumen de un cubo
volumen = lado ** 3
print(f"El volumen del cubo es: {volumen} unidades cúbicas")  # El volumen del cubo es: 64 unidades cúbicas

# Calculando raíces usando exponentes fraccionarios
numero = 25
raiz_cuadrada = numero ** 0.5
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")  # La raíz cuadrada de 25 es: 5.0

# Raíz cúbica
numero = 27
raiz_cubica = numero ** (1/3)
print(f"La raíz cúbica de {numero} es: {raiz_cubica}")  # La raíz cúbica de 27 es: 3.0


# Ejemplo de precedencia (orden de operaciones)
resultado = 10 + 5 * 2
print(f"10 + 5 * 2 = {resultado}")  # 10 + 5 * 2 = 20 (la multiplicación se realiza primero)

# Usando paréntesis para modificar la precedencia
resultado_con_parentesis = (10 + 5) * 2
print(f"(10 + 5) * 2 = {resultado_con_parentesis}")  # (10 + 5) * 2 = 30

# Ejemplo práctico: Calculando el precio final con descuento e impuestos
precio_base = 100
descuento = 20
tasa_impuesto = 0.16

# Sin paréntesis (incorrecto): primero aplica el impuesto y luego resta el descuento
precio_final_incorrecto = precio_base * tasa_impuesto + precio_base - descuento
print(f"Precio final (cálculo incorrecto): {precio_final_incorrecto}")  # 116.0

# Con paréntesis (correcto): primero resta el descuento y luego aplica el impuesto
precio_final_correcto = (precio_base - descuento) * (1 + tasa_impuesto)
print(f"Precio final (cálculo correcto): {precio_final_correcto}")  # 92.8

# Entero + Entero = Entero
suma_enteros = 5 + 3
print(f"5 + 3 = {suma_enteros}, tipo: {type(suma_enteros)}")  # 5 + 3 = 8, tipo: <class 'int'>

# Entero + Float = Float
suma_mixta = 5 + 3.5
print(f"5 + 3.5 = {suma_mixta}, tipo: {type(suma_mixta)}")  # 5 + 3.5 = 8.5, tipo: <class 'float'>

# División siempre produce float, incluso con números enteros
division = 10 / 2
print(f"10 / 2 = {division}, tipo: {type(division)}")  # 10 / 2 = 5.0, tipo: <class 'float'>


# Problemas de precisión con números flotantes
resultado = 0.1 + 0.2
print(f"0.1 + 0.2 = {resultado}")  # 0.1 + 0.2 = 0.30000000000000004

# Solución: usar la función round() para redondear
resultado_redondeado = round(resultado, 2)
print(f"Redondeado a 2 decimales: {resultado_redondeado}")  # Redondeado a 2 decimales: 0.3

# Ejemplo práctico: Calculando el precio final con impuestos
precio_producto = 19.99
tasa_impuesto = 0.16
precio_con_impuesto = precio_producto * (1 + tasa_impuesto)
print(f"Precio con impuesto (sin redondear): {precio_con_impuesto}")  # 23.1884
print(f"Precio con impuesto (redondeado): {round(precio_con_impuesto, 2)}")  # 23.19

# Calculando el tiempo total de un viaje
distancia = 150  # km
velocidad_promedio = 60  # km/h
tiempo_horas = distancia / velocidad_promedio
tiempo_horas_enteras = distancia // velocidad_promedio
tiempo_minutos_adicionales = (tiempo_horas - tiempo_horas_enteras) * 60

print(f"Tiempo total: {tiempo_horas_enteras} horas y {round(tiempo_minutos_adicionales)} minutos")
# Tiempo total: 2 horas y 30 minutos

# Calculando el consumo de combustible
litros_combustible = 35
kilometros_recorridos = 420
consumo = kilometros_recorridos / litros_combustible

print(f"Consumo: {round(consumo, 2)} km/l")  # Consumo: 12.0 km/l

# Calculando el interés compuesto
capital_inicial = 1000  # euros
tasa_interes_anual = 0.05  # 5%
años = 3
capital_final = capital_inicial * (1 + tasa_interes_anual) ** años

print(f"Capital después de {años} años: {round(capital_final, 2)} euros")
# Capital después de 3 años: 1157.63 euros

