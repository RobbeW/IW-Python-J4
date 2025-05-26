## Opgave
Schrijf een functie `trappen_lopen(aantal)` dat ons vertelt in hoeveel verschillende manieren we een trap van `aantal` treden omhoog kunnen lopen, als we maximaal 2 treden kunnen nemen per stap.

Voor 3 treden hebben we volgende mogelijkheden:
* 1 trede, 1 trede, 1 trede
* 1 trede, 2 treden
* 2 treden, 1 trede
Ons functie zou hier dus 3 als antwoord geven.

#### Voorbeelden
```python
>>> trappen_lopen(4)
5
```

```python
>>> trappen_lopen(10)
89
```
