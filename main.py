from lib import *

while True:
    if jogar():
       break




    while True:
      apelido = input('Digite seu apelido sem (; e -): ')
      if ';' in apelido or '-' in apelido:
        print('Apelido inválido!')
        continue
      break
    # Abre o arquivo de dados para leitura ou escrita
    consta = False
    with open('dados.txt', 'r+') as arquivo:
        for linha in arquivo:
            dados = linha.split(';')
            apelido_salvo = dados[0]

            if apelido_salvo == apelido: # Verifica se o apelido consta no bando de dados
                pontuação = int(dados[1])
                p_adivinhadas = dados[2].split()
                consta = True
                break
        if not consta:
            arquivo.write(f'\n{apelido};0;') # grava o apelido no bando de dados caso não esteja
    print(apelido)