# Imports de modulos e pacotes
import random
from racas_data import *
from skills_pericias_atributos import *

'''
   Modulo onde todas as funcoes essencias para a confeccao de toda a parte bruta/escrita na ficha.
        Varias variaveis sao declaradas e definidas.
        Aqui tem tudo para sair as infos da ficha inteira so que em forma de texto.
'''

# Declarando essas variveis que vao ser utilizadas em varios locais diferentes.
raca = ""
artefato_musical_escolhido = ""
arma_escolhida = ""
equipamentos = []


# Funcao para gerar raca aleatoria.
def gerar_raca():
    raca_aleatoria = random.choice(racas)
    raca_info = racas_info[raca_aleatoria]
    return raca_aleatoria, raca_info

# Funcao para gerar classe.
def gerar_classe(raca,racas_info,classes):
    classe = random.choice(racas_info[raca]["profissoes_tipicas"])
    return classe

# Funcao para obter os atributos chaves.
def obter_atributos_chave(classe, raca, raca_info):
    atributo_chave_classe = classe_info[classe]["atributo_chave"]
    atributo_chave_raca = raca_info["atributo_chave"]
    # Verifique se os atributos-chave são iguais e crie a lista de atributos.
    atributos_chave = []
    if atributo_chave_classe != atributo_chave_raca:
        atributos_chave.append(atributo_chave_classe)
    atributos_chave.append(atributo_chave_raca)
    return atributos_chave

# Funcao para calcular idade.
def calcular_idade(raca):
    if raca == "Elfo":
        idade = random.randint(26, 1000)
        faixa_etaria = "Adulto"
        return idade, "Adulto"
    else:
        if raca in idade_racas:
            intervalos = idade_racas[raca]
            faixa_etaria = random.choices(list(intervalos.keys()), k=1)[0]
            idade_min, idade_max = intervalos[faixa_etaria]
            print(f"Intervalo de idade encontrado para a raça {raca}.")

            # Verifica se idade_min e idade_max nn sao vazios antes de usar random.randint
            if idade_min is not None and idade_max is not None:
                idade = random.randint(idade_min, idade_max)
                return idade, faixa_etaria

        # Se nn encontrou intervalo de idade para a raca, chama a função novamente (recursão)
        print(f"Intervalo de idade não encontrado para a raça {raca}. Tentando novamente.")
        return calcular_idade(raca)

# Funcao onde os pontos de atributo sao distribuidos e o valor/nivel dos atributos determinados.
def escolher_atributos(faixa_etaria, atributos_chave):
    if faixa_etaria == "Jovem":
        pontos_disponiveis = 15
    elif faixa_etaria == "Adulto":
        pontos_disponiveis = 14
    else:  # Idoso
        pontos_disponiveis = 13

    todos_atributos = ['Força', 'Agilidade', 'Empatia', 'Inteligência']

    atributos_randomizados = {atributo: [0, 5] for atributo in todos_atributos}

    # Distribuir 2 pontos para cada atributo não-chave.
    for atributo in todos_atributos:
        if atributo not in atributos_chave:
            atributos_randomizados[atributo][0] = 2
            pontos_disponiveis -= 2

    # Distribuir pontos igualmente entre os atributos chave.
    pontos_por_atributo_chave = pontos_disponiveis // len(atributos_chave)

    for atributo in atributos_chave:
        atributos_randomizados[atributo][0] = min(pontos_por_atributo_chave, 5)
        pontos_disponiveis -= atributos_randomizados[atributo][0]

    # Distribuir pontos restantes, se houver.
    pontos_restantes = pontos_disponiveis
    atributos_ordenados = list(atributos_randomizados.keys())
    random.shuffle(atributos_ordenados)

    for i in range(pontos_restantes):
        atributo = atributos_ordenados[i]
        pontos_a_adicionar = min(5 - atributos_randomizados[atributo][0], 1)
        atributos_randomizados[atributo][0] += pontos_a_adicionar

    # Adicionar +1 ponto ao atributo-chave se houver apenas um.
    if len(atributos_chave) == 1:
        atributo_chave = atributos_chave[0]
        atributos_randomizados[atributo_chave][0] += 1

    atributos_randomizados = {atributo: valor[0] for atributo, valor in atributos_randomizados.items()}

    return atributos_randomizados

# Funcao para distribuir pontos de pericia.
def distribuir_pontos_pericia(faixa_etaria, classe):
    pontos_disponiveis = 0

    if faixa_etaria == "Jovem":
        pontos_disponiveis = 8
    elif faixa_etaria == "Adulto":
        pontos_disponiveis = 10
    elif faixa_etaria == "Idoso":
        pontos_disponiveis = 12

    pericias_permitidas = classe_info[classe]["pericias"]
    pericias_distribuidas = {pericia: 0 for pericia in pericias_permitidas}

    while pontos_disponiveis > 0:
        pericia = random.choice(pericias_permitidas)
        if pericias_distribuidas[pericia] < 3 and pontos_disponiveis > 0:
            pericias_distribuidas[pericia] += 1
            pontos_disponiveis -= 1

    return pericias_distribuidas

def randomizar_talento_ascendente(raca, talentos_sem_lvl):
    talento_ascendente_sem_lvl = racas_info[raca]["talento_ascendente"]
    talentos_sem_lvl.append(talento_ascendente_sem_lvl)
    #print(f"Talento ascendente:", talentos_sem_lvl)
    return talentos_sem_lvl

# Funcao para randomizar talento
def randomizar_talento_classe(classe, talentos_sem_lvl):
    if classe in talentos_classes:
        #print(f"Talentos para a classe {classe} encontrados.")
        talentos_disponiveis = talentos_classes[classe]
        talento_escolhido_classe_sem_lvl = random.choice(talentos_disponiveis)
        talentos_sem_lvl.append(talento_escolhido_classe_sem_lvl)
        #print(f"Talento de classe:", talento_escolhido_classe_sem_lvl)
        return talentos_sem_lvl
    else:
        #print(f"Talentos para a classe {classe} não encontrados. Tentando novamente.")
        return randomizar_talento_classe(classe)

# Funcao para randomizar talentos gerais.
def randomizar_talentos_gerais(faixa_etaria, classe, nivel, talentos_sem_lvl):
    quantidade_talentos = 0

    if faixa_etaria == "Jovem":
        quantidade_talentos = 1
    elif faixa_etaria == "Adulto":
        quantidade_talentos = 2
    elif faixa_etaria == "Idoso":
        quantidade_talentos = 3

    # Declaração do dicionário para armazenar talentos escolhidos
    talentos_escolhidos = {}

    # Randomiza se vai ter 1 talento sacrificado ou não
        # Se um talento eh sacrificado na criacao da ficha, ele tem direito de subir outro talento para o lvl2
    talento_sacrificado = random.choice([True, False])
    #print(f"Talento sacrificado: {talento_sacrificado}")

    if talento_sacrificado:
        talentos_atuais_escolhidos = None

        if faixa_etaria == "Jovem" or faixa_etaria == "Adulto":
            # Escolhe os talentos com 1 a menos do que o necessário
            talentos_atuais_escolhidos = random.sample(talentos_gerais[classe], quantidade_talentos - 1)
            talentos_sem_lvl.extend(talentos_atuais_escolhidos)

        else: # Idoso
            # Escolhe qual dos dois talentos vai ser nivel 2
            talentos_gerais_escolhidos_sem_lvl = list(
                random.sample(talentos_gerais[classe], quantidade_talentos - 1))

            talentos_sem_lvl.extend(talentos_gerais_escolhidos_sem_lvl)

        talento_nivel_2 = random.choice(talentos_sem_lvl)
        talentos_sem_lvl.remove(talento_nivel_2)

        # Add o talento nivel 2 no dicionário de talentos escolhidos
        talentos_escolhidos[talento_nivel_2] = {"Nivel": nivel + 1}

        # Adiciona os talentos de nivel 1 ao dicionário de talentos escolhidos
        for talento in talentos_sem_lvl:
            talentos_escolhidos[talento] = {"Nivel": nivel}

        #print(f"Talento geral:", talentos_atuais_escolhidos)

    else:  # Adicionando os talentos de nivel 1 ao dicionário com o nivel especificado
        talentos_gerais_escolhidos = random.sample(talentos_gerais[classe], quantidade_talentos)
        talentos_sem_lvl.extend(talentos_gerais_escolhidos)
        for talento in talentos_sem_lvl:
            talentos_escolhidos[talento] = {"Nivel": nivel}

        #print(f"Talento geral:", talentos_gerais_escolhidos)

    return talentos_escolhidos

# Funcao para adicionar os talentos na ficha.
# Funcao central dos talentos. Essa funcao puxa as outras 3 funcoes acima e juntas elas em uma logica para conseguir uma quantidade de talentos balanceados.
def escolher_talentos(classe, raca, faixa_etaria):
    talentos = []
    talentos_sem_lvl = []
    nivel = 1

    # Adicionando talento ascendente da raca.
    talentos_sem_lvl = randomizar_talento_ascendente(raca, talentos_sem_lvl)
    #print(f"Talento ascendente: {talentos_sem_lvl}")

    # Chama a funcao que randomiza talento da classe.
    talentos_sem_lvl = randomizar_talento_classe(classe, talentos_sem_lvl)
    #print(f"Talento da classe: {talentos_sem_lvl}")

    # Chama a funcao que randomiza os talentos gerais.
    talentos_escolhidos = randomizar_talentos_gerais(faixa_etaria, classe, nivel, talentos_sem_lvl)

    return talentos_escolhidos

# Funcao para rolar o numero de dados da prata, ja q ela eh dada em string eh necessario fazer dessa forma pra nn sumir com o "D"
def rolar_dados_prata(dados_str):
    if dados_str.startswith("D"):
        num_faces = int(dados_str[1:])
        return random.randint(1, num_faces)
    else:
        return 0

# Funcao onde a arma do personagem eh gerada
# Ela vai puxar as infos das classes e randomizar uma arma dentre as opcoes dadas para cada classe.
# A classe rider tem 2 armas esclhidas, por conta disso a variavel de arma dessa classe eh diferente.
def gerar_arma(classe):
    # Escolhendo arma
    global artefato_musical_escolhido, arma_escolhida
    armas_disponiveis = classe_info[classe]["equipamentos"]["Arma"]
    arma_escolhida = None
    armas_escolhidas = None

    # Verificar se a classe tem armas disponíveis
    if armas_disponiveis:
        if classe == "Rider":
            armas_escolhidas = random.sample(armas_disponiveis, 2)
            arma_escolhida = None

            while ["Lança", "Machadinha"] in armas_escolhidas or ["Arco Curto", "Funda"] in armas_escolhidas:
                armas_escolhidas = random.sample(armas_disponiveis, 2)

            

            # Se chegou aqui, então as armas escolhidas são válidas
            equipamentos.extend(armas_escolhidas)

        elif classe == "Bardo":
            armas_escolhidas = None
            arma_escolhida = classe_info[classe]["equipamentos"]["Arma"][0]  # Pega o primeiro item da lista
            artefato_musical_disponiveis = classe_info[classe]["equipamentos"]["Artefato Musical"]
            artefato_musical_escolhido = random.choice(artefato_musical_disponiveis)

            equipamentos.insert(0, arma_escolhida)
            equipamentos.insert(1, artefato_musical_escolhido)

        elif classe == "Guerreiro":
            armas_escolhidas = None
            arma_escolhida = random.choice(armas_1m_lista)
            equipamentos.append(arma_escolhida)

        else:
            armas_escolhidas = None
            arma_escolhida = random.choice(armas_disponiveis)
            equipamentos.append(arma_escolhida)

        if arma_escolhida!= None:
            print(f"Arma escolhida 1 etapa: {arma_escolhida}")
        else:
            print(f"Armas escolhidas 1 etapa: {armas_escolhidas}")

        if arma_escolhida in ["Arco"]:
            arma_escolhida = random.choice(["Arco Curto", "Arco Longo"])
            equipamentos.remove("Arco")
            equipamentos.append(arma_escolhida)

        elif arma_escolhida in ["Lança"]:
            # Escolhendo um dos tipos de Lanças possíveis
            arma_escolhida = random.choice(["Lança Curta", "Lança Longa"])
            equipamentos.remove("Lança")
            equipamentos.append(arma_escolhida)

        if arma_escolhida != None:
            print(f"Arma escolhida 2 etapa: {arma_escolhida}")
        else:
            print(f"Armas escolhidas 2 etapa: {armas_escolhidas}")

        if "artefato_musical" in equipamentos:
            print(f"Artefato musical escolhido: {artefato_musical_escolhido}")

    return arma_escolhida, armas_escolhidas

# Inicializando um dicionario vazio para mapear os talentos e os niveis deles.
talentos_e_niveis = {}

# Funcao para distribuir XP.
# Se o usuario disse que quer dar XPs extras para uma ficha, essa funcao fica responsavel por receber a quantidade e dividir nas ficha.
def dividir_XP(talentos_escolhidos, pericias_distribuidas, classe, pericias):
    try:
        pontos_xp = int(input("Digite a quantidade de pontos de XP que o personagem vai ter: "))
    except ValueError:
        print("Digite um número inteiro válido.")
        return dividir_XP(talentos_escolhidos, pericias_distribuidas, classe, pericias)

    #Declarando lista de pericias e talentos para o while que vai acontecer
    pericias_disponiveis = list(pericias.keys())
    talentos_disponiveis = list(talentos_gerais[classe])

    

    # Variáveis para controlar se todas as opções estão no máximo
    todas_pericias_maximo = False
    todos_talentos_maximo = False
    pericias_disponiveis_para_aumentar = False
    talentos_disponiveis_para_aumentar = False

    while pontos_xp > 0:
        opcoes = [
            "Perícia nova",
            "Talento novo",
            "Aumentar nivel de perícia",
            "Aumentar nivel de talento"
        ]

        escolha = random.choice(opcoes)

        if escolha == "Perícia nova":
            custo = 5
            if not pericias_disponiveis:
                print("Todas as perícias estão distribuídas. Escolhendo novamente.")
                todas_pericias_maximo = True
                continue  # Pule esta iteração do loop
            nova_pericia = random.choice(pericias_disponiveis)

            pericias_disponiveis.remove(nova_pericia)
            pericias_distribuidas[nova_pericia] = 1

        elif escolha == "Talento novo":
            custo = 3
            if not talentos_disponiveis:
                print("Todos os talentos disponíveis já foram escolhidos. Escolhendo novamente.")
                todos_talentos_maximo = True
                continue  # Pule esta iteração do loop
            novo_talento = random.choice(talentos_disponiveis)

            talentos_disponiveis.remove(novo_talento)
            talentos_escolhidos[novo_talento] = {"Nivel": 1}

        elif escolha == "Aumentar nivel de perícia":
            custo = 0
            pericias_disponiveis_para_aumentar = [pericia for pericia, nivel in pericias_distribuidas.items() if nivel < 3]

            if not pericias_disponiveis_para_aumentar:
                print("Todas as perícias estão no nível máximo. Escolhendo novamente.")
                talentos_disponiveis_para_aumentar = True
                continue  # Pula esta iteração do loop

            pericia_aumentar = random.choice(pericias_disponiveis_para_aumentar)
            nivel_pericia = pericias_distribuidas[pericia_aumentar]
            custo = 5 * nivel_pericia  # Custo é 5 vezes o nível atual da perícia
            # Aumente o nível da perícia
            pericias_distribuidas[pericia_aumentar] += 1

        elif escolha == "Aumentar nivel de talento":
            custo = 0
            talentos_disponiveis_para_aumentar = [talento for talento, info in talentos_escolhidos.items() if info["Nivel"] < 3]

            if not talentos_disponiveis_para_aumentar:
                print("Todos os talentos estão no nível máximo. Escolhendo novamente.")
                pericias_disponiveis_para_aumentar = True
                continue  # Pula esta iteração do loop

            talento_aumentar = random.choice(talentos_disponiveis_para_aumentar)
            nivel_talento = talentos_escolhidos[talento_aumentar]["Nivel"]
            custo = 3 * nivel_talento
            talentos_escolhidos[talento_aumentar]["Nivel"] += 1

        pontos_xp -= custo

        if todas_pericias_maximo and todos_talentos_maximo and pericias_disponiveis_para_aumentar and talentos_disponiveis_para_aumentar:
            print("Sua ficha está no nível máximo, não é necessário mais XP")
            break

    return talentos_escolhidos, pericias_distribuidas


# Funcao para gerar informacoes da ficha
# Essa funcao junta todas as informacoes que foram dadas pelas outras funcoes e dessa forma gera a ficha inteira em texto.
def gerar_info_ficha(classe, raca, atributos_chave, idade, faixa_etaria, atributos_randomizados, talentos_escolhidos, pericias_distribuidas, armas_escolhidas):

    # Rolando quantidade de prata
    prata_rolada = rolar_dados_prata(classe_info[classe]["dados_recurso"]["Prata"])
    print(f"prata: {prata_rolada}")

    # Randomizador de itens da lista de itens de comercio
    quantidade_itens = classe_info[classe]["equipamentos"]["Itens"]  # Verifica a quantidade de itens que o personagem pode ter
    print(f"quantidade_itens: {quantidade_itens}")

    if arma_escolhida in ["Arco Curto", "Arco Longo"]:
        # Vai ser randomizado todos os itens, inclusive as duas flechas que são os 2 itens iniciais da lista de comercio
        itens_randomizados = random.sample(itens_comercio, quantidade_itens)  # Randomiza eles
        equipamentos.extend(itens_randomizados)  # adiciona eles nos equipamentos

    elif armas_escolhidas in ["Arco Curto", "Arco Longo"]:
        # Vai ser randomizado todos os itens, inclusive as duas flechas que são os 2 itens iniciais da lista de comercio
        itens_randomizados = random.sample(itens_comercio, quantidade_itens)  # Randomiza eles
        equipamentos.extend(itens_randomizados)  # adiciona eles nos equipamentos

    else:
        itens_randomizados = random.sample(itens_comercio[2:], quantidade_itens)  # Randomiza eles só que como não tem o arco, ele não considera os 2 itens de flechas
        equipamentos.extend(itens_randomizados)  # adiciona eles nos equipamentos

    
    print(f"itens_randomizados: {itens_randomizados,}")

    # Criando variaveis Necessarias
    cavalo = classe_info[classe]["equipamentos"]["Cavalo"]
    armadura_disponivel = classe_info[classe]["equipamentos"]["Armadura"]
    info_armaduras = lista_armaduras.get("armadura_disponivel")
    Dx_comida = classe_info[classe]['dados_recurso']['Comida']
    Dx_agua = classe_info[classe]['dados_recurso']['Água']
    armas_escolhidas_1 = None
    armas_escolhidas_2 = None

    # Printando a ficha do personagem
    print("\n--- Ficha do personagem ---")
    print(f"Raça: {raca}")
    print(f"Classe: {classe}")
    print(f"=============================")
    print(f"Atributo(s) Chave: {atributos_chave}")
    print(f"Atributos: {atributos_randomizados}")
    print(f"=============================")
    print(f"Idade: {idade}")
    print(f"Faixa etaria: {faixa_etaria}")
    print(f"=============================")
    print(f"Talentos :")
    for talento, info in talentos_escolhidos.items():
        print(f"{talento} - nivel {info['Nivel']}")
    print(f"=============================")
    print(f"Perícias: {pericias_distribuidas}")
    print(f"=============================")
    print(f"Equipamentos: {', '.join(equipamentos)}")
    # Dividindo a variavel arma escolhida em dois ja que o Rider tem duas armas
    if classe == "Rider":
        armas_escolhidas_1, armas_escolhidas_2 = armas_escolhidas  # Separando a variavel em 2

        info_arma_1 = lista_armas_FINAL.get(armas_escolhidas_1)  # Criando as infos de cada
        info_arma_2 = lista_armas_FINAL.get(armas_escolhidas_2)  # Criando as infos de cada

        print(f"Sua 1º arma:", armas_escolhidas_1)
        print(f"Infos da sua 1º arma:", info_arma_1)
        print(f"Sua 2º arma: ", armas_escolhidas_2)
        print(f"Infos da sua 2º arma:", info_arma_2)

    else:
        info_armas = lista_armas_FINAL.get(arma_escolhida)
        print(f"Sua arma:", arma_escolhida)
        print(f"Infos da sua arma:", info_armas)

    if armadura_disponivel != None:
        print(f"Sua armadura: {armadura_disponivel}")
        print(f"Infos da armadura: {info_armaduras}")

    if cavalo != None:
        print("Voce tem um cavalo")
        print("Essas sao as infos da sua montaria: ")
        #Forca: 5 Agilidade: 4 |Pericias: Movimentacao: +2 Patrulha: +3 |Dano: 1

    if artefato_musical_escolhido != None:
        print(f"Seu instrumento: ", artefato_musical_escolhido)
    print(f"Comida: {Dx_comida}")
    print(f"Água: {Dx_agua}")

    if "Arco Curto" in equipamentos or "Arco Longo" in equipamentos:
        print("Flecha: D10")

    print(f"Prata: {prata_rolada}")
    print("--------------------------\n")

    if classe == "Rider":
        return armas_escolhidas_1, armas_escolhidas_2, info_arma_1, info_arma_2