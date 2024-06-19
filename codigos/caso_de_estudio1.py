
def pertenece(lista, numero):
    if lista == []: 
        return False
    else:
        if numero == lista[0]:
            return True
        else:
            return pertenece(lista[1:], numero)    

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else: 
        if exponente % 2 == 0: 
            pot = potencia(base, exponente/2)    
            return pot * pot
        else:
            pot = potencia(base, (exponente - 1)/2)    
            return pot * pot * base


lista = [1, 2, 3, 4, 5]
print("CE 01- Verificar si un Número pertenece a la lista")
print(lista)
n= int(input('Ingrese un nro: '))
print(n, ' pertenece a la lista?: ', pertenece(lista, n))

print("CE 02- Calcular la potencia de un número")
base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese exponente: '))
print('resultado: ', potencia(base, exponente))