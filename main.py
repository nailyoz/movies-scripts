import re
from itertools import combinations

def extrair_personagens(cena):
    padrao_personagem = r"\b(.*):"
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


def dividir_cenas(roteiro):
    cenas = []  
    cena_atual = ""
    dentro_cena = False

    for linha in roteiro:
        if linha.startswith("[INT.") or linha.startswith("[EXT."):
            dentro_cena = True
            if cena_atual:
                cenas.append(cena_atual.strip())
                cena_atual = ""
        if dentro_cena:
            cena_atual += linha + "\n"

    if cena_atual:
        cenas.append(cena_atual.strip())

    return cenas

def extrair_duplas(cena):
    personagens_encontrados = extrair_personagens(cena)
    personagens = personagens_unicos(personagens_encontrados)
    duplas = gerar_duplas(personagens)
    return duplas


#manipulando roteiro
arquivo = open("input.txt", "r")
roteiro = arquivo.readlines()

cenas_divididas = dividir_cenas(roteiro)

#criando arquivo de saida

for cena in cenas_divididas:
    duplas = extrair_duplas(cena)
    print(duplas)
    print("-"*30)
