In een spel stelt elk getal het aantal zombies voor in een sector van de stad.

Zo stelt `[3, 0, 5, 0, 2, 2, 0, 6]` een stad met acht sectoren voor. De allereerste sector is geïnfecteerd met 3 zombies, de tweede sector is nog niet geïnfecteerd, enz...

## Opgave

In deze oefening moet je **twee functies** programmeren.

- Programmeer een functie `aantal_gezond(sectoren)` dat het aantal gezonde (niet-geïnfecteerde) sectoren retourneert.
- Programmeer een tweede functie `infectie(sectoren)` die elke gezonde sector vervang door het gemiddelde van het aantal naburige zombies. Gebruik `math.floor()` om dit gemiddelde naar beneden af te ronden. 

#### Voorbeeld

```python
>>> aantal_gezond([3, 0, 5, 0, 2, 2, 0, 6])
3
```

```python
>>> infectie([3, 0, 5, 0, 2, 2, 0, 6])
[3, 4, 5, 3, 2, 2, 4, 6]
```