from processos import melhor_aluno, processar_alunos



alunos = [
    ("Ana", [8, 7.5, 9]),
    ("Bruno", [5, 6, 6.5]),
    ("Carlos", [10, 9, 8]),
    ("Diana", []),
    ("Eduardo", [7, "a", 8])
    ]

resultados = processar_alunos(alunos)

    
with open("resultados.txt", "w", encoding="utf-8") as arquivo:

    for nome, notas, media, situacao in resultados:
        linha = (
            f"Aluno: {nome}\n"
            f"Notas: {notas}\n"
            f"Média: {media}\n"
            f"Situação: {situacao}\n"
            + "-" * 30 + "\n"
            )

        print(linha)          
        arquivo.write(linha)  

        
    melhor = melhor_aluno(resultados)

    if melhor:
        nome, notas, media, situacao = melhor
        texto = (
            "\nMelhor aluno:\n"
            f"Nome: {nome}\n"
            f"Média: {media}\n"
            )
    else:
        texto = "\nNenhum aluno válido encontrado.\n"

    print(texto)
    arquivo.write(texto)


