numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

try:
    resultado = numero1 // numero2
except ZeroDivisionError:
    while numero2 == 0:
        print("No es posible dividir por cero.")
        numero2 = int(input("Vuelva a ingresar el segundo número: "))
    resultado = numero1 // numero2
finally:
    print(f"El resultado de la división es: {resultado}")
        