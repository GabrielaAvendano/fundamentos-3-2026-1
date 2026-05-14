cant_notas = int(input("Ingrese la cantidad de notas a promediar: "))
notas = []
suma = 0
for i in range(cant_notas):
    notas.append(float(input(f"Ingrese la nota número {i + 1}: ")))
    
for nota in notas:
    suma += nota

promedio = suma/len(notas)

if promedio >= 4.0:
    print("Aprueba con", round(promedio,2))
    
elif promedio < 4.0 and promedio >= 3.0:
    print("Habilita con", round(promedio,2))
    
else:
    print("Reprueba con", round(promedio,2))