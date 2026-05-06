edad = int(input("Edad: "))

if edad < 12:
    print("Niño: pasa gratis")

elif edad >= 12 and edad <= 17:
    print("Adolescente: media tarifa")

elif edad >= 18 and edad < 65:
    print("Adulto: tarifa completa")

else:
    print("Adulto mayor: media tarifa")