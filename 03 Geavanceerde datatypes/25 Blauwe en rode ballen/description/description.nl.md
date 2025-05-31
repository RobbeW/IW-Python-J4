Beschouw deze lijst met blauwe en rode ballen: `["🔴", "🔵", "🔵", "🔴", "🔴", "🔵"]`. Als we bij elke bal tellen hoeveel blauwe ballen er rechts van die liggen, de bal zelf ook meegeteld, dan bekomt men deze lijst `[3, 3, 2, 1, 1, 1]`.

Door van elk getal in deze lijst de rest te nemen bij deling door 2 bekomt men `[1, 1, 0, 1, 1, 1]`.

Stel nu dat men zo'n lijst men `0` en `1` waarden krijgt, kan je dan zo'n oorspronkelijke ballenrij opstellen?

## Opgave

Schrijf een functie `ballenrij(lijst)` die gegeven een lijst met `0` en `1` waarden, zo'n oorspronkelijke ballenrij retourneert.

Als er meerdere oplossing zijn, volstaat het één oplossing te retourneren.

Bestudeer onderstaande voorbeelden grondig.

#### Voorbeelden

```python
>>> ballenrij([1, 1, 0, 1, 1, 1])
["🔴", "🔵", "🔵", "🔴", "🔴", "🔵"]
```

```python
>>> ballenrij([0, 1, 1, 1, 0, 1, 0, 0])
["🔵", "🔴", "🔴", "🔵", "🔵", "🔵", "🔴", "🔴"]
```

{: .callout.callout-secondary}
>#### Bron
> Gebaseerd op probleem *Ballenrij*, Bebras 2024 (Padawan). 