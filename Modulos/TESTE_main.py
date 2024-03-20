from FUNCOES_geral import *

'''
   Modulo que serve com um main test.
        Aqui eu pego as funcoes brutas e vou pondo na ordem correta e decidindo algumas variaveis.
        Dessa forma eu vou testando varias possibilidade enquanto vou fazendo o codigo.
'''

# Gerar raca aleatoria
raca, raca_info = gerar_raca()
print(f"Raca escolhida: {raca}")

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

# Gerar armas
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
    talentos_escolhidos, pericias_distribuidas = dividir_XP(talentos_escolhidos, pericias_distribuidas, classe,
                                                            PERICIAS)
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
                                                                                    idade, faixa_etaria,
                                                                                    atributos_randomizados,
                                                                                    talentos_escolhidos,
                                                                                    pericias_distribuidas,
                                                                                    armas_escolhidas)
    info_armas_formatado_1 = f"{info_arma_1['Bonus']} {info_arma_1['Dano']}"
    info_armas_formatado_2 = f"{info_arma_2['Bonus']} {info_arma_2['Dano']}"
    bonus_arma_1, dano_arma_1 = info_armas_formatado_1.split()
    bonus_arma_2, dano_arma_2 = info_armas_formatado_2.split()

else:
    gerar_info_ficha(classe, raca, atributos_chave, idade, faixa_etaria, atributos_randomizados, talentos_escolhidos,
                     pericias_distribuidas, armas_escolhidas)

# =============================================================================================================================================