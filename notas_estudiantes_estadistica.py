
#inicializar variables
contador_estudiantes = 0
suma_calificaciones = 0
calificacion_mas_alta = 1.0
calificacion_mas_baja = 7.0
nombre_mas_alta = ""
nombre_mas_baja = ""
acumulador_excelentes = 0 #6.0 - 7.0
acumulador_buenos = 0 #5.0 - 6.0
acumulador_aprobados = 0 #4.0 - 5.0
acumulador_reprobados = 0 #1.0 - 3.0
suma_notas_aprobadas = 0.0
suma_notas_reprobadas = 0.0

#ciclo para ingresar datos
continuar = True
while continuar:
    try:
        nombre = input("\nIngrese nombre del estudiante (o 'salir' para terminar)")

        if nombre.lower().strip() == "salir":
            continuar = False

        
        nombre_limpio = nombre.strip().title()

        if not nombre_limpio.replace(' ','').isalpha() or len(nombre_limpio) < 2:
            raise ValueError("El nombre solo debe contener letras y tener al menos 2 caracteres.")

        calificacion_str = input(f"Ingrese nota de {nombre_limpio} (1.0 a 7.0): ")
        calificacion = float(calificacion_str)

        if calificacion >= 1.0 and calificacion <= 7.0:
            calificacion = round(calificacion,1) 

            contador_estudiantes += 1
            suma_calificaciones += calificacion

            if calificacion > calificacion_mas_alta:
                calificacion_mas_alta = calificacion
                nombre_mas_alta = nombre_limpio

            if calificacion < calificacion_mas_baja:
                calificacion_mas_baja = calificacion
                nombre_mas_baja = nombre_limpio

            if calificacion >= 6.0 and calificacion <= 7.0:
                acumulador_excelentes += 1
                suma_notas_aprobadas += calificacion

                print(f"{nombre_limpio} registrado con nota: {calificacion} - EXCELENTE")

            elif calificacion >= 5.0 and calificacion <= 5.9:
                acumulador_buenos += 1
                suma_notas_aprobadas += calificacion

                print(f"{nombre_limpio} registrado con nota: {calificacion} - BUENO")

            elif calificacion >= 4.0 and calificacion <= 4.9:
                acumulador_aprobados += 1 
                suma_notas_aprobadas += calificacion

                print(f"{nombre_limpio} registrado con nota: {calificacion} - APROBADO")

            elif calificacion >= 1.0 and calificacion <= 3.9:
                acumulador_reprobados += 1
                suma_notas_reprobadas += calificacion

                deficit = 4.0 - calificacion
                print(f"{nombre_limpio} registrado con nota: {calificacion} - REPROBADO (faltaron {deficit:.1f} puntos para aprobar)")

            else:
                print(f"Error: La nota {calificacion} está fuera del rango chileno 1.0 a 7.0")

    except ValueError as e:
        print(f"Error de entrada: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


    if contador_estudiantes > 0 and suma_calificaciones > 0:
        print("\n" + "="*60)
        print("Resultados del análisis")
        print("="*60)

        promedio_general = suma_calificaciones/contador_estudiantes
        promedio_general = round(promedio_general,2)


        if (acumulador_aprobados + acumulador_buenos + acumulador_excelentes) > 0:
            total_aprobados = acumulador_aprobados + acumulador_buenos + acumulador_excelentes
            promedio_aprobados = round(suma_notas_aprobadas/total_aprobados,2)

        else:
            promedio_aprobados = 0

        print("\n--- Estadísticas generales ---")
        print(f"Total de estudiantes: {contador_estudiantes}")
        print(f"Suma total de notas: {suma_calificaciones:.2f}")
        print(f"Promedio general del grupo: {promedio_general}")

        if promedio_general >= 4.0 and promedio_general <= 7.0:
            print(f"Curso aprobado con promedio {promedio_general}")
            if promedio_general >= 5.0:
                print("¡Rendimiento sobresaliente! Promedio general sobre 5.0")
        elif promedio_general >= 3.0 and promedio_general < 4.0:
            print(f"Curso en riesgo con promedio {promedio_general} ({(4.0 - promedio_general):.1f} puntos para aprobar)")
        elif promedio_general >= 1.0 and promedio_general < 3.0:
            print(f"Curso reprobado con promedio {promedio_general}")
        

        print("\n---Notas extremas---")
        print(f"Nota más alta: {calificacion_mas_alta} ({nombre_mas_alta})")
        print(f"Nota más baja: {calificacion_mas_baja} ({nombre_mas_baja})")

        print("\n---Distribución de rendimiento---")
        print(f"Excelentes (6.0 - 7.0): {acumulador_excelentes} estudiantes")
        print(f"Buenos (5.0 - 6.0): {acumulador_buenos} estudiantes")
        print(f"Aprobados mínimos (4.0 - 5.0): {acumulador_aprobados} estudiantes")
        print(f"Reprobados (1.0 - 3.9): {acumulador_reprobados} estudiantes")

        porcentaje_excelentes = (acumulador_excelentes*100)/contador_estudiantes
        porcentaje_buenos = (acumulador_buenos*100)/contador_estudiantes
        porcentaje_aprobados = (acumulador_aprobados*100)/contador_estudiantes
        porcentaje_reprobados = (acumulador_reprobados*100)/contador_estudiantes
        porcentaje_aprobacion_total = (total_aprobados*100)/contador_estudiantes

        print("\n---Porcentajes---")
        print(f"Excelentes: {porcentaje_excelentes:.1f}%")
        print(f"Buenos: {porcentaje_buenos:.1f}%")
        print(f"Aprobados: {porcentaje_aprobados:.1f}%")
        print(f"Reprobados: {porcentaje_reprobados:.1f}%")
        print(f"Tasa de aprobación total: {porcentaje_aprobacion_total:.1f}%")

        print("\n"+"="*60)
        print("---Evaluación final---")
        print("="*60)

        if promedio_general >= 4.0 and porcentaje_aprobacion_total >= 70:
            print("¡Rendimiento exitoso! El curso cumple con los estándares")
            print("Tasa de aprobción superior al 70% y promedio sobre 4.0")
        elif promedio_general >= 4.0 and porcentaje_aprobacion_total < 70:
            print("Rendimiento aceptable, pero con alta tasa de reprobación")
            print("Promedio sobre 4.0, pero menos del 70% de aprobación")
        elif promedio_general < 4.0 and porcentaje_aprobacion_total < 50:
            print("¡Rendimiento crítico! Curso en situación de riesgo académico")
            print("Promedio bajo 4.0 y menos del 50% de aprobación")
        else:
            print("Rendimiento regular - Se recomienda plan de mejora")

        if acumulador_excelentes > 0 or acumulador_buenos > 3:
            print("\nHay estudiantes con rendimiento destacado en el curso")

        if acumulador_reprobados > 0 and acumulador_reprobados > (acumulador_buenos + acumulador_excelentes):
            print("\nADVERTENCIA: Hay más reprobados que estudiantes con buen rendimiento")

        if contador_estudiantes > 0 and promedio_general < 4.0:
            puntos_faltantes = (4.0 * contador_estudiantes) - suma_calificaciones
            print(f"\nPara alcanzar el 4.0 como curso, se necesitan {puntos_faltantes:.1f} puntos adicionales")
        elif contador_estudiantes <= 0 and promedio_general < 4.0:
            print("\nNo se registró ningún estudiante válido")
        
        #ignoré todo lo que evalué innecesario para el programa