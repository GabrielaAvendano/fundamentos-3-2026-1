password = input("Ingrese su contraseña: ")

if len(password) >= 8 and not password.isalpha() and not password.isnumeric() and password.find(" ") == -1:
    print("Contraseña fuerte.")

elif len(password) < 8:
    print("Contraseña demasiado corta.")

else:
    print("La contraseña debe incluir letras y números, y no contener espacios.")