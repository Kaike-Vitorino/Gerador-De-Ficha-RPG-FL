from PIL import Image, ImageDraw, ImageFont
from FichaCoordenadas import *

'''
   Modulo onde eu faco as funcoes relacionadas a impressao das informacoes na ficha.
        Onde tem as funcoes que vao de fato reunir as informacoes e editar a imagem da ficha.
'''

# Funcao onde eh decidido a fonte da maioria das escritas e tambem onde ocorre os comandos para a impressao das infos na ficha
def adicionar_texto_na_ficha(imagem, texto, cord, espacamento=0):
    tamanho_da_fonte = 50

    # Carrega a fonte padrão com o tamanho desejado
    fonte = ImageFont.truetype("arial", tamanho_da_fonte)

    # Obtém as coordenadas do campo
    x, y = cord

    # Cria um objeto desenho para adicionar texto à imagem
    desenho = ImageDraw.Draw(imagem)

    # Converte o texto para uma string
    texto_str = str(texto)

    # Adiciona o texto à imagem com o espaçamento vertical
    desenho.text((x, y + espacamento), texto_str, fill="black", font=fonte)

# Funcao que escreve na ficha uma coisa em varias coordenadas diferentes, no caso coisas relacionadas ao jogador.
def escrever_texto_em_varias_coordenadas_JOGADOR(imagem, texto, coordenadas):
    draw = ImageDraw.Draw(imagem)
    tamanho_da_fonte = 50

    fonte = ImageFont.truetype("arial", tamanho_da_fonte)

    # Especifica cor do texto (por exemplo, preto)
    cor_do_texto = (0, 0, 0)  # RGB (preto)

    # Itera sobre as coordenadas e escreva o texto em cada uma delas
    for coord in coordenadas:
        draw.text(coord, texto, fill=cor_do_texto, font=fonte)

# Funcao que escreve na ficha uma coisa em varias coordenadas diferentes, no caso coisas relacionadas ao Mestre.
def escrever_texto_em_varias_coordenadas_MESTRE(imagem, texto, coordenadas):
    draw = ImageDraw.Draw(imagem)
    tamanho_da_fonte = 30

    fonte = ImageFont.truetype("arial", tamanho_da_fonte)

    # Especifica a cor do texto (por exemplo, preto)
    cor_do_texto = (0, 0, 0)  # RGB (preto)

    # Itera sobre as coordenadas e escreva o texto em cada uma delas
    for coord in coordenadas:
        draw.text(coord, texto, fill=cor_do_texto, font=fonte)

# Funcao que escreve na ficha uma as infos da armadura, ela esta em uma funcao separada pq nn era necessario criar uma variavel
# armadura ate o momento atual.
def escrever_armadura(imagem, texto, coordenadas):
    draw = ImageDraw.Draw(imagem)
    tamanho_da_fonte = 55

    fonte = ImageFont.truetype("arial", tamanho_da_fonte)

    # Especifica a cor do texto (por exemplo, preto)
    cor_do_texto = (0, 0, 0)  # RGB (preto)

    # Itere sobre as coordenadas e escreva o texto em cada uma delas
    for coord in coordenadas:
        draw.text(coord, texto, fill=cor_do_texto, font=fonte)