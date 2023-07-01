def separar_cenas(roteiro):
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


roteiro = '''[Spider-Man and MJ PLUMMET into view behind him... Spider-Man WEBBING a grate in the sidewalk... YANKING it up... DROPPING them through the hole and... SLAMMING it closed behind them!]
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
[Still carrying MJ, Spider-Man swings and lands outside his bedroom window. An unsteady MJ lifts the glass as Spider-Man hoists her up.]
Spider-Man: I'm sorry!
INT. PETER & MAY’S APARTMENT - LIVING ROOM - SAME TIME (DAY)
[INT. TRAIN TUNNEL - CONTINUOUS (DAY)]
'''


cenas_separadas = separar_cenas(roteiro)

for cena in cenas_separadas:
    print("--- Cena ---")
    print(cena)
    print()
    print("--- Cena ---")

