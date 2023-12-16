from lib import *

while jogar():

    while True:
      apelido = input('Digite um apelido: ')
      if ';' in apelido or '-' in apelido:
          print('Apelido inválido! Não pode conter ; ou -')
          continue
      break

    # Retorna os dados do jogador
    apelido, pontuação, palavras_adv = verificar_apelido(apelido)

    while True:
        palavra, dica = carrega_palavra(palavras_adv)

        if palavra == None:
            print('Você zerou o jogo!')
            break

        palavra_secreta = (esconde_letras(palavra))

        print(f'Dica: {dica}')
        print(palavra_secreta)
        break