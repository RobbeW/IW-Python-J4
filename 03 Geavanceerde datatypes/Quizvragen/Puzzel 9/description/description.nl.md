## Opgave
Schrijf een functie `som_van_drie(lijst)` die ons alle mogelijke opties van 3 getallen uit deze lijst geeft, waarbij de som gelijk is aan 10. De functie geeft als resultaat een lijst met tuples, waarbij elke tuple precies 3 **indexen** bevat die naar elementen uit de lijst wijzen.

#### Voorbeelden
```python
>>> som_van_drie([1, 2, 3, 4, 5])
[]
```

```python
>>> som_van_drie(1, 2, 3, 4, 5, -9)
[(3, 4, 5)]
```

```python
>>> som_van_drie(1, 2, 3, 4, 5, -9, -9)
[(3, 4, 5), (3, 4, 6)]
```