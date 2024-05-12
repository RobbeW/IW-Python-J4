Bij kwalitatieve kleurendruk wordt meestal geen RGB kleurensysteem gebruikt, maar het <a href="https://nl.wikipedia.org/wiki/CMYK" target="_blank">CMYK kleurensysteem</a> (Cyaan, Magenta, Yellow, Key). 

![Het CYMK kleurmodel.](media/CMYK.png "Afbeelding door Hemidah op Wikipedia."){:data-caption="Het CYMK kleurmodel." width="30%"}

## Opgave
Schrijf een functie `RGB_to_CMYK(kleurcode)` die gegeven een **RGB**-kleurcode als **tupel** de vier CMYK-waarden (als tupel) bepaalt. Rond af op 2 decimalen. Gebruik hiervoor de volgende formules:

<div class="dodona-centered-group">

K = 1- maximum (<span style="color:#FF0000">R</span>, <span style="color:#00FF00">G</span>, <span style="color:#0000FF">B</span> ) / 255<br/>
<span style="color:#00C5C0">C</span> = (1- <span style="color:#FF0000">R</span>/255 - K) / (1 - K)<br/>

<span style="color:#FD01FD">M</span> = (1- <span style="color:#00FF00">G</span>/255 - K) / (1 - K)<br/>

<span style="color:#F1EB01">Y</span> = (1- <span style="color:#0000FF">B</span>/255 - K) / (1 - K)
</div>

#### Voorbeeld
```
>>> RGB_to_CMYK( (48, 213, 200) )
(255, 127, 127)
```