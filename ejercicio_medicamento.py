med_base = 60000
despacho_base = 8000

opt = "N"
while opt != "Y":
    edad = int(input("Ingrese su edad: "))
    tramo = input("Ingrese su tramo (A, B, C o D): ").upper()

    while tramo not in "ABCD":
        print("Opción inválida,")
        tramo = input("ingrese su tramo (A, B, C o D): ").upper()

    descuento_med = 1
    descuento_despacho = 1

    if edad <= 30:
        if tramo == "A" or tramo == "B":
            descuento_med = 0.82
        elif tramo == "C" or tramo == "D":
            descuento_med = 0.88
        else: 
            print("Opción no válida.")
        print()

    elif edad > 30 and edad <= 60:
        if tramo == "A" or tramo == "B":
            descuento_med = 0.92
        elif tramo == "C" or tramo == "D":
            descuento_med = 1
        else: 
            print("Opción no válida.")
        print()

    elif edad > 60 and edad <= 90:
        print()

    else:
        print("Edad no controlada.")

    if tramo == "A" or tramo == "B":
        descuento_despacho = 0.90
    if edad >= 55:
        descuento_despacho = 0.95


    valor_final_med = med_base * descuento_med
    valor_final_despacho = despacho_base * descuento_despacho

    print(f"El valor del medicamento es: ${round(valor_final_med)}")
    print(f"El valor de despacho es: ${round(valor_final_despacho)}")

    opt = input("¿Desea salir? [Y/N]\n").upper()

    while opt not in "YN":
        opt = input("Opción inválida, ingrese Y o N: ").upper()