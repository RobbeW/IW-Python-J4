De <a href='https://nl.wikipedia.org/wiki/Discriminant' target='_blanc'>discriminant</a> is de uitdrukking die zal bepalen of een vierkantsvergelijking al dan niet oplossingen heeft.

## Opgave

Schrijf een programma dat, **met behulp van een functie** de discriminant bepaalt van de veelterm $$\mathsf{2x^2+6x+5}$$ en van de veelterm $$\mathsf{4x^2+3x-2}$$. Je schrijft hiervoor een **algemene** functie `discriminant()`.

In het hoofdprogramma vraag je om deze functie (tweemaal) uit te voeren en het resultaat in volzin naar het scherm te schrijven.

## Voorbeeld

```
De discriminant van de veelterm 2x²+6x+5 is -4
De discriminant van de veelterm 4x²+3x-2 is 41
```
want er geldt:
```python
>>> discriminant(2, 6, 5)
-4
>>> discriminant(4, 3, -2)
41
```