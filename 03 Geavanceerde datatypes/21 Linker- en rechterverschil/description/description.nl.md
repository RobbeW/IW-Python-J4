## Opgave

Gegeven een `lijst` met getallen:

- Schrijf een functie `linkersom(lijst)` die een nieuwe lijst retourneert, met op elke plaats de som van alle getallen links van die plaats. Staan er links geen getallen, neem dan `0`.

- Schrijf een functie `rechtersom(lijst)` die een nieuwe lijst retourneert, met op elke plaats de som van alle getallen rechts van die plaats. Staan er rechts geen getallen, neem dan `0`.

- Schrijf tot slot een functie `links_rechts_verschil(lijst)` die een nieuwe lijst retourneert met op elke plaats de absolute waarde van het verschil tussen de linker- en rechtersom.

Bestudeer onderstaande voorbeelden grondig.

#### Voorbeeld 1

```python
>>> links_rechts_verschil([10, 4, 8, 3])
[15, 1, 11, 22]
```

want:

```python
>>> linkersom([10, 4, 8, 3])
[0, 10, 14, 22]
>>> rechtersom([10, 4, 8, 3])
[15, 11, 3, 0]
```

en inderdaad `abs(0 - 15) = 15`,  `abs(10 - 11) = 1`, `abs(14 - 3) = 11` en `abs(22 - 0) = 22`.


#### Voorbeeld 2

```python
>>> links_rechts_verschil([2, 2, 2, 2])
[6, 2, 2, 6]
```

want:

```python
>>> linkersom([2, 2, 2, 2])
[0, 2, 4, 6]
>>> rechtersom([2, 2, 2, 2])
[6, 4, 2, 0]
```