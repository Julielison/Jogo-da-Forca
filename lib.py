import random

def jogar(): # Verifica se o usuário quer jogar ou sair
    inicio_fim = input('1) Jogar\n2) Sair\n') # solicita um input do usuário
    if inicio_fim == '2': # se for 2
        return False # sai da função e do jogo
    elif inicio_fim != '1': # se for diferente de 1
        print('Digite um valor válido!') # exibe essa mensagem
        jogar() # chama novamente a função
    return True # usuário digitou 1, o jogo começa

# Retorna o histórico de dados do jogador se o apelido for encontrado na base de dados, se não, retorna os dados zerados
def verificar_apelido(apelido):
    with open('dados.txt', 'r+', encoding='utf-8') as arquivo: # abre o arquivo
        for linha in arquivo: # var linha recebe o conteúdo de cada linha do arquivo
            apelido_salvo, pontuação, palavras_adv = linha.split(';')
            if apelido_salvo == apelido: # Verifica se o apelido consta no bando de dados
                return apelido, int(pontuação), palavras_adv

        return apelido, int(0),''

def carrega_palavra(palavras_adv):
    palavras_sorteadas = set()
    with open('banco_de_palavras.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        
        while len(linhas) > len(palavras_sorteadas):
            palavra, dica = random.choice(linhas).strip().split(';')
            palavras_sorteadas.add(palavra) 
            if palavra in palavras_adv:
                continue
            return palavra, dica
    return None, None

def esconde_letras(palavra):
    for letra in palavra:
        if letra != '-':
            palavra = palavra.replace(letra, '*')
    return palavra