n = int(input(""))
suma_pares = 0

for i in range(1, n+1):
    if i % 2 == 0:
        suma_pares += i

print(f"La suma de los números pares es: {suma_pares}")