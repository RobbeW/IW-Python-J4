Wanneer we programmeren in een taal zoals Python, zal de computer onze instructies één voor één, van boven naar onder, uitvoeren. Dit wil **niet** zeggen dat alle code altijd uitgevoerd wordt. Door slim gebruik te maken van conditionele logica en voorwaarden, kunnen er meerdere mogelijkheden zijn. Dit noemen we de **selectie** of **keuze** en maakt binnen Python gebruik van de `if`, `else` en `elif`-functies.

## Syntax

Bij de **selectie** hanteren we volgende syntax: 

```python
if <voorwaarde>:
    <acties>
```

```python
if <voorwaarde 1>:
    <acties>
elif <voorwaarde 2>:
    <acties>
```

```python
if <voorwaarde 1>:
    <acties>
else:
    <acties>
```

{: .callout.callout-danger}
> #### Opgelet!
> Code die bij een bepaalde voorwaarde uitgevoerd wordt krijgt een **indent** of **insprong**.  Python is hier zeer gevoelig voor!

Je kan voorwaarden coderen met de volgende symbolen:

|-----------+---------------------------+
| Symbool   | Grootte                   |
|:---------:|---------------------------|
| `==`      | gelijk aan                |
| `!=`      | niet gelijk aan           |
| `<`       | kleiner dan               |
| `<=`      | kleiner dan of gelijk aan |
| `>`       | groter dan                |
| `>=`      | groter dan of gelijk aan  |
|-----------+---------------------------|
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Je kan voorwaarden **combineren** met de **booleaanse operatoren**, `and`, `or` en `not`.

## Opgave

Een printer kan kleurkopies afdrukken door gebruik te maken van toner, deze bevat een soort poeder dat fungeert als kleurstof. 

Schrijf een programma dat aan de gebruiker het huidige toner-niveau (als percentage) **vraagt**. Afhankelijk van het toner-niveau verschijnt een andere boodschap

- Indien de toner bijna op is (slechts 15% vol), krijgen de mensen van de IT-dienst een melding om een nieuwe toner te bestellen;
- Is de toner bijna volledig leeg is (slechts 10% vol), dan verschijnt er een waarschuwing op het scherm van de printen **én** wordt eenzelfde melding naar de IT-dienst gestuurd;
- Is de toner volledig leeg, dan verschijnt een dwingende melding op het scherm van de printer en kan er niet meer afgedrukt worden. 

#### Voorbeelden

Bij invoer `0.15` (15% vol) verschijnt er:
```
Bestel een nieuwe toner.
```

Bij invoer `0.05` (5% vol) verschijnt er:
```
Toner is bijna leeg.
Bestel een nieuwe toner.
```

Bij invoer `0.0` (0% vol) verschijnt er:
```
Toner is volledig leeg.
Je kan niet meer afdrukken.
```

Bij invoer `0.45` (45% vol) verschijnt er niets.