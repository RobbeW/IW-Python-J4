Neem het het getal 9 425. Dit getal is duidelijk niet priem, maar welk priemgetal ligt het dichtst in de buurt van dit getal?

## Opgave

Schrijf een functie `dichtste_priem(getal)` dat gegeven een getal (groter dan 2) het priemgetal zoekt dat het dichtst van het gegeven getal ligt. Programmeer hiervoor zelf de functies `is_priem(getal)`, `vorige_priem()` en `volgende_priem()`.

Indien het vorige en volgende priemgetal even ver liggen, kies dan het kleinste priemgetal. Zo liggen 3 en 7 even ver van 5, maar de keuze valt dan op 3.

#### Voorbeeld 1

```python
>>> dichtste_priem(9425)
9421
```
want
```python
>>> vorige_priem(9425)
9421
>>> volgende_priem(9425)
9431
```

#### Voorbeeld 2

```python
>>> dichtste_priem(5)
3
```
want
```python
>>> vorige_priem(5)
3
>>> volgende_priem(5)
7
```

