from random import randint

entradas = []
i = 0
cant_entradas = randint(1,10)
while i <= cant_entradas:
    entradas.append(randint(-100,100))
    i += 1

positivos = negativos = suma = 0
i = 0

while i < len(entradas) and entradas[i] != 0:
    if entradas[i] > 0:
        positivos += 1
    elif entradas[i] < 0:
        negativos += 1
    
    suma += entradas[i]
    i += 1


print(f"Suma: {suma}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")