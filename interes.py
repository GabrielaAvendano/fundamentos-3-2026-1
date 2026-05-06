capital = float(input("Capital: $"))
tasa = float(input("Tasa mensual %: "))
meses = int(input("Meses: "))

interes = capital * (tasa/100) * meses
print(f"Interés: {interes}")
print(f"Total: {capital + interes}")