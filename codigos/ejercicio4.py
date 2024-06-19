def encontrar_mayor(lista):
    # Caso base: lista vacía
    if not lista:
        return None
    
    # Caso base: lista con un solo elemento
    if len(lista) == 1:
        return lista[0]
    
    # Obtener el máximo del resto de la lista
    max_resto = encontrar_mayor(lista[1:])
    
    # Comparar el primer elemento con el máximo del resto
    return lista[0] if lista[0] > max_resto else max_resto

# Ejemplo de uso
lista = [5, 3, 9, 1, 7, 2] 
resultado = encontrar_mayor(lista)
print(f"El mayor elemento de la lista {lista} es: {resultado}")