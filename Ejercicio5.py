import random

# Inicializar una lista para almacenar los números generados
numeros = []

# Ingresar 15 números aleatorios negativos con dos decimales
for _ in range(15):
    numero = round(random.uniform(-100, -0.01), 2)  # Generar número aleatorio negativo con dos decimales entre -100 y -0.01
    numeros.append(numero)

# Mostrar los números generados
print("Números generados:")
for numero in numeros:
    print(numero)

# Convertir los números a positivos con dos decimales
numeros_positivos = [round(abs(numero), 2) for numero in numeros]

# Mostrar los números convertidos a positivos con dos decimales
print("\nNúmeros convertidos a positivos:\n")
for numero in numeros_positivos:
    print(numero)