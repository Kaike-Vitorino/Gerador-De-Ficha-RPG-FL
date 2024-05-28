from flask import *
import os
from PIL import Image, ImageDraw, ImageFont
import random

def Ficha_Random(numero_xp):
    # Gerar raca aleatoria
    raca, raca_info = gerar_raca()
    print(f"Raca escolhida: {raca}")

    # Gerar classe aleatoria
    #classe = gerar_classe(raca,RACAS_INFO,CLASSES)
    classe = gerar_classe(raca, racas_info, classes)
    print(f"Classe: {classe}")

    # Funcao para obter atributos chave
    atributos_chave = obter_atributos_chave(classe, raca, raca_info)

    # Gerar idade
    idade, faixa_etaria = calcular_idade(raca)

    # Gerar atributos
    atributos_randomizados = escolher_atributos(faixa_etaria, atributos_chave)

    # Gerar pontos de PERICIAS
    pericias_distribuidas = distribuir_pontos_pericia(faixa_etaria, classe)
    print(f"Pericias distribuidas: {pericias_distribuidas}")

    #Gerar armas
    arma_escolhida, armas_escolhidas = gerar_arma(classe)

    # Gerar talentos
    talentos_escolhidos = escolher_talentos(classe, raca, faixa_etaria)
    print(f"Talentos escolhidos:", talentos_escolhidos)

    if numero_xp >= 1:
        print(f"Número de XP extra: {numero_xp}")

        # Aqui você pode usar o número_xp como precisar, por exemplo, passá-lo para a função dividir_XP
        talentos_escolhidos, pericias_distribuidas = dividir_XP(talentos_escolhidos, pericias_distribuidas, classe, pericias, numero_xp)
        print(f"Talentos escolhidos após dividir XP:", talentos_escolhidos)
        print(f"Perícias distribuídas após dividir XP:", pericias_distribuidas)
    else:
        print("Nenhum XP extra escolhido")

    info_armas = None
    info_armas_formatado = None
    if classe != "Rider":
        info_armas = lista_armas_FINAL.get(arma_escolhida)
        info_armas_formatado = f"{info_armas['Bonus']} {info_armas['Dano']}"


    prata_rolada = rolar_dados_prata(classe_info[classe]["dados_recurso"]["Prata"])
    Dx_comida = classe_info[classe]['dados_recurso']['Comida']
    Dx_agua = classe_info[classe]['dados_recurso']['Água']


    if classe == "Rider":
        # Gerar ficha com return
        arma_escolhida_1, arma_escolhida_2, info_arma_1, info_arma_2 = gerar_info_ficha(classe, raca, atributos_chave,
                                                      idade, faixa_etaria, atributos_randomizados, talentos_escolhidos,
                                                                                pericias_distribuidas, armas_escolhidas)
        info_armas_formatado_1 = f"{info_arma_1['Bonus']} {info_arma_1['Dano']}"
        info_armas_formatado_2 = f"{info_arma_2['Bonus']} {info_arma_2['Dano']}"
        bonus_arma_1, dano_arma_1 = info_armas_formatado_1.split()
        bonus_arma_2, dano_arma_2 = info_armas_formatado_2.split()

    else:
        gerar_info_ficha(classe, raca, atributos_chave,idade, faixa_etaria, atributos_randomizados,talentos_escolhidos,
                         pericias_distribuidas, armas_escolhidas)

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

    # Adiocionado todas as PERICIAS que faltaram, para que sejam impressas nivel 0
    pericias_faltando = {pericia: 0 for pericia in pericias.keys() if pericia not in pericias_distribuidas}
    pericias_distribuidas.update(pericias_faltando)
    pericias_distribuidas = {k.lower(): v for k, v in pericias_distribuidas.items()}
    print(pericias_distribuidas)

    if classe != "Rider":
        bonus_arma, dano_arma = info_armas_formatado.split()


#=======================================================================================================================

    #Pagina 1 da ficha

    # Carrega a imagem da ficha
    imagem_entrada = os.path.join(os.path.dirname(__file__), 'static', 'Pagina1.jpg')
    imagem_saida = os.path.join(os.path.dirname(__file__), 'static', 'Pagina1_preenchida.jpg')

    # Verifique se o caminho do arquivo de saída é relativo ao diretório static
    if not imagem_saida.startswith(os.path.join('static', os.sep)):
        imagem_saida = os.path.join('static', imagem_saida)

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
            # Obtenha o valor do atributo a partir do seu nome
            valor_atributo = atributos_randomizados[variavel.split('_')[0]]
            adicionar_texto_na_ficha(imagem, str(valor_atributo), cord)

        elif variavel in ["Potencia_cord", "Resiliência_cord", "Luta_cord", "Artesanato_cord", "Furtividade_cord",
                  "Artimanha_cord", "Movimentação_cord", "Pontaria_cord", "Patrulha_cord", "Tradição_cord",
                  "Sobrevivência_cord", "Discernimento_cord", "Manipulação_cord", "Atuação_cord", "Cura_cord",
                  "Adestramento_cord"]:

            chave_pericia = variavel.replace("_cord", "").lower()  # Remova o sufixo _cord e converta para minúsculas
            valor_pericia = pericias_distribuidas.get(chave_pericia, 1)

            # Adicione um "+" ao valor se for diferente de 0
            valor_formatado = f"+{valor_pericia}"
            adicionar_texto_na_ficha(imagem, valor_formatado, cord)

        elif variavel == "info_armas_cord" and classe != "Rider":
            valor_formatado = f"{bonus_arma}      {dano_arma}"
            adicionar_texto_na_ficha(imagem, valor_formatado, cord)

        elif variavel == "info_armas_cord" and classe == "Rider":
            espacamento = 70
            valor_formatado_1 = f"{bonus_arma_1}      {dano_arma_1}"
            adicionar_texto_na_ficha(imagem, valor_formatado_1, cord)
            valor_formatado_2 = f"{bonus_arma_2}      {dano_arma_2}"
            adicionar_texto_na_ficha(imagem, valor_formatado_2, cord, espacamento)

        elif variavel == "arma_escolhida_cord" and classe == "Rider":
            espacamento = 70
            adicionar_texto_na_ficha(imagem, arma_escolhida_1, cord)
            adicionar_texto_na_ficha(imagem, arma_escolhida_2, cord, espacamento)

        else:
            # Obtenha a chave correspondente em vars
            chave_vars = mapa_chaves[variavel]
            # Obtenha o valor da variável a partir do seu nome
            valor = vars[chave_vars]
            # Verifique se o valor é uma lista ou um dicionário
            if not isinstance(valor, (list, dict)):
                adicionar_texto_na_ficha(imagem, str(valor), cord)

        adicionar_texto_na_ficha(imagem, f"XP inicial: {numero_xp}", (110, 325))

    #Por a armadura do guerreiro na ficha
    if classe == "Guerreiro":
        Armadura_couro_str = ("Couro")
        escrever_armadura(imagem, Armadura_couro_str, coordenadas_armadura)

    #Por na ficha onde a escolha vai ser do jogador ou do mestre
    escolha_do_jogador = 'Escolha do JOGADOR'
    escolha_do_mestre = 'Escolha do MESTRE'
    escrever_texto_em_varias_coordenadas_JOGADOR(imagem, escolha_do_jogador, coordenadas_pag1_User)
    escrever_texto_em_varias_coordenadas_MESTRE(imagem, escolha_do_mestre, coordenadas_pag1_Mestre)

    # Salve a imagem com o texto adicionado
    imagem.save(imagem_saida)

    # Feche a imagem
    imagem.close()

#============================================================================================================================================
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

#============================================================================================================================================
'''
   Modulo responsavel por todas as coordenadas necessarias para ser realizada a impressao na ficha.
'''

# Variavel com as coordenadas simples da pagina 1.
coordenadas_pag1 = {
    "raca_cord": (210, 195),
    "classe_cord": (1560, 195),
    #===== Atributos =====#
    "Força_cord": (275, 515),
    "Agilidade_cord": (275, 615),
    "Inteligência_cord": (275, 715),
    "Empatia_cord": (275, 815),
    #====== Talento =======#
    "talento_cord": (1342, 1135),
    "nivel_talento_cord": (1860, 1135),
    #====== Pericias =======#
    "Potencia_cord": (535, 1632),
    "Resiliência_cord": (535, 1702),
    "Luta_cord": (535, 1772),
    "Artesanato_cord": (535, 1842),
    "Furtividade_cord": (535, 1912),
    "Artimanha_cord": (535, 1982),
    "Movimentação_cord": (535, 2052),
    "Pontaria_cord": (535, 2122),
    "Patrulha_cord": (535, 2192),
    "Tradição_cord": (535, 2262),
    "Sobrevivência_cord": (535, 2332),
    "Discernimento_cord": (535, 2402),
    "Manipulação_cord": (535, 2472),
    "Atuação_cord": (535, 2542),
    "Cura_cord": (535, 2612),
    "Adestramento_cord": (535, 2682),
    #======================#
    "idade_cord": (810, 996),
    "faixa_etaria_cord": (810, 1045),
    "arma_escolhida_cord": (700, 2120),
    "info_armas_cord": (1200, 2120)
    #======================#
}

# Coordenadas de coisas que nao tem uma variavel definida.
coordenadas_armadura = [(790, 1780)]
coordenadas_pag1_User = [(770, 440), (770, 630), (770, 830), (1410, 530), (1410, 680), (1410, 820)]
coordenadas_pag1_Mestre = [(1000, 1030)]

# Variavel com as coordenadas simples da pagina 2.
coordenadas_pag2 = {
    "Dx_comida": (322, 392),
    "Dx_agua": (322, 412),
    "prata_rolada": (322, 432),
    "equipamentos_cord": (322, 332),
}

# Um mapa que mostra qual variavel pertence a qual coordenada.
mapa_chaves = {
    "raca_cord": "raca",
    "classe_cord": "classe",
    "Força_cord": "atributos_randomizados",
    "Agilidade_cord": "atributos_randomizados",
    "Inteligência_cord": "atributos_randomizados",
    "Empatia_cord": "atributos_randomizados",
    "talento_cord": "talentos_escolhidos",
    "nivel_talento_cord": "talentos_escolhidos",
    "idade_cord": "idade",
    "faixa_etaria_cord": "faixa_etaria",
    "equipamentos_cord": "equipamentos",
    "arma_escolhida_cord": "arma_escolhida",
    "info_armas_cord": "info_armas",
    "Potencia_cord": "pericias_distribuidas",
    "Resiliência_cord": "pericias_distribuidas",
    "Luta_cord": "pericias_distribuidas",
    "Artesanato_cord": "pericias_distribuidas",
    "Furtividade_cord": "pericias_distribuidas",
    "Artimanha_cord": "pericias_distribuidas",
    "Movimentação_cord": "pericias_distribuidas",
    "Pontaria_cord": "pericias_distribuidas",
    "Patrulha_cord": "pericias_distribuidas",
    "Tradição_cord": "pericias_distribuidas",
    "Sobrevivência_cord": "pericias_distribuidas",
    "Discernimento_cord": "pericias_distribuidas",
    "Manipulação_cord": "pericias_distribuidas",
    "Atuação_cord": "pericias_distribuidas",
    "Cura_cord": "pericias_distribuidas",
    "Adestramento_cord": "pericias_distribuidas",
}


'''
   Modulo onde todas as funcoes essencias para a confeccao de toda a parte bruta/escrita na ficha.
        Varias variaveis sao declaradas e definidas.
        Aqui tem tudo para sair as infos da ficha inteira so que em forma de texto.
'''

# Declarando essas variveis que vao ser utilizadas em varios locais diferentes.
raca = ""
artefato_musical_escolhido = ""
arma_escolhida = ""
equipamentos = []


# Funcao para gerar raca aleatoria.
def gerar_raca():
    raca_aleatoria = random.choice(racas)
    raca_info = racas_info[raca_aleatoria]
    return raca_aleatoria, raca_info


# Funcao para gerar classe.
def gerar_classe(raca, racas_info, classes):
    classe = random.choice(racas_info[raca]["profissoes_tipicas"])
    return classe


# Funcao para obter os atributos chaves.
def obter_atributos_chave(classe, raca, raca_info):
    atributo_chave_classe = classe_info[classe]["atributo_chave"]
    atributo_chave_raca = raca_info["atributo_chave"]
    # Verifique se os atributos-chave são iguais e crie a lista de atributos.
    atributos_chave = []
    if atributo_chave_classe != atributo_chave_raca:
        atributos_chave.append(atributo_chave_classe)
    atributos_chave.append(atributo_chave_raca)
    return atributos_chave


# Funcao para calcular idade.
def calcular_idade(raca):
    if raca == "Elfo":
        idade = random.randint(26, 1000)
        faixa_etaria = "Adulto"
        return idade, "Adulto"
    else:
        if raca in idade_racas:
            intervalos = idade_racas[raca]
            faixa_etaria = random.choices(list(intervalos.keys()), k=1)[0]
            idade_min, idade_max = intervalos[faixa_etaria]
            print(f"Intervalo de idade encontrado para a raça {raca}.")

            # Verifica se idade_min e idade_max nn sao vazios antes de usar random.randint
            if idade_min is not None and idade_max is not None:
                idade = random.randint(idade_min, idade_max)
                return idade, faixa_etaria

        # Se nn encontrou intervalo de idade para a raca, chama a função novamente (recursão)
        print(f"Intervalo de idade não encontrado para a raça {raca}. Tentando novamente.")
        return calcular_idade(raca)


# Funcao onde os pontos de atributo sao distribuidos e o valor/nivel dos atributos determinados.
def escolher_atributos(faixa_etaria, atributos_chave):
    if faixa_etaria == "Jovem":
        pontos_disponiveis = 15
    elif faixa_etaria == "Adulto":
        pontos_disponiveis = 14
    else:  # Idoso
        pontos_disponiveis = 13

    todos_atributos = ['Força', 'Agilidade', 'Empatia', 'Inteligência']

    atributos_randomizados = {atributo: [0, 5] for atributo in todos_atributos}

    # Distribuir 2 pontos para cada atributo não-chave.
    for atributo in todos_atributos:
        if atributo not in atributos_chave:
            atributos_randomizados[atributo][0] = 2
            pontos_disponiveis -= 2

    # Distribuir pontos igualmente entre os atributos chave.
    pontos_por_atributo_chave = pontos_disponiveis // len(atributos_chave)

    for atributo in atributos_chave:
        atributos_randomizados[atributo][0] = min(pontos_por_atributo_chave, 5)
        pontos_disponiveis -= atributos_randomizados[atributo][0]

    # Distribuir pontos restantes, se houver.
    pontos_restantes = pontos_disponiveis
    atributos_ordenados = list(atributos_randomizados.keys())
    random.shuffle(atributos_ordenados)

    for i in range(pontos_restantes):
        atributo = atributos_ordenados[i]
        pontos_a_adicionar = min(5 - atributos_randomizados[atributo][0], 1)
        atributos_randomizados[atributo][0] += pontos_a_adicionar

    # Adicionar +1 ponto ao atributo-chave se houver apenas um.
    if len(atributos_chave) == 1:
        atributo_chave = atributos_chave[0]
        atributos_randomizados[atributo_chave][0] += 1

    atributos_randomizados = {atributo: valor[0] for atributo, valor in atributos_randomizados.items()}

    return atributos_randomizados


# Funcao para distribuir pontos de pericia.
def distribuir_pontos_pericia(faixa_etaria, classe):
    pontos_disponiveis = 0

    if faixa_etaria == "Jovem":
        pontos_disponiveis = 8
    elif faixa_etaria == "Adulto":
        pontos_disponiveis = 10
    elif faixa_etaria == "Idoso":
        pontos_disponiveis = 12

    pericias_permitidas = classe_info[classe]["PERICIAS"]
    pericias_distribuidas = {pericia: 0 for pericia in pericias_permitidas}

    while pontos_disponiveis > 0:
        pericia = random.choice(pericias_permitidas)
        if pericias_distribuidas[pericia] < 3 and pontos_disponiveis > 0:
            pericias_distribuidas[pericia] += 1
            pontos_disponiveis -= 1

    return pericias_distribuidas


def randomizar_talento_ascendente(raca, talentos_sem_lvl):
    talento_ascendente_sem_lvl = racas_info[raca]["talento_ascendente"]
    talentos_sem_lvl.append(talento_ascendente_sem_lvl)
    # print(f"Talento ascendente:", talentos_sem_lvl)
    return talentos_sem_lvl


# Funcao para randomizar talento
def randomizar_talento_classe(classe, talentos_sem_lvl):
    if classe in talentos_classes:
        # print(f"Talentos para a classe {classe} encontrados.")
        talentos_disponiveis = talentos_classes[classe]
        talento_escolhido_classe_sem_lvl = random.choice(talentos_disponiveis)
        talentos_sem_lvl.append(talento_escolhido_classe_sem_lvl)
        # print(f"Talento de classe:", talento_escolhido_classe_sem_lvl)
        return talentos_sem_lvl
    else:
        # print(f"Talentos para a classe {classe} não encontrados. Tentando novamente.")
        return randomizar_talento_classe(classe)


# Funcao para randomizar talentos gerais.
def randomizar_talentos_gerais(faixa_etaria, classe, nivel, talentos_sem_lvl):
    quantidade_talentos = 0

    if faixa_etaria == "Jovem":
        quantidade_talentos = 1
    elif faixa_etaria == "Adulto":
        quantidade_talentos = 2
    elif faixa_etaria == "Idoso":
        quantidade_talentos = 3

    # Declaração do dicionário para armazenar talentos escolhidos
    talentos_escolhidos = {}

    # Randomiza se vai ter 1 talento sacrificado ou não
    # Se um talento eh sacrificado na criacao da ficha, ele tem direito de subir outro talento para o lvl2
    talento_sacrificado = random.choice([True, False])
    # print(f"Talento sacrificado: {talento_sacrificado}")

    if talento_sacrificado:
        talentos_atuais_escolhidos = None

        if faixa_etaria == "Jovem" or faixa_etaria == "Adulto":
            # Escolhe os talentos com 1 a menos do que o necessário
            talentos_atuais_escolhidos = random.sample(talentos_gerais[classe], quantidade_talentos - 1)
            talentos_sem_lvl.extend(talentos_atuais_escolhidos)

        else:  # Idoso
            # Escolhe qual dos dois talentos vai ser nivel 2
            talentos_gerais_escolhidos_sem_lvl = list(
                random.sample(talentos_gerais[classe], quantidade_talentos - 1))

            talentos_sem_lvl.extend(talentos_gerais_escolhidos_sem_lvl)

        talento_nivel_2 = random.choice(talentos_sem_lvl)
        talentos_sem_lvl.remove(talento_nivel_2)

        # Add o talento nivel 2 no dicionário de talentos escolhidos
        talentos_escolhidos[talento_nivel_2] = {"Nivel": nivel + 1}

        # Adiciona os talentos de nivel 1 ao dicionário de talentos escolhidos
        for talento in talentos_sem_lvl:
            talentos_escolhidos[talento] = {"Nivel": nivel}

        # print(f"Talento geral:", talentos_atuais_escolhidos)

    else:  # Adicionando os talentos de nivel 1 ao dicionário com o nivel especificado
        talentos_gerais_escolhidos = random.sample(talentos_gerais[classe], quantidade_talentos)
        talentos_sem_lvl.extend(talentos_gerais_escolhidos)
        for talento in talentos_sem_lvl:
            talentos_escolhidos[talento] = {"Nivel": nivel}

        # print(f"Talento geral:", talentos_gerais_escolhidos)

    return talentos_escolhidos


# Funcao para adicionar os talentos na ficha.
# Funcao central dos talentos. Essa funcao puxa as outras 3 funcoes acima e juntas elas em uma logica para conseguir uma quantidade de talentos balanceados.
def escolher_talentos(classe, raca, faixa_etaria):
    talentos = []
    talentos_sem_lvl = []
    nivel = 1

    # Adicionando talento ascendente da raca.
    talentos_sem_lvl = randomizar_talento_ascendente(raca, talentos_sem_lvl)
    # print(f"Talento ascendente: {talentos_sem_lvl}")

    # Chama a funcao que randomiza talento da classe.
    talentos_sem_lvl = randomizar_talento_classe(classe, talentos_sem_lvl)
    # print(f"Talento da classe: {talentos_sem_lvl}")

    # Chama a funcao que randomiza os talentos gerais.
    talentos_escolhidos = randomizar_talentos_gerais(faixa_etaria, classe, nivel, talentos_sem_lvl)

    return talentos_escolhidos


# Funcao para rolar o numero de dados da prata, ja q ela eh dada em string eh necessario fazer dessa forma pra nn sumir com o "D"
def rolar_dados_prata(dados_str):
    if dados_str.startswith("D"):
        num_faces = int(dados_str[1:])
        return random.randint(1, num_faces)
    else:
        return 0


# Funcao onde a arma do personagem eh gerada
# Ela vai puxar as infos das CLASSES e randomizar uma arma dentre as opcoes dadas para cada classe.
# A classe rider tem 2 armas esclhidas, por conta disso a variavel de arma dessa classe eh diferente.
def gerar_arma(classe):
    # Escolhendo arma
    global artefato_musical_escolhido, arma_escolhida
    armas_disponiveis = classe_info[classe]["equipamentos"]["Arma"]
    arma_escolhida = None
    armas_escolhidas = None

    # Verificar se a classe tem armas disponíveis
    if armas_disponiveis:
        if classe == "Rider":
            armas_escolhidas = random.sample(armas_disponiveis, 2)
            arma_escolhida = None

            while ["Lança", "Machadinha"] in armas_escolhidas or ["Arco Curto", "Funda"] in armas_escolhidas:
                armas_escolhidas = random.sample(armas_disponiveis, 2)

            # Se chegou aqui, então as armas escolhidas são válidas
            equipamentos.extend(armas_escolhidas)

        elif classe == "Bardo":
            armas_escolhidas = None
            arma_escolhida = classe_info[classe]["equipamentos"]["Arma"][0]  # Pega o primeiro item da lista
            artefato_musical_disponiveis = classe_info[classe]["equipamentos"]["Artefato Musical"]
            artefato_musical_escolhido = random.choice(artefato_musical_disponiveis)

            equipamentos.insert(0, arma_escolhida)
            equipamentos.insert(1, artefato_musical_escolhido)

        elif classe == "Guerreiro":
            armas_escolhidas = None
            arma_escolhida = random.choice(armas_1m_lista)
            equipamentos.append(arma_escolhida)

        else:
            armas_escolhidas = None
            arma_escolhida = random.choice(armas_disponiveis)
            equipamentos.append(arma_escolhida)

        if arma_escolhida != None:
            print(f"Arma escolhida 1 etapa: {arma_escolhida}")
        else:
            print(f"Armas escolhidas 1 etapa: {armas_escolhidas}")

        if arma_escolhida in ["Arco"]:
            arma_escolhida = random.choice(["Arco Curto", "Arco Longo"])
            equipamentos.remove("Arco")
            equipamentos.append(arma_escolhida)

        elif arma_escolhida in ["Lança"]:
            # Escolhendo um dos tipos de Lanças possíveis
            arma_escolhida = random.choice(["Lança Curta", "Lança Longa"])
            equipamentos.remove("Lança")
            equipamentos.append(arma_escolhida)

        if arma_escolhida != None:
            print(f"Arma escolhida 2 etapa: {arma_escolhida}")
        else:
            print(f"Armas escolhidas 2 etapa: {armas_escolhidas}")

        if "artefato_musical" in equipamentos:
            print(f"Artefato musical escolhido: {artefato_musical_escolhido}")

    return arma_escolhida, armas_escolhidas


# Inicializando um dicionario vazio para mapear os talentos e os niveis deles.
talentos_e_niveis = {}


# Funcao para distribuir XP.
# Se o usuario disse que quer dar XPs extras para uma ficha, essa funcao fica responsavel por receber a quantidade e dividir nas ficha.
def dividir_XP(talentos_escolhidos, pericias_distribuidas, classe, pericias, numero_xp):
    try:
        pontos_xp = numero_xp
    except ValueError:
        print("Digite um número inteiro válido.")
        return dividir_XP(talentos_escolhidos, pericias_distribuidas, classe, pericias, numero_xp)

    # Declarando lista de PERICIAS e talentos para o while que vai acontecer
    pericias_disponiveis = list(pericias.keys())
    talentos_disponiveis = list(talentos_gerais[classe])

    # Variáveis para controlar se todas as opções estão no máximo
    todas_pericias_maximo = False
    todos_talentos_maximo = False
    pericias_disponiveis_para_aumentar = False
    talentos_disponiveis_para_aumentar = False

    while pontos_xp > 0:
        opcoes = [
            "Perícia nova",
            "Talento novo",
            "Aumentar nivel de perícia",
            "Aumentar nivel de talento"
        ]

        escolha = random.choice(opcoes)

        if escolha == "Perícia nova":
            custo = 5
            if not pericias_disponiveis:
                print("Todas as perícias estão distribuídas. Escolhendo novamente.")
                todas_pericias_maximo = True
                continue  # Pule esta iteração do loop
            nova_pericia = random.choice(pericias_disponiveis)

            pericias_disponiveis.remove(nova_pericia)
            pericias_distribuidas[nova_pericia] = 1

        elif escolha == "Talento novo":
            custo = 3
            if not talentos_disponiveis:
                print("Todos os talentos disponíveis já foram escolhidos. Escolhendo novamente.")
                todos_talentos_maximo = True
                continue  # Pule esta iteração do loop
            novo_talento = random.choice(talentos_disponiveis)

            talentos_disponiveis.remove(novo_talento)
            talentos_escolhidos[novo_talento] = {"Nivel": 1}

        elif escolha == "Aumentar nivel de perícia":
            custo = 0
            pericias_disponiveis_para_aumentar = [pericia for pericia, nivel in pericias_distribuidas.items() if
                                                  nivel < 3]

            if not pericias_disponiveis_para_aumentar:
                print("Todas as perícias estão no nível máximo. Escolhendo novamente.")
                talentos_disponiveis_para_aumentar = True
                continue  # Pula esta iteração do loop

            pericia_aumentar = random.choice(pericias_disponiveis_para_aumentar)
            nivel_pericia = pericias_distribuidas[pericia_aumentar]
            custo = 5 * nivel_pericia  # Custo é 5 vezes o nível atual da perícia
            # Aumente o nível da perícia
            pericias_distribuidas[pericia_aumentar] += 1

        elif escolha == "Aumentar nivel de talento":
            custo = 0
            talentos_disponiveis_para_aumentar = [talento for talento, info in talentos_escolhidos.items() if
                                                  info["Nivel"] < 3]

            if not talentos_disponiveis_para_aumentar:
                print("Todos os talentos estão no nível máximo. Escolhendo novamente.")
                pericias_disponiveis_para_aumentar = True
                continue  # Pula esta iteração do loop

            talento_aumentar = random.choice(talentos_disponiveis_para_aumentar)
            nivel_talento = talentos_escolhidos[talento_aumentar]["Nivel"]
            custo = 3 * nivel_talento
            talentos_escolhidos[talento_aumentar]["Nivel"] += 1

        pontos_xp -= custo

        if todas_pericias_maximo and todos_talentos_maximo and pericias_disponiveis_para_aumentar and talentos_disponiveis_para_aumentar:
            print("Sua ficha está no nível máximo, não é necessário mais XP")
            break

    return talentos_escolhidos, pericias_distribuidas


# Funcao para gerar informacoes da ficha
# Essa funcao junta todas as informacoes que foram dadas pelas outras funcoes e dessa forma gera a ficha inteira em texto.
def gerar_info_ficha(classe, raca, atributos_chave, idade, faixa_etaria, atributos_randomizados, talentos_escolhidos,
                     pericias_distribuidas, armas_escolhidas):
    # Rolando quantidade de prata
    prata_rolada = rolar_dados_prata(classe_info[classe]["dados_recurso"]["Prata"])
    print(f"prata: {prata_rolada}")

    # Randomizador de itens da lista de itens de comercio
    quantidade_itens = classe_info[classe]["equipamentos"][
        "Itens"]  # Verifica a quantidade de itens que o personagem pode ter
    print(f"quantidade_itens: {quantidade_itens}")

    if arma_escolhida in ["Arco Curto", "Arco Longo"]:
        # Vai ser randomizado todos os itens, inclusive as duas flechas que são os 2 itens iniciais da lista de comercio
        itens_randomizados = random.sample(itens_comercio, quantidade_itens)  # Randomiza eles
        equipamentos.extend(itens_randomizados)  # adiciona eles nos equipamentos

    elif armas_escolhidas in ["Arco Curto", "Arco Longo"]:
        # Vai ser randomizado todos os itens, inclusive as duas flechas que são os 2 itens iniciais da lista de comercio
        itens_randomizados = random.sample(itens_comercio, quantidade_itens)  # Randomiza eles
        equipamentos.extend(itens_randomizados)  # adiciona eles nos equipamentos

    else:
        itens_randomizados = random.sample(itens_comercio[2:],
                                           quantidade_itens)  # Randomiza eles só que como não tem o arco, ele não considera os 2 itens de flechas
        equipamentos.extend(itens_randomizados)  # adiciona eles nos equipamentos

    print(f"itens_randomizados: {itens_randomizados,}")

    # Criando variaveis Necessarias
    cavalo = classe_info[classe]["equipamentos"]["Cavalo"]
    armadura_disponivel = classe_info[classe]["equipamentos"]["Armadura"]
    info_armaduras = lista_armaduras.get("armadura_disponivel")
    Dx_comida = classe_info[classe]['dados_recurso']['Comida']
    Dx_agua = classe_info[classe]['dados_recurso']['Água']
    armas_escolhidas_1 = None
    armas_escolhidas_2 = None

    # Printando a ficha do personagem
    print("\n--- Ficha do personagem ---")
    print(f"Raça: {raca}")
    print(f"Classe: {classe}")
    print(f"=============================")
    print(f"Atributo(s) Chave: {atributos_chave}")
    print(f"Atributos: {atributos_randomizados}")
    print(f"=============================")
    print(f"Idade: {idade}")
    print(f"Faixa etaria: {faixa_etaria}")
    print(f"=============================")
    print(f"Talentos :")
    for talento, info in talentos_escolhidos.items():
        print(f"{talento} - nivel {info['Nivel']}")
    print(f"=============================")
    print(f"Perícias: {pericias_distribuidas}")
    print(f"=============================")
    print(f"Equipamentos: {', '.join(equipamentos)}")
    # Dividindo a variavel arma escolhida em dois ja que o Rider tem duas armas
    if classe == "Rider":
        armas_escolhidas_1, armas_escolhidas_2 = armas_escolhidas  # Separando a variavel em 2

        info_arma_1 = lista_armas_FINAL.get(armas_escolhidas_1)  # Criando as infos de cada
        info_arma_2 = lista_armas_FINAL.get(armas_escolhidas_2)  # Criando as infos de cada

        print(f"Sua 1º arma:", armas_escolhidas_1)
        print(f"Infos da sua 1º arma:", info_arma_1)
        print(f"Sua 2º arma: ", armas_escolhidas_2)
        print(f"Infos da sua 2º arma:", info_arma_2)

    else:
        info_armas = lista_armas_FINAL.get(arma_escolhida)
        print(f"Sua arma:", arma_escolhida)
        print(f"Infos da sua arma:", info_armas)

    if armadura_disponivel != None:
        print(f"Sua armadura: {armadura_disponivel}")
        print(f"Infos da armadura: {info_armaduras}")

    if cavalo != None:
        print("Voce tem um cavalo")
        print("Essas sao as infos da sua montaria: ")
        # Forca: 5 Agilidade: 4 |Pericias: Movimentacao: +2 Patrulha: +3 |Dano: 1

    if artefato_musical_escolhido != None:
        print(f"Seu instrumento: ", artefato_musical_escolhido)
    print(f"Comida: {Dx_comida}")
    print(f"Água: {Dx_agua}")

    if "Arco Curto" in equipamentos or "Arco Longo" in equipamentos:
        print("Flecha: D10")

    print(f"Prata: {prata_rolada}")
    print("--------------------------\n")

    if classe == "Rider":
        return armas_escolhidas_1, armas_escolhidas_2, info_arma_1, info_arma_2

#============================================================================================================================================
'''
   Modulo com todas as informacoes, listas da maior parte dos itens e armas do sistema.
'''

# Declarando variavel equipamente para que no futuro seja completa com os itens do personagem a ser gerado.
equipamentos = []

# Lista de itens de comercio - pagina 182.
itens_comercio = [
    "Flechas, Ponta de Ferro", "Flechas, Ponta de Madeira", "Aljava", "Arpéu",
    "Corda, 10 Metros", "Vela de Sebo", "Lamparina a Óleo", "Lanterna", "Tochas",
    "Saco", "Mochila", "Cantil", "Bandagens", "Óleo de Lâmpada", "Pena e Tinta",
    "Pergaminho", "Cobertor", "Cobertor de Peles", "Pederneira", "Gazuas",
    "Cozinha de Campo", "Caldeirão", "Cálice de Metal", "Caneca", "Prato de Metal",
    "Faca de Cozinha", "Colher", "Armadilha de Urso", "Armadilha de Laço", "Barril",
    "Jarra", "Tenda Pequena", "Tenda Grande", "Anzol e Linha", "Rede de Pesca",
    "Lupa", "Símbolo Sagrado", "Giz", "Mapa", "Luneta", "Bola de Cristal",
    "Ampulheta", "Balança", "Flauta", "Berrante", "Lira", "Harpa", "Tambor",
    "Veneno Letal/Antídoto", "Veneno Paralisante/Antídoto", "Veneno Sonífero/Antídoto", "Veneno Alucinógeno/Antídoto"
]

# Declarando variavel aqui pq por algum motivo/bug eu nn conseguia declarar ela na func da linha 193 do modulo util.
arma_escolhida = ""
artefato_musical_escolhido = None

'''
    Quando esta escrito um numero x com um M do lado (xM)
        Exemplo: 1M.
    Significa qual a quantidade de maos necessarias para empunhar aquelas arma/item.
'''

# Dicionario de armas com empunhadura 1M.
armas_1m = {
    "Faca": {"Bonus": "+1", "Dano": "1"},
    "Adaga": {"Bonus": "+1", "Dano": "1"},
    "Facão": {"Bonus": "+2", "Dano": "2"},
    "Espada Curta": {"Bonus": "+2", "Dano": "1"},
    "Espada Larga": {"Bonus": "+2", "Dano": "2"},
    "Espada Longa": {"Bonus": "+2", "Dano": "2"},
    "Cimitarra": {"Bonus": "+1", "Dano": "2"},
    "Machadinha": {"Bonus": "+2", "Dano": "2"},
    "Machado de Batalha": {"Bonus": "+2", "Dano": "2"},
    "Maça": {"Bonus": "+2", "Dano": "1"},
    "Maça Estrela": {"Bonus": "+2", "Dano": "2"},
    "Martelo de Guerra": {"Bonus": "+2", "Dano": "2"},
    "Mangual": {"Bonus": "+1", "Dano": "2"},
    "Porrete": {"Bonus": "+1", "Dano": "1"},
    "Lança Curta": {"Bonus": "+1", "Dano": "1"},
    "Tridente": {"Bonus": "+1", "Dano": "2"},
}

# Dicionario de armas com empunhadura 2M.
armas_2m = {
    "Montante": {"Bonus": "+3", "Dano": "3"},
    "Machado de Duas Mãos": {"Bonus": "+2", "Dano": "3"},
    "Clava": {"Bonus": "+1", "Dano": "2"},
    "Malho": {"Bonus": "+2", "Dano": "3"},
    "Bastão": {"Bonus": "+1", "Dano": "1"},
    "Lança Longa": {"Bonus": "+2", "Dano": "1"},
    "Pique": {"Bonus": "+2", "Dano": "2"},
    "Alabarda": {"Bonus": "+2", "Dano": "2"},
}

# Os 2 dicionarios de armas juntos.
lista_armas = {**armas_1m, **armas_2m}

# Dicionario de armas a distância com empunhadura 1M.
armas_distancia_1m = {
    "Pedra": {"Bonus": "+0", "Dano": "1"},
    "Faca de Arremesso": {"Bonus": "+1", "Dano": "1"},
    "Machado de Arremesso": {"Bonus": "+1", "Dano": "2"},
    "Azagaia": {"Bonus": "+2", "Dano": "1"},
    "Funda": {"Bonus": "+1", "Dano": "1"},
}

# Dicionario de armas a distância com empunhadura 2M.
armas_distancia_2m = {
    "Arco Curto": {"Bonus": "+2", "Dano": "1"},
    "Arco Longo": {"Bonus": "+2", "Dano": "1"},
    "Besta Leve": {"Bonus": "+1", "Dano": "2"},
    "Besta Pesada": {"Bonus": "+1", "Dano": "3"},
}

# Juntando os dicionarios das armas1M a distancia e as normais.
lista_todas_armas_1m = {**armas_1m, **armas_distancia_1m}

# Juntando os dois dicionarios de armas a distancia.
lista_armas_a_distancia = {**armas_distancia_1m, **armas_distancia_2m}

# Juntando todos os dicionarios de armas.
lista_armas_FINAL = {**lista_armas_a_distancia, **lista_armas}

# Dicionario de Escudos.
lista_escudos = {
    "Escudo Pequeno": {"Bonus": "+1"},
    "Escudo Grande": {"Bonus": "+2"},
}

# Dicionario de Armaduras e Elmos.
lista_armaduras = {
    "Couro": {"Valor de Armadura": "2", "Parte do Corpo": "Corpo"},
    "Couro Batido": {"Valor de Armadura": "3", "Parte do Corpo": "Corpo"},
    "Cota de Malha": {"Valor de Armadura": "6", "Parte do Corpo": "Corpo"},
    "Armadura de Placas": {"Valor de Armadura": "8", "Parte do Corpo": "Corpo"},
    "Capuz de Couro Batido": {"Valor de Armadura": "1", "Parte do Corpo": "Cabeça"},
    "Elmo Aberto": {"Valor de Armadura": "2", "Parte do Corpo": "Cabeça"},
    "Elmo Fechado": {"Valor de Armadura": "3", "Parte do Corpo": "Cabeça"},
    "Grande Elmo": {"Valor de Armadura": "4", "Parte do Corpo": "Cabeça"},
}
#============================================================================================================================================
'''
   Modulo com todas informacoes de todas as CLASSES.
'''

# Lista q contem as todas as CLASSES.
classes = ["Caçador", "Druida", "Mago", "Rider", "Guerreiro", "Ladino", "Mascate", "Bardo"]

# Infos da classe/profissoes.
classe_info = {
    "Caçador": {
        "atributo_chave": "Agilidade",
        "PERICIAS": ["Furtividade", "Movimentação", "Pontaria", "Patrulha", "Sobrevivência"],
        "equipamentos": {
            "Arma": ["Arco", "Funda"],
            "Armadura": None,
            "Itens": 2,
            "Artefato Musical": None,
            "Cavalo": 0
        },
        "dados_recurso": {"Comida": "D8", "Água": "D8", "Flechas": "D10", "Prata": "D6"}
    },
    "Druida": {
        "atributo_chave": "Inteligência",
        "PERICIAS": ["Resiliência", "Sobrevivência", "Discernimento", "Cura", "Adestramento"],
        "equipamentos": {
            "Arma": ["Bastão", "Faca"],
            "Armadura": None,
            "Itens": 1,
            "Artefato Musical": None,
            "Cavalo": 0
        },
        "dados_recurso": {"Comida": "D8", "Água": "D8" , "Prata": "D6"}
    },
    "Mago": {
        "atributo_chave": "Inteligência",
        "PERICIAS": ["Artesanato", "Artimanha", "Tradição", "Discernimento", "Manipulação"],
        "equipamentos": {
            "Arma": ["Bastão", "Faca"],
            "Armadura": None,
            "Itens": 1,
            "Artefato Musical": None,
            "Cavalo": 0
        },
        "dados_recurso": {"Comida": "D6", "Água": "D8" , "Prata": "D8"}
    },
    "Rider": {
        "atributo_chave": "Agilidade",
        "PERICIAS": ["Resiliência", "Luta", "Pontaria", "Sobrevivência", "Adestramento"],
        "equipamentos": {
            "Arma": ["Lança Curta", "Machadinha","Arco Curto", "Funda"],
            "Armadura": None,
            "Itens": 1,
            "Artefato Musical": None,
            "Cavalo": 1
        },
        "dados_recurso": {"Comida": "D8", "Água": "D8", "Flechas": "D10", "Prata": "D6"}
    },
    "Guerreiro": {
        "atributo_chave": "Força",
        "PERICIAS": ["Potência", "Resiliência", "Luta", "Movimentação"],
        "equipamentos": {
            "Arma": armas_1m,
            "Armadura": "Couro",
            "Itens": 1,
            "Artefato Musical": None,
            "Cavalo": 0
        },
        "dados_recurso": {"Comida": "D8", "Água": "D6", "Prata": "D6"}
    },
    "Ladino": {
        "atributo_chave": "Agilidade",
        "PERICIAS": ["Luta", "Furtividade", "Artimanha", "Movimentação", "Manipulação"],
        "equipamentos": {
            "Arma": ["Adaga"],
            "Armadura": None,
            "Itens": 2,
            "Artefato Musical": None,
            "Cavalo": 0
        },
        "dados_recurso": {"Comida": "D6", "Água": "D6", "Prata": "D10"}
    },
    "Mascate": {
        "atributo_chave": "Empatia",
        "PERICIAS": ["Artesanato", "Artimanha", "Patrulha", "Discernimento", "Manipulação"],
        "equipamentos": {
            "Arma": ["Faca"],
            "Armadura": None,
            "Itens": 3,
            "Artefato Musical": None,
            "Cavalo": 0
        },
        "dados_recurso": {"Comida": "D8", "Água": "D8", "Prata": "D12"}
    },
    "Bardo": {
        "atributo_chave": "Empatia",
        "PERICIAS": ["Tradição", "Discernimento", "Manipulação", "Atuação", "Cura"],
        "equipamentos": {
            "Arma": ["Faca"],
            "Armadura": None,
            "Itens": 1,
            "Artefato Musical": ["Lira", "flauta"],
            "Cavalo": 0
        },
        "dados_recurso": {"Comida": "D8", "Água": "D6", "Prata": "D8"}
    }
}

# Dicionario de talentos das CLASSES.
talentos_classes = {
    "Caçador": ["Caminho da Fera", "Caminho da Flecha", "Caminho da Floresta"],
    "Druida": ["Caminho da Cura", "Caminho da Visão", "Caminho do Metamorfo"],
    "Mago": ["Caminho da Morte", "Caminho das Rochas", "Caminho do Sangue", "Caminho dos Símbolos"],
    "Rider": ["Caminho das Planícies", "Caminho do Cavaleiro", "Caminho do Companheiro"],
    "Guerreiro": ["Caminho da Lâmina", "Caminho do Escudo", "Caminho do Inimigo"],
    "Ladino": ["Caminho do Matador", "Caminho do Rosto", "Caminho do Veneno"],
    "Mascate": ["Caminho da Mentira", "Caminho das Muitas Coisas", "Caminho do Ouro"],
    "Bardo": ["Caminho da Canção", "Caminho do Grito de Guerra", "Caminho do Hino"]
}

# Dicionario de armas de 1m (que so precisa empunhar com uma mao).
# Tive que declarar somente ela dessa forma pq o guerreiro eh o unico que usa ela.
armas_1m_lista = list(lista_todas_armas_1m.keys())
#============================================================================================================================================

'''
   Modulo com todas informacoes de todas as RACAS.
'''

# Variavel Lista q contem as RACAS.
racas = ["Humano", "Elfo", "Anão", "Goblin", "Orc", "Meio-Elfo", "Halfling", "Lupino"]

# Dicionário que armazena informações sobre as raças.
racas_info = {
    "Humano": {"atributo_chave": "Empatia", "talento_ascendente": "Adaptive", "profissoes_tipicas": classes},
    "Meio-Elfo": {"atributo_chave": "Inteligência", "talento_ascendente": "Poder mental", "profissoes_tipicas": ["Druida", "Mago", "Ladino"]},
    "Anão": {"atributo_chave": "Força", "talento_ascendente": "Bravura Indômita", "profissoes_tipicas": ["Guerreiro", "Mascate", "Bardo"]},
    "Halfling": {"atributo_chave": "Empatia", "talento_ascendente": "Difícil de Acertar", "profissoes_tipicas": ["Bardo", "Mascate", "Ladino"]},
    "Lupino": {"atributo_chave": "Agilidade", "talento_ascendente": "Instinto de Caça", "profissoes_tipicas": ["Caçador", "Druida", "Guerreiro"]},
    "Orc": {"atributo_chave": "Força", "talento_ascendente": "Imbatível", "profissoes_tipicas": ["Caçador", "Guerreiro", "Ladino"]},
    "Goblin": {"atributo_chave": "Agilidade", "talento_ascendente": "Noturno", "profissoes_tipicas": ["Caçador", "Rider", "Ladino"]},
    "Elfo": {"atributo_chave": "Agilidade", "talento_ascendente": "Paz Interior", "profissoes_tipicas": ["Caçador", "Druida", "Bardo"]}
}

# Dicionário com as idades para cada raça.
idade_racas = {
    "Humano": {"Jovem": (16, 25), "Adulto": (26, 50), "Idoso": (51, 80)},
    "Meio-Elfo": {"Jovem": (16, 30), "Adulto": (31, 100), "Idoso": (101, 180)},
    "Anão": {"Jovem": (20, 40), "Adulto": (41, 80), "Idoso": (81, 121)},
    "Halfling": {"Jovem": (16, 25), "Adulto": (26, 60), "Idoso": (61, 98)},
    "Lupino": {"Jovem": (13, 20), "Adulto": (21, 40), "Idoso": (41, 65)},
    "Orc": {"Jovem": (13, 20), "Adulto": (21, 45), "Idoso": (46, 70)},
    "Goblin": {"Jovem": (16, 25), "Adulto": (26, 60), "Idoso": (61, 95)},
    "Elfo": {"Adulto": (26, 1000)}  # Elfos sempre são adultos.
}
#============================================================================================================================================
'''
   Modulo com todas a parte dos status do personagem.
        Todas os atributos, skills, PERICIAS, talentos e etc.
'''

# Variavel lista com os atributos.
atributos = {
    'Força': [0, 5],
    'Agilidade': [0, 5],
    'Inteligência': [0, 5],
    'Empatia': [0, 5]
}

# Dicionario mapeando as PERICIAS e atributos correspondentes.
pericias = {
    "Potência": "Força", "Resiliência": "Força", "Luta": "Força", "Artesanato": "Força", "Furtividade": "Agilidade",
    "Artimanha": "Agilidade", "Movimentação": "Agilidade", "Pontaria": "Agilidade", "Patrulha": "Inteligência",
    "Tradição": "Inteligência", "Sobrevivência": "Inteligência", "Discernimento": "Inteligência", "Manipulação": "Empatia",
    "Atuação": "Empatia", "Cura": "Empatia", "Adestramento": "Empatia"
}

# Dicionario de talentos gerais e qual classe pode ter cada um.
talentos_gerais = {
    "Caçador": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
                "Sangue frio", "Saque rapido", "Sortudo", "Aquartelador", "Arremessador", "Cozinheiro", "Defensor",
                "Atirador preciso", "Atirador veloz", "Desbravador", "Herbalista", "Marinheiro", "Mestre da Caçada",
                "Pés ligeiros", "Pescador", "Sexto sentido"],

    "Druida": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
               "Sangue frio", "Saque rapido", "Sortudo", "Andarilho", "Aquartelador", "Cozinheiro", "Defensor",
               "Mestre em facas","Desbravador", "Destemido", "Herbalista", "Incorruptível", "Marinheiro",
               "Mestre da Caçada", "Pescador"],

    "Mago": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
             "Sangue frio", "Saque rapido", "Sortudo", "Arremessador", "Arrombador", "Artífice de arcos", "Cozinheiro",
             "Curtidor", "Destemido", "Envenenador", "Ferreiro", "Incorruptível", "Língua afiada", "Mestre em facas"],

    "Rider": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
              "Mestre em lanças","Sangue frio", "Saque rapido", "Sortudo", "Andarilho", "Aquartelador", "Desbravador",
              "Herbalista","Atirador preciso","Atirador veloz", "Investida", "Lutador", "Marinheiro", "Mestre da Caçada",
              "Mestre da montaria", "Pés ligeiros", "Pescador","Mestre em machados"],

    "Guerreiro": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
                  "Sangue frio", "Saque rapido", "Sortudo", "Ameaçador", "Andarilho", "Aquartelador", "Defensor","Investida",
                  "Lutador", "Atirador preciso", "Atirador veloz", "Mestre em lanças", "Mestre em machados", "Mestre em espadas",
                  "Mestre em facas", "Mestre em martelos"],

    "Ladino": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
               "Sangue frio", "Saque rapido", "Sortudo", "Arrombador", "Defensor", "Investida", "Língua afiada",
               "Lutador", "Pés ligeiros", "Mestre em facas"],

    "Mascate": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
                "Sangue frio", "Saque rapido", "Sortudo", "Arrombador", "Artífice de arcos", "Curtidor", "Destemido",
                "Envenenador", "Ferreiro", "Incorruptível", "Língua afiada", "Sexto sentido", "Mestre em facas"],

    "Bardo": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
              "Sangue frio", "Saque rapido", "Sortudo", "Artífice de arcos", "Cozinheiro", "Curtidor", "Defensor",
              "Desbravador", "Destemido", "Herbalista", "Incorruptível", "Língua afiada", "Mestre em facas"],
}
#============================================================================================================================================
app = Flask(__name__)

# Obtenha o diretório do script atual
diretorio_atual = os.path.dirname(os.path.realpath(__file__))

@app.route('/')
def index():
    return render_template('index.html', ficha_gerada=False)

@app.route('/generate', methods=['POST'])
def generate():
    # Obtenha o número de XP do formulário
    numero_xp = int(request.form['xp'])

    # Chame sua função para criar a imagem
    Ficha_Random(numero_xp)

    # Construa o caminho para o arquivo Pagina1_preenchida.jpg no diretório static
    filename = 'Pagina1_preenchida.jpg'
    path = os.path.join(app.root_path, 'static', filename)

    # Use send_file para enviar a imagem como resposta
    return render_template('index.html', ficha_gerada=True)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)