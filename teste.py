nome_do_arquivo = 'seu_arquivo.txt'
linha_alvo = 3  # Substitua pelo número da linha que deseja reescrever (começando do 1)

with open(nome_do_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()

# Verificar se a linha_alvo é válida
if 1 <= linha_alvo <= len(linhas):
    linhas[linha_alvo - 1] = "Nova linha que substituirá a antiga.\n"

    with open(nome_do_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)
else:
    print("Número de linha inválido.")
