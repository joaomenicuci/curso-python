#   Variáveis Compostas - Dicionários
    # Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
    # Dicionários são definidos entre chaves {}.

#   Exercício 1

pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())

#   Exercício 2

pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
del pessoas['sexo']
pessoas['nome'] = 'Lucas'
pessoas['peso'] = 90.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(pessoas.items())

#   Exercício 3

brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1]['uf'])

#   Exercício 4

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
