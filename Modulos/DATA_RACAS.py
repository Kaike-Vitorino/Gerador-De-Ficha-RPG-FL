from DATA_CLASSES import *

'''
   Modulo com todas informacoes de todas as RACAS.
'''

# Variavel Lista q contem as RACAS.
RACAS = ["Humano", "Elfo", "Anão", "Goblin", "Orc", "Meio-Elfo", "Halfling", "Lupino"]

# Dicionário que armazena informações sobre as raças.
RACAS_INFO = {
    "Humano": {"atributo_chave": "Empatia", "talento_ascendente": "Adaptive", "profissoes_tipicas": CLASSES},
    "Meio-Elfo": {"atributo_chave": "Inteligência", "talento_ascendente": "Poder mental", "profissoes_tipicas": ["Druida", "Mago", "Ladino"]},
    "Anão": {"atributo_chave": "Força", "talento_ascendente": "Bravura Indômita", "profissoes_tipicas": ["Guerreiro", "Mascate", "Bardo"]},
    "Halfling": {"atributo_chave": "Empatia", "talento_ascendente": "Difícil de Acertar", "profissoes_tipicas": ["Bardo", "Mascate", "Ladino"]},
    "Lupino": {"atributo_chave": "Agilidade", "talento_ascendente": "Instinto de Caça", "profissoes_tipicas": ["Caçador", "Druida", "Guerreiro"]},
    "Orc": {"atributo_chave": "Força", "talento_ascendente": "Imbatível", "profissoes_tipicas": ["Caçador", "Guerreiro", "Ladino"]},
    "Goblin": {"atributo_chave": "Agilidade", "talento_ascendente": "Noturno", "profissoes_tipicas": ["Caçador", "Rider", "Ladino"]},
    "Elfo": {"atributo_chave": "Agilidade", "talento_ascendente": "Paz Interior", "profissoes_tipicas": ["Caçador", "Druida", "Bardo"]}
}

# Dicionário com as idades para cada raça.
IDADE_RACAS = {
    "Humano": {"Jovem": (16, 25), "Adulto": (26, 50), "Idoso": (51, 80)},
    "Meio-Elfo": {"Jovem": (16, 30), "Adulto": (31, 100), "Idoso": (101, 180)},
    "Anão": {"Jovem": (20, 40), "Adulto": (41, 80), "Idoso": (81, 121)},
    "Halfling": {"Jovem": (16, 25), "Adulto": (26, 60), "Idoso": (61, 98)},
    "Lupino": {"Jovem": (13, 20), "Adulto": (21, 40), "Idoso": (41, 65)},
    "Orc": {"Jovem": (13, 20), "Adulto": (21, 45), "Idoso": (46, 70)},
    "Goblin": {"Jovem": (16, 25), "Adulto": (26, 60), "Idoso": (61, 95)},
    "Elfo": {"Adulto": (26, 1000)}  # Elfos sempre são adultos.
}