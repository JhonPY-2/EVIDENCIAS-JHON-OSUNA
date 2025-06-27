anchoEscalera = n * 1 
for i in range(1, n + 1):
        escalon = "#" * i
        escalonJustificado = escalon.rjust(anchoEscalera)
        print(escalonJustificado)