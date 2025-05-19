def escala(worpen):
    flag = True
    for i in range(1, len(worpen)):
        if worpen[i] != worpen[i-1] + 1:
            flag = False
    return flag
