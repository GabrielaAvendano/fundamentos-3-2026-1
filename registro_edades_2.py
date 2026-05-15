edades = [0]
i = 0
menores = mayores = 0

while edades[i] != -1:
    if edades[i] < 18:
        menores += 1
    else:
        mayores += 1
    edades.append(int(input("Ingrese una edad: ")))
    i += 1

print(f"Menores de edad: {menores}")
print(f"Mayores de edad: {mayores}")