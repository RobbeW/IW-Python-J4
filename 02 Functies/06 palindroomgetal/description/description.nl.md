## Opgave

Schrijf een functie `is_palindroom( getal )` dat gegeven een natuurlijk getal controleert of dit een palindroomgetal is.

#### Voorbeelden

```
>>> is_palindroom( 1221 )
True
```

```
>>> is_palindroom( 14541 )
True
```

```
>>> is_palindroom( 13321 )
False
```

{: .callout.callout-info}
> #### Tip
> - Gebruik **geen** tekstfuncties!
> - Maak een nieuw getal aan waarbij je de waarden van achter naar leest. Dit kan je nadien vergelijken met het oorspronkelijke getal. Gebruik hierbij `%` en `//` in een `while` lus.
>   Bijvoorbeeld voor `2541` maak je achtereenvolgens een getal `1`, `14`, `145` en tot slot `1452`. Doordat `2541` niet gelijk is aan `1452` kan je besluiten dat het geen palindroomgetal is.
