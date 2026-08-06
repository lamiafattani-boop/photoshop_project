# Étapes de la modélisation 
- [1. Gestionnaire de fichier](#Gestionnaire-de-fichier)
- [2. Ajustement de la couleur](#Ajustement-de-couleur)
- [3. Transformation géometrique](#Transformation-géométrique)
- [4. Outils de dessin](#Outils-de-dessin)
- [5. Filtres matricielle](#Filtres-matricielle)

## 1. Gestionnaire de fichier

Le gestionnaire de fichier consiste a importer ou exporter une photo afin de la modifier. Pour gérer cela, on utilisera une fichier json. Le seule problème réside dans la transformation les données binaire d'une image en une suite de caractère string car le json refuse le binaire. En effet, json est un format base sur javascript. En gros, le language javascript utilise le texte pour les structure de donnée. Donc on est obligé de tous transformer en texte rendu dans les fichier json

### 1.1 Exportation

    1. Le programme ouvre l'image et les donne sont lit en octets
    2. Le programme procèede ensuite a l'encodage on passe de binaire a java text
    3. Le programme emballe l'image sous une étiquette
    4. Le programme sauvegarde le fichier dans le disque dur

### 1.2 Importation

    1. Le programme lit le fichier json
    2. Le programme transforme le texte en octets
    3. Le programme copie les octed dans un fichier vierge 
    4. En appliquand la bonne extension .png .jpeg . Le syst`me reconnait L,image et l'exporte


## 2. Ajustement des couleurs



### 2.1 Système TSV ou TSL
En gros, toute midifcation de couleur que ce soit par le saturage, contraste, teinte etc.. joue avec les valeur des pixels tout simplement. Dans le cadre de notre projet, nous jouerons sur ces 3 aspects principale: teinte, saturation et luminisité. le fameux TSL. Le TSL est un système de couleur différent du RGB, on construit une couleur à partir de 3 composante : La teinte, La saturation et La lumière

![Réglages photoshop](https://www.pspourphotographes.com/wp-content/uploads/2018/04/coul4-2.jpg)

#### 2.1.1 Teinte
La teinrte se défénit par la forme pur d'une couleur. En gros, c'est le tuple de donne RGB tout simplement. Celle-ci est souvent défénis par le modulo de 360 dans le cercle chromatique.


![Cercle chromatique](https://www.aly-abbara.com/museum/chromographie/images/CMJ_cercle_chromatique.png)

Donnée importantes:
- 0° ou 360° : rouge ;
- 60° : jaune ;
- 120° : vert ;
- 180° : cyan ;
- 240° : bleu ;
- 300° : magenta.

#### 2.1.2 Saturation
La saturation est l'intensité de la couleur. Celle-ci varie entre 0 et 100%. Plus une saturation est faible plus l'image est grise. 

Un très bon exemple est ceci

![L'effet de saturation](https://media.greatbigphotographyworld.com/wp-content/uploads/2022/04/landscape-photo-before-after-using-saturation-773x1024.jpg)


#### 2.1.3 Valeur ou lumière
La valeur représente seulment à quel point on se rapproche du noir ou du blanc. la valeur zéro représente le noir et la valeur 100 représente le blanc


### 2.2 Système RGB

Le système RGB est plus simple a comprendre. En gros chaque couleur crée est un mélange de différente valeur des 3 couleurs primaire. Ces trois couleur principales sont le rouge le vert et le bleu.

#### 2.2.1 Valeurs
Les valeurs de chaque couleur étant situé entre 0 et 225. La valeur de zéro représente le plus sombre et la valeur de 225 représente le plus clair

![Système RGB](https://makerlex.com/wp-content/uploads/Easy-RGB-Split-Effect-Photoshop-Step-1-1024x548.png)

### 2.3 Conversion entre les deux système 
Pour qu'une couleur rgb passe au système hsv ou tsv, il faut faire en sorte de convertir les donnée de chaque système.

- Pour cela il existe une démarche scientifique

#### 2.3.1 De RGB à TSV

Imaginons une couleur rgb comme celle-ci : 
$$ (r,g,b) $$
chaque variable du système tsv possède sa formule 

##### 2.3.1.1 Teinte
$$
t =
\begin{cases}
0, & \text{si } \max = \min \\[6pt]
\left(60^\circ \times \dfrac{g-b}{\max-\min} + 360^\circ\right)
\bmod 360^\circ, & \text{si } \max = r \\[6pt]
60^\circ \times \dfrac{b-r}{\max-\min} + 120^\circ,
& \text{si } \max = g \\[6pt]
60^\circ \times \dfrac{r-g}{\max-\min} + 240^\circ,
& \text{si } \max = b
\end{cases}
$$

##### 2.3.1.2 Satruration
$$
s =
\begin{cases}
0, & \text{si } \max = 0 \\[6pt]
1-\dfrac{\min}{\max}, & \text{sinon}
\end{cases}
$$

##### 2.3.1.3 Valeur

$$
v = \max
$$

*** PETITE NOTE: quand on parle de maximum et de minimum on est entrain de discuter les plus grande  valeur du tuples $(r,g,b)$

##### 2.3.1.4 Explication simple des formule

Tout d'abord on cherche le maximum et le minimum. 

- Pour la valeur c'est simple on prend le maximum car celle-ci représente le niveau maximale de la luminosité de la couleur
- Pour la saturation, la pourcentage représente à quel point on s'éloigne du gris et que les couleur sont plus intenses donc 0%= completement gris. Donc avec la max et le min on peut déterminer la saturation. En effet, les compopsante sont différentes entre elles, plus la saturation est forte. pra exemple si une seul couleur est forte et les autres 0 la formule donnera 100% de saturation.
- Pour la teinte, c'est plus complexe. La fomule depend de quel couleur esrt au maximum pour situer la couleur principale ensuite on soustrait les deux autre couleur pour situer plus précisément cette couleur dans le cercle chromatique. Par exemple si le rouge est dominant. On soustrait le green et le bleu ensemble . Si le green est plus grand que blue , on se rapproche du jaune rouge, et à l'inverse on se rapprochera du rouge mangenta. Ainsi, si on divise par le max-min , c'est tout simplement pour normaliser. Pour de ce qui est la valeur 60 degres, c'est par ce que le cercle est divisé en 6 couleurs principales. 

#### 2.3.2 De TSV à RGB

- On commence d'abord par multiplier la saturation et la valeur qui va donner la quantité de couleur forte ou la composante forte  
$$ C= V\times\S $$

- Ensuite on va défénir une teinte prime $H^\prime$ qui sera le numéro du secteur dans lequel se trouve la couleur. En effet, le cercle est divissé en 6 sections de 60$^\circ$ chaque. Donc la formule:
$$ H^\prime= \dfrac{H}{60}$$ 

- Par la suite, la formule de :
$$ X= C (1- \abs{H^\prime mod 2-1})$$
Le X donne la composante intermédiaire parmi le rouge, vert et bleu

- Pour finir, X= intermediare et C= forte, Grace au $H^\prime$ on peut determiner dans quel section on est et la prochaine section ce tableasu indique clairement les section: 
  
- |    `H'` || Transition      |
- | ------: || --------------- |
- | `0 → 1` || rouge → jaune   |
- | `1 → 2` || jaune → vert    |
- | `2 → 3` || vert → cyan     |
- | `3 → 4` || cyan → bleu     |
- | `4 → 5` || bleu → magenta  |
- | `5 → 6` || magenta → rouge |

***Source ChatGPT

- Grâce a ces trois information, on est capable de créer un tuple rgb
- On classe dans le tuple en 4 étape
  1. Trouver la valeur de C
  2. Trouver la valeur de H prime
  3. Trouver la valwur de X
  4. Grace au H prime, trouver la couleur dominante parmi R,G,B et attribuer la valeur de C a celle-ci, 
  5. Trouver la valeur intermédiaire qui change , souvent diminue et donner la la valeur X
  6. Créer la combinaison et c'est terminé

- Combinaisons
$$
(R_1, G_1, B_1) =
\begin{cases}
(0,0,0) & \text{si } H \text{ est indéfini} \\
(C,X,0) & \text{si } 0 \leq H' < 1 \\
(X,C,0) & \text{si } 1 \leq H' < 2 \\
(0,C,X) & \text{si } 2 \leq H' < 3 \\
(0,X,C) & \text{si } 3 \leq H' < 4 \\
(X,0,C) & \text{si } 4 \leq H' < 5 \\
(C,0,X) & \text{si } 5 \leq H' < 6
\end{cases}
$$

## 3. Transformation géométrique

Il y a différentes type de transformation d'image: rigide et non rigide

### 3.1 Trnasformation rigide

 Les transformation rigides sont une forme de transformation ou la taille et les forme sont conservée. En gros, on parle seulment de deplacement (translation ou rotation) dans l'espace. Cependant, cette transformation requiert une base d'algèbre linaire:

 En effet, il y'a 