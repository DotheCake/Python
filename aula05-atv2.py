import random
from os import system

def escolher_palavra():
    palavras = ['pikachu', 'bulbasauro', 'charmander', 'squirtle', 'eevee', 'jigglypuff']
    return random.choice(palavras)

def mostrar_palavra(palavra ,letras_escolhidas):
    exibicao  = ''
    for letra in palavra:
        if letra in letras_escolhidas:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def jogar():
    palavra_secreta = escolher_palavra()
    tentativas_restante = 6
    letras_escolhidas = []


    print('''
   ___                      __                    
  |_  |                    / _|                   
    | | ___   __ _  ___   | |_ ___  _ __ ___ __ _ 
    | |/ _ \ / _` |/ _ \  |  _/ _ \| '__/ __/ _` |
/\__/ / (_) | (_| | (_) | | || (_) | | | (_| (_| |
\____/ \___/ \__, |\___/  |_| \___/|_|  \___\__,_|
              __/ |                               
             |___/                                 
          ''')

    print('Bem vindo ao jogo da forca da galerinha')
    print('Advinhe a palavra secreta')
    palavra_mostrar = mostrar_palavra(palavra_secreta, letras_escolhidas)
    

    while tentativas_restante > 0:
        letra = input('Digite uma letra: ').lower()

        if len(letra) != 1 or letra.isnumeric():
            print('Por favor, digite apenas uma letra')
            continue

        if letra in letras_escolhidas:
            print('Você já escolheu essa letra, tente novamente!')
            continue

        letras_escolhidas.append(letra) #adciona a informação a lista

        if letra not in palavra_secreta:
            tentativas_restante -= 1
            print('Letra incorreta. você tem {} tentativas restantes'.format(tentativas_restante))
        else:
            print('Letra correta!😉')
            palavra_mostrar = mostrar_palavra(palavra_secreta, letras_escolhidas)
            print(palavra_mostrar)
        if '_' not in palavra_mostrar:
            print("Você acertou a palavra!")
            break

        if tentativas_restante == 0:
            print('Você perdeu T-T')

op = ''
while op.lower() != 's':
    jogar()
    
    op = input('Digite s para sair ou c para continuar ')