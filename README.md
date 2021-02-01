<h1 align="center">Welcome to qualite-donnees-tp 👋</h1>
<p>
  <a href="https://twitter.com/YannDurand11" target="_blank">
    <img alt="Twitter: YannDurand11" src="https://img.shields.io/twitter/follow/YannDurand11.svg?style=social" />
  </a>
</p>

> TP1 du cours sur la qualité des données

## Install

Installation des dépendances :
```sh
pip install -r requirements.txt
```

PS: il est conseillé d'utiliser un environnement virtuel (virtualenv ou venv)

## Usage

Exécution du programme avec les données valides
```sh
python3 main.py
```

Exécution du programme avec les données non conformes
```sh
python3 App/app.py
```

## Question du TP

Les premières questions, celles sur le calcul de statistiques et affichage des données via des courbes et un cursor mobile sont inclus dans les fichiers main.py et graph.py situer à la racine.

Exemple de courbe : 

![screenshot](/Data/screenshots/screenshot.png)
### Recommencez	avec	le	jeu	SI-erreur	après	avoir	corrigé	les	valeurs	en	erreur.	Précisez	vos	méthodes.

Pour corriger le fichier des données SI-erreur,
Nous avons en premier déterminé les données erronées telles que
- Les valeurs vide (NaN)
- Les valeurs incohérentes (valeur hexadécimale comme température)

pour le traitement nous avons trouvé deux solutions

- oublier les valeurs
- Deviner à partir d'autres variables

Nous avons choisi comme solution de deviner les variables manquantes ou erronées en faisant la moyenne des valeurs existantes pour chaque mois 

### Les	données	corrigées	sont	elles	proches	des	valeurs	sans	erreur	?

Les résultats obtenus sont sensiblement identique. Il y a des écarts (max août à 48° par exemple) mais qui ne viennent pas des erreurs corrigées.

### A	partir	de	données	opendata	du	second	fichier,	retrouver	le	type	de	climat

Ces données proviennent de Finlande, où règne un climat froid, voir tempéré mais avec de grands écarts observable entre les période estivale et hivernale.

### reprendre	les	données	typiques	de	la	localisaon	proche		fournies	en	complément	,	comparer	les	écarts.

L'objectif est d'extraire les données d'une ville européenne, effectuer le traitement comme pour les données que l'ont possède et y opérer un ratio sur chacune des données pour vérifier la corrélation. 
* De 0 à 0,5, les données ne sont pas corrélé,
* De 0,5 à 0,8, les données commencent à se ressembler
* de 0,8 à 0,9, les données sont cohérente et corrélé, 
* de 0,9 à 1 les données sont identiques (ou presque).

Il serait aussi envisageable d'effectuer la différence entre les valeurs lue à chaque X, ou même effectuer la différence des aires entre les deux courbes superposées, afin d'éviter une estimation de corrélation "validé" alors que visuellement, les courbes se croisent et sont en miroir, ce qui en ferait des courbes absolument pas identique.

#### Méthode

Afin d'estimer d'où proviennent les données, nous avons utilisé deux sites :
* https://nomadlist.com/
* https://www.infoclimat.fr/

Nous avons d'abord comparer visuellement les moyennes de températures avec des villes de régions du monde cohérente avec celles que nous possèdons. Via le site nomadlist nous avons pu trouver une ville qui correspond plus ou moins à nos données, en se basant sur une recherche à partir des valeur maximale et minimale sur un mois car à l'année, les écartes étaient trop grand et ne permettait pas un filtre optimisé. 

Le second site nous a permis d'obtenir les données sous format csv et donc permettre la comparaison expliciter plus haut.
### Qu'en	concluez	vous	?

### De	quelle	la	capitale	européenne	avez	vous		eu	les	données.

## Author

👤 **Yann Durand**

* Website: https://codewithnefaden.wordpress.com/
* Twitter: [@YannDurand11](https://twitter.com/YannDurand11)
* Github: [@nefaden](https://github.com/nefaden)

👤 **Marouwane Bah**

* Github: [@marouwanebah](https://github.com/marouwanebah)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
