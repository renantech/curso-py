"""
Exercícios

Peça ao usuário para digitar o seu nome
Peça ao usuário para digitar a sua idade

Se o nome e dade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não espaços)
        Seu nome tem n letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for exibido em nome ou idade:
    Exiba: "Desculpe, você deixou campos vazios"
"""

nome = input('Digite o seu nome: ')
idade_string = input('Digite o seu nome: ')

if nome and idade_string:
    idade = int(idade_string)

    print(f'Seu nome é {nome}')
    print('Sua idade é {x}'.format(x = idade))
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome: 
        print('Seu nome é composto')
    else:
        print('Seu nome não é composto')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazio')