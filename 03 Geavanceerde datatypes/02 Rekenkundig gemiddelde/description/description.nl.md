## Herhalen over een lijst

Itereren over een lijst kan met de gebruikelijke `for`-lus, je weet immers op voorhand hoeveel items er in de lijst zitten via `len(lijst)`.

```python
lijst = [ "banaan", "appel", "peer" ]
for i in range( len(lijst) ):
    print( lijst[i] )
```

Dit zal achtereenvolgend `"banaan"`, `"appel"` en `"peer"` op het scherm weergeven.

Je kan deze syntax echter **sterk vereenvoudigen** als volgt:

```python
lijst = [ "banaan", "appel", "peer" ]
for fruit in lijst:
    print(fruit)
```

## Opgave

Vul de functie `gemiddelde(lijst)` aan, zodat deze gegeven een lijst met een aantal getallen, het rekenkundig gemiddelde berekent. Het gemiddelde wordt afgerond op 3 decimalen.

#### Voorbeelden

```
>>> gemiddelde( [3.0, 2.0, 5.0, 4.0] )
3.5
```