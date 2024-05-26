Je kan in Python een nieuwe lijst aanmaken via:

```python
lijst = []
```

Achteraf kan je er elementen aan toevoegen via `lijst.append(3)`. In dat geval zou de lijst vervolgens gelijk zijn aan `[3]`.

## Opgave

Programmeer een functie `lijstproduct(lijst1, lijst2)` dat gegeven twee lijsten van eenzelfde lengte **paarsgewijs** het product gaat bepalen. 

#### Voorbeeld

```
>>> lijstproduct( [1,3], [2,-5] )
[2, -15]
```

{: .callout.callout-info}
> #### Tip
> Gebruik een `for` loop, waarbij je de lengte van de lijst moet bepalen.