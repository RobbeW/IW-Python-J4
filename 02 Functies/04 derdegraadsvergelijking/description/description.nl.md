Na het bepalen van een algemene methode voor het oplossen van vierkantsvergelijkingen werd gezocht naar de algemene oplossing van een derdegraadsvergelijking. Dit is een vergelijking van de gedaante:

$$\mathsf{ax^3+bx^2+cx+d=0}$$

In 1545 onstond in Italië een ware rel toen de wiskundige Gerolamo Cardano een algemene oplossing publiceerde voor een **gereduceerde derdegraadsvergelijking**. Dit is een vergelijking van de gedaante:

$$\mathsf{x^3+px+q=0}$$

![De wiskundigen Gerolamo Cardano en Niccolò Fontana Tartaglia.](media/Cardano-Tartaglia.jpg "Cardano en Tartaglia"){:data-caption="De wiskundigen Gerolamo Cardano en Niccolò Fontana Tartaglia." width="40%"}

Oorzaak van de rel was dat een andere wiskundige Niccolò Fontana Tartaglia in 1539 zijn oplossingsmethode deelde met Cardano, maar onder de belofte dat hij dit nooit zou publiceren. Ondertussen had Cardano een analoge oplossingsmethode besproken met een derde wiskundige, namelijk Scipione del Ferro. Het volledige dispuut ging gepaard met heel wat beledigingen.

Net als bij een vierkantsvergelijking speelt een getal $$\mathsf{D}$$, genaamd de discriminant, een informerende rol. Voor de gereduceerde derdegraadsvergelijking is de discriminant van de vorm:

$$\mathsf{D = -4p^3 -27q^2}$$

Een derdegraadsvergelijking zal in het meest algemene geval, namelijk indien de discriminant strikt positief is, **drie verschillende** reële oplossingen hebben. Is de discriminant echter gelijk aan nul dan zullen **minstens twee oplossingen aan elkaar gelijk zijn**. En bij een strikt negatieve discriminant is altijd **slechts één reële oplossing**.

## Opgave

Schrijf een functie `discriminant(p, q)` die voor een gereduceerde derdegraadsvergelijking $$\mathsf{x^3+px+q=0}$$ de discriminant retourneert. 

Test het programma vervolgens uit door aan de gebruiker de waarde van $$\mathsf{p}$$ en $$\mathsf{q}$$ te vragen, de discriminant uit te rekenen met behulp van de functie en daarna het **aantal oplossingen** op het scherm afdrukt.

#### Voorbeelden
De derdegraadsvergelijking $$\mathsf{x^3-3x+2=0}$$ heeft als oplossingenverzameling $$\mathsf{V = \{-2, 1\}}$$.
```
Van de drie oplossingen zijn er minstens twee aan elkaar gelijk.
```
want
```python
>>> discriminant(-3, 2)
0
```

De derdegraadsvergelijking $$\mathsf{x^3+x+2 = 0}$$ heeft als oplossingenverzameling $$\mathsf{V = \{-1\}}$$.
```
Er is exact één reële oplossing.
```
want
```python
>>> discriminant(1, 2)
-112
```

De derdegraadsvergelijking $$\mathsf{x^3-4x= 0}$$ heeft als oplossingenverzameling $$\mathsf{V = \{-2,0,2\}}$$.
```
Er zijn drie verschillende reële oplossingen.
```
want
```python
>>> discriminant(-4, 0)
256
```