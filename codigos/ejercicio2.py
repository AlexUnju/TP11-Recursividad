import random

def jugar(guess, intento):
    """
    Función recursiva para simular el juego de adivinanza.
    
    Args:
    - guess (int): Número generado aleatoriamente que el usuario debe adivinar.
    - intento (int): Contador de intentos realizados por el usuario.
    """
    nro = int(input("Ingrese número: "))  # Usuario ingresa un número para adivinar
    
    if guess != nro:  # Si el número ingresado no es igual al número a adivinar
        if intento < 3:  # Si aún quedan intentos disponibles (máximo 3)
            print("Fallaste")  # Informar al usuario que falló
            intento += 1  # Incrementar el contador de intentos
            print("Intentos restantes:", 3 - intento)  # Mostrar intentos restantes
            jugar(guess, intento)  # Llamar recursivamente para continuar el juego
        else:  # Si se agotaron los 3 intentos permitidos
            print("El número es:", guess)  # Mostrar el número correcto
    else:  # Si el número ingresado es igual al número a adivinar
        print("¡Bien! Ganaste")  # Informar al usuario que ha ganado

# Principal
guess = random.randint(0, 10)  # Generar un número aleatorio entre 0 y 10
intento = 1  # Inicializar el contador de intentos en 1
print("Adivine un número entre 0 y 10")
jugar(guess, intento)  # Llamar a la función jugar para comenzar el juego

'''
● Identifique el bloque base y el bloque recursivo.
● Modifique el código de forma que muestre los intentos restantes.
● Realice la traza del algoritmo
● Identifique el comportamiento de los parámetros de la función jugar() en cada llamado.
● ¿Cuál es la condición de salida?
'''

