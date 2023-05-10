from arquivo import *
from ler_str import *
import sys
# [NUMERO] [NOME] [NUMERO-1] [NUMERO+1] [DOWNLOAD]

print('\033[32mAdicione os episódios de um perfil de anime de maneira mais prática! Aqui você gera as páginas dos episódios de maneira automatizada.\033[m')
while True:
    name = str(input('Qual é o nome do perfil? (O que aparecerá para o usuário) '))
    while True:
        link1 = str(input('Link 1/2: (digite "help" caso tenha dúvida) ')).replace(' ', '')
        if link1 == 'help':
            print('''\033[32mLink sem modificações: "https://video.servertv001.com/animes/t/tonikaku-kawaii-2/01.mp4"\nNotando que "01" é o número que se altera de acordo com a variação de episódios, o que vier antes será o link 1/2. E o que vier depois será o link 2/2.\n\nLink 1/2: "https://video.servertv001.com/animes/t/tonikaku-kawaii-2/"\nlink 2/2: ".mp4"\033[m\n''')
        else:
            break
    link2 = str(input('Link 2/2: ')).replace(' ', '')
    start = escrever_inteiro('Em que episódio será o começo para a execução? ')
    end = escrever_inteiro('Em que episódio será o ponto final para a execução? ')
    ep_por_temporada = escrever_inteiro('Quantas episódios tem cada temporada do anime? (O normal é 12) ')

    question = str(input('Aperte N para não especificar o(s) link(s) de download ')).lower().replace(' ', '')
    if question == 'n':
        download_espeficy = False
    else:
        download_espeficy = True

    arquivo(name, [link1, link2], start, end, ep_por_temporada, download_espeficy)

    question = str(input('\nQuer começar uma nova execução? (Digite S para sim) ')).replace(' ', '').lower()
    if question == 's':continue
    else:break
print('\033[32mObrigado por usar o programa!\033[m')

#EX: ("Tonikaku Kawaii", ['https://video.servertv001.com/animes/t/tonikaku-kawaii-2/', '.mp4'], 13, 24)
#arquivo("Black Clover", ['https://hd3.servertv001.com/animeshd/b/black-clover/', '.mp4'], 1, 170, 170)