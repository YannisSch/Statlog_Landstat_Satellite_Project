# Statlog_Landstat_Satellite_Project

GIT of our Python for Data Analysis final project

- INFORMATION SUR LE DATASET : 

Ces données correspondent au "Statlog (Landsat Satellite) Data Set". Les données Landsat originales pour cette base de données ont été générées à partir de données achetées à la NASA par le Centre australien pour la télédétection, et utilisé pour la recherche par le Centre de télédétection Université de Nouvelle-Galles du Sud Kensington, boîte postale 1 NSW 2033 L'Australie.

La base de données comprend les valeurs multispectrales des pixels des quartiers 3x3 d'une image satellite, et la classification associée au pixel central dans chaque quartier. La résolution spatiale d'un pixel est d'environ 80m x 80m. Chaque image contient 2340 x 3380 de ces pixels.

La base de données est une (minuscule) sous-zone d'une scène, composée de 82 x 100 pixels. Chaque ligne de données correspond à un quartier de 3x3 carrés de pixels entièrement contenus dans la sous-zone de 82x10. Chaque pixel est constitué de 4 valeurs numériques comprisent entre 0 et 255 correspondant à la couleur du pixel dans 4 grandes bandes spectrales :

Bande Verte

Bande Rouge

Bande Near Infrarouge 1

Bande Near Infrarouge 2

Ce qui nous donnent 4 X 9 (3X3) = 36 colonnes + 1 colonne de classification = 37 colonnes.

Le but de cette analyse est de prédire cette classification, en utilisant des valeurs multispectrales. Dans la base de données échantillon, la classe d'un pixel est codée sous forme de nombre. La classe à prédire correspond à des valeurs entre 1 et 7. Nous avons 4435 valeurs dans le training set et 2000 dans le testing set. C'est un dataset associée à une multi classififcation, le but étant de connaitre quel est la classe associé au pixel.

Numéro de la classe :

1 : terre rouge
2 : la culture du coton
3 : terre grise
4 : sol gris humide
5 : sol avec chaumes de végétation
6 : classe de mélange (tous les types présents)
7 : sol gris très humide
NB. Il n'y a pas d'exemples avec la classe 6 dans cet ensemble de données.
Les données sont données dans un ordre aléatoire et certaines lignes de données ont été supprimées pour ne pas reconstruire l'image originale à partir de cet ensemble de données. Dans chaque ligne de données, les quatre valeurs spectrales pour le pixel supérieur gauche sont données en premier, suivies des quatre valeurs spectrales pour le pixel moyen supérieur, puis de celles pour le pixel supérieur droit, et ainsi de suite avec les pixels lus en séquence de gauche à droite et de haut en bas.

Ainsi, les quatre valeurs spectrales pour le pixel central sont données par les attributs 17, 18, 19 et 20. La classification est assocé uniquement au pixel central
(Schéma explicatif dans notre PDF et dans notre fichier .ipynb) 

- Modèle choisi : 

Après comparaison avec plusieurs modèles, nous avons choisi de prendre le Random Forest Classifier.

- API Flask :

Nous avons choisi de créer une API avec Flask pour ensuite l’appelé dans une simple appli web afin de permettre à l’utilisateur de rentrer les 4 valeurs du pixel sur les 4 bandes spectrales et ainsi à partir du modèle que nous avons créé pouvoir prédire la classe du pixel ainsi que la probabilité grâce au module numpy.

  Pour l'exécuter : 

    Lancer le fichier python "app.py" (présent dans le dosssier ApiFlask/ ) sur Anaconda ou autre puis se rendre à l'URL indiqué par l'invité de commande (localhost normalement)

Merci pour votre attention
