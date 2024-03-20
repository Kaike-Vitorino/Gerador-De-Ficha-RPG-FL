'''
   Modulo responsavel por todas as coordenadas necessarias para ser realizada a impressao na ficha.
'''

# Variavel com as coordenadas simples da pagina 1.
COORDENADAS = {
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
COORDENADAS_ARMADURA = [(790, 1780)]
COORDENADAS_USER = [(770, 440), (770, 630), (770, 830), (1410, 530), (1410, 680), (1410, 820)]
COORDENADAS_MESTRE = [(1000, 1030)]

# Variavel com as coordenadas simples da pagina 2.
COORDENADAS_PAG2 = {
    "Dx_comida": (322, 392),
    "Dx_agua": (322, 412),
    "prata_rolada": (322, 432),
    "equipamentos_cord": (322, 332),
}

# Um mapa que mostra qual variavel pertence a qual coordenada.
MAPA_CHAVES = {
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
