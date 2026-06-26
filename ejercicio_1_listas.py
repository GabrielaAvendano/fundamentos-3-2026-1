colores = ["rojo", "verde", "azul", "negro"]

color_a_buscar = input("Ingrese el color a buscar: ").strip().lower()
color_encontrado = False

for indice, color in enumerate(colores):
    if color_a_buscar == color:
        print(f"{indice+1} - {color}")
        color_encontrado = True
        break

if not color_encontrado:
    print(f"El color {color_a_buscar} no se encuentra en la lista")
