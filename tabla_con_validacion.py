num = int(input("Ingrese un número a multiplicar: "))

if num > 0:
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
        
else:
    print("El número debe ser mayor que cero.")
    