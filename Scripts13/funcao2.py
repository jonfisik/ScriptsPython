# docstring

def contador(i,f,p):
    """
    A função faz uma contagem e mostra na tela
    i: início da contagem
    f: fim da contagem
    p: passo da contagem
    return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(10, 100, 2.5)

#help(contador)


