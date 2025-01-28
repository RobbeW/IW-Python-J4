Stel dat je ijssalon met tien verschillende smaken ijs uitbaat, hoeveel verschillende mogelijkheden ijsjes met drie bollen kan je kiezen indien deze uit drie verschillende smaken moet bestaan?

Voor de eerste bol zijn er 10 smaakmogelijkheden, daarna heb je 9 mogelijke smaken en tot slot nog keuze uit 8 mogelijke smaken. In het totaal zijn er dus 720 verschillende opties.

Wat men hier berekent noemt men wiskundig een **variatie**. Bij een keuze van $$\mathsf{k}$$ opties uit $$\mathsf{n}$$ aantal mogelijkheden werkt men met de volgende formule:

$$
\mathsf{\dfrac{n!}{(n-k)!}}
$$

In dit voorbeeld geldt dus `n = 10` en `k = 3`, zodat:

$$
\mathsf{\dfrac{10!}{(10-3)!} = \dfrac{10!}{7!} = 720}
$$

Je berekent met andere woorden het quotiënt van **10 faculteit** en **7 faculteit**.

## Opgave

* Kopieer de functie `faculteit(n)` uit de vorige oefeningen reeks.

* Schrijf een functie `variatie(n, k)` die de variatie van `k` opties uit `n` berekent. Gebruik in deze functie de vorige functie `faculteit(n)`.

* Vraag de gebruiker nadien **in volgorde** om `n` en `k` en bepaal de variatie van `k` keuzes uit `n` opties.

#### Voorbeeld

Bij invoer `10` en `3` verschijnt er:
```
Er zijn 720 mogelijken voor 3 verschillende keuzes uit 10 opties.
```

Want de uitvoer van de aparte functies is als volgt:
```python
>>> variatie(10, 3)
720
```

```python
>>> faculteit(10)
3628800
>>> faculteit(7)
5040
```
en `3628800 / 5040 = 720`
