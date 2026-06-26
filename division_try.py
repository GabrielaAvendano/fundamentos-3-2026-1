print("Programa que realiza una división.")

try:
    numerador = float(input("Ingrese el primer número: "))
    denominador = float(input("Ingrese el segundo número: "))

    resultado = numerador/denominador
except ValueError:
    print("Por favor ingrese un número.")
except ZeroDivisionError:
    print("No es posible dividir por cero.")

else:
    print(f"El resultado es: {resultado}")
finally:
    print("Operación realizada con éxito.")