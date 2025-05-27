## Opgave
Schrijf een functie `som_van_drie(lijst)` die ons alle mogelijke opties van 3 getallen uit deze lijst geeft, waarbij de som gelijk is aan 0. De functie geeft als resultaat een lijst met tuples, waarbij elke tuple precies 3 **indexen** bevat die naar elementen uit de lijst wijzen.

#### Voorbeelden
```python
>>> som_van_drie([1, 2, 3, 4, 5])
[(0, 3, 4), (1, 2, 4)]
```

```python
>>> som_van_drie([1, 2, 3, 4, 5, 4])
[(0, 3, 4), (0, 4, 5), (1, 2, 4), (1, 3, 5)]
```

```python
>>> som_van_drie([1, 2, 3, 4, 5, -9, -9])
[(0, 3, 4), (1, 2, 4)]
```