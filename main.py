from lib import *

while jogar():
    while True:
      apelido = input('Digite um apelido: ')
      if ';' in apelido or '-' in apelido:
          print('Apelido inválido! Não pode conter ; ou -')
          continue
      break

    # Retorna os dados do jogador
    apelido, pontuação, palavras_adv,linha_jogador = verificar_apelido(apelido)

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
            chute = input('Qual a letra? ').upper()
            if chute in palavra:
                palavra_secreta = marcar_chute_correto(palavra, chute, palavra_secreta)
                pontuação += 10
            else:
                erros += 1
                print(f'Você errou {erros} de 6 tentativas')
            print(palavra_secreta)
            if '*' not in palavra_secreta:
                print('Parabéns, você acertou!!!')
                palavras_adv += f' {palavra}'
                acertou = True
                break
        segue = input('Deseja continuar? (s/n) ').lower()
        if segue == 's':
            continue
        print(f'Sua pontuação até aqui: {pontuação}')
        atualiza_dados(apelido,pontuação,palavras_adv,linha_jogador)
        break
    break