lista_animales = []
cantidad = 0

salir = False
while not salir:
    print("1. Ingrese la cantidad")
    print("2. Ingrese los nombres")
    print("3. Salir")
    
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Valor ingresado no válido, intente nuevamente")
    else:
        if opcion == 1:
            cantidad_valida = False
            while cantidad_valida == False:
                try:
                    cantidad = int(input("Ingrese la cantidad de animales que desea guardar: "))
                except ValueError:
                    print("Valor ingresado no válido: sólo se permiten números, intente de nuevo")
                else:
                    if cantidad > 0:
                        cantidad_valida = True
                    else: 
                        print("Cantidad debe ser mayor a cero.")
                    
        elif opcion == 2:
            if cantidad > 0:
                for i in range(cantidad):
                    formato_nombre = False
                    while formato_nombre == False:
                        nombre = input("Ingrese el nombre del animal: ").strip().lower()
                        if len(nombre) >= 3 and nombre != "":
                            lista_animales.append(nombre)
                            print("Nombre guardado.")
                            formato_nombre = True
                        else:
                            print("Formato de nombre inválido, intente de nuevo.")
            else:
                print("Cantidad de be ser ingresada en la primera opción primero.")
        
        elif opcion == 3:
            salir = True
        else:
            print("Opción inválida.")

print("Fin del programa.")