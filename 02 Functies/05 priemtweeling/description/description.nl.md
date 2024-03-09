Functies zijn zeer handig om **complexe voorwaarden** tot één *zin* te reduceren.

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

Schrijf een functie `priemtweeling( getal )` dat controleert of er van een gegeven getal een priemtweeling gevonden kan worden. Gebruik hierbij de functie `is_priem()`.

#### Voorbeelden

```
>>> priemtweeling( 5 )
Je kan twee priemtweelingen vinden van 5, namelijk 3 en 7.
```

```
>>> priemtweeling( 11 )
Je kan één priemtweeling vinden van 11, namelijk 13.
```

```
>>> priemtweeling( 20 )
Je kan geen priemtweeling vinden van 20.
```

```
>>> priemtweeling( 53 )
Je kan geen priemtweeling vinden van 53.
```

{: .callout.callout-primary}
> #### Trivia
> Men vermoedt dat er oneindig veel priemtweelingen zijn. Wiskundigen speculeren hier al honderden jaren over, maar er is nog steeds **geen bewijs** voor gevonden.
