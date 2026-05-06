precio_base_m  = 30000
inscripcion = 10000

meses = int(input("Meses: "))
tipo_plan = int(input("Plan: "))

if meses >= 6 and (tipo_plan == 1 or tipo_plan == 2):
    if tipo_plan == 2:
        inscripcion = 0

    total = precio_base_m * meses * 0.85
    print(f"Mensualidad: ${total} Inscripción: ${inscripcion}")

elif meses >= 6 and tipo_plan == 3:
    inscripcion = 0

    total = precio_base_m * meses * 0.75
    print(f"Mensualidad: ${total} Inscripción: ${inscripcion}")

elif meses <= 5 and meses >= 3:
    if tipo_plan == 2 or tipo_plan == 3:
        inscripcion = inscripcion * 0.5

    total = precio_base_m * meses * 0.92
    print(f"Mensualidad: ${total} Inscripción: ${inscripcion}")

else:
    if tipo_plan == 2 or tipo_plan == 3:
        inscripcion = inscripcion * 0.5
    
    total = precio_base_m * meses
    
    print(f"Mensualidad: ${total} Inscripción: ${inscripcion}")

