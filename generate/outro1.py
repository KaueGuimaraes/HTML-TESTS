import sys
from time import sleep


print(f'\033[32mFaça o home do site de animes de maneira mais prática! Aqui você faz a lista de episódios para clicar.\033[0m')

while True:
    a = str(input('Em qual episódio iniciar? '))
    b = str(input('Em qual episódio terminar? '))
    try:
        a = int(a)
        b = int(b)
    except:
        print('Digite apenas números!')
        continue
    else:
        break

for c in range(a, b + 1):
    arquivo = open('outro1.txt', 'a')
    arquivo.write(f'''<li>
            <a href="{a}.html" target="_self" rel="next">Episodio {c}</a>
        </li>''')
    sleep(0.01)
    print(c)