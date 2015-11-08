#programa de jogo simples: adivinha as palavras
"""
_author_: André Lascas
_version_:1.0.0
_source_: VASCONCELOS, José Braga de; RIBEIRO, Nuno - Título: Tecnologias de Programação de Jogos,
FCA Editora
"""

ntimes = ['1ª tentativa', '2ª tentativa', '3ª tentativa', '4ª tentativa', '5ª tentativa']

words = 'lalos burro python azul warcraft league vermelho cat monkey pereira carro \
dog motor mobile mouse sapato router cisco blizzard riot sound screen cow serpente \
real moldura card ipb buntz asus rabbit legion heroes porrada biqueiro teamspeak'.split()

#funcao que devolve aleatoriamente uma palavra da lista anterior
def getRandomWord(lista_pal):
    wordIndex = random.randint(0, len(lista_pal) -1)
    return lista_pal[wordIndex]

#funcao que define e visualiza o interface de jogo
def displayBoard(ntimes, missedLetters, correctLetters, palavra):
    print (ntimes[len(missedLetters)])
    print()
    print ('Letras anteriores:', end = ' ') # end == \n
    for letter in missedLetters: print (letter, end=' ')
    print()
    blanks = '_' * len(palavra)

    #substitui os espacos em branco com as letras correctas
    for i in range(len(palavra)):
        if palavra[i] in correctLetters:
            blanks = blanks[:i]+palavra[i]+blanks[i+1:]

    #mostra a palavra secreta com espaços entre as letras
    for letter in blanks: print (letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #funcao que valida e devolve cada letra introduzida
    while True:
        adv_letra = input('Adivinha uma letra: ')
        adv_letra = adv_letra.lower()
        if len(adv_letra) != 1: print ('Inserir uma unica letra')
        elif adv_letra in alreadyGuessed:
            print('Ja escolheste "'+adv_letra+'". PF escolhe outra letra')
        elif adv_letra not in 'abcdefghijklmnopqrstuvwxyz':
            print('Inserir uma letra do alfabeto(a-z)')
        else: return adv_letra
        
#funcao que devolve True se o jogador pretender jogar novamente
def playAgain():
    print('Jogar novamente? (Sim ou Nao)')
    return input().lower().startswith('s')

import random
print ('ADIVINHA A PALAVRA')
missedLetters = ''
correctLetters = ''
palavra = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(ntimes, missedLetters, correctLetters, palavra)
    #escrever uma letra
    adv_letra = getGuess(missedLetters + correctLetters)

    if adv_letra in palavra:
        correctLetters = correctLetters + adv_letra
        #verificar se o jogador ganhou
        foundAllLetters = True
        for i in range(len(palavra)):
            if palavra[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Sim! Palavra secreta: "'+palavra+'"! Acertaste!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + adv_letra
        #determina numero de tentativas ate 'perder'
        if len(missedLetters) == len(ntimes) -1:
            displayBoard(ntimes, missedLetters, correctLetters, palavra)
            print('Terminaram as tentativas!\nDepois de '+str(len(missedLetters))+
                  ' tentativas erradas e ' + str(len(correctLetters))+
                  ' letras correctas, a palavra correcta era "'+palavra+'"')
            gameIsDone = True

    #pergunta se pretende jogar novamente
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            palavra = getRandomWord(words)
        else: break
