vocales = input("Ingrese una palabra: ")

numero_vocales = 0
for i in range(len(vocales)):
    if vocales[i] == "a" or vocales[i] == "e" or vocales[i] == "i" or vocales[i] == "o" or vocales[i] == "u":
        numero_vocales += 1
print("El número de vocales es:", numero_vocales)