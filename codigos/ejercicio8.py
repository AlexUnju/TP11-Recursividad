def t_pascal(n):
    triangulo = []  # Lista para almacenar todas las filas del triángulo de Pascal
    
    for i in range(n):
        fila = [1]  # Comenzamos cada fila con un 1
        if i > 0:
            for j in range(1, i):
                fila.append(triangulo[i-1][j-1] + triangulo[i-1][j])
            fila.append(1)  # Terminamos cada fila con un 1
        triangulo.append(fila)
        # Imprimir la fila actual formateada como un triángulo
        print(" " * (n-i-1) + " ".join(map(str, fila)))

    return triangulo[n-1]

# Ejemplo de uso
n = 8
resultado = t_pascal(n)
print("\nResultado:", resultado)
