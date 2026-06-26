from funciones_4_1 import mostrar_menu, leer_opcion, agregar_ticket, buscar_ticket, eliminar_ticket, actualizar_ticket, mostrar_registros

tickets = []

salir = False
while not salir: 
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        agregar_ticket(tickets)
    elif opcion == 2:
        dato_busqueda = input("Ingrese el asunto del ticket a buscar: ").strip()
        posicion = buscar_ticket(tickets, dato_busqueda)

        if posicion != -1:
            print("Registro encontrado:")
            print(tickets[posicion])
        else:
            print("No se encontró el registro solicitado.")
    elif opcion == 3:
        eliminar_ticket(tickets)
    elif opcion == 4:
        actualizar_ticket(tickets)
        print("Estados actualizados correctamente.")
    elif opcion == 5:
        mostrar_registros(tickets)
    elif opcion == 6:
        salir = True

print("Gracias por utilizar nuestro sistema de soporte. Hasta luego.")