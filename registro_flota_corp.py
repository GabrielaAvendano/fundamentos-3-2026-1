vehiculos_pesados = 0
vehiculos_ligeros = 0

cantidad_vehiculos_valida = False
while not cantidad_vehiculos_valida:
    try:
        total_vehiculos = int(input("Ingrese la cantidad de vehículosa registrar: "))
    except ValueError:
        print("Valor ingresado debe ser un número entero.")
    else:
        if total_vehiculos > 0:
            cantidad_vehiculos_valida = True
        else:
            print("Cantidad debe ser mayor a cero.")

for vehiculo in range(total_vehiculos):
    vehiculos_valido = False
    while not vehiculos_valido:
        placa_vehiculo = input("Ingrese la placa del vehículo: ")

        if " " not in placa_vehiculo and len(placa_vehiculo) >= 6:
            vehiculos_valido = True

        else:
            print("La placa del vehículo debe tener al menos 6 caracteres y no contener espacios.")
    
    capacidad_valida = False
    while not capacidad_valida:
        try:
            capacidad = int(input("Ingrese la capacidad del vehículo: "))
        except ValueError:
            print("Valor ingresado debe ser un número entero.")
        else:
            if capacidad > 55:
                vehiculos_pesados += 1
            else:
                vehiculos_ligeros += 1
    
print(f"\n¡La flota cuenta con {vehiculos_pesados} vehículos pesados y {vehiculos_ligeros} vehículos ligeros! ¡Rutas asignadas!")
