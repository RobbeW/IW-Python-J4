
## Opgave
Schrijf een functie `verwissel(lijst, nummer1, nummer2)` die uit een lijst `lijst` de elementen op plaatsen `nummer1` en `nummer2` omwisselt. Je retourneert nadien de aangepaste lijst.

Let wel op dat de nummers overeenkomen met een normale telling van de elementen uit de lijst. Het *eerste* element, het *tweede* element, enz...

Bestudeer onderstaande voorbeelden grondig.

#### Voorbeelden

```python
>>> verwissel(["appel", "banaan", "peer", "citroen", "druif"], 1, 3)
["peer", "banaan", "appel", "citroen", "druif"]
```

De fruitsoorten op de eerste en derde plaats werden van plaats omgewisseld.

```python
>>> verwissel(["appel", "banaan", "peer", "citroen", "druif"], 3, 1)
["peer", "banaan", "appel", "citroen", "druif"]
```

```python
>>> verwissel(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "z"], 5, 5)
["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "z"]
```

Het element op de vijfde plaats (`"e"`) werd met zichzelf omgewisseld.