def winnaar(lijst):
    Owon = False
    Xwon = False
    if list[0][0] == "O" and list[0][1] == "O" and list[0][2] == "O" or list[1][0] == "O" and list[1][1] == "O" and list[1][2] == "O" or list[2][0] == "O" and list[2][1] == "O" and list[2][2] == "O" or list[0][0] == "O" and list[1][0] == "O" and list[2][0] == "O" or list[0][1] == "O" and list[1][1] == "O" and list[2][1] == "O" or list[0][2] == "O" and list[1][2] == "O" and list[2][2] == "O" or list[0][0] == "O" and list[1][1] == "O" and list[2][2] == "O" or list[0][2] == "O" and list[1][1] == "O" and list[2][0] == "O":
        Owon = True
    if list[0][0] == "X" and list[0][1] == "X" and list[0][2] == "X" or list[1][0] == "X" and list[1][1] == "X" and list[1][2] == "X" or list[2][0] == "X" and list[2][1] == "X" and list[2][2] == "X" or list[0][0] == "X" and list[1][0] == "X" and list[2][0] == "X" or list[0][1] == "X" and list[1][1] == "X" and list[2][1] == "X" or list[0][2] == "X" and list[1][2] == "X" and list[2][2] == "X" or list[0][0] == "X" and list[1][1] == "X" and list[2][2] == "X" or list[0][2] == "X" and list[1][1] == "X" and list[2][0] == "X":
        Xwon = True
    result = ""
    if Xwon == Owon:
        result = "Draw"
    elif Xwon:
        result = "X"
    else:
        result = "O"
    return result