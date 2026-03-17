from processo import melhor_aluno, processar_alunos



alunos = [
    ("Ana", [8, 7.5, 9]),
    ("Bruno", [5, 6, 6.5]),
    ("Carlos", [10, 9, 8]),
    ("Diana", []),
    ("Eduardo", [7, "a", 8])
    ]
resultados = processar_alunos(alunos)
melhor = melhor_aluno(resultados)
if melhor:
    print(f"O melhor aluno é {melhor[0]} com média {melhor[2]:.2f}")