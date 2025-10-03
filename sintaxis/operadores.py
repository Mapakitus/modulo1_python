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

print("\n")
print("=" * 20)
print("OPERADORES DE COMPARACIÓN")
print("=" * 20)
print("\n")

# Comparando precios de productos
precio_producto_a = 15
precio_producto_b = 10

es_mas_barato = precio_producto_b < precio_producto_a
print(f"¿El producto B es más barato que el A? {es_mas_barato}")  # True

# Verificando si tenemos suficiente dinero para una compra
dinero_disponible = 50
costo_total = 45

podemos_comprar = dinero_disponible >= costo_total
print(f"¿Tenemos suficiente dinero? {podemos_comprar}")  # True

# Comparando calificaciones
calificacion = 75
aprobado = calificacion >= 70
print(f"¿El estudiante aprobó? {aprobado}")  # True

# Verificando si un número es par
numero = 10
es_par = numero % 2 == 0
print(f"¿{numero} es un número par? {es_par}")  # True

# Comprobando si la respuesta es correcta
respuesta_usuario = "París"
respuesta_correcta = "París"
es_correcta = respuesta_usuario == respuesta_correcta
print(f"¿La respuesta es correcta? {es_correcta}")  # True

# Verificando si un usuario tiene acceso
nivel_acceso = 2
nivel_requerido = 3
tiene_acceso = nivel_acceso >= nivel_requerido
print(f"¿El usuario tiene acceso? {tiene_acceso}")  # False

# Comparando enteros y flotantes
print(f"5 == 5.0: {5 == 5.0}")  # True (Python compara el valor, no el tipo)

# Comparando cadenas (comparación lexicográfica)
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # True (comparación alfabética)
print(f"'apple' < 'Apple': {'apple' < 'Apple'}")  # False (las mayúsculas tienen menor valor ASCII)
print(f"'123' == 123: {'123' == 123}")  # False (diferentes tipos)

# Comparando booleanos con números
print(f"True == 1: {True == 1}")  # True
print(f"False == 0: {False == 0}")  # True
print(f"True > False: {True > False}")  # True (True es 1, False es 0)

# Verificando si un número está en un rango
edad = 25
es_adulto_joven = 18 <= edad < 30
print(f"¿Es un adulto joven? {es_adulto_joven}")  # True

# Equivalente a:
# es_adulto_joven = (18 <= edad) and (edad < 30)

# Verificando si una temperatura está en un rango confortable
temperatura = 22
es_temperatura_confortable = 20 <= temperatura <= 25
print(f"¿La temperatura es confortable? {es_temperatura_confortable}")  # True

# Verificando calificaciones
calificacion = 85
es_notable = 70 < calificacion <= 90
print(f"¿La calificación es notable? {es_notable}")  # True

# Comparando listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

# Igualdad de valor (==): ¿Tienen el mismo contenido?
print(f"lista1 == lista2: {lista1 == lista2}")  # True (mismo contenido)

# Igualdad de identidad (is): ¿Son el mismo objeto en memoria?
print(f"lista1 is lista2: {lista1 is lista2}")  # False (diferentes objetos)
print(f"lista1 is lista3: {lista1 is lista3}")  # True (mismo objeto)

# El operador 'is' compara identidad, no valor
a = 1000
b = 1000
print(f"a == b: {a == b}")  # True (mismo valor)
print(f"a is b: {a is b}")  # False (diferentes objetos)

# Nota: Para pequeños enteros (-5 a 256), Python puede reutilizar objetos
c = 5
d = 5
print(f"c is d: {c is d}")  # True (Python reutiliza pequeños enteros)


print("\n")
print("=" * 20)
print("OPERADORES ARITMÉTICOS")
print("=" * 20)
print("\n")

# Ejemplo: Requisitos para obtener un préstamo
ingresos_suficientes = True
buen_historial_crediticio = True

aprobacion_prestamo = ingresos_suficientes and buen_historial_crediticio
print(f"¿Préstamo aprobado? {aprobacion_prestamo}")  # True, ambas condiciones son verdaderas

# Ejemplo: Verificando si un número está en un rango
numero = 15
en_rango = numero > 10 and numero < 20
print(f"¿El número {numero} está entre 10 y 20? {en_rango}")  # True

# Ejemplo: Verificando requisitos para una oferta de trabajo
años_experiencia = 3
conoce_python = True
conoce_sql = False

cumple_requisitos = años_experiencia >= 2 and conoce_python and conoce_sql
print(f"¿Cumple todos los requisitos? {cumple_requisitos}")  # False (no conoce SQL)

# Ejemplo: Acceso a un evento
es_socio = False
tiene_invitacion = True

puede_entrar = es_socio or tiene_invitacion
print(f"¿Puede entrar al evento? {puede_entrar}")  # True, tiene invitación

# Ejemplo: Descuento en una tienda
es_cliente_frecuente = False
es_primera_compra = False
gasto_superior_100 = True

aplica_descuento = es_cliente_frecuente or es_primera_compra or gasto_superior_100
print(f"¿Aplica para descuento? {aplica_descuento}")  # True, por gasto superior a 100

# Ejemplo: Verificando si un producto no está disponible
disponible = False
no_disponible = not disponible
print(f"¿El producto no está disponible? {no_disponible}")  # True

# Ejemplo: Verificando si un número es impar
numero = 7
es_par = numero % 2 == 0
es_impar = not es_par
print(f"¿El número {numero} es impar? {es_impar}")  # True

# Ejemplo: Sistema de acceso a una aplicación
usuario_registrado = True
contraseña_correcta = True
cuenta_bloqueada = False

puede_acceder = usuario_registrado and contraseña_correcta and not cuenta_bloqueada
print(f"¿Puede acceder al sistema? {puede_acceder}")  # True

# Ejemplo: Elegibilidad para un programa
edad = 25
es_estudiante = False
ingresos_bajos = True

es_elegible = (edad < 30 and es_estudiante) or ingresos_bajos
print(f"¿Es elegible para el programa? {es_elegible}")  # True, por ingresos bajos

# Sin paréntesis (puede ser confuso)
resultado = True or False and False
print(f"Resultado sin paréntesis: {resultado}")  # True

# Con paréntesis (más claro)
resultado1 = True or (False and False)  # and se evalúa primero
print(f"Resultado con paréntesis (1): {resultado1}")  # True

resultado2 = (True or False) and False
print(f"Resultado con paréntesis (2): {resultado2}")  # False

# Ejemplo de cortocircuito con and
x = 5
# La segunda parte no se evalúa porque la primera es False
if x > 10 and x/0 > 1:  # No da error de división por cero
    print("Esto no se imprimirá")

# Ejemplo de cortocircuito con or
y = 20
# La segunda parte no se evalúa porque la primera es True
if y > 10 or y/0 > 1:  # No da error de división por cero
    print("Esto se imprimirá")

# Ejemplos con valores no booleanos
print(f"0 and 5: {0 and 5}")  # 0 (primer valor falso)
print(f"5 and 0: {5 and 0}")  # 0 (primer valor falso)
print(f"2 and 5: {2 and 5}")  # 5 (último valor, todos son verdaderos)

print(f"0 or 5: {0 or 5}")  # 5 (primer valor verdadero)
print(f"5 or 0: {5 or 0}")  # 5 (primer valor verdadero)
print(f"0 or '': {0 or ''}")  # '' (último valor, todos son falsos)

# Ejemplo: Sistema de recomendación de películas
le_gustan_accion = True
le_gustan_comedia = False
le_gustan_drama = True

pelicula_accion = "John Wick"
pelicula_comedia = "Superbad"
pelicula_drama = "El Padrino"
pelicula_accion_drama = "Gladiador"

# Recomendación basada en preferencias
if le_gustan_accion and le_gustan_drama:
    recomendacion = pelicula_accion_drama
elif le_gustan_accion:
    recomendacion = pelicula_accion
elif le_gustan_comedia:
    recomendacion = pelicula_comedia
elif le_gustan_drama:
    recomendacion = pelicula_drama
else:
    recomendacion = "No tenemos recomendaciones para ti"

print(f"Te recomendamos ver: {recomendacion}")  # Te recomendamos ver: Gladiador

# Ejemplo: Sistema de acceso a una aplicación
usuario_registrado = True
contraseña_correcta = True
cuenta_bloqueada = False

puede_acceder = usuario_registrado and contraseña_correcta and not cuenta_bloqueada
print(f"¿Puede acceder al sistema? {puede_acceder}")  # True

# Ejemplo: Elegibilidad para un programa
edad = 25
es_estudiante = False
ingresos_bajos = True

es_elegible = (edad < 30 and es_estudiante) or ingresos_bajos
print(f"¿Es elegible para el programa? {es_elegible}")  # True, por ingresos bajos

