def aumentar(preço = 0, taxa = 0, formato=False):
    res =  preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço = 0, taxa = 0, formato=False):
    res =  preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)

def metade(preço = 0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)

def moeda(preço, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço = 0, taxaA = 10, taxaR = 5):
    print('-'*50)
    print('RESUMO DO VALOR'.center(50))
    print('-'*50)
    print(f'Preço Analisado: {moeda(preço)}')
    print('-'*50)
    print(f'Dobro do Preço: \t\t{dobro(preço, True)}')
    print(f'Metade do Preço: \t\t{metade(preço, True)}')
    print(f'Aumento de {taxaA}% do Preço: \t{aumentar(preço, taxaA, True)}')
    print(f'Redução de {taxaR}% do Preço: \t{diminuir(preço, taxaR, True)}')
    print('-'*50)
