De schijf (HDD, SSD) in je laptop is onderverdeeld in clusters. Doorgaans is een cluster 4 096 bytes groot.

![8 clusters.](media/image-0.png "8 clusters."){:data-caption="8 clusters." .light-only width="50%"}

![8 clusters.](media/image_dark-0.png "8 clusters."){:data-caption="8 clusters." .dark-only width="50%"}

Als je een bestand wegschrijft naar je schijf, zoekt het besturingssysteem naar voldoende ongebruikte clusters om het volledige bestand in te bewaren
Bijvoorbeeld, stel dat het bestand 5 × 4 096 = 20 480 bytes groot is, dan past dit in 5 clusters.

![8 clusters.](media/image-1.png "8 clusters."){:data-caption="8 clusters." .light-only width="50%"}

![8 clusters.](media/image_dark-1.png "8 clusters."){:data-caption="8 clusters." .dark-only width="50%"}

Maar wat indien de grootte van het bestand geen veelvoud is van 4 096? Wat als het bijvoorbeeld 20 481 bytes groot is? Het is duidelijk dat 5 clusters niet
meer voldoende zijn. Kan een bestand misschien enkel een stukje van een cluster inpalmen?

Om efficiëntieredenen wordt dit niet toegelaten: elk bestand moet een geheel aantal clusters innemen. Clusters kunnen dan ook niet gedeeld worden door meerdere bestanden. Hierdoor gaat wat schijfruimte verloren: een bestand van 5 keer 4 096 + 1 = 20 481 groot zal 6 clusters innemen, wat overeenkomt met 6 × 4 096 = 24 576 bytes. Het bestand verbruikt dus 24 576 bytes aan schijfruimte, terwijl het slechts 20 481 bytes groot is. Dit verlies wordt interne fragmentatie genoemd.

Voor deze opgave moet je, gegeven de grootte van een bestand, uitrekenen hoeveel schijfruimte deze innemen, rekening houdend met interne fragmentatie.

## Gevraagd
Schrijf een programma dat aan de gebruiker de **grootte van een bestand** (in bytes) vraagt. 

Vervolgens geef je het aantal clusters weer dat nodig is om dit bestand te bewaren en bepaal je de efficiëntie van de opslag. Met andere woorden, hoeveel ruimte er procentueel verloren gaat. Rond dit af op 1 decimaal.


#### Voorbeeld
Bij een bestand van `20480` bytes, verschijnt er:
```
Er zijn 5 clusters nodig. Dit is 100.0 % efficiënt.
```

Bij een bestand van `20481` bytes, verschijnt er:
```
Er zijn 6 clusters nodig. Dit is 83.3 % efficiënt.
```

{: .callout.callout-secondary}
>#### Bron
> Vlaamse programmeerwedstrijd 2024 - categorie 1.
