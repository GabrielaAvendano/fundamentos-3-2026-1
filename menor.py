menor = None

for i in range(5): 
    num = float(input("Número: "))
    if menor is None or menor > num:
        menor = num

print(f"Menor: {menor}")