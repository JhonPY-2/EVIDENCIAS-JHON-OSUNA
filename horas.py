horas = float(input("Ingrese las horas trabajadas: "))
pago = float(input("Ingrese el pago por hora: "))


if horas <= 40:
    horasNormales = horas * pago
    horaExtras = 0
    total = horasNormales
else:
    horasNormales = 40 * pago
    horaExtras = horas - 40
    if horas <= 8:
        horass = horas * pago * 2
    else:
        horass = (8 * pago * 2) + ((horas - 8) * pago * 3)
    total = horasNormales + horass

# Salida de resultados
print(f"Pago por hora: ${pago}")
print(f"Pago total: ${total}")
print(f"Pago salario base: ${horasNormales}")
print(f"Pago por horas extras: ${horass}")
