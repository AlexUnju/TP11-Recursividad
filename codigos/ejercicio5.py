def imprimir_lista_recursivo(lista, indice=0):
    # Caso base: cuando el índice es igual a la longitud de la lista
    if indice == len(lista):
        return
    
    # Imprimir el elemento en el índice actual
    print(lista[indice])
    
    # Llamar recursivamente a la función para el siguiente índice
    imprimir_lista_recursivo(lista, indice + 1)

# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
print("Elementos de la lista:")
imprimir_lista_recursivo(lista)
