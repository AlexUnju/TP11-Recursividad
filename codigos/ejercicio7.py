def es_palindrome(cadena):
    # Caso base: una cadena vacía o de un solo carácter es siempre un palíndromo
    if len(cadena) <= 1:
        return True
    else:
        # Verificar si el primer y último caracter son iguales
        if cadena[0] == cadena[-1]:
            # Llamar recursivamente con la cadena sin el primer y último caracter
            return es_palindrome(cadena[1:-1])
        else:
            return False

# Ejemplos de uso
print(es_palindrome("aba"))    # True
print(es_palindrome("abba"))   # True
print(es_palindrome("abcba"))  # True
print(es_palindrome("aaa"))    # True
print(es_palindrome("ababa"))  # True
print(es_palindrome("hello"))  # False
print(es_palindrome("python")) # False
