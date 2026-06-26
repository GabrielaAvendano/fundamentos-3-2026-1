camaras_seguras = 0
camaras_alerta = 0

cant_camaras = 0
while cant_camaras == 0:
    try:
        cant_camaras = int(input("Ingrese la cantidad de cámaras a revisar: "))#ValueError
    except ValueError:
        print("Valor ingresado debe ser un número entero, intente nuevamente.")
    else:
        if cant_camaras <= 0:
            print("Valor ingresado debe ser mayor a cero.")

for camara in range(cant_camaras):
    codigo_valido = False
    while not codigo_valido:
        codigo_camara = input("Ingrese el código de la cámara: ").strip().upper()
        if len(codigo_camara) >= 4 and " " not in codigo_camara:
            codigo_valido = True
        else: 
            print("El código debe tener al menos 4 caracteres y no contener espacios.")
    
    temp_valida = False
    while not temp_valida:
        try:
            temp = float(input("Ingrese la temperatura de la cámara en grados celsios."))
        except ValueError:
            print("El valor de temperatura debe ser un número, intente nuevamente.")
        else:
            if temp <= 5 and temp >= 0:
                camaras_seguras += 1
            else:
                camaras_alerta += 1
            temp_valida = True
    
print(f"Cámaras seguras: {camaras_seguras}")
print(f"Cámaras en alerta: {camaras_alerta}")