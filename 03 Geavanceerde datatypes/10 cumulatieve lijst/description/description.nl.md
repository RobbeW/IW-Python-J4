## Opgave

Programmeer een functie `somlijst(lijst)` dat voor een gegeven lijst de cumulatieve lijst samenstelt. Dit is een lijst met de som van alle waarden kleiner of gelijk aan bepaalde index.

#### Voorbeelden
Bestudeer onderstaande voorbeelden grondig.

```python
>>> somlijst([1, 5, 7, -2])
[1, 6, 13, 11]
```

Want er geldt *bijvoorbeeld* dat 13 = 1 + 5 + 7.

```python
>>> somlijst([1, 5, 6, -2, 0, 5, 9])
[1, 6, 12, 10, 10, 15, 24]
```

{: .callout.callout-warning}
> #### Opgelet
>
> Er werd een tijdslimiet ingesteld voor deze oefening. Het uitvoeren van je code mag maximaal 5s in beslag nemen.
