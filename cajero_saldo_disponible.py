saldo = 300
retiros = [50, 120, 200, -5]
i = 0

while i < len(retiros):
    
    retiro = retiros[i]

    if retiro <= 0:
        print(f"Retiro invalido: {retiro}")

    elif retiro <= saldo:
        saldo -= retiro
        print(f"Retiro exitoso: {retiro} -> saldo restante: {saldo}")

    else:
        print(f"Fondos insuficientes para retirar {retiro}")

    i += 1

