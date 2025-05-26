def som_van_drie(lijst):
    result = []
    for i in range(len(lijst)):
        for j in range(i + 1, len(lijst)):
            for k in range(j + 1, len(lijst)):
                if list[i] + list[j] + list[k] == 10:
                    result.append((i, j, k))
    return result