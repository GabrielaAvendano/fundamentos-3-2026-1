print("#####Calculadora#####")
print("#" *20,"\n")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
opt = int(input("Ingrese una opción: "))

while opt != 5:
    numeros = []
    cant_numeros = 0
    
    match opt:
        case 1:
            print("Sumando.")
            suma = 0
            cant_numeros = int(input("Ingrese la cantidad de numeros a sumar: "))
            try:
                for i in range(0,cant_numeros):
                    num = int(input(f"Ingrese el {len(numeros) + 1} número: "))
                    numeros.append(num)
                    suma += num 
                print(f"El resultado de la suma es: {suma}\n")
            except ValueError:
                print("Por favor ingrese un número.")
                i = 0
                while i < cant_numeros:
                    num = int(input(f"Ingrese el {len(numeros) + 1} número: "))
                    numeros.append(num)
                    suma += num
                print(f"El resultado de la suma es: {suma}\n")

        case 2:
            print("Restando.")
            resta = 0
            cant_numeros = int(input("Ingrese la cantidad de numeros a restar: "))
            try:
                num = int(input(f"Ingrese el {len(numeros) + 1} número: "))
                numeros.append(num)
                resta = num
                for i in range(1,cant_numeros):
                    num = int(input(f"Ingrese el {len(numeros) + 1} número: "))
                    numeros.append(num)
                    resta -= num 
                print(f"El resultado de la resta es: {resta}\n")
            except ValueError:
                print("Por favor ingrese un número.")
                i = 0
                num = int(input(f"Ingrese el {len(numeros) + 1} número: "))
                numeros.append(num)
                if numeros == None:    
                    resta = num
                while i < cant_numeros:
                    num = int(input(f"Ingrese el {len(numeros) + 1} número: "))
                    numeros.append(num)
                    resta -= num
                print(f"El resultado de la resta es: {resta}\n")


        case 3:
            print("Multiplicando.")
            multiplicacion = 1
            cant_numeros = int(input("Ingrese la cantidad de numeros a multiplicar: "))
            try:
                for i in range(0,cant_numeros):
                    num = int(input(f"Ingrese el {len(numeros) + 1} número: "))
                    numeros.append(num)
                    multiplicacion *= num 
                print(f"El resultado de la multiplicación es: {multiplicacion}\n")
            except ValueError:
                print("Por favor ingrese un número.")
                i = 0
                while i < cant_numeros:
                    num = int(input(f"Ingrese el {len(numeros) + 1} número: "))
                    numeros.append(num)
                    multiplicacion *= num
                print(f"El resultado de la multiplicación es: {multiplicacion}\n")
        

        case 4:
            print("Dividiendo.")
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            resultado = num1 / num2
        case _:
            print("Opción inválida, intente nuevamente.")
            opt = int(input("Ingrese una opción:"))


    print("#####Calculadora#####")
    print("#" *20,"\n")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opt = int(input("Ingrese una opción: "))