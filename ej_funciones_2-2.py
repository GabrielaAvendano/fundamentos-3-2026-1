def total_a_pagar(precio_jugo,precio_pan,cant_jugo,cant_pan):
    total_jugo = precio_jugo*cant_jugo
    total_pan = precio_pan*cant_pan

    subtotal = total_jugo+total_pan
    if subtotal >= 5000:
        descuento = subtotal*0.1
    else:
        descuento = 0
    total = subtotal - descuento
    return  subtotal, descuento, total


jugos = int(input("Ingrese la cantidad de jugos a comprar: "))
panes = int(input("Ingrese la cantidad de panes a comprar: "))
subtotal, descuento, total = total_a_pagar(1200,1800,jugos,panes)

print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${int(descuento)}")
print(f"Total: ${int(total)}")