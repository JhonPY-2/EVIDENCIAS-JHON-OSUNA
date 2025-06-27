import random
import time  

preguntas = {
    1: [
        {'pregunta': '¿Cuál es la capital de Colombia?',
         'opciones': ['a) Medellín', 'b) Cali', 'c) Bogotá', 'd) Cartagena'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuántos días tiene una semana?',
         'opciones': ['a) 5', 'b) 6', 'c) 7', 'd) 8'],
         'respuesta': 'c'}
    ],
    2: [
        {'pregunta': '¿Qué animal es conocido por producir miel?',
         'opciones': ['a) Vaca', 'b) Cerdo', 'c) Abeja', 'd) Caballo'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuál es el resultado de 5 + 3?',
         'opciones': ['a) 7', 'b) 8', 'c) 9', 'd) 10'],
         'respuesta': 'b'}
    ],
    3: [
        {'pregunta': '¿Quién pintó la Mona Lisa?',
         'opciones': ['a) Pablo Picasso', 'b) Vincent van Gogh', 'c) Leonardo da Vinci', 'd) Salvador Dalí'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuántos continentes hay en el mundo?',
         'opciones': ['a) 4', 'b) 5', 'c) 6', 'd) 7'],
         'respuesta': 'd'}
    ],
    4: [
        {'pregunta': '¿Cuál es el elemento químico más abundante en la corteza terrestre?',
         'opciones': ['a) Hidrógeno', 'b) Oxígeno', 'c) Carbono', 'd) Nitrógeno'],
         'respuesta': 'b'},
        {'pregunta': '¿En qué año llegó Cristóbal Colón a América?',
         'opciones': ['a) 1490', 'b) 1492', 'c) 1500', 'd) 1510'],
         'respuesta': 'b'}
    ],
    5: [
        {'pregunta': '¿Cuál es la fórmula química del agua?',
         'opciones': ['a) CO_2', 'b) O_2', 'c) H_2O', 'd) CH_4'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuál es el río más largo del mundo?',
         'opciones': ['a) Amazonas', 'b) Nilo', 'c) Yangtsé', 'd) Misisipi'],
         'respuesta': 'b'}
    ],
    6: [
        {'pregunta': '¿Qué país es conocido como la "Tierra del Sol Naciente"?',
         'opciones': ['a) China', 'b) Corea del Sur', 'c) Japón', 'd) Tailandia'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuál es el nombre del proceso por el cual las plantas convierten la luz solar en energía?',
         'opciones': ['a) Respiración', 'b) Transpiración', 'c) Fotosíntesis', 'd) Fermentación'],
         'respuesta': 'c'}
    ],
    7: [
        {'pregunta': '¿Quién fue el primer hombre en pisar la Luna?',
         'opciones': ['a) Buzz Aldrin', 'b) Michael Collins', 'c) Neil Armstrong', 'd) Yuri Gagarin'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuál es el teorema matemático que establece que en un triángulo rectángulo, el cuadrado de la longitud de la hipotenusa es igual a la suma de los cuadrados de los otros dos lados?',
         'opciones': ['a) Teorema de Tales', 'b) Teorema de Pitágoras', 'c) Teorema de Fermat', 'd) Teorema de Euclides'],
         'respuesta': 'b'}
    ],
    8: [
        {'pregunta': '¿Cuál es el único metal líquido a temperatura ambiente?',
         'opciones': ['a) Oro', 'b) Plata', 'c) Mercurio', 'd) Plomo'],
         'respuesta': 'c'},
        {'pregunta': '¿Qué escritor ganó el Premio Nobel de Literatura en 1982 por su obra "Cien años de soledad"?',
         'opciones': ['a) Mario Vargas Llosa', 'b) Jorge Luis Borges', 'c) Gabriel García Márquez', 'd) Julio Cortázar'],
         'respuesta': 'c'}
    ],
    9: [
        {'pregunta': '¿Qué estructura celular es la responsable de la producción de energía en una célula eucariota?',
         'opciones': ['a) Núcleo', 'b) Ribosoma', 'c) Mitocondria', 'd) Retículo endoplasmático'],
         'respuesta': 'c'},
        {'pregunta': '¿Cuál es el nombre del principio físico que establece que un cuerpo sumergido en un fluido experimenta un empuje igual al peso del volumen desalojado?',
         'opciones': ['a) Principio de Pascal', 'b) Principio de Bernoulli', 'c) Principio de Arquímedes', 'd) Ley de Boyle'],
         'respuesta': 'c'}
    ],
    10: [
        {'pregunta': '¿Cuál es la constante de Avogadro?',
         'opciones': ['a) 6.022 × 10^23 mol⁻¹', 'b) 9.8 m/s²', 'c) 3 × 10^8 m/s', 'd) 1.602 × 10⁻¹⁹ C'],
         'respuesta': 'a'},
        {'pregunta': '¿Qué acontecimiento histórico marcó el fin de la Edad Media y el comienzo de la Edad Moderna?',
         'opciones': ['a) La caída del Imperio Romano de Occidente', 'b) La Revolución Francesa', 'c) La toma de Constantinopla por los turcos otomanos', 'd) El descubrimiento de América'],
         'respuesta': 'c'}
    ]
}

dinero = 0
recompensa = 1000000
comodinUsado1 = False
comodinUsado2 = False
comodinUsado3 = False
uso = False


print(" Bienvenidos a...\n")
time.sleep(1)
print(" ¡¡¡¿QUIÉN QUIERE SER MILLONARIO?!!! 💸💸 ")
time.sleep(1.5)

print(f"👏"*50)
nombre = input("\n ¿Cómo te llamas, concursante?: ").capitalize()
print(f"\n ¡Bienvenido/a al juego, {nombre}! Prepárate para ganar mucho dinero ")
time.sleep(1.5)

 
for nivel in range(1, 11):
    print(f"---------Nivel---- {nivel}")
    time.sleep(0.8)
    indicePregunta = random.choice([0, 1])
    preguntaActual = preguntas[nivel][indicePregunta]

    while True:
        if not uso:
            print(preguntaActual['pregunta'])
            time.sleep(0.8)
            for opcion in preguntaActual['opciones']:
                print(opcion)
                time.sleep(0.8)
        uso = False
        correcta = preguntaActual['respuesta']
        respuesta = input('¿Cuál es tu respuesta? (o escribe "comodines"): ').lower()
        time.sleep(0.8)

        if respuesta == 'comodines':
            print("\nComodines disponibles:")
            if not comodinUsado1:
                print("1. Llamar a un amigo 🎭")
            if not comodinUsado2:
                print("2. 50/50 ⏱")
            if not comodinUsado3:
                print("3. Cambiar de pregunta 🧬 ")

            eleccion = input("¿Cuál comodín quieres usar? (1, 2 o 3): ")

            if eleccion == '1' and not comodinUsado1:
                sugerencia = random.choice(['a', 'b', 'c', 'd'])
                print("📞 Tu amigo sugiere que la respuesta es:", sugerencia)
                comodinUsado1 = True

            elif eleccion == '2' and not comodinUsado2:
                incorrectas = [letra for letra in ['a', 'b', 'c', 'd'] if letra != correcta]
                opciones_mostradas = [correcta, random.choice(incorrectas)]
                print("\nOpciones posibles después del 50/50: ⏱")
                for letra in opciones_mostradas:
                    for opcion in preguntaActual['opciones']:
                        if opcion.startswith(letra):
                            print(opcion)
                comodinUsado2 = True
                uso = True  # no volver a imprimir pregunta completa

            elif eleccion == '3' and not comodinUsado3:
                nuevo_indice = 1 if indicePregunta == 0 else 0
                preguntaActual = preguntas[nivel][nuevo_indice]
                print("\n🔄 Cambiando a otra pregunta...\n")
                comodinUsado3 = True
                uso = False  # mostrar nueva pregunta completa

            else:
                print("⚠️ Ese comodín ya fue usado o no es válido.")
            continue  # volver a pedir la respuesta después del comodín

        if respuesta == correcta:
            dinero += recompensa
            print("¡Correcto! Llevas acumulado:", dinero, "\n")
            time.sleep(0.8)
            if dinero == 10000000:
                print(" ¡Felicidades has ganado el juego! Tienes un nivel intelectual de 500.")
                time.sleep(0.8)
        else:
            print("❌ Respuesta incorrecta. Fin del juego.")
            time.sleep(0.8)
            exit()
        break