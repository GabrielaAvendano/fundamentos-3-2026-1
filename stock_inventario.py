inventario = {
    "Teclado": 0,
    "Mouse": 4,
    "Monitor":9,
    "USB":2,
}
#^ no recuerdo haber estudiado esto, revisar después

for producto,cantidad in inventario.items():
    if cantidad == 0:
        print(f"{producto} -> sin stock.")
    elif cantidad > 0 and cantidad <= 5:
        print(f"{producto} -> stock bajo.")
    else:
        print(f"{producto} -> stock suficiente.")