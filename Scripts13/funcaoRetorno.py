def traco():
    print('---'*10)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

traco()
r1 = somar(3,2,5)
r2 = somar(2,6)
r3 = somar(5)
print(f'Os resultados foram {r1}, {r2} e {r3}.')
traco()
f1 = fatorial(5)
f2 = fatorial(6)
f3 = fatorial(0)
print(f'Os resutados são {f1}, {f2}, {f3}.')
traco()
num = int(input('Digite um numero: '))
if par(num):
    print(f'{num} É par!')
else:
    print(f'{num} Não é par!')
traco()