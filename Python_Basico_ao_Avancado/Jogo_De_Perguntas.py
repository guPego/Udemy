# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'pergunta': 'Quanto é 25 + 50 ?',
        'opcoes': ['65', '75', '85', '55'],
        'resposta': '75',
    },
    {
        'pergunta': '5*5 é 25 ?',
        'opcoes': ['True', 'False'],
        'resposta': 'True',
    },
    {
        'pergunta': 'Quanto é 25/2?',
        'opcoes': ['7.5', '13.5', '15', '12.5'],
        'resposta': '12.5',
    },
]

quantidade_acertos = 0;

for pergunta in perguntas:
    print(f'\npergunta:', pergunta['pergunta'], '\n');

    opcoes = pergunta['opcoes'];
    for i, opcao in enumerate(opcoes):
        print(f'{i+1})', opcao);

    escolha = input('\nEscolha uma opção: ');

    acertou = False;
    escolha_int = None;
    qtd_opcoes = len(opcoes);

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <= qtd_opcoes:
            if opcoes[escolha_int - 1] == pergunta['resposta']:
                acertou = True

    if acertou:
        quantidade_acertos += 1
        print('\nAcertou 👍')
    else:
        print('\nErrou ❌')

print('\nVocê acertou', quantidade_acertos)
print('de', len(perguntas), 'perguntas.')
