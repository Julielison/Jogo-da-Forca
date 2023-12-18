import random


# Menu jogar/sair e validar input
def jogar():
    inicio_fim = input('1) Jogar\n2) Sair\n')
    if inicio_fim == '2':
        return False
    elif inicio_fim != '1':
        print('Digite 1 ou 2!')
        jogar()
    return True


# Retorna o histórico de dados do jogador se o apelido for encontrado na base de dados, se não, retorna os dados zerados
def verificar_apelido(apelido):
    linha_jogador = 0
    with open('dados.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            apelido_salvo, pontuação, palavras_adv = linha.split(';')
            if apelido_salvo == apelido:
                return apelido.strip(), int(pontuação), palavras_adv.upper().rstrip('\n'), linha_jogador
            linha_jogador += 1
        return apelido.strip(), int(0),'',-1


# Carrega a palavra e a dica. Se todas tiverem sido sorteadas, devolve None
def carrega_palavra_dica(palavras_adv):
    palavras_sorteadas = set()
    with open('banco_de_palavras.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        while len(linhas) > len(palavras_sorteadas):
            palavra, dica = random.choice(linhas).strip().split(';')
            palavras_sorteadas.add(palavra)
            if palavra.upper() in palavras_adv:
                continue
            return palavra.upper(), dica

    return None, None


# Troca cada letra da palavra por um *
def esconde_letras(palavra):
    for letra in palavra:
        if letra != '-':
            palavra = palavra.replace(letra, '*')
    return palavra


# Verifica se o chute foi repetido ou é inválido
def validar_chute(chute,chutes):
    if len(chute) > 1:
        print('Digite apenas uma letra!')
        return True
    elif chute in chutes:
        print('Letra repetida! Digite outra!')
        return True
    return False


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


# Verifica se a palavra foi adivinhada
def acertou(palavra_secreta):
    return '*' not in palavra_secreta


# Verifica se o arquivo está vazio ou não
def arquivo_esta_vazio():
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        return not conteudo


#Atualiza o arquivo de dados
def atualiza_dados(apelido,pontuação,palavras_adv,linha_jogador):
    palavras_adv_se = palavras_adv.strip()

    if linha_jogador >= 0:
        with open('dados.txt', 'r+', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            linhas[linha_jogador] = f'{apelido};{pontuação};{palavras_adv_se}\n'
            # remove o \n caso a linha  a ser alterada seja a última do arquivo
            if linha_jogador == len(linhas) - 1:
                linhas[linha_jogador] = linhas[linha_jogador].rstrip('\n')
            arquivo.seek(0)
            arquivo.writelines(linhas)

    else: # caso o jogador não tenha sido encontrado
        with open('dados.txt', 'a', encoding='utf-8') as arquivo:
            if arquivo_esta_vazio():
                arquivo.write(f'{apelido};{pontuação};{palavras_adv_se}')
            else:
                arquivo.write(f'\n{apelido};{pontuação};{palavras_adv_se}')


# Apaga os dados do jogador caso ele tenha zerado o jogo
def apaga_jogador(linha_jogador):
    with open('dados.txt', 'r+', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        arquivo.seek(0)
        if len(linhas) - 1 == linha_jogador:
            # remove o \n da linha anterior à última
            linhas[linha_jogador-1] = linhas[linha_jogador-1].rstrip('\n')
        del linhas[linha_jogador]
        arquivo.writelines(linhas) # sobrescreve as linhas
        arquivo.truncate() # remove o que há depois da última linha escrita


# Desenha o boneco na forca
def desenhar_boneco(erros):
    if erros == 1:
        print('┌────┐')
        print('│   😐')
        print('│')
        print('│')
        print('│')
    elif erros == 2:
        print('┌────┐')
        print('│   😐')
        print('│   ╱')
        print('│')
        print('│')
    elif erros == 3:
        print('┌────┐')
        print('│   😐')
        print('│   ╱░')
        print('│')
        print('│')
    elif erros == 4:
        print('┌────┐')
        print('│   😐')
        print('│   ╱░╲')
        print('│')
        print('│')
    elif erros == 5:
        print('┌────┐')
        print('│   😐')
        print('│   ╱░╲')
        print('│   ╱')
        print('│')
    else:
        print('┌────┐')
        print('│   😐')
        print('│   ╱░╲')
        print('│   ╱ ╲')
        print('│')
        print('Você perdeu!')