peliculas = [
    {
        "nombre":"rocky 1",
        "año":1976,
        "categoria":"drama"
        "reparto":[]
    },
    {
        "nombre":"titanic",
        "año":1998,
        "categoria":"romance"
        "reparto":[]
    },
    {
        "nombre":"alien 2",
        "año":1986
        "categoria":"terror"
        "reparto":[]
    }
]
    



salir = False
while not salir:
    print("1. Guardar película")
    print("2. Mostrar películas")
    print("3. Buscar película")
    print("4. Editar película")
    print("5. Eliminar película")
    print("6. Salir")
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error, por favor ingrese sólo números.")
    else:
        if opcion == 1:
            actores = []

            nombre_pelicula = input("Ingrese la película a guardar: ").strip().lower()
            año_pelicula = int(input("Ingrese el año de la película: "))
            categoria_pelicula = input("Ingrese la categoría: ").strip().lower()
            cantidad_actores = int(input("Ingrese la cantidad de actores a guardar: "))

            for cant in range(cantidad_actores):
                nombre_actor = input("Ingrese el actor: ").strip().lower()
                actores.append(nombre_actor)

            pelicula_dic = {
                "nombre":nombre_pelicula,
                "año":año_pelicula,
                "categoria":categoria_pelicula
                "reparto":actores 
            }

            peliculas.append(pelicula_dic)

            print("Película guardada con éxito.")

        elif opcion == 2:
            if not peliculas:
                print("No hay películas.")
                continue

            for posicion,pelicula in enumerate(peliculas,1):
                reparto_formateado = ", ".join([actor.title() for actor in pelicula["reparto"]])

                print(f"{posicion + 1} - {pelicula['nombre'].title()} {pelicula['año'].title()} - {pelicula['categoria'].title()}")
                print(f"Reparto: {reparto_formateado}")

        elif opcion == 3:
            pelicula_a_buscar = input("Ingrese la película a buscar: ").strip().lower()
            while pelicula_a_buscar == "":
                print("No se aceptan vacíos, intente nuevamente.")
                pelicula_a_buscar = input("Ingrese la película a buscar: ").strip().lower()
            
            pelicula_encontrada = False
            for posicion,pelicula in enumerate(peliculas):
                if pelicula_a_buscar == pelicula['nombre']:
                    print("Encontrada.")
                    print(f"{posicion+1} - {pelicula['nombre'].title()}")
                    pelicula_encontrada = True
                
            if not pelicula_encontrada:
                print("Sin coincidencias.")
        
        elif opcion == 4:
            if not peliculas:
                print("No hay películas registradas para editar.")
                continue

            print("\n--- Lista de películas ---")
            for posicion,pelicula in enumerate(peliculas,1):
                print(f"{posicion} - {pelicula["nombre"].title()} ({pelicula["año"]})")

            try:
                indice = int(input("\nIngrese el número de la película que desea editar: "))
                if indice < 1 or indice > len(peliculas):
                    print("Número de película inválido.")
                    continue

                pelicula_editar = peliculas[indice - 1]

                print(f"\nEditando: {pelicula}")

                pelicula_encontrada = False
                for posicion,pelicula in enumerate(peliculas):
                    if pelicula_editar == pelicula['nombre']:
                        print(f"Editando {pelicula_editar.title()}")

                        nuevo_nombre_pelicula = input("Nuevo nombre: ").strip().lower()
                        while nuevo_nombre_pelicula == "":
                            nuevo_nombre_pelicula = input("No puede estar vacío, ingrese un nombre: ")

                        pelicula_actual = peliculas[posicion]
                        pelicula_actual['nombre'] = nuevo_nombre_pelicula
                        
                        print(f"¡Ahora es {nuevo_nombre_pelicula.title()}!")
                        pelicula_encontrada = True
                        break
                    if not pelicula_encontrada:
                        print("Película no encontrada.")
            except ValueError:
                print()
            

        elif opcion == 5:
            if not peliculas:
                print("Lista vacía")
                continue

            pelicula_eliminar = input("Ingrese el nombre de la película que desea eliminar: ").strip().lower()

            pelicula_encontrada = False
            for pelicula in peliculas:
                if pelicula_eliminar == pelicula['nombre']:
                    print(f"Eliminando: {pelicula_eliminar.title()}")

                    peliculas.remove(pelicula_eliminar)
                    print("Película eliminada con éxito.")
                    pelicula_encontrada = True

                if not pelicula_encontrada:
                    print("Sin coincidencias para eliminar.")

        elif opcion == 6:
            salir = True

        else:
            print()