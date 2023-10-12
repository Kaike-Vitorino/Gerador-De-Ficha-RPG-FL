from utilFichaJPG import *
from FichaCoordenadas import *
import webbrowser
from util import *

#=============================================================================================================================================

# Gerar raca aleatoria
raca, raca_info = gerar_raca()
#print(f"Raca escolhida: {raca}")

# Gerar classe aleatoria
classe = gerar_classe(raca,racas_info,classes)
#print(f"Classe: {classe}")

# Funcao para obter atributos chave
atributos_chave = obter_atributos_chave(classe, raca, raca_info)

# Gerar idade
idade, faixa_etaria = calcular_idade(raca)

# Gerar atributos
atributos_randomizados = escolher_atributos(faixa_etaria, atributos_chave)

# Gerar pontos de pericias
pericias_distribuidas = distribuir_pontos_pericia(faixa_etaria, classe)
print(f"Pericias distribuidas: {pericias_distribuidas}")

# Gerar arma
arma_escolhida = gerar_arma(classe)

# Gerar talentos
talentos_escolhidos = escolher_talentos(classe, raca, faixa_etaria)
print(f"Talentos escolhidos:", talentos_escolhidos)

# Dividir XP
vai_ter_xp_escolha = input(f"Vai ter algum xp extra para essa ficha? s/n\n")
if vai_ter_xp_escolha == "s":
    talentos_escolhidos, pericias_distribuidas = dividir_XP(talentos_escolhidos, pericias_distribuidas, classe, pericias)
    print(f"Talentos escolhidos após dividir XP:", talentos_escolhidos)
    print(f"Pericias distribuidas após dividir XP:", pericias_distribuidas)
else:
    pass

prata_rolada = rolar_dados_prata(classe_info[classe]["dados_recurso"]["Prata"])
info_armas = lista_armas_FINAL.get(arma_escolhida)
Dx_comida = classe_info[classe]['dados_recurso']['Comida']
Dx_agua = classe_info[classe]['dados_recurso']['Água']
info_armas_formatado = f"{info_armas['Bonus']} {info_armas['Dano']}"

# Gerar ficha
gerar_info_ficha(classe, raca, atributos_chave, idade, faixa_etaria, atributos_randomizados, talentos_escolhidos, pericias_distribuidas)

#=============================================================================================================================================

# Dicionario de variaveis
vars = {
    "raca": raca,
    "classe": classe,
    "atributos_randomizados": atributos_randomizados,
    "idade": idade,
    "faixa_etaria": faixa_etaria,
    "talentos_escolhidos": talentos_escolhidos,
    "pericias_distribuidas": pericias_distribuidas,
    "equipamentos": equipamentos,
    "arma_escolhida": arma_escolhida,
    "info_armas": info_armas_formatado,
    "Dx_comida": Dx_comida,
    "Dx_agua": Dx_agua
}

# Carrega a imagem da ficha
imagem_entrada = 'Pagina1.jpg'
imagem_saida = 'Pagina1_preenchida.jpg'
imagem = Image.open(imagem_entrada)

# Adicione todas as variáveis à ficha usando as coordenadas
for variavel, cord in coordenadas_pag1.items():
    if variavel == "nivel_talento_cord" or variavel == "talento_cord":
        espacamento = 70  # Defina o valor do espaçamento aqui
        for i, (talento, nivel) in enumerate(talentos_escolhidos.items()):
            if variavel == "talento_cord":
                adicionar_texto_na_ficha(imagem, f"{talento}", cord, espacamento * i)
            elif variavel == "nivel_talento_cord":
                nivel_valor = nivel['Nivel']

                adicionar_texto_na_ficha(imagem, f"{nivel_valor}", cord, espacamento * i)
    elif variavel in ["Força_cord", "Agilidade_cord", "Inteligência_cord", "Empatia_cord"]:
        print(type(atributos_randomizados), atributos_randomizados)
        print(f"variavel: {variavel}")  # Adicione esta linha
        # Obtenha o valor do atributo a partir do seu nome
        valor_atributo = atributos_randomizados[variavel.split('_')[0]]
        adicionar_texto_na_ficha(imagem, str(valor_atributo), cord)


    elif variavel == "info_armas_cord":
        # Obtém as informações da arma em formato '+1 1'
        info_armas_formatado = f"{info_armas['Bonus']} {info_armas['Dano']}"
        # Divide o texto em duas partes
        bonus, dano = info_armas_formatado.split()
        # Defina um espaçamento personalizado
        espacamento = 130
        # Adicione o texto à imagem com o espaçamento personalizado
        adicionar_texto_na_ficha(imagem, bonus, cord, 0)
        adicionar_texto_na_ficha(imagem, dano, (cord[0] + espacamento, cord[1]), 0)


    else:
        # Obtenha a chave correspondente em vars
        chave_vars = mapa_chaves[variavel]
        # Obtenha o valor da variável a partir do seu nome
        valor = vars[chave_vars]
        adicionar_texto_na_ficha(imagem, str(valor), cord)

# Salve a imagem com o texto adicionado
imagem.save(imagem_saida)

# Abra a imagem no navegador padrão
webbrowser.open(imagem_saida)

# Feche a imagem
imagem.close()