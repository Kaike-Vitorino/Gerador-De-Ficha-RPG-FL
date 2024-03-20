from FICHA_Funcoes import *
from FICHA_coordenadas import *
import webbrowser
from FUNCOES_geral import *
from PIL import Image

'''
   Modulo onde eh feito a funcao PRINCIPAL.
        Aqui se puxa todas as outras funcoes de todos os outros modulos e faz a ficha inteira.
        Desde consegui todas as infos da ficha e ela escrita, quanto a edicao e o print do arquivo da ficha.
'''
def Ficha_Random():
    # Gerar raca aleatoria
    raca, raca_info = gerar_raca()
    print(f"Raca escolhida: {raca}")

    # Declarando variaveis globais que vao ser usador posteriormente
    global bonus_arma, dano_arma, bonus_arma_1, dano_arma_1, dano_arma_2, bonus_arma_2, arma_escolhida_1, arma_escolhida_2

    # Gerar classe aleatoria
    classe = gerar_classe(raca, RACAS_INFO, CLASSES)
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

    '''
    if classe == "Rider":
        armas_escolhidas = gerar_arma(classe)
        print(f"arma_escolhida_final: {armas_escolhidas}")
    else:
        arma_escolhida = gerar_arma(classe)
        print(f"arma_escolhida_final: {arma_escolhida}")'''

    # Gerar talentos
    talentos_escolhidos = escolher_talentos(classe, raca, faixa_etaria)
    print(f"Talentos escolhidos:", talentos_escolhidos)

    # Dividir XP
    vai_ter_xp_escolha = input(f"Vai ter algum xp extra para essa ficha? s/n\n")
    vai_ter_xp_escolha = (vai_ter_xp_escolha).lower()
    if vai_ter_xp_escolha == "s":
        talentos_escolhidos, pericias_distribuidas = dividir_XP(talentos_escolhidos, pericias_distribuidas, classe, PERICIAS)
        print(f"Talentos escolhidos após dividir XP:", talentos_escolhidos)
        print(f"Pericias distribuidas após dividir XP:", pericias_distribuidas)
    else:
        pass

    info_armas = None
    info_armas_formatado = None
    if classe != "Rider":
        info_armas = LISTA_ARMAS_FINAL.get(arma_escolhida)
        info_armas_formatado = f"{info_armas['Bonus']} {info_armas['Dano']}"
    

    prata_rolada = rolar_dados_prata(CLASSE_INFO[classe]["dados_recurso"]["Prata"])
    Dx_comida = CLASSE_INFO[classe]['dados_recurso']['Comida']
    Dx_agua = CLASSE_INFO[classe]['dados_recurso']['Água']


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


    # Dicionario de variaveis
    VARS_CODE = {
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
    pericias_faltando = {pericia: 0 for pericia in PERICIAS.keys() if pericia not in pericias_distribuidas}
    pericias_distribuidas.update(pericias_faltando)
    pericias_distribuidas = {k.lower(): v for k, v in pericias_distribuidas.items()}
    print(pericias_distribuidas)

    if classe != "Rider":
        bonus_arma, dano_arma = info_armas_formatado.split()


    #Pagina da ficha
    # Carrega a imagem da ficha
    imagem_entrada = 'Pagina1.jpg'
    imagem_saida = 'Pagina1_preenchida.jpg'
    imagem = Image.open(imagem_entrada)

    # Adicione todas as variáveis à ficha usando as coordenadas
    for variavel, cord in COORDENADAS.items():

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
            # Obtenha a chave correspondente em VARS_CODE
            chave_vars = MAPA_CHAVES[variavel]
            # Obtenha o valor da variável a partir do seu nome
            valor = VARS_CODE[chave_vars]
            # Verifique se o valor é uma lista ou um dicionário
            if not isinstance(valor, (list, dict)):
                adicionar_texto_na_ficha(imagem, str(valor), cord)

    #Por a armadura do guerreiro na ficha
    if classe == "Guerreiro":
        Armadura_couro_str = ("Couro")
        escrever_armadura(imagem, Armadura_couro_str, COORDENADAS_ARMADURA)

    #Por na ficha onde a escolha vai ser do jogador ou do mestre
    escolha_do_jogador = 'Escolha do JOGADOR'
    escolha_do_mestre = 'Escolha do MESTRE'
    escrever_texto_em_varias_coordenadas_JOGADOR(imagem, escolha_do_jogador, COORDENADAS_USER)
    escrever_texto_em_varias_coordenadas_MESTRE(imagem, escolha_do_mestre, COORDENADAS_MESTRE)

    # Salve a imagem com o texto adicionado
    imagem.save(imagem_saida)

    # Abra a imagem no navegador padrão
    webbrowser.open(imagem_saida)

    # Feche a imagem
    imagem.close()