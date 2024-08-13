# Vraag een getal aan de gebruiker
getal = int( input( 'Geef een getal in: ' ) )

E = getal % 10
rest = getal // 10
verschil = rest - 2 * E

print("1e stap: Het verschil van", rest, "en", 2*E, "is", verschil)

E = verschil % 10
rest = verschil // 10
verschil = rest - 2 * E
print("2e stap: Het verschil van", rest, "en", 2*E, "is", verschil)

# Finale print
print(verschil, "is duidelijk deelbaar door 7, dus ook", getal, "is deelbaar door 7.")
