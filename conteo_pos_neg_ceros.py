cant_nums = int(input("Ingrese la cantidad de números a clasificar: "))
numeros = []
positivos = 0
negativos = 0
ceros = 0

for i in range(cant_nums):
    numeros.append(float(input(f"Ingrese el {i + 1} número: ")))
    
for n in numeros:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        ceros += 1
        

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")