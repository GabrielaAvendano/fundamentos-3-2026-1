def validar_usuario(user):
    usuario_valido = False

    while not usuario_valido:
        if len(user) < 6 and " " in user:
            print("El nombre de usuario debe ser mayor a 6 caracteres y no contener espacios.")
            user = input("Ingrese un nombre de usuario: ")
        else:
            usuario_valido = True

    



user = input("Ingrese un nombre de usuario: ")
validar_usuario(user)

print("Usuario creado.")
