a = 0
b = 1


while a <= 100:
    if a % 2 == 0:
        print(f"{a} es par.")
    else:
        print(f"{a} es impar.")

    siguiente = a+b
    a = b
    b = siguiente


