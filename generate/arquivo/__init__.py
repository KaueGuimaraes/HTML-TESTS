import sys


def arquivo(nome, link, start=1, end=1, ep_por_temporada=12):
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
            download = str(input(f'Informe o link de download do ep{numero} do perfil {nome}: '))
            arquivo.write(escrever(nome, numero, download, link, link_num))
        #
        #
        #
        except:
            print("Não foi possivel escrever no arquivo")
            return
        else:
            continue
        

def escrever(nome, numero, download, link, link_num):
    if numero < 9:
        return(f'''<!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{nome} - Episodio {numero}</title>
                <link rel="stylesheet" href="../style.css">
            </head>
            <body>
                <a href="../index.html" target="_self" rel="prev">
                    <img src="../imagens/imageSize.png" alt="SuperAnimes - Vivendo em um novo Mundo!!"></img>
                </a>
                <br>
                <h1>{nome} - Episodio {numero}</h1>
                <br>

                <video controls width="720">
                    <source src="{link[0] + link_num + link[1]}">
                    <source src="videos/0{numero}.mp4">
                </video>
                <br>

                <a href="{'0' + str(numero-1)}.html" target="_self" rel="prev">
                    <img src="../imagens/play-anterior.png" alt="Video Anterior" width="24">
                </a>
                <a href="{'0' + str(numero+1)}.html" target="_self" rel="next">
                    <img src="../imagens/video-next.png" alt="Proximo Video" width="24">
                </a>
                <br>
                
                <a href="{download}" target="_blank" rel="external">
                    <img src="../imagens/baixar.png" alt="Fazer download" width="24">
                </a>
                <br>
                <a href="home.html" target="_self" rel="prev">
                    <img src="../imagens/video-list-2.png" alt="Voltar ao anime">
                </a>
            </body>
            </html>''')
    elif numero == 9:
        return(f'''<!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{nome} - Episodio {numero}</title>
                <link rel="stylesheet" href="../style.css">
            </head>
            <body>
                <a href="../index.html" target="_self" rel="prev">
                    <img src="../imagens/imageSize.png" alt="SuperAnimes - Vivendo em um novo Mundo!!"></img>
                </a>
                <br>
                <h1>{nome} - Episodio {numero}</h1>
                <br>

                <video controls width="720">
                    <source src="{link[0] + link_num + link[1]}">
                    <source src="videos/0{numero}.mp4">
                </video>
                <br>

                <a href="08.html" target="_self" rel="prev">
                    <img src="../imagens/play-anterior.png" alt="Video Anterior" width="24">
                </a>
                <a href="10.html" target="_self" rel="next">
                    <img src="../imagens/video-next.png" alt="Proximo Video" width="24">
                </a>
                <br>
                
                <a href="{download}" target="_blank" rel="external">
                    <img src="../imagens/baixar.png" alt="Fazer download" width="24">
                </a>
                <br>
                <a href="home.html" target="_self" rel="prev">
                    <img src="../imagens/video-list-2.png" alt="Voltar ao anime">
                </a>
            </body>
            </html>''')
    elif numero == 10:
        return(f'''<!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{nome} - Episodio {numero}</title>
                <link rel="stylesheet" href="../style.css">
            </head>
            <body>
                <a href="../index.html" target="_self" rel="prev">
                    <img src="../imagens/imageSize.png" alt="SuperAnimes - Vivendo em um novo Mundo!!"></img>
                </a>
                <br>
                <h1>{nome} - Episodio {numero}</h1>
                <br>

                <video controls width="720">
                    <source src="{link[0] + link_num + link[1]}">
                    <source src="videos/0{numero}.mp4">
                </video>
                <br>

                <a href="09.html" target="_self" rel="prev">
                    <img src="../imagens/play-anterior.png" alt="Video Anterior" width="24">
                </a>
                <a href="11.html" target="_self" rel="next">
                    <img src="../imagens/video-next.png" alt="Proximo Video" width="24">
                </a>
                <br>
                
                <a href="{download}" target="_blank" rel="external">
                    <img src="../imagens/baixar.png" alt="Fazer download" width="24">
                </a>
                <br>
                <a href="home.html" target="_self" rel="prev">
                    <img src="../imagens/video-list-2.png" alt="Voltar ao anime">
                </a>
            </body>
            </html>''')
    elif numero > 10:
        return(f'''<!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{nome} - Episodio {numero}</title>
                <link rel="stylesheet" href="../style.css">
            </head>
            <body>
                <a href="../index.html" target="_self" rel="prev">
                    <img src="../imagens/imageSize.png" alt="SuperAnimes - Vivendo em um novo Mundo!!"></img>
                </a>
                <br>
                <h1>{nome} - Episodio {numero}</h1>
                <br>

                <video controls width="720">
                    <source src="{link[0] + link_num + link[1]}">
                    <source src="videos/0{numero}.mp4">
                </video>
                <br>

                <a href="{numero-1}.html" target="_self" rel="prev">
                    <img src="../imagens/play-anterior.png" alt="Video Anterior" width="24">
                </a>
                <a href="{numero+1}.html" target="_self" rel="next">
                    <img src="../imagens/video-next.png" alt="Proximo Video" width="24">
                </a>
                <br>
                
                <a href="{download}" target="_blank" rel="external">
                    <img src="../imagens/baixar.png" alt="Fazer download" width="24">
                </a>
                <br>
                <a href="home.html" target="_self" rel="prev">
                    <img src="../imagens/video-list-2.png" alt="Voltar ao anime">
                </a>
            </body>
            </html>''')