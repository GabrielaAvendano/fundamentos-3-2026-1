precio_base = 2000

horas = int(input("Ingrese las horas ocupadas: "))
tipo_vehiculo = int(input("Ingrese el tipo de su vehículo: "))

if horas > 12:
    print("Máximo 12 horas.")

elif horas >= 3 and tipo_vehiculo == 1:
    total = precio_base * 0.90 * horas
    print(f"Total: ${round(total)} (10% desc.)")

elif tipo_vehiculo == 2:
    total = precio_base * 0.50 * horas
    print(f"Total: ${round(total)} (50% desc.)")

elif tipo_vehiculo == 3:
    total = precio_base * 1.30 * horas
    print(f"Total: ${round(total)} (30% recarga)")

elif horas < 3 and tipo_vehiculo == 1:
    total = precio_base * horas
    print(f"Total: ${round(total)}")
