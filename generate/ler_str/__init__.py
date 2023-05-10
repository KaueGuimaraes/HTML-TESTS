def escrever_inteiro(content='Escreva algo: '):
    while True:
        x = str(input(content))
        try:
            x = int(x)
            return x
        except:
            print('\033[31mDigite apenas valores inteiros!\033[m')
        else:
            continue