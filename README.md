# TP0 — Création de données de test

Ce guide explique comment préparer les fichiers d’entrée, compiler les programmes et générer les cinq jeux de données du TP0.

## 1. Préparer les fichiers d’entrée

Depuis le dossier `Tp0/`, créez le dossier `data/` s’il n’existe pas, puis ajoutez-y un fichier d’entrée pour chaque programme :

```text
Tp0/data/Random100_input.txt
Tp0/data/Random1000_input.txt
Tp0/data/Test-1_input.txt
Tp0/data/Test-2_input.txt
Tp0/data/Test-3_input.txt
```

Chaque fichier doit contenir des nombres entiers, séparés par des espaces ou placés un par ligne. Assurez-vous qu’il contient assez de valeurs pour la tâche correspondante :

- `Random100_input.txt` : au moins 100 valeurs.
- `Random1000_input.txt` : au moins 1 000 valeurs.
- `Test-1_input.txt` : au moins 100 nombres premiers entre 1 000 et 1 000 000.
- `Test-2_input.txt` : au moins 10 nombres de chaque longueur, de 3 à 9 chiffres.
- `Test-3_input.txt` : au moins 25 nombres de chacune des longueurs 3, 6, 9 et 12 chiffres.

Vous pouvez créer ces fichiers avec un éditeur de texte et y coller les nombres collectés. Les programmes sélectionnent aléatoirement les valeurs admissibles et enregistrent les résultats dans `data/`.

## 2. Linux

Ouvrez un terminal à la racine du dépôt, puis entrez dans `Tp0/` et compilez les programmes :

```bash
cd Tp0
bash compile.sh
```

Après avoir placé les fichiers d’entrée dans `data/`, générez les jeux de données :

```bash
./dist/Random100 data/Random100_input.txt data/Random100.txt
./dist/Random1000 data/Random1000_input.txt data/Random1000.txt
./dist/Test-1 data/Test-1_input.txt data/Test-1.txt
./dist/Test-2 data/Test-2_input.txt data/Test-2.txt
./dist/Test-3 data/Test-3_input.txt data/Test-3.txt
```

## 3. Windows avec PowerShell et MinGW-w64

Installez MinGW-w64 et vérifiez que `gcc` est accessible depuis PowerShell. Depuis la racine du dépôt, entrez dans `Tp0/`, puis créez les dossiers nécessaires :

```powershell
Set-Location .\Tp0
New-Item -ItemType Directory -Force dist, data
```

Compilez chaque fichier source en exécutable Windows :

```powershell
gcc -std=c11 -O2 .\src\Random100.c -o .\dist\Random100.exe
gcc -std=c11 -O2 .\src\Random1000.c -o .\dist\Random1000.exe
gcc -std=c11 -O2 .\src\Test-1.c -o .\dist\Test-1.exe
gcc -std=c11 -O2 .\src\Test-2.c -o .\dist\Test-2.exe
gcc -std=c11 -O2 .\src\Test-3.c -o .\dist\Test-3.exe
```

Après avoir placé les fichiers d’entrée dans `data/`, lancez les programmes :

```powershell
.\dist\Random100.exe .\data\Random100_input.txt .\data\Random100.txt
.\dist\Random1000.exe .\data\Random1000_input.txt .\data\Random1000.txt
.\dist\Test-1.exe .\data\Test-1_input.txt .\data\Test-1.txt
.\dist\Test-2.exe .\data\Test-2_input.txt .\data\Test-2.txt
.\dist\Test-3.exe .\data\Test-3_input.txt .\data\Test-3.txt
```

## Résultats

Chaque fichier de sortie contient une valeur par ligne : `Random100.txt`, `Random1000.txt`, `Test-1.txt`, `Test-2.txt` et `Test-3.txt`. Si un programme signale qu’il manque des valeurs, complétez le fichier d’entrée concerné puis relancez la commande.

## 4. Préparer l’archive de remise

Chaque groupe de quatre étudiants remet une seule archive nommée `NomDuGroupe_TP0.zip`. Elle doit contenir les cinq dossiers suivants; chaque dossier comprend le code source et le fichier de données généré correspondant :

```text
NomDuGroupe_TP0.zip
├── Random100/
│   ├── Random100.c
│   └── Random100.txt
├── Random1000/
│   ├── Random1000.c
│   └── Random1000.txt
├── Test-1/
│   ├── Test-1.c
│   └── Test-1.txt
├── Test-2/
│   ├── Test-2.c
│   └── Test-2.txt
└── Test-3/
    ├── Test-3.c
    └── Test-3.txt
```

Les fichiers sources se trouvent dans `Tp0/src/` et les fichiers de données générés dans `Tp0/data/`. Copiez chaque paire correspondante dans son dossier avant de créer l’archive ZIP. N’incluez pas les exécutables de `dist/` à la place des sources.
