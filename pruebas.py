"""

# Elimina numeros primos
lista = []

def esprimo(n):
    if n < 2:
        return " es primo"
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def eliminar_primos(lista):
    return[num for num in lista if not esprimo(num)]

entrada = input("Pon los numeros")

numeros = list(map(int, entrada.split(',')))

resultado = eliminar_primos(numeros)

print (f'Lista de numeros no primos {resultado}')


palabra = input("Que palabra quieres?")

reves = 0

for i in palabra:
    reves = palabra [::-1]



print (reves)

"""