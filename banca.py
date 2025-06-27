import random

perdidas = []
ganadas = []
print("JUEGO JUGADOR VS BANCA")

while True:
    preguntar = input(("QUIERES JUGAR (SI / NO)")).lower()

    if preguntar == "no":
        print("HAS SALIDO DEL JUEGO ")
        break 
    elif preguntar == "si":
        cartasJugador = random.randint(1, 13)
        cartasBanca = random.randint(1, 13)
        print(f"Cartas de banca {cartasBanca}")
        print(f"Cartas Jugador{cartasJugador}")

    if cartasJugador > cartasBanca:
        print("has ganado")
        ganadas.append(1)
    elif cartasJugador < cartasBanca:
        print("has perdido")
        perdidas.append(1)
    else:
        print("empate")
    if len(perdidas) == 3:
        print("haz perdido el juego")
        break
    elif len(ganadas) == 5:
        print("haz ganado el juego ")
        break
print(f"Ganaste {len(ganadas)} veces y perdiste {len(perdidas)} veces")
print("Gracias por jugar")