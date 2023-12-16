from lib import *
import random #Biblioteca para pegar uma palvra aleatoria do banco de palavras

#Função para jogar o jogo
def jogar():
    print('Seja Bem vindo ao jogo da Forca! ')

    palavra_secreta = carrega_palavra()


    letras_acertadas = ['*' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = input('Qual a letra? ')
        if chute in palavra_secreta:
            marcar_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print(f'Você errou {erros} de 6 tentativas')
        enforcou = erros == 6
        acertou = '*' not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        print('Parabéns, você ganhou!!!')
    else:
        print('Você Perdeu!!!')
            

#Funçâo para marcar o chute correto
def marcar_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra

        index += 1

jogar()