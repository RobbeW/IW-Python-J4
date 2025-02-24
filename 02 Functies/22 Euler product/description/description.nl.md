Leonhard Euler kon aantonen dat men $$\mathsf{\dfrac{\pi^2}{6}}$$ kan uitrekenen door middel van een **oneindig product**. Namelijk als volgt:

$$
\mathsf{\dfrac{\pi^2}{6} = \dfrac{2^2}{2^2 - 1} \cdot \dfrac{3^2}{3^2-1}\cdot \dfrac{5^2}{5^2-1}\cdot \dfrac{7^2}{7^2-1}\cdot \ldots}
$$

Aan het oneindig product wordt dus telkens een factor $$\mathsf{dfrac{p^2}{p^2-1}}$$ toevoegd, waarbij $$\mathsf{p}$$ een **priemgetal** is.


## Opgave
- Schrijf een functie `is_priem(getal)` dat gegeven een getal controleert of dit al dan niet priem is.

- Schrijf een functie `benadering_euler(aantal_factoren)` dat bovenstaande benadering van $$\mathsf{\dfrac{\pi^2}{6}}$$ uitrekent, afgerond op **6 cijfers** na de komma. Het aantal factoren van de benadering wordt gegeven als argument in de functie.
  
  De functie gebruikt uiteraard de vorige functie `is_priem(getal)`.

- Schrijf tot slot een programma dat aan de gebruiker een aantal factoren vraagt, de functie `benadering_euler()` gebruikt om een benadering voor $$\mathsf{\dfrac{\pi^2}{6}}$$ bepaalt en daarna hieruit een benadering voor $$\pi$$ uitrekent. Als $$\mathsf{B}$$ een benadering voor het product is, dan zal $$\mathsf{\pi \approx \sqrt{6\cdot B}}$$ zijn... rond af op 4 decimalen.


#### Voorbeelden
Als de gebruiker bijvoorbeeld `4` intikt, dan levert

```pyton
>>> benadering_euler(4)
1.595052
```

zodat de einduitvoer vervolgens dit is:

```
De benadering van pi met 4 factoren is: 3.0936
```