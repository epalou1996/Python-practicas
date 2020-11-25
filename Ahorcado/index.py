
import random
from palabras import palabras_posibles

palabra=random.choice(palabras_posibles)

print(palabra)

#Ahorcado

IMAGES = ['''   

    +---+
    |   |
        |
        |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
        |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''','''   

    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''','''   

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''']

FIN_DIBUJO = ['''--- * --- * --- * --- * --- * --- * --- * --- * --- * ---''']


def juego(palabra):

    slot = '-'
    espacios = len(palabra)
    sustituta = list(slot*espacios)
    palabra = list(palabra)

    for a in IMAGES:
        miss = False
        while miss == False:
            print('')
            print(a)
            print('')
            print(sustituta)
            print('')
            print(FIN_DIBUJO)
            letra = input('Inserta la letra: ')
            if letra in palabra:
                tempo = []
                for l in palabra:
                    if l == letra:   
                        sustituta[palabra.index(letra)]  = letra
                        print(palabra.index(letra))
            else:
                miss == True



if __name__ == '__main__':
    juego(palabra)