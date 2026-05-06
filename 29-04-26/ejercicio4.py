codigo = input("Ingrese el código de producto: ").strip().upper()

if codigo.startswith("PROD-") and len(codigo) == 9 and codigo[5:].isdigit():
    print("Código de producto válido.")

elif not codigo.startswith("PROD-"):
    print("Error: El código debe empezar con 'PROD-'.")

else: 
    print("Error: La parte final debe contener exáctamente 4 dígitos.")