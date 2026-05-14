precios = [35, 50, 120, 89, 210]
for precio in precios:
    if precio > 100:
        total = precio * 0.80
        print(precio, "-> descuento 20% ->", total)
    elif precio >= 50 and precio <= 100:
        total = precio * 0.90
        print(precio, "-> descuento 10% ->", total)
    else:
        print(precio, "-> sin descuento ->", precio)