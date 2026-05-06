n = int(input("Ingrese la cantidad de números de la secuencia que desea generar: "))

a = 0
b = 1
contador = 0
nth = 0

if n <= 0:
    print("Por favor ingrese un número entero positivo.")

elif n == 1:
    print("Secuencia Fibonacci: ")
    print(a)

else: 
    print("Secuencia Fibonacci: ")
    while contador < n:
        print(nth, end=" ")
        nth = a + b
        a = b
        b = nth
        contador += 1
        #print(nth, end=" ")

