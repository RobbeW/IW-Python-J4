def trappen_lopen(aantal):
    prev1 = 1
    prev2 = 1
    for i in range(2, aantal + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1