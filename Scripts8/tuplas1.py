# exemplos tuplas (manipulando) 11/08/2020
lanche = ('Habúrguer','Suco','Pizza','Pudim')
print('-'*8)
print(lanche)
print('-'*8)
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print('-'*8)
print(lanche[0:2])
print(lanche[1:])
print(lanche[:2])
print(lanche[-1])
print(lanche[-3:])
print('-'*8)
print(len(lanche))
print('-'*8)
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!!!')
print('-'*8)
for cont in range(0,len(lanche)):
    print(cont)
    print(lanche[cont])
print('-'*8)
for posicao, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {posicao}.')
print('-'*8)
print(sorted(lanche)) # ordena a tupla 
a = (3,5,1)
b = (6,5,9,0)
c = a + b
d = b + a
print(c)
print(d)
print(d.count(9))
print(d.count(10))
print('-'*8)
print(c.index(5,2)) # a partir da posição 2
del(d) # deleta a tupla
