import math
def RGBtoCMYK( code ):
    R = code[0]
    G = code[1]
    B = code[2]
    
    K = round(1 - max(R,G,B)/255, 2)
    if K != 1:
        C = abs( round( (1 - R/255 - K) / (1-K), 2) )
        M = abs( round( (1 - G/255 - K) / (1-K), 2) )
        Y = abs( round( (1 - B/255 - K) / (1-K), 2) )
    else:
        C = 0
        M = 0
        Y = 0
    return (C, M, Y, round(K, 2) )

def CMYKtoRGB( code ):
    C = code[0]
    M = code[1]
    Y = code[2]
    K = code[3]
    
    R = math.ceil( 255 * ( 1 - C ) * (1 - K) )
    G = math.ceil( 255 * ( 1 - M ) * (1 - K) )
    B = math.ceil( 255 * ( 1 - Y ) * (1 - K) )
    return (R, G, B)