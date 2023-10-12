from classes import *

# Variavel lista com os atributos
atributos = {
    'Força': [0, 5],
    'Agilidade': [0, 5],
    'Inteligência': [0, 5],
    'Empatia': [0, 5]
}

# Dicionario mapeando as pericias e atributos correspondentes
pericias = {
    "Potência": "Força", "Resiliência": "Força", "Luta": "Força", "Artesanato": "Força",
    "Furtividade": "Agilidade", "Artimanha": "Agilidade", "Movimentação": "Agilidade", "Pontaria": "Agilidade",
    "Patrulha": "Inteligência", "Tradição": "Inteligência", "Sobrevivência": "Inteligência", "Discernimento": "Inteligência",
    "Manipulação": "Empatia", "Atuação": "Empatia", "Cura": "Empatia", "Adestramento": "Empatia"
}

# Dicionario de talentos gerais
# Classe: [talentos que podem escolher] = talentos_gerais[classe]
talentos_gerais = {
    "Caçador": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
                "Sangue frio", "Saque rapido", "Sortudo", "Aquartelador", "Arremessador", "Cozinheiro", "Defensor",
                "Desbravador", "Herbalista", "Marinheiro", "Mestre da Caçada", "Pés ligeiros", "Pescador", "Sexto sentido"],

    "Druida": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
               "Sangue frio", "Saque rapido", "Sortudo", "Andarilho", "Aquartelador", "Cozinheiro", "Defensor",
               "Desbravador", "Destemido", "Herbalista", "Incorruptível", "Marinheiro", "Mestre da Caçada", "Pescador"],

    "Mago": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
             "Sangue frio", "Saque rapido", "Sortudo", "Arremessador", "Arrombador", "Artífice de arcos", "Cozinheiro",
             "Curtidor", "Destemido", "Envenenador", "Ferreiro", "Incorruptível", "Língua afiada"],

    "Rider": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
              "Sangue frio", "Saque rapido", "Sortudo", "Andarilho", "Aquartelador", "Desbravador", "Herbalista",
              "Investida", "Lutador", "Marinheiro", "Mestre da Caçada", "Mestre da montaria", "Pés ligeiros", "Pescador"],

    "Guerreiro": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
                  "Sangue frio", "Saque rapido", "Sortudo", "Ameaçador", "Andarilho", "Aquartelador", "Defensor",
                  "Investida", "Lutador"],

    "Ladino": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
               "Sangue frio", "Saque rapido", "Sortudo", "Arrombador", "Defensor", "Investida", "Língua afiada",
               "Lutador", "Pés ligeiros"],

    "Mascate": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
                "Sangue frio", "Saque rapido", "Sortudo", "Arrombador", "Artífice de arcos", "Curtidor", "Destemido",
                "Envenenador", "Ferreiro", "Incorruptível", "Língua afiada", "Sexto sentido"],

    "Bardo": ["Ambidestria", "Berseker", "Carrasco", "Empunhadura Firme", "Rapido como um raio", "Ruína dos Dragões",
              "Sangue frio", "Saque rapido", "Sortudo", "Artífice de arcos", "Cozinheiro", "Curtidor", "Defensor",
              "Desbravador", "Destemido", "Herbalista", "Incorruptível", "Língua afiada"],
}

'''' 
Se tiver arco - Atirador preciso, Atirador veloz
Se tiver lança - Mestre em lanças
Se tiver machado - Mestre em machados
Se tiver espada - Mestre em espadas
Se tiver faca - Mestre em facas
Se tiver martelo - Mestre em martelos

'''''