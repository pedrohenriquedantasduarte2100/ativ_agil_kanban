from processo import validar_notas

alunos = [
    ("Ana", [8, 7.5, 9]),
    ("Bruno", [5, 6, 6.5]),
    ("Carlos", [10, 9, 8]),
    ("Diana", []),
    ("Eduardo", [7, "a", 8])
    ]
for aluno in alunos:
    nome, notas = aluno
    print(f"Validando notas de {nome}...")
    if validar_notas(notas):
        print(f"As notas de {nome} são válidas.")
    else:
        print(f"As notas de {nome} são inválidas.")
