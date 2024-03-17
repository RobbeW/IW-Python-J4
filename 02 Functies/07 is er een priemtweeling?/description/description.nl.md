## Opgave

Men noemt twee getallen <a href="https://nl.wikipedia.org/wiki/Priemtweeling" target="_blank">priemtweelingen</a> indien het beide priemgetallen zijn en ze precies twee van elkaar verwijderd zijn. Zo zijn 3 en 5 bijvoorbeeld priemtweelingen.

Schrijf een functie `priemtweeling( getal )` dat controleert of er voor een gegeven getal een priemtweeling gevonden kan worden. Gebruik hierbij de functie `is_priem()`.

Schrijf **uiteindelijk** een programma dat een getal aan de gebruiker vraagt en daar de functie `priemtweeling()` op los laat.

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