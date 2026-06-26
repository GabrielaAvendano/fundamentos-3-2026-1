institucionales = 0
no_institucionales = 0

cantidad_valida = False
while not cantidad_valida:
    try:
        cant_correos = int(input("Ingrese la cantidad de correos a clasificar: "))

    except ValueError:
        print("Cantidad inválida.")

    else:
        cantidad_valida = cant_correos > 0
        if cantidad_valida == False:
            print("Cantidad inválida.")


for i in range(cant_correos):
    correo_valido = False
    while correo_valido == False:
        correo = input("Ingrese correo: ").strip().lower()
        correo_valido = "@" in correo and " " not in correo and len(correo) >= 6

        if correo_valido == False:
            print("Correo inválido.")

    es_institucional = correo.endswith("duoc.cl")
    if es_institucional:
        institucionales += 1
    else:
        no_institucionales += 1
    
print(f"\nInstitucionales: {institucionales}")
print(f"No institucionales: {no_institucionales}")

