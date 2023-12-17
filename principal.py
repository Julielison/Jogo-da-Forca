from biblioteca import *

while jogar():
    while True:
      apelido = input('Digite um apelido: ')
      if ';' in apelido or '-' in apelido:
          print('Apelido inválido! Não pode conter ; ou -')
          continue
      break

    # Retorna os dados do jogador
    while True:
        pontos = erros = 0 
        apelido, pontuação, palavras_adv,linha_jogador = verificar_apelido(apelido)
        palavra, dica = carrega_palavra_dica(palavras_adv)
        if palavra == None:
            print('Você zerou o jogo!')
            break
        palavra_secreta = esconde_letras(palavra)

        chutes = ''
        while erros < 6:
            print(f'Dica: {dica}')
            print(palavra_secreta)
            chute = input('Qual a letra? ').upper()

            if validar_chute(chute,chutes):
                continue
            chutes += chute

            if chute in palavra:
                palavra_secreta = marcar_chute_correto(palavra, chute, palavra_secreta)
                pontos += 10
                if acertou(palavra_secreta):
                    print('Parabéns, você acertou!!!')
                    print(f'A palavra era {palavra}')
                    palavras_adv += f' {palavra}'
                    pontuação += pontos
                    atualiza_dados(apelido,pontuação,palavras_adv,linha_jogador)
                    break
            else:
                erros += 1
                print(f'Você errou {erros} de 6 tentativas')
                desenhar_boneco(erros)

        # Pergunta se o usuário quer seguir ou não e atualiza os dados
        segue = input('Deseja continuar? (s/n) ').lower()
        if segue == 's':
            continue
        print(f'Sua pontuação até aqui: {pontuação}')
        print(f'Jogo Encerrado!')
        break
    break