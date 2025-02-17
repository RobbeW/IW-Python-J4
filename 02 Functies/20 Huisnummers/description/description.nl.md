Iemand woont in een straat met een merkwaardige eigenschap. De som van **alle** huisnummers kleiner dan zijn huisnummer, is hetzelfde als de som van alle huisnummers groter dan zijn huisnummer.

![Foto door Clem Onojeghuo op Unsplash.](media/clem-onojeghuo.jpg "Foto door Clem Onojeghuo op Unsplash."){:data-caption="Foto door Clem Onojeghuo op Unsplash."  width="35%"}

Het huisnummer kan bijvoorbeeld 6 zijn (in een straat van 8 huizen), want 1 + 2 + 3 + 4 + 5 = 15 en 7 + 8 is ook 15. Het huisnummer 6 voldoet aan een bepaalde *symmetrie* in deze straat.

Komt dit nog vaak voor? Je gaat dit (wiskundig) probleem hieronder oplossen met behulp van Python.

## Opgave

* Schrijf een functie `som_onder(huisnummer)` die gegeven een huisnummer, de som van alle huisnummers eronder bepaalt.

* Schrijf een functie `is_symmetrisch(huisnummer)` die gegeven het huisnummer onderzoekt of er een *nummer* bestaat zodat de som van alle getallen kleiner dan het gegeven huisnummer gelijk is aan de som van alle getallen groter dan het huisnummer. Deze functie retourneert enkele `True` of `False`. Gebruik **in deze functie** de vorige functie `som_onder(huisnummer)`.

* Vraag de gebruiker nadien om een bovengrens en druk alle huisnummers af, **kleiner dan of gelijk aan** deze bovengrens, die aan de gevraagde eigenschap voldoen.

#### Voorbeeld 1

Bij invoer `10` verschijnt er:
```
Huisnummer 6 voldoet aan de bijzondere eigenschap.
```

Want de uitvoer van de aparte functies is als volgt:
```python
>>> som_onder(6)
15
```
en
```python
>>> is_symmetrisch(6)
True
```

#### Voorbeeld 2

Bij invoer `100` verschijnt er:
```
Huisnummer 6 voldoet aan de bijzondere eigenschap.
Huisnummer 35 voldoet aan de bijzondere eigenschap.
```
