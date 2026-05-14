cant_edades = int(input("Ingrese la cantidad de edades a clasificar: "))
edades = []

for i in range(8):
    edades.append(float(input(f"Ingrese la edad número {i + 1}: ")))
    
for edad in edades:
    if edad < 12:
        print(f"{edad} -> niño.")
    elif edad >= 12 and edad < 18:
        print(f"{edad} -> adolescente.")
    elif edad >= 18 and edad < 60:
        print(f"{edad} -> adulto.")
    else:
        print(f"{edad} -> adulto mayor.")
