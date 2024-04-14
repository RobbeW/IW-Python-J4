De Weerwolf is een <a href="https://nl.wikipedia.org/wiki/Weerwolf_(achtbaan)" target="_blank">houten achtbaan</a> in Walibi Waver. 

<div class="hidden-print">
    <div class="dodona-centered-group">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/jBsPNMuXcEI?start=54" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
</div>

Indien er één trein actief is, dan kan deze per rit 24 personen vervoeren. Een rit duurt met in- en uitladen van personen ongeveer 3 minuten.

## Opgave

Schrijf een programma dat aan de gebruiker **eerst** het aantal mensen in de wachtrij vraagt, daarna wordt er gevraagd naar hoeveel mensen er na 3 minuten bijkomen. 

Omdat de wachtrij niet eindeloos blijft groeien mag je er van uitgaan dat dat er telkens minder mensen aanschuiven. Vraag de gebruiker hoeveel mensen er elke beurt **minder** aanschuiven. 

Geef telkens het scherm weer **hoeveel mensen er aanschuiven** zolang de wachtrij groter wordt. Geef nadien weer na hoeveel minuten de wachttijd het langst was.

#### Voorbeeld 1
Stel bijvoorbeeld dat er `40` mensen in de wachtrij staan. Elke 3 minuten komen er `30` en dit aantal neemt telkens met `5` af. De eerste keer komen er dus 30 mensen bij, daarna 25, daarna 20, daarna 15, enz...

```
Na 3 minuten bevat de wachtrij 46 personen
Na 6 minuten bevat de wachtrij 47 personen
De wachtrij was het langst na 6 minuten.
```

Inderdaad, want de eerste keer berekent men het aantal mensen in de wachtrij via: 40 - 24 + 30 = 46. De tweede keer via: 46 - 24 + 25 = 47. De volgende keer via: 47 - 24 + 20 = 43. De wachtrij was na 6 minuten dus het langste.

#### Voorbeeld 2
Stel bijvoorbeeld dat er `60` mensen in de wachtrij staan. Elke 3 minuten komen er `50` en dit aantal neemt telkens met `3` af. De eerste keer komen er dus 50 mensen bij, daarna 47, daarna 44, daarna 41, enz...

```
Na 3 minuten bevat de wachtrij 86 personen
Na 6 minuten bevat de wachtrij 109 personen
Na 9 minuten bevat de wachtrij 129 personen
Na 12 minuten bevat de wachtrij 146 personen
Na 15 minuten bevat de wachtrij 160 personen
Na 18 minuten bevat de wachtrij 171 personen
Na 21 minuten bevat de wachtrij 179 personen
Na 24 minuten bevat de wachtrij 184 personen
Na 27 minuten bevat de wachtrij 186 personen
De wachtrij was het langst na 27 minuten.
```