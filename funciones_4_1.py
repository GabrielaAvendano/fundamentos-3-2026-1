def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar ticket")
    print("2. Buscar ticket")
    print("3. Eliminar ticket")
    print("4. Actualizar estado")
    print("5. Mostrar registros")
    print("6. Salir")

def leer_opcion():
    opcion = 0
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Ingrese una opción (1-6): "))
        except ValueError:
            print("Opción inválida, por favor ingrese sólo números.")
        else: 
            if opcion < 1 and opcion > 6:
                print("Opción inválida, intente nuevamente.")
                
    return opcion
    
def validar_asunto(valor):
    return valor.strip() != ""

def validar_impacto(valor):
    return 1 <= valor and valor <= 10

def validar_horas(valor):
    return valor > 0

def agregar_ticket(tickets):
    asunto = input("Asunto del ticket: ")
    
    try:
        impacto = int(input("Nivel de impacto: "))
        horas_estimadas = float(input("Horas estimadas de resolución: "))
    except ValueError:
        print("Por favor ingrese números.")
    
    if not validar_asunto(asunto):
        print("Error: No puede estar vacío ni compuesto sólo por espacios.")
    elif not validar_impacto(impacto):
         print("Error: Debe ser un número entre 1 y 10.")
    elif not validar_horas(horas_estimadas):
        print("Error: Debe ser mayor a 0.")
    else:
        nuevo_ticket = {
            "asunto":asunto.strip(),
            "impacto":impacto,
            "horas_estimadas":horas_estimadas,
            "escalado":False
        }
        tickets.append(nuevo_ticket)
        print("Ticket agregado correctamente.")

def buscar_ticket(tickets, dato_busqueda):
    posicion = -1
    i = 0

    while i < len(tickets) and posicion == -1:
        if tickets[i][asunto] == dato_busqueda:
            posicion = i
        i += 1

    return posicion

def eliminar_ticket(tickets):
    dato_busqueda = input("Ingrese el asunto del ticket a eliminar: ").strip()
    posicion = buscar_ticket(tickets,dato_busqueda)

    if posicion != -1:
        tickets.pop(posicion)
        print("Ticket eliminado correctamente.")
    else:
        print(f"El registro '{dato_busqueda}' no se encuentra registrado.")

def actualizar_estado(tickets):
    for ticket in tickets:
        if ticket["impacto"] >= 7:
            ticket["escalado"] = True
        else:
            ticket["escalado"] = False

def mostrar_registros(tickets):
    actualizar_estado(tickets)
    print("\n--- LISTA DE TICKETS ---")

    if len(tickets) == 0:
        print("No hay registros para mostrar.")
    else:
        for ticket in tickets:
            print(f"Asunto del ticket: {ticket["asunto"]}")
            print(f"Nivel de impacto: {ticket["impacto"]}")
            print(f"Horas estimadas de resolución: {ticket["horas_estimadas"]}")
            if ticket["escalado"]:
                print("Estado: ESCALADO")
            else:
                print("Estado: NORMAL")
            print("*"*50)
