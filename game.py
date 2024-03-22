import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_fails = 10
vocales= ["a","e","i","o","u","á","é","í","ó","ú"]
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
diff=input("""----DIFICULTAD----
        1:FACIL-REVELA LAS VOCALES
        2:MEDIA-REVELA LA PRIMERA Y ULTIMA LETRA
        3:DIFICIL-NO SE REVELA NINGUNA LETRA
Elija el numero de dificultad""")
palabra = []
match diff:
    case "1":
        guessed_letters.extend(vocales)
        for letra in secret_word:
            if letra in vocales:
                palabra.append(letra)
            else:
                palabra.append("_")
    case "2":
        for ind,letra in enumerate(secret_word):
            if ind == 0 or ind == len(secret_word)-1:
                palabra.append(letra)
            else:
                palabra.append("_")
    case _:
        for ind in secret_word:
            palabra.append("_")
palabra_secreta = "".join(palabra)
print(palabra_secreta)
cant=0
while cant<max_fails:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si la letra ya ha sido adivinada
    if letter == "":
        print("Lo siento, no ingreso una letra")
        cant+=1
    else:
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            cant+=1
            continue
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)
        # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            cant+=1
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for i,letter in enumerate(secret_word):
        match diff:
            case "1":
                if letter in vocales or letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            case "2":
                if i == 0 or i == len(secret_word)-1 or letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            case "3":
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_fails} fallos.")
    print(f"La palabra secreta era: {secret_word}")
