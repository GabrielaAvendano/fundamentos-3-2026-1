print("----- Sistema de registro de pacientes -----")
edades_pacientes = []
cant_pacientes = int(input("Ingrese la cantidad de pacientes a registrar: "))


while len(edades_pacientes) < cant_pacientes:
    entrada = input(f"Ingrese la edad del paciente {len(edades_pacientes) + 1}: ")

    try:
        edad = int(entrada)
        edades_pacientes.append(edad)
        print("Entrada registrada con éxito.\n")
    except ValueError:
        print("Error de formato, por favor ingrese un número válido.")

print("Registro completo, edades guardadas satisfactoriamente:", edades_pacientes)