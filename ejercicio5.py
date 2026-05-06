palabra = input("Ingrese una palabra: ")
palabra_limpia = palabra.replace(" ","").lower()

if len(palabra_limpia) > 0 and palabra_limpia == palabra_limpia[::-1]:
    print("Es un palíndromo.")

elif len(palabra_limpia) == 0:
    print("Error: Entrada vacía.")

else: 
    print("No es un palíndromo.")