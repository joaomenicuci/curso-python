# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from ex115menu import *
from ex115dados import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #   Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        #   Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #   Opção de sair do sistema.
        cabeçalho('Saindo do Sistema. Até logo!')
        break
    else:
        #   Digitou uma opção errada no menu.
        print('\033[31mErro! Digite uma opção válida.\033[m')
    sleep(2)
