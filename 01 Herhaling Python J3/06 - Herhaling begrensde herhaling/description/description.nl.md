Een **begrensde herhaling** is een herhaling van acties waarvan we, **op voorhand** (dus bij de fase van de analyse in het computationeel denken), weten hoeveel keer die uitgevoerd moet worden. Het aftellen bij verstoppertje, het verzamelen van 100 schelpen ... 

## Syntax

Voor een begrensde herhaling gebruiken we volgende syntax: 

```python
for i in range():
    <acties>
```

Hier is `i` de naam van de een variabele (soms ook *teller* genoemd).

De waarden die `i` aanneemt hangen af van het gebruik van de `range()` functie:

```python
range( 4 )       # i is achtereenvolgens 0, 1, 2, 3
range( 3, 6 )    # i is achtereenvolgens 3, 4, 5
range( 0, 8, 2 ) # i is achtereenvolgens 0, 2, 4, 6
```

## Opgave

Elk jaar groeit de bevolking van België aan met ongeveer 62 770 inwoners. Dit door een combinatie van geboortecijfers (nataliteit die hoger ligt dan de mortaliteit) en immigratie. Op 1 januari 2023 telde België 11 697 557 inwoners.

Voor de begrotingsopmaak en de staatsschuld wil men berekenen hoeveel Belgen er zullen zijn in een eindjaar. 

Schrijf een programma dat:
- Het eindjaar vraagt (bvb 2070);
- per jaar berekent hoeveel inwoners België volgens de verwachtingen zal tellen (op 1 januari van dat jaar);
- **indien** het jaartal deelbaar is door tien, het jaartal en het aantal inwoners weergeeft op het scherm;

Gebruik de voorgedefinieerde variabelen `inwoners` en `toename`.

#### Voorbeelden

Bij een invoer van `2070` krijgt men de volgende uitvoer:
```
In 2030 verwacht men 12136947 inwoners in België.
In 2040 verwacht men 12764647 inwoners in België.
In 2050 verwacht men 13392347 inwoners in België.
In 2060 verwacht men 14020047 inwoners in België.
In 2070 verwacht men 14647747 inwoners in België.
```

Bij een invoer van `2030` krijgt men de volgende uitvoer:
```
In 2030 verwacht men 12136947 inwoners in België.
```
