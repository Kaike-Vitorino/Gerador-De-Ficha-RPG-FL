#
equipamentos = []

#Lista de itens de comercio, pagina 182
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

# Variavel para arma escolhida e artefato musical com valor vazio inicialmente, posto aq pq por algum motivo nn tava funfando la dentrod da func da linha 193
arma_escolhida = ""
artefato_musical_escolhido = None

# Dicionario de armas com empunhadura 1M
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

# Dicionario de armas com empunhadura 2M
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

# Os 2 dicionarios de armas juntos
lista_armas = {**armas_1m, **armas_2m}

# Dicionario de armas a distância com empunhadura 1M
armas_distancia_1m = {
    "Pedra": {"Bonus": "+0", "Dano": "1"},
    "Faca de Arremesso": {"Bonus": "+1", "Dano": "1"},
    "Machado de Arremesso": {"Bonus": "+1", "Dano": "2"},
    "Azagaia": {"Bonus": "+2", "Dano": "1"},
    "Funda": {"Bonus": "+1", "Dano": "1"},
}

# Dicionario de armas a distância com empunhadura 2M
armas_distancia_2m = {
    "Arco Curto": {"Bonus": "+2", "Dano": "1"},
    "Arco Longo": {"Bonus": "+2", "Dano": "1"},
    "Besta Leve": {"Bonus": "+1", "Dano": "2"},
    "Besta Pesada": {"Bonus": "+1", "Dano": "3"},
}

# Juntando os dois dicionarios de armas a distancia
lista_armas_a_distancia = {**armas_distancia_1m, **armas_distancia_2m}

# Juntando todos os dicionarios de armas
lista_armas_FINAL = {**lista_armas_a_distancia, **lista_armas}

# Dicionario de Escudos
lista_escudos = {
    "Escudo Pequeno": {"Bonus": "+1"},
    "Escudo Grande": {"Bonus": "+2"},
}

# Dicionario de Armaduras e Elmos
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