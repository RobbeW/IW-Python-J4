Priemgetallen vormen de bouwstenen van de wiskunde, ze worden als volgt gedefinieerd:

{: .callout.callout-danger}
> #### Definitie
> Een priemgetal is een **natuurlijk getal** groter dan 1 dat **enkel** deelbaar is door 1 en zichzelf.

In Python kan je relatief gemakkelijk controleren of een getal priem is. Beschouw bijvoorbeeld onderstaande code:

```python
getal = int( input( "Geef een getal in: " ) )
is_priem = True
for i in range(2, getal):
    if getal % i == 0:
        is_priem = False

if is_priem:
    print(getal, "is priem.")
else:
    print(getal, "is niet priem.")
```

Is de variabele `is_priem` na het uitvoeren van dit stukje code nog steeds `True`, dan werden **geen** *delers* gevonden en kan je besluiten dat het een priemgetal was.

Bovenstaande code kan wel **geoptimaliseerd** worden. Als je immers reeds één deler hebt gevonden, dan hoef je de andere getallen niet meer te controleren.

## Opgave
Optimaliseer het programma zodat het na dit vinden van één eerste deler meteen stopt.

#### Voorbeeld
Voert de gebruiker `182882380` dan verschijnt
```
182882380 is niet priem.
```

{: .callout.callout-warning}
> #### Opgelet
>
> Er werd een tijdslimiet ingesteld voor deze oefening. Het uitvoeren van je code mag maximaal 25s in beslag nemen.
