import random

# Generar 10 números aleatorios del 1 al 1000 y guardarlos en numeros_ingresados
numeros_ingresados = []
for _ in range(10):
    numero_aleatorio = random.randint(1, 1000)
    numeros_ingresados.append(numero_aleatorio)

# Imprimir los números generados aleatoriamente
print("Números aleatorios generados:", numeros_ingresados)

# Calcular cantidad de números mayores y menores a 100
mayores_a_100 = 0
menores_a_100 = 0

for numero in numeros_ingresados:
    if numero > 100:
        mayores_a_100 += 1
    elif numero < 100:
        menores_a_100 += 1

# Obtener número máximo y mínimo de los números ingresados
numero_maximo = max(numeros_ingresados)
numero_minimo = min(numeros_ingresados)

# Imprimir resultados
print("Cantidad de números mayores a 100:", mayores_a_100)
print("Cantidad de números menores a 100:", menores_a_100)
print("Número máximo ingresado:", numero_maximo)
print("Número mínimo ingresado:", numero_minimo)