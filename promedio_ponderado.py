nota1 = float(input("Ingrese la primera nota: "))
pond1 = float(input("Ingrese la ponderación de la primera nota (%): "))
nota2 = float(input("Ingrese la segunda nota: "))
pond2 = float(input("Ingrese la ponderación de la segunda nota (%): "))

promedio = nota1 * (pond1/100) + nota2 * (pond2/100)

print(f"Su promedio es {round(promedio, 2)}")