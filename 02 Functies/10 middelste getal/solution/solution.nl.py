def midden( a, b, c ):
    maximum = max(a,b,c)
    minimum = min(a,b,c)
    
    result = (a+b+c) - maximum - minimum
    return result
