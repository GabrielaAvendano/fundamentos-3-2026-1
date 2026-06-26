ligeros = 0
pesados = 0
value_error = True
while value_error == True:
    try:
        
        cantidad_vehiculos = int(input("Ingrese la cantidad de vehículos a registrar: ")) #ValueError
        value_error = False
    except ValueError:
        print("¡Cantidad inválida! Ingrese un número entero positivo para continuar.")

value_error = True

while value_error == True:
    try:
        for i in range(cantidad_vehiculos):
            placa_vehiculo = input(f"Ingrese la placa del vehículo {i+1}: ").upper() #TypeError
            while len(placa_vehiculo) != 6 and " " not in placa_vehiculo:
                print("La placa del vehículo debe tener 6 caracteres y no contener espacios.")
                placa_vehiculo = input(f"Ingrese la placa del vehículo {i+1}: ").upper() #TypeError
            capacidad = int(input(f"Ingrese la capacidad del vehículo {i+1}: ")) #ValueError
            
            if capacidad > 55:
                pesados += 1

            else:
                ligeros += 1
        
        value_error = False
    except ValueError:
            print("¡Error logístico! Ingrese un número entero positivo para la capacidad de carga.")
            ligeros = 0
            pesados = 0
else:        
    print(f"¡La flota cuenta con {len(pesados)} vehículos Pesados y {len(ligeros)} vehículos Ligeros! ¡Rutas asignadas!")