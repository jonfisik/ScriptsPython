'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
print('-='*30)
#cont = 0
expr = str(input('Digite uma experessão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
            #if simb == ')':
            #    cont = cont + 1
if len (pilha) == 0:
    print('Sua expressão é VÁLIDA! ')
else: 
    print('Sua expressão está ERRADA!')
#print(cont)
print('-='*30)