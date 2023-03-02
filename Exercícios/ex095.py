# Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. 

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols  na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('Erro! Digite apenas S ou N.')
    if resp == 'N':
        break
print('-'*50)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar)? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código informado.')
    else:
        print(f'Levantamento do Jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'- No jogo {i} fez {g} gols.')
    print('-'*50)
print('Obrigado!')
