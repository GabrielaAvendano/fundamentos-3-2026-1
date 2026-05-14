resultado = 0

try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    
    try: 
        resultado = numero1 // numero2
    except ZeroDivisionError:
        print("No es posible dividir por cero.")
        numero2 = int(input("Vuelva a ingresar el segundo número: "))
        
        resultado = numero1//numero2
        
except ValueError:
    print("Deben ingresarse valores numéricos.")
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    resultado = numero1 // numero2