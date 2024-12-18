Een **evenwichtig priemgetal** is een priemgetal dat even ver ligt van het voorgaande en het volgende priemgetal. Met andere woorden: het is het rekenkundig gemiddelde van het voorgaande en het volgende priemgetal.

Wiskundig kan je dit uitdrukken als volgt. Een priemgetal p<sub>n</sub>, met n het volgnummer is in de lijst van priemgetallen, is evenwichtig indien:

$$
\mathsf{p_n = \dfrac{p_{n-1}+p_{n+1}}{2}}
$$

Bijvoorbeeld: 53 is het 16<sup>de</sup> priemgetal; het 15<sup>de</sup> (47) en het 17<sup>de</sup> priemgetal (59) zijn samen 106, en de helft daarvan is terug 53; daarom heet 53 een evenwichtig priemgetal. 

## Opgave

Schrijf een functie `is_priem(getal)` die controleert of een gegeven getal priem is.

Schrijf daarna twee functies `vorige_priem(getal)` en `volgende_priem(getal)` dat voor een gegeven getal respectievelijk het vorige en het volgende priemgetal zal retourneren.

Schrijf **daarna** een programma dat aan de gebruiker een volgnummer n vraagt en vervolgens het n<sup>de</sup> evenwichtige priemgetal op het scherm afdrukt.

#### Voorbeelden

Bij invoer `2` verschijnt er:
```
53 is het 2 e evenwichtige priemgetal.
```
er geldt immers dat 53 = (47 + 59) / 2
```python
>>> is_priem(53)
True
>>> vorige_priem(53)
47
>>> volgende_priem(53)
59
```

Bij invoer `3` verschijnt er:
```
157 is het 3 e evenwichtige priemgetal.
```
er geldt immers dat 157 = (151 + 163) / 2
```python
>>> is_priem(157)
True
>>> vorige_priem(157)
151
>>> volgende_priem(157)
163
```

{: .callout.callout-info}
> #### Tip
> Gebruik `while` lussen.
