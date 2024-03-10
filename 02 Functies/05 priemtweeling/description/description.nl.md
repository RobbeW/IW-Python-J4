Functies zijn zeer handig om **complexere code** tot één *regel* te reduceren.

Beschouw bijvoorbeeld onderstaande functie:

```python
def is_priem( getal ):
    priem = True
    for i in range(2, getal):
        if getal % i == 0:
            priem = False
    
    return priem
```

Deze functie controleert of een getal al dan niet priem is. Er geldt:

```
>>> is_priem( 11 )
True
```

```
>>> is_priem( 12 )
False
```

Vervolgens kan je deze functie gebruiken in andere programma's zoals:

```python
for i in range(2, 100):
    if is_priem( i ):
        print( i )
```

Dit programma zal alle priemgetallen kleiner dan 100 afdrukken. Merk op dat de code zeer gemakkelijk leest. Je hoeft niet te weten wat de exacte details van de functie `is_priem()` zijn. De naamgeving zorgt ervoor dat dit duidelijk is.

## Opgave

Men noemt twee getallen <a href="https://nl.wikipedia.org/wiki/Priemtweeling" target="_blank">priemtweelingen</a> indien het beide priemgetallen zijn en ze precies twee van elkaar verwijderd zijn. Zo zijn 3 en 5 bijvoorbeeld priemtweelingen.

Schrijf een programma dat aan de gebruiker een bovengrens vraagt en vervolgens alle priemtweelingen **kleiner** dan deze bovengrens op het scherm afdrukt. Gebruik hierbij de functie `is_priem()`.

#### Voorbeelden

Bij invoer `20` verschijnt er:
```
3 en 5 zijn priemtweelingen.
5 en 7 zijn priemtweelingen.
11 en 13 zijn priemtweelingen.
17 en 19 zijn priemtweelingen.
```

Bij invoer `100` verschijnt er:
```
3 en 5 zijn priemtweelingen.
5 en 7 zijn priemtweelingen.
11 en 13 zijn priemtweelingen.
17 en 19 zijn priemtweelingen.
29 en 31 zijn priemtweelingen.
41 en 43 zijn priemtweelingen.
59 en 61 zijn priemtweelingen.
71 en 73 zijn priemtweelingen.
```

{: .callout.callout-primary}
> #### Trivia
> Men vermoedt dat er oneindig veel priemtweelingen zijn. Wiskundigen speculeren hier al honderden jaren over, maar er is nog steeds **geen bewijs** voor gevonden.
