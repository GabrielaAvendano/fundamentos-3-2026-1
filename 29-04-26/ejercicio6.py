archivo = input("Ingrese el nombre del archivo: ").lower()

if archivo.endswith(".jpg") or archivo.endswith(".png") or archivo.endswith(".gif"):
    print("El archivo es una imagen.")

elif archivo.endswith(".doc") or archivo.endswith(".pdf"):
    print("El archivo es un documento.")

else:
    print("Tipo de archivo desconocido.")