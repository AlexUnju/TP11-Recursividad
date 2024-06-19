def potencia(b, n):
    # Caso base: b^0 = 1 para cualquier base b diferente de 0
    if n == 0:
        return 1
    
    # Calculamos b^(n/2)
    aux = potencia(b, n // 2)
    
    # Si n es par, b^n = aux * aux
    if n % 2 == 0:
        return aux * aux
    else:
        # Si n es impar, b^n = aux * aux * b
        return aux * aux * b

# Ejemplos de uso:
base = 2
exponente = 10
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

base = 3
exponente = 5
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")
