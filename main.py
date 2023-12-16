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
        palavra, dica = carrega_palavra_dica(palavras_adv)

        if palavra == None:
            print('Você zerou o jogo!')
            break

        palavra_secreta = esconde_letras(palavra)

        erros = 0

        print(f'Dica: {dica}')
        print(palavra_secreta)

        while erros < 6:
            chute = input('Qual a letra? ')
            if chute in palavra:
                palavra_secreta = marcar_chute_correto(palavra, chute, palavra_secreta)
            else:
                erros += 1
                print(f'Você errou {erros} de 6 tentativas')
            print(palavra_secreta)
            if '*' not in palavra_secreta:
                print('Parabéns, você acertou!!!')
                acertou = True
                break
        segue = input('Deseja continuar? (s/n) ')
        if segue == 's':
            continue
        break