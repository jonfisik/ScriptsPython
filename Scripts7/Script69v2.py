totM = totH = tot18 = 0
while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoa(s) com mais de 18: {tot18}.')
print(f'Total de homem(ens): {totH}.')
print(f'Total de mulhere(s) com menos de 20 anos: {totM}.')