## Opgave

Programmeer een functie `somlijst_omgekeerd(lijst)` dat voor een gegeven lijst de cumulatieve lijst samenstelt maar in de omgekeerde richting. Je geeft telkens de som van alle waarden met een index groter dan of gelijk aan de huidige index.

#### Voorbeelden
Bestudeer onderstaande voorbeelden grondig.

```python
>>> somlijst_omgekeerd([1, 5, 7, -2])
[11, 10, 5, -2]
```

Want er geldt *bijvoorbeeld* dat 10 = 5 + 7 + (-2).

```python
>>> somlijst_omgekeerd([1, 5, 6, -2, 0, 5, 9])
[24, 23, 18, 12, 14, 14, 9]
```

{: .callout.callout-warning}
> #### Opgelet
>
> Er werd een tijdslimiet ingesteld voor deze oefening. Het uitvoeren van je code mag maximaal 5s in beslag nemen.
