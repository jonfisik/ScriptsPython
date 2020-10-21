'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''
def voto(ano):
    from datetime import date # escopo de importação
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return (f'Com {idade} ano: NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    

#programa principal
print('---'*10)
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
print('---'*10)