def even_strings(lijst):
    result = []
    for i in range(lijst):
        if len(lijst[i] % 2 == 0):
            result.append(lijst[i])
    return result