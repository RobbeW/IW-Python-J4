leerling = input("Wat is de naam van de leerling?")
scoreOp20 = int(input("Wat is de score van de leerling? (op 20)"))

if scoreOp20 < 10:
    print("Je behaalt een onvoldoende voor deze toets", leerling + "je krijgt van mij een remediëring.")
elif scoreOp20 <= 13:
    print("Je behaalt een voldoende", leerling + ", maar zal je toch moeten herpakken. Herhaal deze leerstof en maak meer oefeningen voor het examen!")
elif scoreOp20 < 17:
    print("Beste", leerling + ", dit is een goed resultaat. Doe zo voort!")
else:
    print(" Wat een subliem resultaat! Met een", score, "bewijs je talent te hebben voor dit vak!")