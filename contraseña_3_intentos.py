clave_correcta = "Python123"

intentos = []
i = 0
acceso = False

while i < 3:
    intentos.append(input("Ingrese la contraseña: "))
    if intentos [i] == clave_correcta:
        acceso = True
        break
    else:
        print(f"Intento {i + 1} incorrecto.")
    i += 1

if acceso:
    print("Acceso concedido.")

else: 
    print("Acceso bloqueado.")