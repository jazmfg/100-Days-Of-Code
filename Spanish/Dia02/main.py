factura = float(input("Ingresa el total de la factura: $"))
propina = int(input("Qué porcentaje de propina deseas dar 10, 12 0 15%: "))
personas = int(input("Entre cuantas personas se repartirá la cuenta: "))

pago_por_persona = (factura * (propina / 100 + 1)) / personas

print(f"Cada persona debe pagar: ${pago_por_persona:.2f}")