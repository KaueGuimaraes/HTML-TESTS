import sys
from time import sleep


def arquivo(nome, link, start=1, end=1, ep_por_temporada=12, download_espeficy=True):
    """
    Bilioteca para organizar as variáveis para a criação de sites derivados de certo template

    nome: Nome do anime (que será mostrado ao usuário)
    link: [link1, link2],
        Exemplo:
        Link sem modificações: "https://video.servertv001.com/animes/t/tonikaku-kawaii-2/01.mp4"
        Notando que "01" é o número que se altera de acordo com a variação de episódios, o que vier antes será o link 1/2. E o que vier depois será o link 2/2.
        
        Link 1/2: "https://video.servertv001.com/animes/t/tonikaku-kawaii-2/"
        link 2/2: ".mp4"
    start: Em que episódio começará as páginas
    end: Em que episódio terminará as páginas
    download_espeficy: True-especificar link de download; False-pegar link de download automaticamente
    ep_por_temporada: Quantos episódios cada temporada do anime tem tem
    """


    numero = start
    for numero in range(start, end + 1):
        if numero > ep_por_temporada:
            link_num = numero % ep_por_temporada
            if link_num < 10:
                link_num = '0' + str(link_num)
            else:
                link_num = str(link_num)
        else:
            if numero < 10:
                link_num = '0' + str(numero)
            else:
                link_num = str(numero)
        print(link_num)
        #str(input("Pressione qualquer tecla para continuar"))
        
        try:
            if numero < 10:
                arquivo = open(f"0{str(numero)}.html", "a")
            else:
                arquivo = open(f"{str(numero)}.html", "a")
        except FileNotFoundError:
            return False
        
        try:
            if download_espeficy:
                download = str(input(f'Informe o link de download do ep{numero} do perfil {nome}: '))
            else:
                download = link[0] + link_num + link[1]
            arquivo.write(escrever(nome, numero, download, link, link_num))
        #
        #
        #
        except:
            print("Não foi possivel escrever no arquivo")
            return
        else:
            continue
        sleep(0.1)
    arquivo.close()
        

def escrever(nome, numero, download, link, link_num):
    """
    Usado para gerar páginas para assistir perfis de anime (com variáveis já definidas)

    nome: Nome do anime
    numero: Número do episódio
    download: Link de download do episódio
    link: [link1, link2]
    link_num: Número do episódio para o site
    """


    if numero < 9:
        return acessar_template(nome=nome, numero=numero, download=download, numero_mais_1='0' + str(numero+1), numero_menos_1='0' + str(numero-1), link1=link[0], link2=link[1], numero_show='0' + str(numero))
    elif numero == 9:
        return acessar_template(nome=nome, numero=numero, download=download, numero_mais_1='10', numero_menos_1='08', link1=link[0], link2=link[1], numero_show='0' + str(numero))
    elif numero == 10:
        return acessar_template(nome=nome, numero=numero, download=download, numero_mais_1='11', numero_menos_1='09', link1=link[0], link2=link[1], numero_show=numero)
    elif numero > 10:
        return acessar_template(nome=nome, numero=numero, download=download, numero_mais_1=numero+1, numero_menos_1=numero-1, link1=link[0], link2=link[1], numero_show=str(numero))
    

def acessar_template(nome=0, numero=0, download=0, numero_mais_1=0, numero_menos_1=0, link1=0, link2=0, numero_show=0):
    """
    Função para trocar as informações diretamente do template

    nome: Nome do perfil
    numero: Número do episódio
    donwload: Link de download do episódio
    numero_mais_1: Próximo episódio
    numero_menos1: Episódio anterior
    link1 e link2: [link1, link2]
    numer_show: Número usado para estabelecer o link de assistir
    """
    #.replace('[NUMERO]', numero).replace('[NUMERO-1]', '0' + str(numero-1)).replace('[NUMERO+1]', '0' + str(numero+1)).replace('[DOWNLOAD]', download).replace('[LINK1]', link[0]).replace('[LINK2]', link[1])
    
    
    global template
    template = open('template.txt', 'r')
    template = template.read()
    template = str(template)

    template = template.replace('[NOME]', str(nome))
    template = template.replace('[NUMERO]', str(numero))
    template = template.replace('[NUMERO-1]', str(numero_menos_1))
    template = template.replace('[NUMERO+1]', str(numero_mais_1))
    template = template.replace('[DOWNLOAD]', str(download))
    template = template.replace('[LINK1]', str(link1))
    template = template.replace('[LINK2]', str(link2))
    template = template.replace('[NUMERO_SHOW]', str(numero_show))
    '''template = template.replace('[NOME]', nome)
    template = new.replace('[NUMERO]', numero)
    template = template.replace('[NUMERO-1]', numero_menos_1)
    template = template.replace('[NUMERO+1]', numero_mais_1)
    template = template.replace('[DOWNLOAD]', download)
    template = template.replace('[LINK1]', link1)
    template = template.replace('[LINK2]', link2)'''

    return template