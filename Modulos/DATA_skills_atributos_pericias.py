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
PERICIAS = {
    "Potência": "Força", "Resiliência": "Força", "Luta": "Força", "Artesanato": "Força", "Furtividade": "Agilidade",
    "Artimanha": "Agilidade", "Movimentação": "Agilidade", "Pontaria": "Agilidade", "Patrulha": "Inteligência",
    "Tradição": "Inteligência", "Sobrevivência": "Inteligência", "Discernimento": "Inteligência", "Manipulação": "Empatia",
    "Atuação": "Empatia", "Cura": "Empatia", "Adestramento": "Empatia"
}

# Dicionario de talentos gerais e qual classe pode ter cada um.
TALENTOS_GERAIS = {
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