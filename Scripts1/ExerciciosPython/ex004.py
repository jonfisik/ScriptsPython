'''Dê toda descrição da variável que foi digitada. 20/04/2020'''
print('--------------------------------------------')
x = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(x))
print('O valor digitado só tem espaço, verdadeiro ou falso? ', x.isspace())
print('O valor é número? ', x.isnumeric())
print('O valor é letra? ', x.isalpha())
print('O valor é alfanumérico? ', x.isalnum())
print('O valor é maiúscula? ', x.isupper())
print('O valor é minúscula? ', x.islower())
print('O valor capitalizada? ', x.istitle())
print('--------------------------------------------')