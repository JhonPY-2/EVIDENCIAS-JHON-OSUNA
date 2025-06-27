notas = ["matematicas", "fisica", "quimica", "historia", "lengua"]

reprobadas = []
aprobadas = []
for i in range(len(notas)):
    nota = float(input(f"Ingrese la nota de {notas[i]}: "))
    if nota >= 3.0 and nota <= 5.0:
        reprobadas.append(notas[i])

    else:
        aprobadas.append(notas[i])
print("Materias aprobadas:", reprobadas)
print("Materias reprobadas tiene que recuperar:", aprobadas)
