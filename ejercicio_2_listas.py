colores = ["rojo", "verde", "azul", "negro"]

#colores.append("amarillo")
#colores.append("cyan")
#colores.append("magenta")
cant_valida = False
while not cant_valida:
    try:
        cantidad = int(input("Ingrese la cantidad de colores a agregar: "))
    except ValueError:
        print("Cantidad inválida, intente nuevamente")
    else:
        if cantidad > 0:
            cant_valida = True

for i in range(cantidad):
    color = ""
    color_validar = False
    while not color_validar:
        color = input("Ingrese un color: ").strip().lower()
        if len(color) >= 4 and " " not in color and color != "":
            color_validar = True
        else:
            print("Valor inválido, intente nuevamente")
        
    colores.append(color)

for indice, color in enumerate(colores):
    print(f"{indice+1} - {color}")

color_existe = False
while not color_existe:
    try:
        color = input("Ingrese un color: ").strip().lower()
    except ValueError:
        print("Color no encontrado, intente nuevamente")
    else:
        if color in colores:
            colores.remove(color)
            color_existe = True
    
for indice, color in enumerate(colores):
    print(f"{indice+1} - {color}")
    