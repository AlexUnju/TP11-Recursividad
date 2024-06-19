def fibonacci_iterativo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Inicializamos la lista con los primeros dos términos de Fibonacci
    fibo_list = [0, 1]
    
    # Iteramos para generar los términos restantes
    for i in range(2, n):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    
    return fibo_list

# Ejemplo de uso
n = 10
fibonacci_n = fibonacci_iterativo(n)
print(f"Los primeros {n} términos de la sucesión de Fibonacci son: {fibonacci_n}")
