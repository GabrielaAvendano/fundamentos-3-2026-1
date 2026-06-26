peliculas = []

salir = False
while not salir:
    print("#####Películas#####")
    print("1. Guardar película")
    print("2. Mostrar películas")
    print("3. Buscar película")
    print("4. Editar película")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error, por favor ingrese solo números.")
    else:
        if opcion == 1:
            guardar_peli = input("Ingrese el nombre de la película: ").strip().lower()
            
            while guardar_peli == "":
                print("No puede guardar una película sin título, intente nuevamente.")
                guardar_peli = input("Ingrese el nombre de la película: ").strip().lower()

            peliculas.append(guardar_peli)
        elif opcion == 2:
            for posicion, pelicula in enumerate(peliculas):
                print(f"{posicion+1}) - {pelicula.title()}")

        elif opcion == 3:
            buscar_peli = input("Ingrese el nombre de la película a buscar: ").strip().lower()
            encontrado = False
            for posicion, pelicula in enumerate(peliculas):
                if pelicula == buscar_peli:
                    print("Película encontrada.")
                    print(f"{posicion + 1}) - {pelicula}")
                    encontrado = True
                
            if not encontrado:
                print("Busqueda sin éxito.")
        elif opcion == 4:
            if not peliculas:
                print("Lista vacía.")
                continue
            editar_peli = input("Ingrese el nombre de la película a editar: ").strip().lower()
            encontrado = False
            
            if editar_peli in peliculas:
                posicion = peliculas.index(editar_peli)
                print(f"Editando: {editar_peli}")

                nueva_peli = input("Nuevo nombre: ")
                while nueva_peli == "":
                    print("No puede guardar una película sin título, intente nuevamente.")
                    nueva_peli = input("Ingrese el nombre de la película: ").strip().lower()
                
                peliculas[posicion] = nueva_peli
                print(f"¡Ahora es {nueva_peli.title()}!")
            else:
                print("Película no encontrada.")
                    
        elif opcion == 5:
            salir = True
        else:
            print("Opción no controlada, intente nuevamente.")

print("Gracias por utilizar nuestro programa, hasta luego.")