'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''
# Função
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} m x {comp} m é de {a} m²') # tabela ASCII: alt + 253
    print("--"*25)

# Programa principal
print("--"*25)
print(f"{'Cálculo de área':^50}")
print("--"*25)

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)