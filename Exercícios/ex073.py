# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time do Guaçuano.

times = ('Corinthians', 'Palmeiras', 'São Paulo', 'Santos', 'Portuguesa', 'Guarani', 'Ponte Preta', 'Paulista', 'Mogi Mirim', 'Guaçuano')

print('-='*80)
print(f'Lista de times: {times}')
print('-='*80)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*80)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*80)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*80)
print(f'O Guaçuano está na {times.index("Guaçuano")} posição.')
