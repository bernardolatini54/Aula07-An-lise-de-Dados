contador = 0
soma = 0

while True:
    despesa = float(input('\nDespesas: R$ '))
    soma = soma + despesa
    
    contador += 1
    print(f'Total: R$ {soma}')

    resposta = input('\nQuer continuar? [S/N] ').upper()

    if resposta == 'N':
        break

print(f'Vendas: ')
print(f'Despesas: ')