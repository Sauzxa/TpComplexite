# TP3 - Exercice 2: Recherche de sous-matrice

## Description

Cet exercice implémente deux algorithmes pour rechercher une matrice B dans une matrice A plus grande:

- **sousMat1**: Recherche naïve (matrices non triées)
- **sousMat2**: Recherche optimisée avec recherche binaire (lignes triées)

## Problème

Soit `A(n,m)` et `B(n',m')` deux tableaux 2D avec `n' < n` et `m' < m`.  
Rechercher la matrice B dans la matrice A.

## Algorithmes Implémentés

### 1. sousMat1 - Recherche Naïve

**Hypothèse**: Les éléments de A et B ne sont pas triés.

**Approche**:

- Parcourir toutes les positions possibles (i,j) dans A
- Pour chaque position, vérifier si B correspond

**Complexité Théorique**:

- **Temps**: O((n-n')×(m-m')×n'×m')
- **Pire cas**: O(n × m × n' × m')
- **Classe**: Polynomiale de degré 4

### 2. sousMat2 - Recherche Optimisée

**Hypothèse**: Chaque ligne de A et B est triée par ordre croissant.

**Approche**:

- Pour chaque ligne i de A
- Utiliser la recherche binaire pour trouver le premier élément de B
- Vérifier si B correspond à cette position

**Complexité Théorique**:

- **Temps**: O((n-n')×log(m)×n'×m')
- **Amélioration**: log(m) au lieu de (m-m')
- **Classe**: Polynomiale avec facteur logarithmique

**Gain théorique**: O((m-m')/log(m))

## Structure du Projet

```
ex2/
├── src/
│   └── submatrix_search.c    # Programme C
├── scripts/
│   └── generate_graphs.py    # Génération des graphiques
├── dist/
│   ├── submatrix_search      # Exécutable
│   └── ex2_resultats.csv     # Résultats
└── graphiques/
    ├── ex2_comparaison.png   # Comparaison des deux algorithmes
    ├── ex2_ratio.png         # Ratios de performance
    └── ex2_evolution.png     # Évolution des temps
```

## Utilisation

### Compilation et Exécution

```bash
# Compiler
gcc -Wall -O2 src/submatrix_search.c -o dist/submatrix_search -lm

# Exécuter
./dist/submatrix_search

# Générer les graphiques
cd scripts
python3 generate_graphs.py
```

## Résultats

### Configurations Testées

| N   | M   | N'  | M'  | Description                           |
| --- | --- | --- | --- | ------------------------------------- |
| 50  | 50  | 5   | 5   | Petite matrice, petite recherche      |
| 100 | 100 | 5   | 5   | Moyenne matrice, petite recherche     |
| 200 | 200 | 10  | 10  | Grande matrice, moyenne recherche     |
| 500 | 500 | 20  | 20  | Très grande matrice, grande recherche |

### Observations

**Résultats Expérimentaux**:

- Pour les petites matrices, sousMat1 et sousMat2 ont des performances similaires
- L'overhead de la recherche binaire peut rendre sousMat2 plus lent pour petites tailles
- Le gain théorique de sousMat2 se manifeste pour de très grandes matrices

**Facteurs Influençant les Performances**:

1. **Taille de la matrice**: Plus grande → plus de bénéfice pour sousMat2
2. **Taille de la sous-matrice**: Plus petite → moins d'impact de la vérification
3. **Cache CPU**: Les petites matrices tiennent en cache
4. **Position de B dans A**: Impact sur le nombre d'itérations

## Analyse Théorique vs Expérimentale

### Complexité Temporelle

**sousMat1**:

```
T1(n,m,n',m') = O(n × m × n' × m')
```

**sousMat2**:

```
T2(n,m,n',m') = O(n × log(m) × n' × m')
```

**Ratio Théorique**:

```
T1/T2 = m / log(m)
```

Pour m = 500: 500 / log₂(500) ≈ 500 / 9 ≈ 55x plus rapide (théoriquement)

### Observations Pratiques

Les mesures expérimentales montrent que:

- Les constantes cachées dans la notation O() sont importantes
- L'overhead de la recherche binaire peut dominer pour petites tailles
- Les optimisations du compilateur et le cache CPU influencent les résultats

## Graphiques Générés

1. **ex2_comparaison.png**: Barres comparant sousMat1 vs sousMat2
2. **ex2_ratio.png**: Ratios de performance (T1/T2)
3. **ex2_evolution.png**: Courbes d'évolution des temps

## Conclusion

### Quand Utiliser sousMat1?

- Matrices non triées
- Petites tailles (n, m < 100)
- Simplicité du code prioritaire

### Quand Utiliser sousMat2?

- Lignes triées disponibles
- Grandes matrices (m > 1000)
- Performance critique

### Amélioration Possible

Pour de meilleures performances, on pourrait:

- Utiliser des algorithmes de recherche de motifs 2D (KMP 2D)
- Paralléliser la recherche
- Utiliser des heuristiques pour sauter des positions

## Bibliothèques

- **C**: stdlib.h, stdio.h, time.h, stdbool.h
- **Python**: matplotlib, numpy, csv
