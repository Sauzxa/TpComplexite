# Guide d’exécution du TP0

## Compiler

Depuis le dossier `Tp0/` :

```bash
bash compile.sh
```

Le script compile les sources de `src/` et place les exécutables dans `dist/`.

## Générer les jeux de données

Chaque commande reçoit le fichier d’entrée puis le fichier de sortie. Les fichiers d’entrée doivent contenir des nombres entiers séparés par des espaces ou des retours à la ligne. Ils seront ajoutés ultérieurement. Les sorties sont écrites une valeur par ligne dans `data/`.

```bash
./dist/Random100 input.txt data/Random100.txt
./dist/Random1000 input.txt data/Random1000.txt
./dist/Test-1 input.txt data/Test-1.txt
./dist/Test-2 input.txt data/Test-2.txt
./dist/Test-3 input.txt data/Test-3.txt
```

Les programmes choisissent aléatoirement les valeurs admissibles. Ils échouent avec un message explicite si l’entrée est invalide ou ne contient pas assez de valeurs admissibles. Test-1 demande 100 nombres premiers de l’intervalle `[1000, 1000000]`. Test-2 demande 10 nombres de chacune des longueurs 3 à 9 chiffres. Test-3 demande 25 nombres de chacune des longueurs 3, 6, 9 et 12 chiffres.

## Préparer le rendu

L’archive collective doit contenir un dossier par jeu de données, réunissant son fichier source et le fichier de données généré :

```text
NomDuGroupe_TP0.zip
├── Random100/  (source + Random100.txt)
├── Random1000/ (source + Random1000.txt)
├── Test-1/     (source + Test-1.txt)
├── Test-2/     (source + Test-2.txt)
└── Test-3/     (source + Test-3.txt)
```
