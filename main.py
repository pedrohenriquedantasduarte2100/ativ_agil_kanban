from processo import calcular_media

alunos = [
    ("Ana", [8, 7.5, 9]),
    ("Bruno", [5, 6, 6.5]),
    ("Carlos", [10, 9, 8]),
    ("Diana", []),
    ("Eduardo", [7, "a", 8])
    ]
for nome, notas in alunos:
    media = calcular_media(notas)
    if media is not None:
        print(f"A média de {nome} é {media:.2f}")
    else:
        print(f"Não foi possível calcular a média de {nome} devido a notas inválidas.")


