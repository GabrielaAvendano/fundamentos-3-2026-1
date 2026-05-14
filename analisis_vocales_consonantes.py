frase = input("Ingrese una frase: ")
vocales = consonantes = espacios = 0
simbolo = 0


for caracter in frase.lower():
    if caracter in "aeiouáéíóú":
        vocales += 1
    elif caracter == " ":
        espacios += 1
    elif caracter in "!#$%&/()=?¡+´¨*~[]^-_<>,;.:":
        simbolo += 1
    else:
        consonantes += 1
        
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
print(f"Espacios: {espacios}")