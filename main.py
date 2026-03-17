from processo import processar_alunos



alunos = [
    ("Ana", [8, 7.5, 9]),
    ("Bruno", [5, 6, 6.5]),
    ("Carlos", [10, 9, 8]),
    ("Diana", []),
    ("Eduardo", [7, "a", 8])
    ]

resultados = processar_alunos(alunos)

for nome, notas, media, situacao in resultados:
    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media}")
    print(f"Situação: {situacao}")
    print("-" * 20)



