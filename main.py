import re


def extrair_personagens(cena):
    padrao_personagem = r"\bPersonagem [A-Z]\b"
    personagens_encontrados = re.findall(padrao_personagem, cena)
    return personagens_encontrados


def dividir_cenas(roteiro):
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


# Exemplo de uso
roteiro = """
[Cena 1]
[INT. Casa - Sala - Dia]
Personagem A: Olá, como vai?
Personagem B: Bem, obrigado. E você?
Personagem C: Bem, obrigado. E você?
Personagem A: Olá, como vai?

[Cena 2]
[EXT. Rua - Dia]
Personagem C: Vamos dar uma volta?
Personagem B: Claro, vamos lá.
Personagem D: Bem, obrigado. E você?

[Cena 3]
[INT. Restaurante - Noite]
Personagem A: Gostaria de fazer um pedido?
Personagem D: Sim, por favor.

[Cena 4]
[INT. Casa - Quarto - Noite]
Personagem A: Boa noite.
Personagem E: Boa noite.
"""

cenas_divididas = dividir_cenas(roteiro)

# Extrair e imprimir os personagens únicos de cada cena
for i, cena in enumerate(cenas_divididas, start=1):
    personagens = extrair_personagens(cena)
    print(f"Cena {i}:")
    for personagem in personagens:
        print(personagem)
    print("-" * 30)