import uteis
# from uteis import fatorial, dobro,triplo // não é preciso usar a função antes do objeto.
# from módulo import função

num = int(input('Digite um numero: ')) 
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')