"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'uai'
letras_acertadas = ''
quantidade_tentativas = 0

while True:
    letra_inserida = input('Digite uma letra: ')
    quantidade_tentativas += 1

    if len(letra_inserida) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_inserida in palavra_secreta:
        letras_acertadas += letra_inserida

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Parabéns, você ganhou!')
        print('A palavra era', f'"{palavra_secreta}"')
        print('Tentativas:', quantidade_tentativas)
        letras_acertadas = ''
        quantidade_tentativas = 0