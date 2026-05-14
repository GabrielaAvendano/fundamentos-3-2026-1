for num in range(1,21):
    if num % 2 == 0 and num % 5 == 0:
        print(num, "es par y múltiplo de 5.")
    elif num % 2 == 0:
        print(num, "es par.")
    elif num % 2 != 0 and num % 5 == 0:
        print(num, "es impar y múltiplo de 5.")
    else:
        print(num, "es impar.")