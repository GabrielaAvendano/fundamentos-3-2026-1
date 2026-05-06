precio = float(input("Ingrese el precio del producto: "))
socio = input("¿Es socio? [s/n]").lower().strip()

if precio > 50000 and socio == "s":
    precio = precio * 0.8
    print(f"Descuento 20% -> ${precio: .2f}")

elif precio > 50000 and socio == "n":
    precio = precio * 0.9
    print(f"Descuento 10% -> ${precio: .2f}")

elif precio <= 50000 and socio == "s":
    precio = precio * 0.95
    print(f"Descuento 5% -> ${precio: .2f}")

else: 
    print(f"Sin descuentos aplicables -> ${precio: .2f}")