Je kan in Python een nieuwe lijst aanmaken via:

```python
lijst = []
```

Achteraf kan je er elementen aan toevoegen via `lijst.append(3)`. In dat geval zou de lijst vervolgens gelijk zijn aan `[3]`.

## Opgave

Programmeer een functie `lijstproduct(lijst1, lijst2)` dat gegeven twee lijsten van eenzelfde lengte **paarsgewijs** het product gaat bepalen. 

#### Voorbeelden

```python
>>> lijstproduct([1, 3], [2, -5])
[2, -15]
```
want 1 · 2 = 2 en 3 · (-5) = -15.


```python
>>> lijstproduct([-2, 0, 5], [-2, 9, 3])
[4, 0, 15]
```
want -2 · (-2) = 4, 0 · 9 = 0 en 5 · 3 = 15.


{: .callout.callout-info}
> #### Tip
> Implementeer een `for` loop, waarbij je de lengte van de lijst gebruikt.