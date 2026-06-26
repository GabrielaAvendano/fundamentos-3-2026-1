presentes = 0
ausentes = 0
tardios = 0

cantidad_estudiantes_valida = False
while not cantidad_estudiantes_valida:
    try:
        total_estudiantes = int(input("Ingrese la cantidad de estudiantes a registrar: "))
    except ValueError:
        print("Valor debe ser un número entero, intente nuevamente.")
    else:
        if total_estudiantes > 0:
            cantidad_estudiantes_valida = True
        else:
            print("Cantidad debe ser mayor a cero.")

for estudiante in range(total_estudiantes):
    nombre_valido = False
    while nombre_valido == False:
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        if len(nombre_estudiante) > 2:
            nombre_valido = True
        else:
            print("Nombre debe tener al menos 2 letras.")
    
    codigo_valido = False
    while not codigo_valido:
        codigo_asistencia = input("Ingrese asistencia del estudiante (P, A, T): ").strip().upper()
        if codigo_asistencia == "P":
            presentes += 1
        elif codigo_asistencia == "A":
            ausentes += 1
        elif codigo_asistencia == "T":
            tardios += 1



print(f"\nPresentes: {presentes}")
print(f"Ausentes: {ausentes}")
print(f"Atrasados: {tardios}")

