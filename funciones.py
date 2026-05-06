def menu_calculadora():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Resto")
    print("6. Potencia")
    print("7. Salir")


def calcular(opt):
    
    
    if opt == 1:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1+num2
        return (resultado)


    elif opt == 2:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1-num2
        return (resultado)


    elif opt == 3:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1*num2
        return (resultado)


    elif opt == 4:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        while num2 == 0:
            print("No se puede dividir por cero.")
            num2 = int(input("Ingrese el segundo número nuevamente: "))
        resultado = num1//num2
        return (resultado)


    elif opt == 5:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        while num2 == 0:
            print("No se puede dividir por cero.")
            num2 = int(input("Ingrese el segundo número nuevamente: "))
        resultado = num1%num2
        return (resultado)


    elif opt == 6:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1**num2
        return (resultado)


    else:
        print("Opción no válida, intente nuevamente")

    

    
   