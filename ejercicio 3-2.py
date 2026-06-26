print("¡Bienvenido al sistema de gestión de localidades del Teatro Municipal!")

localidades_disponibles = 200
ventas_netas = 0
print("#####Menú de opciones#####")
print("##########################")
print("1. Localidades disponibles")
print("2. Vender localidades")
print("3. Devolver localidades.")
print("4. Historial de ventas.")
print("5. Salir.")
try:
    opt = int(input("Ingrese una opción: "))#ValueError
except IndexError:
    print()
except TypeError:
    print()

ejecutando = True
while ejecutando:
    print("#####Menú de opciones#####")
    print("##########################")
    print("1. Localidades disponibles")
    print("2. Vender localidades")
    print("3. Devolver localidades.")
    print("4. Historial de ventas.")
    print("5. Salir.")
        
    try:
        opt = int(input("Ingrese una opción: "))#ValueError
        match opt:
            case 1:
                print(localidades_disponibles)
            case 2:
                cant_localidades_vender = int(input("Ingrese la cantidad de localidades a vender: "))
                while cant_localidades_vender < 0 or cant_localidades_vender > localidades_disponibles:
                    print("El número de localidades a vender debe ser mayor a cero y menor que la cantidad disponible: ")
                    cant_localidades_vender = int(input("Ingrese la cantidad de localidades a vender: "))
                localidades_disponibles -= cant_localidades_vender
                ventas_netas += cant_localidades_vender
            case 3:
                print()
                cant_localidades_devolver = int(input("Ingrese la cantidad de localidades a devolver: "))
                while cant_localidades_devolver < 0 or cant_localidades_devolver > 200:
                    print("El número de localidades por devolver debe ser mayor a cero y menor a la cantidad disponible inicial (200).")
                    cant_localidades_devolver = int(input("Ingrese la cantidad de localidades a devolver: "))
                localidades_disponibles += cant_localidades_devolver
                ventas_netas -= cant_localidades_devolver
            case 4:
                print(f"Historial de ventas hasta ahora: {ventas_netas}")
        
    except IndexError:
        print()
    except TypeError:
        print()


print("Gracias por utilizar nuestro software, hasta la próxima.")