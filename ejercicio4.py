import random

# Inicializar una lista para almacenar los números generados
numeros = []

# Ingresar 10 números aleatorios reales con dos decimales
for _ in range(10):
    numero = round(random.uniform(-100, 100), 2)  # Generar número aleatorio real con dos decimales entre -100 y 100
    numeros.append(numero)

# Mostrar todos los números generados
print("Números generados:")
for numero in numeros:
    print(numero)

# Filtrar y mostrar solo los números positivos
numeros_positivos = [numero for numero in numeros if numero > 0]
sumatoria_positivos = round(sum(numeros_positivos), 2)

print("\nNúmeros positivos:")
for numero in numeros_positivos:
    print(numero)

# Mostrar la sumatoria de los números positivos con dos decimales
print("Sumatoria de números positivos:", sumatoria_positivos)