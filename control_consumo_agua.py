normales = 0
altos = 0
cantidad_valida = False

#Pedir cantidad de viviendas
while not cantidad_valida:
    try:
        cantidad_viviendas = int(input("Ingrese la cantidad de viviendas a revisar: "))    
    except ValueError:
        print("Cantidad inválida, intente de nuevo.")
    else:
        cantidad_valida = cantidad_viviendas > 0
        if not cantidad_valida:
            print("Cantidad inválida, intente de nuevo.")

#Pedir identificador por vivienda
for i in range(cantidad_viviendas):
    identificador = input("Ingrese identificador: ").strip().upper()
    consumo_valido = False
    while not consumo_valido:
        try:
            consumo = float(input("Ingrese consumo en litros: "))
            consumo_valido = consumo >= 0
            if not consumo_valido:
                print("El conumo no puede ser menor a 0.")

        except ValueError:
            print("Ingrese un consumo válido.")
    
    consumo_normal = consumo <= 500
    if consumo_normal:
        normales += 1
    else:
        altos += 1

print(f"\nViviendas con consumo normal: {normales}")
print(f"Viviendas con consumo alto: {altos}")