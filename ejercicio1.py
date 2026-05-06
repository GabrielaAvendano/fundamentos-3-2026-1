from funciones import menu_calculadora
from funciones import calcular


menu_calculadora()

opcion = int(input("Ingrese una opción: "))
resultado = 0

while opcion != 7:
    
    print(f"El resultado es: {calcular(opcion)}")

    menu_calculadora()

    opcion = int(input("Ingrese una opción: "))


print("Fin del proceso, vuelva pronto.")


