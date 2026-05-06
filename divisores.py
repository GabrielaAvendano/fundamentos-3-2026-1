num = int(input("Ingrese un número: "))
divisores = 0

for i in range(1, num+1):
    if num%i == 0:
        divisores += 1

    
print(f"Divisores: {divisores}")