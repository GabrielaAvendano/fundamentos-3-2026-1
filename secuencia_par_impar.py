num = int(input("Ingresa un número N: "))

print("Números pares: ")
for i in range(1, num + 1):
    if i % 2 == 0:
        print(i, end=" ")

    
print("\nNúmeros impares: ")
for i in range (1, num + 1):
    if i % 2 != 0:
        print(i, end=" ")

