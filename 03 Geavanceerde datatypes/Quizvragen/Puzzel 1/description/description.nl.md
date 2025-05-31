
## Opgave
Schrijf een functie `schuif_links(lijst, aantal)` die een de elementen uit een lijst **aantal** keer naar links doorschuift. De uitvoer is dan deze doorgeschoven lijst.


#### Voorbeelden

```python
>>> schuif_links([1, 2, 3, 4, 5], 2)
[3, 4, 5, 1, 2]
```

```python
>>> schuif_links(["appel", "banaan", "peer", "citroen", "druif"], 3)
["citroen", "druif", "appel", "banaan", "peer"]
```

```python
>>> schuif_links([1, 2, 3, 4, 5], 5)
[1, 2, 3, 4, 5]
```

```python
>>> schuif_links([1, 2, 3, 4, 5], 7)
[3, 4, 5, 1, 2]
```