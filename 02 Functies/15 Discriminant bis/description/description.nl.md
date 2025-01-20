## Opgave

Programmeer de functie `discriminant(a, b, c)` dat gegeven de coëfficiënten $$\sf a$$, $$\sf b$$, $$\sf c$$ van een vierkantsvergelijking $$\mathsf{ax² + bx + c = 0}$$, de discriminant uitrekent en retourneert.

Maak daarna een twee functie `aantal_oplossingen(a, b, c)` die de vorige functie gebruikt en het aantal reële oplossing van de vierkantsvergelijking retourneert.

Vraag daarna in volgorde naar deze coëfficiënten en gebruik de functie `aantal_oplossingen(a, b, c)` om het aantal oplossingen weer te geven.

#### Voorbeeld 1

Indien het over de vergelijking $$\mathsf{2x^2 + 6x + 5 = 0}$$ gaat, dan verschijnt er:
```
Er zijn geen reële oplossingen.
```
want de achterliggende functies werken als volgt:
```python
>>> discriminant(2, 6, 5)
-4.0
```

```python
>>> aantal_oplossingen(2, 6, 5)
0
```


#### Voorbeeld 2

Indien het over de vergelijking $$\mathsf{x^2 + 2x + 1 = 0}$$ gaat, dan verschijnt er:
```
Er is exact één reële oplossing.
```
want de achterliggende functies werken als volgt:
```python
>>> discriminant(1, 2, 1)
0
```

```python
>>> aantal_oplossingen(1, 2, 1)
1
```


#### Voorbeeld 3

Indien het over de vergelijking $$\mathsf{x^2 + 3x -4 = 0}$$ gaat, dan verschijnt er:
```
Er zijn twee verschillende reële oplossingen.
```
want de achterliggende functies werken als volgt:
```python
>>> discriminant(1, 3, -4)
25
```

```python
>>> aantal_oplossingen(1, 3, -4)
2
```
