resposta = 'S'

while resposta == 'S':
    venda = float(input('\nVenda: R$ '))
    meta = 2000
    atingimento = (venda / meta) * 100
    print(f'O atingimento é de: {atingimento}%')

    resposta = input('\nDeseja continuar? [S/N] ').upper()