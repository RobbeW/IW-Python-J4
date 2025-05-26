<a href="https://en.wikipedia.org/wiki/Cacho_Alalay" target="_blank">Cacho Alalay</a> is een populair dobbelspel in Bolivië. In het spel worden vijf dobbelstenen gerold, (a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, a<sub>4</sub>, a<sub>5</sub>). Hierna noteert men deze worp en bepaalt men de score volgens bepaalde regels. 

We zullen ons focussen op één bijzondere: *Escala*. Dit is een worp waarbij de dobbelstenen een rij opeenvolgende getallen vormen.

Onderstaande worp is een voorbeeld van een *Escala*:

<span class="mdi mdi-36px mdi-dice-1-outline"></span> <span class="mdi mdi-36px mdi-dice-2-outline"></span> <span class="mdi mdi-36px mdi-dice-3-outline"></span> <span class="mdi mdi-36px mdi-dice-4-outline"></span> <span class="mdi mdi-36px mdi-dice-5-outline"></span>

## Opgave

Programmeer een functie `escala(worpen)` die gegeven een tupel `worpen` met de vijf worpen **in stijgende volgorde** bepaalt of dit al dan niet een *Escala* worp is.

#### Voorbeelden

```python
>>> escala([1, 2, 3, 4, 5])
True
```

```python
>>> escala([2, 3, 4, 5, 6])
True
```

```python
>>> escala([1, 4, 4, 4, 5])
False
```

```python
>>> escala([1, 3, 4, 5, 6])
False
```

```python
>>> escala([1, 2, 2, 3, 6])
False
```


{: .callout.callout-secondary}
>#### Bron
> Universiteit van Valladolid (UVa), probleem *Cacho*.
