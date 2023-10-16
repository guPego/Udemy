# Exercicio com intuito de contar a quantidade de letras de uma frase.

frase = 'Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.'

i = 0
quantidade_letra_mais_repetida = 0
letra_mais_repetida = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantidade_letra_mais_repetida_atual = frase.count(letra_atual)

    if quantidade_letra_mais_repetida < quantidade_letra_mais_repetida_atual:
        quantidade_letra_mais_repetida = quantidade_letra_mais_repetida_atual
        letra_mais_repetida = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_repetida}" que apareceu '
    f'{quantidade_letra_mais_repetida}x'
)