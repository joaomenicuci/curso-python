# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: – Quantidade de notas. – A maior nota. – A menor nota. – A média da turma. – A situação (opcional).

def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r

resp = notas(5.5, 2.5, 1, 8.5, sit=True)
print(resp)
