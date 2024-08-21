<a href="https://nl.wikipedia.org/wiki/Mexicanen_(dobbelspel)" target="_blank">Mexicanen</a> of **Mexen** is een dobbelspel dat door twee personen gespeeld kan worden. Elke worp bestaat uit twee dobbelstenen. Het dobbelspel gaat vooral over bluffen over wat je gegooid hebt, maar hier focussen we ons enkel op de scoringsregels. In tegenstelling tot veel andere dobbelspellen is de score van een worp niet zomaar de som van de dobbelstenen.

![Afbeelding door Edge2Edge Media op Unsplash.](media/edge2edge-media.jpg "Afbeelding door Edge2Edge Media op Unsplash."){:data-caption="Afbeelding door Edge2Edge Media op Unsplash." width="40%"}

In plaats daarvan is de puntentelling voor een worp als volgt:
- Een *Mex* is altijd de hoogste score, namelijk 1000;
  <span class="mdi mdi-36px mdi-dice-1-outline"></span> <span class="mdi mdi-36px mdi-dice-2-outline"></span> of <span class="mdi mdi-36px mdi-dice-2-outline"></span> <span class="mdi mdi-36px mdi-dice-1-outline"></span>
- Daarna komen de dubbele worpen, bijvoorbeeld
  <span class="mdi mdi-36px mdi-dice-4-outline"></span> <span class="mdi mdi-36px mdi-dice-4-outline"></span>, ...
  Indien beide spelers een dubbele worp hebben, dan wint diegene met het hoogste aantal ogen, vermenigvuldig hiervoor aantal ogen met 100.
- De andere worpen worden gerangschikt zodat grootste aantal ogen eerst komt te staan, bijvoorbeeld:
  <span class="mdi mdi-36px mdi-dice-4-outline"></span>  <span class="mdi mdi-36px mdi-dice-3-outline"></span>
  krijgt als score 43.

## Opgave

Schrijf een functie `mexen(s0, s1, t0, t1)` dat de winnaar bepaalt, waarbij `s0` en `s1` de worpen van speler 1 voorstellen en `t0` en `t1` deze van speler 2. Indien speler 1 wint, retourneer je `"speler 1"`, wint speler 2, dan retourneer je `"speler 2"` en anders `"gelijkspel`.

Om deze functie te kunnen maken programmeer je eerst een hulpfunctie `score(worp1, worp2)` dat gegeven twee worpen de waarde van deze worp gaat bepalen. 

Bestudeer zorgvuldig onderstaande voorbeelden.

#### Voorbeelden

```python
>>> mexen(1, 2, 1, 3)
speler 1
```
want
```python
>>> score(1, 2)
1000
>>> score(1, 3)
31
```


```python
>>> mexen(3, 3, 2, 1)
speler 2
```
want
```python
>>> score(3, 3)
300
>>> score(2, 1)
1000
```


```python
>>> mexen(6, 6, 2, 2)
speler 1
```
want
```python
>>> score(6, 6)
600
>>> score(2, 2)
200
```


```python
>>> mexen(4, 2, 2, 4)
gelijkspel
```
want
```python
>>> score(4, 2)
42
>>> score(2, 4)
42
```

{: .callout.callout-secondary}
>#### Bron
> Virginia Tech High School Programming Contest 2014
