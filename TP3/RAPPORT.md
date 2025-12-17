# TP3 - Rapport d'Analyse: Complexité Polynomiale

## Informations Générales

- **Sujet**: Produit de deux matrices carrées
- **Date**: 2025-12-17
- **Algorithme**: Multiplication matricielle classique (naïve)

---

## 1. Programme C - Calcul du Produit de Matrices

### Formule Implémentée

Pour calculer `C(n,p) = A(n,m) × B(m,p)` :

```
C(i,j) = Σ(A(i,k) × B(k,j))  pour k = 1...m
```

### Cas des Matrices Carrées (n=m=p)

Le programme se concentre sur les matrices carrées de taille n×n.

---

## 2. Complexité Temporelle Théorique

### Analyse Générale

Pour le produit `C(n,p) = A(n,m) × B(m,p)` :

**Nombre d'opérations** :

- **Multiplications** : n × p × m
- **Additions** : n × p × (m-1)
- **Complexité** : **O(n × m × p)**

### Cas des Matrices Carrées (n=m=p)

**Nouvelle formulation** :

- **Complexité** : **O(n³)**
- **Classe** : Polynomiale cubique
- **Justification** :
  - Boucle externe (i) : n itérations
  - Boucle intermédiaire (j) : n itérations
  - Boucle interne (k) : n itérations
  - **Total** : n × n × n = n³ opérations

---

## 3. Espace Mémoire Nécessaire

### Calcul pour Matrices Carrées n×n

**Mémoire requise** :

- Matrice A : n² × 8 octets (type double)
- Matrice B : n² × 8 octets (type double)
- Matrice C : n² × 8 octets (type double)
- Pointeurs : 3n × 8 octets (système 64 bits)

**Formule totale** :

```
Mémoire = 3n² × 8 + 3n × 8 octets
        = 24n² + 24n octets
```

**Complexité spatiale** : **O(n²)**

### Exemples Concrets

| N   | Mémoire (octets) | Mémoire (MB) |
| --- | ---------------- | ------------ |
| 100 | 242,400          | 0.23 MB      |
| 500 | 6,012,000        | 5.73 MB      |
| 800 | 15,379,200       | 14.67 MB     |

---

## 4. Mesures Expérimentales

### Tableau des Résultats

| N   | Temps (s) | Mémoire (MB) | T(n)/n³   |
| --- | --------- | ------------ | --------- |
| 10  | 0.000006  | 0.00         | 6.00×10⁻⁹ |
| 20  | 0.000023  | 0.01         | 2.88×10⁻⁹ |
| 50  | 0.000417  | 0.06         | 3.34×10⁻⁹ |
| 100 | 0.004717  | 0.23         | 4.72×10⁻⁹ |
| 150 | 0.015225  | 0.52         | 4.51×10⁻⁹ |
| 200 | 0.041219  | 0.92         | 5.15×10⁻⁹ |
| 250 | 0.097641  | 1.44         | 6.25×10⁻⁹ |
| 300 | 0.177160  | 2.07         | 6.56×10⁻⁹ |
| 350 | 0.315660  | 2.81         | 7.36×10⁻⁹ |
| 400 | 0.464023  | 3.67         | 7.25×10⁻⁹ |
| 450 | 0.575164  | 4.65         | 6.31×10⁻⁹ |
| 500 | 0.997565  | 5.73         | 7.98×10⁻⁹ |
| 600 | 1.913890  | 8.25         | 8.86×10⁻⁹ |
| 700 | 2.961285  | 11.23        | 8.63×10⁻⁹ |
| 800 | 4.580811  | 14.67        | 8.95×10⁻⁹ |

---

## 5. Graphiques Générés

### 5.1 Temps d'Exécution en Fonction de N

**Fichier** : `graphiques/temps_execution.png`

**Observations** :

- Croissance cubique claire du temps d'exécution
- La courbe expérimentale suit la tendance O(n³)
- Pour n=800, le temps atteint ~4.58 secondes

### 5.2 Mémoire Utilisée en Fonction de N

**Fichier** : `graphiques/memoire_utilisee.png`

**Observations** :

- Croissance quadratique de la mémoire
- Parfaite concordance avec le modèle O(n²)
- Croissance prévisible et linéaire sur l'échelle

### 5.3 Comparaison Théorique vs Expérimental

**Fichier** : `graphiques/comparaison_theorique_experimental.png`

**Deux vues** :

- **Échelle linéaire** : Montre la croissance cubique
- **Échelle logarithmique** : Vérifie que log(T) ∝ 3×log(n)

---

## 6. Comparaison: Complexité Théorique vs Expérimentale

### Analyse du Rapport T(n)/n³

**Statistiques** :

- **Moyenne** : 6.32×10⁻⁹
- **Écart-type** : 1.85×10⁻⁹
- **Coefficient de variation** : 29.35%

### Interprétation

✅ **CONCLUSION : Bonne concordance avec le modèle O(n³)**

**Justification** :

1. Le rapport T(n)/n³ reste relativement constant
2. Coefficient de variation < 50% indique une bonne cohérence
3. Les variations observées sont dues à :
   - Cache CPU et optimisations matérielles
   - Gestion mémoire du système d'exploitation
   - Autres processus système

**Concordance** : **OUI**

- Le modèle théorique O(n³) est **validé** par les mesures expérimentales
- Les mesures confirment la nature polynomiale cubique de l'algorithme

---

## 7. Observations et Remarques

### Points Clés

1. **Complexité Temporelle** :

   - Confirmée comme O(n³)
   - Croissance très rapide pour grandes matrices
   - Temps double environ quand n augmente de 26%

2. **Complexité Spatiale** :

   - Confirmée comme O(n²)
   - Plus gérable que la complexité temporelle
   - Limitation principale pour très grandes matrices

3. **Limites Pratiques** :
   - Pour n > 1000, le temps devient prohibitif
   - Algorithmes plus efficaces existent (Strassen, Coppersmith-Winograd)

### Algorithmes Alternatifs

| Algorithme           | Complexité | Note                    |
| -------------------- | ---------- | ----------------------- |
| Naïf (implémenté)    | O(n³)      | Simple, pédagogique     |
| Strassen             | O(n^2.807) | Meilleur pour n > 100   |
| Coppersmith-Winograd | O(n^2.376) | Théorique, peu pratique |

---

## 8. Conclusion Générale

### Objectifs Atteints ✅

1. ✅ Programme C fonctionnel pour le produit de matrices
2. ✅ Complexité temporelle théorique : **O(n³)**
3. ✅ Complexité spatiale : **O(n²)**
4. ✅ Mesures expérimentales effectuées (15 points de données)
5. ✅ Graphiques générés et analysés
6. ✅ **Concordance confirmée** entre théorie et pratique

### Apprentissages

- Compréhension approfondie de la complexité polynomiale
- Validation expérimentale des modèles théoriques
- Importance de l'analyse asymptotique pour prédire les performances
- Limites pratiques des algorithmes naïfs

### Perspectives

Pour améliorer les performances :

- Implémenter l'algorithme de Strassen
- Utiliser la parallélisation (OpenMP, CUDA)
- Optimiser l'accès mémoire (cache-friendly)
- Utiliser des bibliothèques optimisées (BLAS, LAPACK)

---

**Fin du Rapport**
