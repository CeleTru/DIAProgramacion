def contar_pares_impares(numeros):
    pares = []
    impares = []
    suma_pares = 0

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
            suma_pares += numero
        else:
            impares.append(numero)

    return pares, impares, suma_pares

# Obtener los números del usuario
numeros = []
for i in range(4):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

# Llamar a la función y obtener los resultados
resultado_pares, resultado_impares, resultado_suma_pares = contar_pares_impares(numeros)

# Mostrar los resultados
print("Cantidad de números pares:", len(resultado_pares))
print("Números pares ingresados:", resultado_pares)
print("Cantidad de números impares:", len(resultado_impares))
print("Números impares ingresados:", resultado_impares)
print("Sumatoria de números pares:", resultado_suma_pares)