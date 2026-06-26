def contador_vocales(texto):
    texto.lower().strip()
    contar_vocales = 0

    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚüÜ"
    for caracter in texto:
        if caracter in vocales:
            contar_vocales += 1

    return contar_vocales


frase = input("Ingrese una palabra o frase: ")

vocales = contador_vocales(frase)

print(f"¡Su texto tiene {vocales} vocales!")