def esconde_letras(palavra):
    for letra in palavra:
        if letra != '-':
            palavra_secreta = palavra.replace(letra, '*')
    return palavra_secreta

# Exemplo de uso
palavra_original = input()
palavra_transformada = esconde_letras(palavra_original)

print(palavra_transformada)

