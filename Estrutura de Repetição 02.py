print (' Estrutura de Repetição - Exercício 02')

nome = input ('Digite o usuário:')
senha = input ('Digite a senha:')

while senha == nome:
    print('Erro')
    nome = input ('Digite o usuário:')
    senha = input ('Digite a senha:')
