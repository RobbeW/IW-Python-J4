<a href="https://nl.wikipedia.org/wiki/Sophie_Germain" target="_blank">Sophie Germain</a> was een Franse wiskundige die belangrijke bijdragen heeft geleverd aan de getaltheorie.

![Sophie Germain, Franse wiskundige.](media/sophie-germain.png "Sophie Germain, Franse wiskundige."){:data-caption="Sophie Germain, Franse wiskundige." .dark-only width="35%"}

Naar haar genoemd zijn de Sophie Germainpriemgetallen, die gebruikt worden in de cryptografie. Men noemt een priemgetal p een Sophie Germainpriemgetal indien 2 · p + 1 ook priem is. Zo is 11 een voorbeeld van een Sophie Germainpriemgetal, want 2 · 11 + 1 = 23 is ook priem, men noemt 23 in dit geval een **veilig** priemgetal.

## Opgave

Schrijf een functie `is_priem(getal)` die controleert of een gegeven getal priem is.

Schrijf daarna een functie `is_germainpriem(getal)` dat controleert of een gegeven getal een Sophie Germainpriemgetal is. Gebruik hierbij de functie `is_priem()`. Test deze functie door een getal aan de gebruiker te vragen en nadien weer te geven of dit al of niet Sophie Germainpriem is. Geef ook het veilige priemgetal weer indien dit bestaat.

#### Voorbeelden

Bij invoer `11` verschijnt er:
```
Dit is een Sophie Germainpriemgetal, het veilige priemgetal is 23
```
```python
>>> is_germainpriem(11)
True
```

Bij invoer `7` verschijnt er:
```
Dit is geen Sophie Germainpriemgetal
```
```python
>>> is_germainpriem(7)
False
```
