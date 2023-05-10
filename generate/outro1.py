import sys
from arquivo import *
from ler_str import *
from time import sleep


print(f'\033[32mFaça o home do site de animes de maneira mais prática! Aqui você faz a lista de episódios para clicar.\033[0m')

a = escrever_inteiro('Em qual episódio iniciar? ')
b = escrever_inteiro('Em qual episódio terminar? ')
nome = str(input('Digite o nome do arquivo que será gerado: '))

lista = list()

for c in range(a, b + 1):
    lista = lista.clear()
    lista = list()

    lista.append(['[EP_SHOW]', str(c)])
    if c < 10: lista.append(['[EP_HTML]', '0' + str(c)])
    else: lista.append(['[EP_HTML]', str(c)])

    arquivo = open(nome, 'a')
    arquivo.write(trocar_template('template1.txt', lista))
    sleep(0.01)
    print(c)