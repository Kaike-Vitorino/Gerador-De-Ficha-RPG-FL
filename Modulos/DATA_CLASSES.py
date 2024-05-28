from DATA_ITENS import *

'''
   Modulo com todas informacoes de todas as CLASSES.
'''

# Lista q contem as todas as CLASSES.
CLASSES = ["Caçador", "Druida", "Mago", "Rider", "Guerreiro", "Ladino", "Mascate", "Bardo"]

# Infos da classe/profissoes.
CLASSE_INFO = {
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
            "Arma": ARMAS_1M,
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
TALENTOS_CLASSES = {
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
ARMAS_1M_LISTA = list(LISTA_TODAS_ARMAS_1M.keys())