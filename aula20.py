primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro = int(primeiro_valor)
segundo = int(segundo_valor)

if (primeiro > segundo):
    print('O primeiro valor é maior que o segundi')
elif (segundo > primeiro):
    print('O segundo é valor é maior quer o primeiro')
else:
    print('Os números são iguais')