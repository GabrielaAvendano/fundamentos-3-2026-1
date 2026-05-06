cant_notas = int(input("Ingrese cantidad de notas a registrar: "))
aprobadas = 0
for i in range(cant_notas):
    nota = float(input("Nota: "))
    if nota >= 4.0:
        aprobadas += 1
    
print(f"Notas aprobadas: {aprobadas}")
