from PIL import Image, ImageDraw, ImageFont
from FichaCoordenadas import *

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

