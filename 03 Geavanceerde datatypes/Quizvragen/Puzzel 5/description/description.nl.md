## Opgave
Schrijf een functie `winnaar(lijst)` dat in een 2D-lijst bepaalt wie er gewonnen heeft in een spelletje Tic tac toe. Je krijgt als input altijd een lijst van lengte 3, met hierin 3 lijsten van lengte 3 waarin de letters **"O"** of **"X"** staan. Als X of O wint return je 'X' of 'O', bij gelijkspel return je 'Draw'.

#### Voorbeelden
```python
[OOX]
[XOX]
[OOX]
>>> winnaar([['O', 'O', 'X'], ['X', 'O', 'X'], ['O', 'O', 'X']])
Draw
```

```python
[OXX]
[OOO]
[OOX]
>>> winnaar([['O', 'X', 'X'], ['O', 'O', 'O'], ['O', 'O', 'X']])
O
```

```python
[XXO]
[OXO]
[XOX]
>>> winnaar([['X', 'X', 'O'], ['O', 'X', 'O'], ['X', 'O', 'X']])
X
```