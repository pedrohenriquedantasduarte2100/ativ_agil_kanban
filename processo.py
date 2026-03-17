def validar_notas(notas):
    if not isinstance(notas, list) or len(notas) == 0:
        return False

    for n in notas:
        if not isinstance(n, (int, float)):
            return False

    return True