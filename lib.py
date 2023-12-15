def jogar(): # Verifica se o usuário quer jogar ou sair
    while True:
        inicio_fim = input('1) Jogar\n2) Sair\n') # solicita um input do usuário
        if inicio_fim == '2': # se for 2
            return True # sai do loop e do jogo
        elif inicio_fim != '1': # se for diferente de 1
            print('Digite um valor válido!') # exibe essa mensagem
            continue # reinicia o loop
        return False # usuário digitou 1, o jogo começa