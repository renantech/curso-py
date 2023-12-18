a = 'A'
b = 'B'
c = 1.1
formato = 'a={1} b={0} c={2:.2f}'.format(a, b, c) # Índices
formato2 = 'Nome: {nome} Sobrenome: {sobrenome}'.format(nome = 'Renan', sobrenome = 'Mendes') # Parâmetro

print(formato)
print(formato2)