## Opgave

Programmeer een functie `somlijst( lijst )` dat voor een gegeven lijst de cumulatieve lijst samenstelt. Dit is een lijst met de som van alle waarden kleiner of gelijk aan bepaalde index.

#### Voorbeelden
Bestudeer onderstaande voorbeelden grondig.

```
>>> somlijst( [1, 5, 6, -2] )
[1, 6, 12, 10]
```

Want er geldt bijvoorbeeld dat 12 = 1 + 5 +6.

```
>>> somlijst( [1, 5, 6, -2, 0, 5, 9] )
[1, 6, 12, 10, 10, 15, 24]
```