Een (vierkant) piramidegetal is een getal dat geschreven kan worden als een som van opeenvolgende kwadraten. Zo is het piramidegetal gelijk aan 30. Want 30 = 1 + 4 + 9 + 16.

![Het vierde (vierkante) piramidegetal.](media/Square_pyramidal_number.png "Het vierde (vierkante) piramidegetal."){:data-caption="Het vierde (vierkante) piramidegetal." width="45%"}

## Opgave

- Schrijf een functie `piramidegetal(nummer)` dat gegeven het rangnummer `nummer`, het zoveelste piramidegetal gaat bepalen.

- Vraag de gebruiker nadien naar een rangnummer en geef het zoveelste piramidegetal weer.

#### Voorbeeld 1

Als de gebruiker `4` invoert verschijnt er:
```
Het 4 e piramidegetal is 30
```

want
```python
>>> piramidegetal(4)
30
```

#### Voorbeeld 2

Als de gebruiker `7` invoert verschijnt er:
```
Het 7 e piramidegetal is 140
```

want
```python
>>> piramidegetal(7)
140
```
Immers 1 + 4 + 9 + 16 + 25 + 36 + 49 = 140.