# Guide d’exécution du TP0

Ce guide décrit la préparation des entrées, la compilation, la génération des données et la structure du rendu demandé.

## 1. Préparer les fichiers d’entrée

Dans `Tp0/data/`, créez un fichier d’entrée distinct pour chaque programme :

```text
Random100_input.txt
Random1000_input.txt
Test-1_input.txt
Test-2_input.txt
Test-3_input.txt
```

Chaque fichier doit contenir des nombres entiers séparés par des espaces ou des retours à la ligne. Prévoyez suffisamment de valeurs :

- `Random100_input.txt` : au moins 100 nombres.
- `Random1000_input.txt` : au moins 1 000 nombres.
- `Test-1_input.txt` : au moins 100 nombres premiers entre 1 000 et 1 000 000.
- `Test-2_input.txt` : au moins 10 nombres de chacune des longueurs 3 à 9 chiffres.
- `Test-3_input.txt` : au moins 25 nombres de chacune des longueurs 3, 6, 9 et 12 chiffres.

Les programmes choisissent aléatoirement les valeurs demandées et écrivent une valeur par ligne dans le fichier de sortie.

## 2. Linux

Depuis la racine du dépôt, compilez les programmes :

```bash
cd Tp0
bash compile.sh
```

Placez les fichiers d’entrée dans `data/`, puis lancez les commandes suivantes depuis `Tp0/` :

```bash
./dist/Random100 data/Random100_input.txt data/Random100.txt
./dist/Random1000 data/Random1000_input.txt data/Random1000.txt
./dist/Test-1 data/Test-1_input.txt data/Test-1.txt
./dist/Test-2 data/Test-2_input.txt data/Test-2.txt
./dist/Test-3 data/Test-3_input.txt data/Test-3.txt
```

## 3. Windows avec PowerShell et MinGW-w64

Installez MinGW-w64 et vérifiez que `gcc` est accessible depuis PowerShell. Depuis la racine du dépôt, entrez dans `Tp0/` et créez les dossiers nécessaires :

```powershell
Set-Location .\Tp0
New-Item -ItemType Directory -Force dist, data
```

Compilez les cinq programmes :

```powershell
gcc -std=c11 -O2 .\src\Random100.c -o .\dist\Random100.exe
gcc -std=c11 -O2 .\src\Random1000.c -o .\dist\Random1000.exe
gcc -std=c11 -O2 .\src\Test-1.c -o .\dist\Test-1.exe
gcc -std=c11 -O2 .\src\Test-2.c -o .\dist\Test-2.exe
gcc -std=c11 -O2 .\src\Test-3.c -o .\dist\Test-3.exe
```

Placez les fichiers d’entrée dans `data/`, puis exécutez :

```powershell
.\dist\Random100.exe .\data\Random100_input.txt .\data\Random100.txt
.\dist\Random1000.exe .\data\Random1000_input.txt .\data\Random1000.txt
.\dist\Test-1.exe .\data\Test-1_input.txt .\data\Test-1.txt
.\dist\Test-2.exe .\data\Test-2_input.txt .\data\Test-2.txt
.\dist\Test-3.exe .\data\Test-3_input.txt .\data\Test-3.txt
```

## 4. Préparer le rendu collectif

Chaque sous-groupe de quatre étudiants remet une seule archive `NomDuGroupe_TP0.zip`. Conformément aux consignes, l’archive contient un dossier par jeu de données avec son code source et son fichier de données généré :

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

Les sources à copier dans ces dossiers se trouvent dans `src/`; les données générées se trouvent dans `data/`. Les fichiers d’entrée et les exécutables de `dist/` ne remplacent pas les scripts et jeux de données exigés pour le rendu.
