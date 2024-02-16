Priemgetallen vormen de bouwstenen van de wiskunde, ze worden als volgt gedefinieerd:

{: .callout.callout-danger}
> #### Definitie
> Een priemgetal is een **natuurlijk getal** groter dan 1 dat **enkel** deelbaar is door 1 en zichzelf.

In Python kan je relatief gemakkelijk controleren of een getal priem is. Beschouw bijvoorbeeld onderstaande code:

```python
getal = int( input( "Geef een getal in" ) )
priem = 1
for i in range(2, getal):
    if getal % i == 0:
        priem = 0
```

Is de variabele `priem` na het uitvoeren van dit stukje code nog steeds `1`, dan werden geen *delers* gevonden en kan je besluiten dat het een priemgetal was.

## Opgave
Schrijf een programma dat een natuurlijk getal groter dan 2 vraagt en vervolgens het **grootste priemgetal** zoekt dat kleiner is dan het opgegeven natuurlijke getal.

#### Voorbeelden
Geef de gebruiker `3` in, dan verschijnt er:
```
Het grootste priemgetal kleiner dan 3 is 2.
```

Geef de gebruiker `50` in, dan verschijnt er:
```
Het grootste priemgetal kleiner dan 50 is 47.
```
