## Opgave

Men noemt twee getallen <a href="https://nl.wikipedia.org/wiki/Priemtweeling" target="_blank">priemtweelingen</a> indien het beide priemgetallen zijn en ze precies twee van elkaar verwijderd zijn. Zo zijn 3 en 5 bijvoorbeeld priemtweelingen.

- Schrijf een functie `priemtweeling(getal)` dat controleert of er voor een gegeven getal een priemtweeling gevonden kan worden. Deze functie retourneert het aantal priemtweelingen van het getal, dit is dus 2, 1 of 0. Gebruik in deze functie de functie `is_priem()`.

- Schrijf **uiteindelijk** een programma dat een getal aan de gebruiker vraagt en daar de functie `priemtweeling()` op los laat. Afhankelijk van de uitvoer (`2`, `1` of `0`) geef je een andere zin weer op het scherm.

#### Voorbeelden

Geeft de gebruiker `5` in, dan verschijnt er:
```
Je kan twee priemtweelingen vinden van 5
```
want 
```python
>>> priemtweeling(5)
2
```


Geeft de gebruiker `11` in, dan verschijnt er:
```
Je kan één priemtweeling vinden van 11
```
want 
```python
>>> priemtweeling(11)
1
```


Geeft de gebruiker `20` in, dan verschijnt er:
```
Je kan geen priemtweeling vinden van 20
```
want 
```python
>>> priemtweeling(20)
0
```


Geeft de gebruiker `53` in, dan verschijnt er:
```
Je kan geen priemtweeling vinden van 53
```
want 
```python
>>> priemtweeling(53)
0
```
