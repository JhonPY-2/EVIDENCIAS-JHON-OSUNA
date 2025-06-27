import random

opciones = ["piedra", "papel", "tijera"]
rondas = int(input("¿Cuántas rondas quieres jugar?: "))
usuarioo = 0
maquinaa = 0

for ronda in range(1, rondas + 1):
    print(f"\nRonda {ronda} de {rondas}")
    usuario = input(" Elige piedra, papel o tijera: ").lower()
    while usuario not in opciones:
        usuario = input("Opción inválida. Elige piedra, papel o tijera: ").lower()
    
    maquina = random.choice(opciones)
    print(f"🙍 Jugadora: {usuario.capitalize()}")
    print(f" Computadora: {maquina.capitalize()}")

    if usuario == maquina:
        print("Empate ")
    elif (usuario == "piedra" and maquina == "tijera") or \
         (usuario == "papel" and maquina == "piedra") or \
         (usuario == "tijera" and maquina == "papel"):
        print("Ganaste ")
        usuarioo += 1
    else:
        print("Perdiste ")
        maquinaa += 1

    print(f"Puntaje: {usuarioo} - {maquinaa}")
    print(f"Rondas restantes: {rondas - ronda}")

print("Juego terminado ")
print(f"Puntaje final: {usuarioo} (Tú) - {maquinaa} (Computadora)")
print(" ¡Ganaste el juego!" if usuarioo > maquinaa else " La computadora ganó." if maquinaa > usuarioo else " Empate final.")
