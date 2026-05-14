numero_a_multiplicar = int(input("Ingrese un número a multiplicar: "))
resultado = 0

for numero_de_tabla in range(1,11):
    resultado = numero_a_multiplicar * numero_de_tabla
    print(f"{numero_a_multiplicar} * {numero_de_tabla} = {resultado}")
    
