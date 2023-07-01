import re
from itertools import combinations

def extrair_personagens(cena):
    padrao_personagem = r"^\[?([A-Za-z\s.-]+)(?:\[vo\])?:\s"
    personagens_encontrados = re.findall(padrao_personagem, cena)
    return personagens_encontrados

def personagens_unicos(personagens_encontrados):
    personagens = []
    for personagem in personagens_encontrados:
        if(personagem not in personagens):
            personagens.append(personagem)
    return personagens

def gerar_duplas(personagens_unicos):
    duplas = list(combinations(personagens_unicos, 2))
    return duplas


#def dividir_cenas(roteiro):
    cenas = []  
    cena_atual = ""
    dentro_cena = False

    linhas = roteiro.split("\n")

    for linha in linhas:
        if "[INT." in linha or "[EXT." in linha:
            dentro_cena = True
            if cena_atual:
                cenas.append(cena_atual.strip())
                cena_atual = ""
        elif "]" in linha and dentro_cena:
            dentro_cena = False
            if cena_atual:
                cenas.append(cena_atual.strip())
                cena_atual = ""
        if dentro_cena:
            cena_atual += linha + "\n"

    if cena_atual:
        cenas.append(cena_atual.strip())

    return cenas

#def extrair_duplas(cena):
    personagens_encontrados = extrair_personagens(cena)
    personagens = personagens_unicos(personagens_encontrados)
    duplas = gerar_duplas(personagens)

    return duplas

def dividir_cenas(roteiro):
    cenas = []
    cena_atual = ''

    linhas = roteiro.split("\n")  # Divide o roteiro em linhas

    for linha in linhas:
        if linha.startswith("[INT.") or linha.startswith("[EXT."):
            # Nova cena encontrada
            if cena_atual:
                cenas.append(cena_atual)
            cena_atual = linha
        else:
            # Continuação da cena atual
            if cena_atual:
                cena_atual += " " + linha  # Concatena a linha com a cena atual

    # Adicionar última cena à lista de cenas
    if cena_atual:
        cenas.append(cena_atual)

    return cenas


# Exemplo de uso
roteiro = """
[INT. Casa - Sala - Dia]
[outra co]
Personagem A: Olá, como vai?
Personagem B: Bem, obrigado. E você?
Personagem C: Bem, obrigado. E você?
Personagem A: Olá, como vai?
[EXT. Rua - Dia]
Personagem C: Vamos dar uma volta?
Personagem B: Claro, vamos lá.
Personagem D: Bem, obrigado. E você?
[INT. Restaurante - Noite]
Personagem A: Gostaria de fazer um pedido?
Personagem D: Sim, por favor.
coisas coisas
[INT. Casa - Quarto - Noite]
Personagem A: Boa noite.
Personagem E: Boa noite.

[INT. TRAIN TUNNEL - CONTINUOUS (DAY)]
[Clutching MJ, Spider-Man SWINGS through the tunnels until--]
MJ: (closing her eyes) Look out!
[A train coming right at them! VVWHOOM! Spider-Man STEERS them into a different tunnel just in time!]
EXT. QUEENS STREET - LATER (DAY)
[A manhole cover slides open. Spider-Man emerges, stopping to help a rattled MJ climb out.]
MJ: That was so much worse! Okay....
Spider-Man: Are you okay?
MJ: Yeah. Yeah...
[INT. TRAIN TUNNEL - CONTINUOUS (DAY)]

[Spider-Man WEBS the manhole shut, then gestures for MJ to hop back on.]
Spider-Man: Come on, come on, come on.
[MJ jumps into Peter’s arms. As they swing off again--]
Spider-Man: I'm so sorry!
EXT. PETER & MAY’S APARTMENT BUILDING - LATER (DAY)

"""

cenas_divididas = dividir_cenas(roteiro)

for cena in cenas_divididas:
    print("--- START ---")
    print(cena)
    print("--- END ---")