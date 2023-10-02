Het <a href="https://nl.wikipedia.org/wiki/Getal_van_Ohnesorge" target="_blank">getal van Ohnesorge</a> $$\text{Oh}$$ is een getal dat aangeeft of een vloeistof eenvoudig, of juist lastig is om te verstuiven.

Men kan dit getal berekenen via de formule:

$$
\text{Oh} = \dfrac{\eta}{\sqrt{\rho\cdot d\cdot \sigma}}
$$

Waarbij eta $$\eta$$ staat voor de **viscositeit** (stroperigheid) van de vloeistof ( in kg/(m·s) ), rho $$\rho$$ de **massadichtheid** van de vloeistof ( in kg/m³ ), $$d$$ de **diameter** van de vloeistofdruppels ( in m ) en tot slot sigma $$\sigma$$ de **oppervlaktespanning** ( in N/m ).

Een *inkjetprinter* kan bijvoorbeeld enkel werken met vloeistoffen waarvan het getal van Ohnsorge tussen 0,1 en 1,0 ligt.

![Inktdruppels bij een inkjetprinter.](media/inkjet.gif "Inktdruppels bij een inkjetprinter."){:data-caption="Inktdruppels bij een inkjetprinter." width="480px"}


## Opgave
Schrijf een programma dat de naam van de vloeistof vraagt en vervolgens **in volgorde** de viscositeit, de massadichtheid, de diameter (**in μm**) en de oppervlaktespanning. 

Tot slot berekent het programma het getal van Ohnesorge geeft dit weer op een specifieke manier. Het getal wordt weergegeven op 3 cijfers na de komma.

#### Voorbeeld
Voor `printerinkt` met een viscositeit van `0.015` kg/(m·s), massadichtheid `920` kg/m³, diameter `50` μm en oppervlaktespanning van `0.029` N/m verschijnt er:
```
Het Ohnsorge getal van kleine druppels printerinkt is 0.411.
```

{: .callout.callout-info}
> #### Tips
> - Vergeet niet de diameter om te zetten van μm naar m;
> - Om bij de weergave op het scherm het eindpunt aan het getal vast te *plakken* kan je gebruik maken van `str()` (om een getal om te zetten naar tekst) en `+` (om te concateneren - tekst samenvoegen - zonder spatie).