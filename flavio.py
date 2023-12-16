import random #Biblioteca para pegar uma palvra aleatoria do banco de palavras

#Função para jogar o jogo
def jogar():
    print('Seja Bem vindo ao jogo da Forca! ')

    palavra_secreta = carregar_palavra_secreta()


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
            

#Função para carregas as palavras do banco de palavras e sortear a palavra secreta
def carregar_palavra_secreta():
    arquivo = open('banco_de_palavras.txt','r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]

    return palavra_secreta

#Funçâo para marcar o chute correto
def marcar_chute_correto(palavra, chute, palavra_secreta):
    index = 0
    for letra in palavra:
        if chute == letra:
            palavra_secreta[index] = letra

        index += 1

jogar()