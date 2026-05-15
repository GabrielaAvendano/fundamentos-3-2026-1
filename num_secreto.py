from random import randint
secreto = randint(0,100)
intentos = []
i = 0
intentos.append(int(input(f"Ingrese un número: ")))
while intentos[i] != secreto:
    if intentos[i] == secreto:
        print("¡Adivinaste el número!")
    elif intentos[i] < secreto:
        print(f"{intentos[i]} es menor que el número secreto.")
        intentos.append(int(input(f"Ingrese un número: ")))
    else:
        print(f"{intentos[i]} es mayor que el número secreto.")
        intentos.append(int(input(f"Ingrese un número: ")))
    i += 1

print("¡Adivinaste el número!")