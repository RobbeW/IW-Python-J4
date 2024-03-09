De **remweg** is de afstand (in meter) die een voertuig aflegt terwijl er wordt geremd. Deze afstand $$s_{\text{rem}}$$ wordt berekend via de formule:

$$
    s_{\text{rem}} = \dfrac{v^2}{2\cdot a_\text{rem}}
$$

Hierbij stelt $$v$$ de **beginsnelheid** in m/s voor en $$a_{\text{rem}}$$ de **remvertraging** in m/s². Bij een droog vlak wegdek en met goede rubberbanden kan de remvertraging 10 m/s² bedragen, is het wegdek glad, dan kan de remvertraging sterk afnemen.

![Homer Simpson gooit alle remmen dicht.](media/simpson.gif "Homer Simpson gooit alle remmen dicht."){:data-caption="Homer Simpson gooit alle remmen dicht." width="400px"}

## Opgave
Schrijf een programma dat een beginsnelheid vraagt (in **km/u**) en daarna de remvertraging (in m/s²). 

Het programma berekent en toont vervolgens de remweg, afgerond op 3 cijfers na de komma.

#### Voorbeelden
De invoer `90` (km/u) en remvertraging `8` m/s² leidt tot uitvoer:
```
Remweg: 39.062 m.
```

De invoer `111.5` (km/u) en remvertraging `9.2` m/s² leidt tot uitvoer:
```
Remweg: 52.135 m.
```

{: .callout.callout-warning}
> #### Opgelet
> Vergeet niet om de invoer van km/u om te laten rekenen naar m/s!