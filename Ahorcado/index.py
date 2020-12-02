
import random
from palabras import palabras_posibles

palabra=random.choice(palabras_posibles)



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
    x = len(IMAGES)
    intentos = 0
    while intentos<x:
        miss = False
        while miss == False:
            print('')
            print(IMAGES[intentos])
            print('')
            print(sustituta)
            print('')
            print(FIN_DIBUJO)
            letra = input('Inserta la letra: ')
            if letra in palabra:
                count = 0
                for i in palabra:
                    if letra == i:
                        sustituta[count] = letra
                    count +=1
                miss =True
                    

            else:
                miss = True
                intentos += 1
        if intentos == x:
            print("Perdiste")
        elif sustituta == palabra:
                print("Ganaste")
                intentos = x

if __name__ == '__main__':
    juego(palabra)