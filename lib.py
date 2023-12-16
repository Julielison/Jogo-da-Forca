import random

def jogar(): # Verifica se o usuário quer jogar ou sair
    inicio_fim = input('1) Jogar\n2) Sair\n') # solicita um input do usuário
    if inicio_fim == '2': # se for 2
        return False # sai da função e do jogo
    elif inicio_fim != '1': # se for diferente de 1
        print('Digite 1 ou 2!') # exibe essa mensagem
        jogar() # chama novamente a função
    return True # usuário digitou 1, o jogo começa


# Retorna o histórico de dados do jogador se o apelido for encontrado na base de dados, se não, retorna os dados zerados
def verificar_apelido(apelido):
    cont = 0
    with open('dados.txt', 'r', encoding='utf-8') as arquivo: # abre o arquivo
        for linha in arquivo: # var linha recebe o conteúdo de cada linha do arquivo
            apelido_salvo, pontuação, palavras_adv = linha.split(';')
            if apelido_salvo == apelido: # Verifica se o apelido consta no bando de dados
                return apelido, int(pontuação), palavras_adv.upper(), cont
            cont += 1

        return apelido, int(0),'',False


def carrega_palavra_dica(palavras_adv):
    palavras_sorteadas = set()
    #palavras_adv = palavras_adv.replace('\\n','')
    with open('banco_de_palavras.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        
        while len(linhas) > len(palavras_sorteadas):
            palavra, dica = random.choice(linhas).strip().split(';')
            #palavra = palavra.replace('\\n','')
            palavras_sorteadas.add(palavra)
            if palavra.upper() in palavras_adv:
                continue
            return palavra.upper(), dica
    return None, None

def esconde_letras(palavra):
    for letra in palavra:
        if letra != '-':
            palavra = palavra.replace(letra, '*')
    return palavra

#Funçâo para marcar o chute correto
def marcar_chute_correto(palavra, chute, palavra_secreta):
    palavra_secreta_at = ''
    index = 0
    for letra in palavra:
        if chute == letra:
            palavra_secreta_at += letra
        else:
            palavra_secreta_at += palavra_secreta[index]
        index += 1
    return palavra_secreta_at

#Atualiza o arquivo de dados
def atualiza_dados(apelido,pontuação,palavras_adv,linha_jogador):
    palavras_adv_se = palavras_adv.strip()
    if linha_jogador:
        with open('dados.txt', 'r+', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            linhas[linha_jogador] = f'{apelido};{pontuação};{palavras_adv_se}'
            arquivo.seek(0)
            arquivo.writelines(linhas)
            arquivo.truncate()
    else:
        with open('dados.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'\n{apelido};{pontuação};{palavras_adv_se}')