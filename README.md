<h1 align="center">Welcome to qualite-donnees-tp 👋</h1>
<p>
  <a href="https://twitter.com/YannDurand11" target="_blank">
    <img alt="Twitter: YannDurand11" src="https://img.shields.io/twitter/follow/YannDurand11.svg?style=social" />
  </a>
</p>

> TP1 du cours sur la qualité des données

## Install

Install any dependancies by :
```sh
pip install -r requirements.txt
```

## Usage

Start the app with :
```sh
python3 main.py
```

## Question du TP

* Recommencez	avec	le	jeu	SI-erreur	après	avoir	corrigé	les	valeurs	en	erreur.	Précisez	vos	méthodes.


Pour corriger le fichier des données SI-erreur
Nous avons en premier déterminé les données erronées  telles que
- Les valeurs vide (NaN)
- Les valeurs incohérentes (valeur hexadécimale comme température)

pour le traitement nous avons  trouvé deux solutions

- oublier les valeurs
- Deviner à partir d'autres variables

Nous avons choisi comme solution de deviner les variables manquantes ou erronées en fessant la moyenne des valeurs existantes pour chaque mois 

* Les	données	corrigées	sont	elles	proches	des	valeurs	sans	erreur	?

Malgré la modification non optimiser, les résultats obtenus sont sensiblement identique. Il y a des écarts (max août à 48° par exemple) mais qui ne viennent pas des erreurs corrigés.

* A	partir	de	données	opendata	du	second	fichier,	retrouver	le	type	de	climat

Ces données proviennent de Finlande, où règne un climat froid, voir tempéré mais avec de grands écarts observable entre les période estivale et hivernale.
  * reprendre	les	données	typiques	de	la	localisaon	proche		fournies	en	complément	,	comparer	les	écarts.

  * Qu'en	concluez	vous	?

  * De	quelle	la	capitale	européenne	avez	vous		eu	les	données.

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
