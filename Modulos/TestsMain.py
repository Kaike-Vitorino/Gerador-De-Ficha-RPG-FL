from util import *

# Gerar raca aleatoria
raca, raca_info = gerar_raca()
#print(f"Raca escolhida: {raca}")

# Gerar classe aleatoria
classe = gerar_classe(raca,racas_info,classes)

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
gerar_arma(classe)

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

# Gerar ficha
gerar_info_ficha(classe, raca, atributos_chave, idade, faixa_etaria, atributos_randomizados, talentos_escolhidos, pericias_distribuidas)

#===============================================================================