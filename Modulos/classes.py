# importasndo as coisa do outro modulo
from itens import *

# Variavel Lista q contem as classes
classes = ["Caçador", "Druida", "Mago", "Rider", "Guerreiro", "Ladino", "Mascate", "Bardo"]

#Infos da classe/profissoes
classe_info = {
    "Caçador": {
        "atributo_chave": "Agilidade",
        "pericias": ["Furtividade", "Movimentação", "Pontaria", "Patrulha", "Sobrevivência"],
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
        "pericias": ["Resiliência", "Sobrevivência", "Discernimento", "Cura", "Adestramento"],
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
        "pericias": ["Artesanato", "Artimanha", "Tradição", "Discernimento", "Manipulação"],
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
        "pericias": ["Resiliência", "Luta", "Pontaria", "Sobrevivência", "Adestramento"],
        "equipamentos": {
            "Arma": ["Lança", "Machadinha","Arco Curto", "Funda"],
            "Armadura": None,
            "Itens": 1,
            "Artefato Musical": None,
            "Cavalo": 1
        },
        "dados_recurso": {"Comida": "D8", "Água": "D8", "Flechas": "D10", "Prata": "D6"}
    },
    "Guerreiro": {
        "atributo_chave": "Força",
        "pericias": ["Potência", "Resiliência", "Luta", "Movimentação"],
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
        "pericias": ["Luta", "Furtividade", "Artimanha", "Movimentação", "Manipulação"],
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
        "pericias": ["Artesanato", "Artimanha", "Patrulha", "Discernimento", "Manipulação"],
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
        "pericias": ["Tradição", "Discernimento", "Manipulação", "Atuação", "Cura"],
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

# Dicionario de talentos das classes
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

# Dicionario de armas de 1m
armas_1m_lista = list(armas_1m.keys())