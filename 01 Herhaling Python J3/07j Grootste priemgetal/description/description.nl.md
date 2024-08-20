Priemgetallen vormen de bouwstenen van de wiskunde, onderstaande code controleert (niet super efficiënt) of een getal al dan niet priem is.

```python
getal = int(input("Geef een getal in: "))
is_priem = True
for i in range(2, getal):
    if getal % i == 0:
        is_priem = False
```

Is de variabele `is_priem` na het uitvoeren van dit stukje code nog steeds `True`, dan werden **geen** *delers* gevonden en kan je besluiten dat het een priemgetal was.

## Opgave
Schrijf een programma dat een natuurlijk getal groter dan 2 vraagt en vervolgens het **grootste priemgetal** zoekt dat kleiner is dan het opgegeven natuurlijke getal. Je mag ook de efficiëntere werkwijze uit de vorige opdracht gebruiken.

#### Voorbeelden
Geef de gebruiker `3` in, dan verschijnt er:
```
Het grootste priemgetal kleiner dan 3 is 2.
```

Geef de gebruiker `50` in, dan verschijnt er:
```
Het grootste priemgetal kleiner dan 50 is 47.
```
