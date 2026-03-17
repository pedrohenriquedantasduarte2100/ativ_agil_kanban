def validar_notas(notas):
    if not isinstance(notas, list) or len(notas) == 0:
        return False

    for n in notas:
        if not isinstance(n, (int, float)):
            return False

    return True


def calcular_media(notas):
    if not validar_notas(notas):
        return None

    soma = 0
    for n in notas:
        soma += n

    return soma / len(notas)


def processar_alunos(lista):
    resultado = []

    for nome, notas in lista:
        media = calcular_media(notas)

        if media is None:
            situacao = "Inválido"
        elif media < 7:
            situacao = "Recuperação"
        else:
            situacao = "Aprovado"

        resultado.append((nome, notas, media, situacao))

    return resultado


def melhor_aluno(resultados):
    melhor = None

    for nome, notas, media, situacao in resultados:
        if media is not None:
            if melhor is None or media > melhor[2]:
                melhor = (nome, notas, media, situacao)

    return melhor