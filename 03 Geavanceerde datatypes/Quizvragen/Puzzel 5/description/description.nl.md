## Opgave
Schrijf een functie `winnaar(lijst)` dat in een 2D-lijst bepaalt wie er gewonnen heeft in een spelletje Tic tac toe. Je krijgt als input altijd een lijst van lengte 3, met hierin 3 lijsten van lengte 3 waarin de letters **"O"** of **"X"** staan. Als X of O wint return je 'X' of 'O', bij gelijkspel return je 'Draw'.

#### Voorbeelden
```
[OOX]
[XOX]
[OOX]
```
```python
>>> winnaar([['O', 'O', 'X'], ['X', 'O', 'X'], ['O', 'O', 'X']])
Draw
```

```
[OXX]
[OOO]
[OOX]
```
```python
>>> winnaar([['O', 'X', 'X'], ['O', 'O', 'O'], ['O', 'O', 'X']])
O
```

```
[XXO]
[OXO]
[XOX]
```
```python
>>> winnaar([['X', 'X', 'O'], ['O', 'X', 'O'], ['X', 'O', 'X']])
X
```