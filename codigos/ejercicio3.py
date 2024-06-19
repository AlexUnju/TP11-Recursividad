def sumatoria(n):
    if n == 1:
        return 1
    else:
        return n + sumatoria(n - 1)

# Prueba de la función
n = int(input("Ingrese un número entero positivo: "))
resultado = sumatoria(n)
print(f"La sumatoria de los números desde 1 hasta {n} es: {resultado}")
