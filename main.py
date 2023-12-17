from lib import * # importa do arquivo lib todas as funções

while jogar(): # Inicia ou sai do jogo

    while True: # Valida o apelido
      apelido = input('Digite um apelido: ')
      if ';' in apelido or apelido == '':
          print('Apelido inválido! O apelido está vazio ou com ;')
          continue
      break

    while True: # Carrega os dados do jogador e da palavra
        pontos = erros = 0
        apelido, pontuação, palavras_adv,linha_jogador = verificar_apelido(apelido)
        palavra, dica = carrega_palavra_dica(palavras_adv)

        if palavra == None: # Verifica se o jogador zerou o jogo
            print('Você zerou o jogo!')
            print(f'Pontuação final: {pontuação}')
            apaga_jogador(linha_jogador) # apaga os dados do jogador
            break

        # Retorna a palavra com *
        palavra_secreta = esconde_letras(palavra)
        chutes = ''

        # Roda até que os erros cheguem a 6 ou a palavra seja acertada
        while erros < 6:
            print(f'Dica: {dica}')
            print(palavra_secreta)
            chute = input('Qual a letra? ').upper()
            if validar_chute(chute,chutes):
                continue
            chutes += chute

            if chute in palavra: # verifica se o usuário acertou o chute
                palavra_secreta = marcar_chute_correto(palavra, chute, palavra_secreta)
                pontos += 10
                if acertou(palavra_secreta): # verifica se acertou a palavra
                    print('Parabéns, você acertou!!!')
                    print(f'A palavra era {palavra}')
                    palavras_adv += f' {palavra}' # atualiza as palavras adivinhadas
                    pontuação += pontos
                    atualiza_dados(apelido,pontuação,palavras_adv,linha_jogador)
                    break
            else:
                erros += 1
                print(f'Você errou {erros} de 6 tentativas')
                desenhar_boneco(erros)

        # Pergunta se o usuário quer seguir ou não
        segue = input('Deseja continuar? (s/n) ').lower()
        if segue == 's':
            continue
        print(f'Sua pontuação até aqui: {pontuação}')
        print(f'Jogo Encerrado!')
        break
    break