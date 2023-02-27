#   Condições Aninhadas
    # Tipo de Condição:   elif:

#   Exercício 1

nome = str(input('Qual é o seu nome? '))

if nome == 'João':
    print('Que nome bonito você tem!')
elif nome == 'Bia' or nome == 'Beatriz':
    print('Seu nome é igual o da minha namorada.')
elif nome in 'Suely Sueli Mônica Tamara Karen Bruna Letícia Tamiris':
    print('Que belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
