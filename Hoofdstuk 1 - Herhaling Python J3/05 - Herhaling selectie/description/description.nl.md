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

Schrijf een programma dat aan de gebruiker het huidige toner-niveau (als percentage) vraagt. Afhankelijk van het toner-niveau gebeuren verschillende acties.

- Indien de toner bijna op is (minstens 75% leeg), krijgen de mensen van de IT-dienst een melding om een nieuwe toner te bestellen;
- Is de toner minstens 90% leeg, dan verschijnt er een waarschuwing op het scherm van de printen én wordt eenzelfde melding naar de IT-dienst gestuurd;
- Is de toner volledig leeg, dan verschijnt een dwingende melding op het scherm van de printer en kan er niet meer afgedrukt worden. 

#### Voorbeelden


* Boodschap voor de IT-dienst: "Toner is bijna op, plaats bestelling bij" of "Toner is volledig op". 
