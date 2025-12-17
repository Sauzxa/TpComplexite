/**
 * TP3 - Exercice 2: Recherche d'une sous-matrice
 * 
 * Programme pour rechercher une matrice B dans une matrice A
 * avec deux approches: non triée et triée
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

/**
 * Structure pour représenter une position dans la matrice
 */
typedef struct {
    int row;
    int col;
    bool found;
} Position;

/**
 * Alloue une matrice de taille rows x cols
 */
int** allouer_matrice(int rows, int cols) {
    int** matrice = (int**)malloc(rows * sizeof(int*));
    if (matrice == NULL) {
        fprintf(stderr, "Erreur d'allocation mémoire\n");
        exit(1);
    }
    
    for (int i = 0; i < rows; i++) {
        matrice[i] = (int*)malloc(cols * sizeof(int));
        if (matrice[i] == NULL) {
            fprintf(stderr, "Erreur d'allocation mémoire\n");
            exit(1);
        }
    }
    
    return matrice;
}

/**
 * Libère la mémoire d'une matrice
 */
void liberer_matrice(int** matrice, int rows) {
    for (int i = 0; i < rows; i++) {
        free(matrice[i]);
    }
    free(matrice);
}

/**
 * Initialise une matrice avec des valeurs aléatoires (non triée)
 */
void initialiser_matrice_random(int** matrice, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrice[i][j] = rand() % 100;
        }
    }
}

/**
 * Initialise une matrice avec des lignes triées
 */
void initialiser_matrice_triee(int** matrice, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        int valeur = rand() % 10;
        for (int j = 0; j < cols; j++) {
            matrice[i][j] = valeur;
            valeur += rand() % 5 + 1; // Incrément aléatoire pour garder trié
        }
    }
}

/**
 * Copie une sous-matrice de src vers dest à partir de la position (start_row, start_col)
 */
void copier_sous_matrice(int** src, int** dest, int start_row, int start_col, 
                         int dest_rows, int dest_cols) {
    for (int i = 0; i < dest_rows; i++) {
        for (int j = 0; j < dest_cols; j++) {
            dest[i][j] = src[start_row + i][start_col + j];
        }
    }
}

/**
 * Vérifie si la sous-matrice B correspond à A à la position (row, col)
 */
bool verifier_correspondance(int** A, int** B, int row, int col, int n_prime, int m_prime) {
    for (int i = 0; i < n_prime; i++) {
        for (int j = 0; j < m_prime; j++) {
            if (A[row + i][col + j] != B[i][j]) {
                return false;
            }
        }
    }
    return true;
}

/**
 * ALGORITHME 1: sousMat1 - Recherche naïve (matrices non triées)
 * 
 * Complexité théorique: O((n-n')×(m-m')×n'×m')
 * - Boucle externe i: (n - n' + 1) itérations
 * - Boucle externe j: (m - m' + 1) itérations
 * - Vérification: O(n' × m') pour chaque position
 * 
 * Dans le pire cas: O(n × m × n' × m')
 */
Position sousMat1(int** A, int n, int m, int** B, int n_prime, int m_prime) {
    Position result = {-1, -1, false};
    
    // Parcourir toutes les positions possibles dans A
    for (int i = 0; i <= n - n_prime; i++) {
        for (int j = 0; j <= m - m_prime; j++) {
            // Vérifier si B correspond à cette position
            if (verifier_correspondance(A, B, i, j, n_prime, m_prime)) {
                result.row = i;
                result.col = j;
                result.found = true;
                return result;
            }
        }
    }
    
    return result;
}

/**
 * Recherche binaire dans une ligne triée
 */
int recherche_binaire(int* ligne, int taille, int valeur) {
    int gauche = 0;
    int droite = taille - 1;
    
    while (gauche <= droite) {
        int milieu = gauche + (droite - gauche) / 2;
        
        if (ligne[milieu] == valeur) {
            return milieu;
        } else if (ligne[milieu] < valeur) {
            gauche = milieu + 1;
        } else {
            droite = milieu - 1;
        }
    }
    
    return -1; // Non trouvé
}

/**
 * ALGORITHME 2: sousMat2 - Recherche optimisée (lignes triées)
 * 
 * Complexité théorique: O((n-n')×log(m)×n'×m')
 * - Boucle externe i: (n - n' + 1) itérations
 * - Recherche binaire: O(log(m)) pour trouver la première colonne
 * - Vérification: O(n' × m') pour chaque position candidate
 * 
 * Amélioration: log(m) au lieu de (m - m' + 1) pour la recherche en colonne
 */
Position sousMat2(int** A, int n, int m, int** B, int n_prime, int m_prime) {
    Position result = {-1, -1, false};
    
    // Valeur du premier élément de B (coin supérieur gauche)
    int premier_element = B[0][0];
    
    // Parcourir les lignes de A
    for (int i = 0; i <= n - n_prime; i++) {
        // Utiliser la recherche binaire pour trouver le premier élément
        int col = recherche_binaire(A[i], m, premier_element);
        
        // Si trouvé et qu'il reste assez de colonnes
        while (col != -1 && col <= m - m_prime) {
            // Vérifier si B correspond à cette position
            if (verifier_correspondance(A, B, i, col, n_prime, m_prime)) {
                result.row = i;
                result.col = col;
                result.found = true;
                return result;
            }
            
            // Chercher la prochaine occurrence dans la même ligne
            col = recherche_binaire(A[i] + col + 1, m - col - 1, premier_element);
            if (col != -1) {
                col = col + (m - (m - col - 1)); // Ajuster l'index
            }
        }
    }
    
    return result;
}

/**
 * Affiche une matrice
 */
void afficher_matrice(int** matrice, int rows, int cols, const char* nom) {
    printf("%s (%dx%d):\n", nom, rows, cols);
    for (int i = 0; i < rows; i++) {
        printf("  ");
        for (int j = 0; j < cols; j++) {
            printf("%4d ", matrice[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

/**
 * Mesure le temps d'exécution de sousMat1
 */
double mesurer_sousMat1(int n, int m, int n_prime, int m_prime) {
    // Créer et initialiser les matrices
    int** A = allouer_matrice(n, m);
    int** B = allouer_matrice(n_prime, m_prime);
    
    initialiser_matrice_random(A, n, m);
    
    // Copier une sous-matrice de A vers B pour garantir qu'elle existe
    int pos_i = rand() % (n - n_prime + 1);
    int pos_j = rand() % (m - m_prime + 1);
    copier_sous_matrice(A, B, pos_i, pos_j, n_prime, m_prime);
    
    // Mesurer le temps
    clock_t debut = clock();
    sousMat1(A, n, m, B, n_prime, m_prime);
    clock_t fin = clock();
    
    double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
    
    // Libérer la mémoire
    liberer_matrice(A, n);
    liberer_matrice(B, n_prime);
    
    return temps;
}

/**
 * Mesure le temps d'exécution de sousMat2
 */
double mesurer_sousMat2(int n, int m, int n_prime, int m_prime) {
    // Créer et initialiser les matrices triées
    int** A = allouer_matrice(n, m);
    int** B = allouer_matrice(n_prime, m_prime);
    
    initialiser_matrice_triee(A, n, m);
    
    // Copier une sous-matrice de A vers B
    int pos_i = rand() % (n - n_prime + 1);
    int pos_j = rand() % (m - m_prime + 1);
    copier_sous_matrice(A, B, pos_i, pos_j, n_prime, m_prime);
    
    // Mesurer le temps
    clock_t debut = clock();
    sousMat2(A, n, m, B, n_prime, m_prime);
    clock_t fin = clock();
    
    double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
    
    // Libérer la mémoire
    liberer_matrice(A, n);
    liberer_matrice(B, n_prime);
    
    return temps;
}

/**
 * Affiche l'analyse théorique
 */
void afficher_analyse_theorique() {
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║        ANALYSE DE COMPLEXITÉ THÉORIQUE                        ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    
    printf("1. ALGORITHME sousMat1 (Matrices non triées):\n");
    printf("   Approche: Recherche naïve exhaustive\n");
    printf("   \n");
    printf("   Pour chaque position (i,j) dans A:\n");
    printf("   - Positions possibles: (n-n'+1) × (m-m'+1)\n");
    printf("   - Vérification: O(n' × m') comparaisons\n");
    printf("   \n");
    printf("   Complexité: O((n-n')×(m-m')×n'×m')\n");
    printf("   Pire cas: O(n × m × n' × m')\n");
    printf("   Classe: Polynomiale de degré 4\n\n");
    
    printf("2. ALGORITHME sousMat2 (Lignes triées):\n");
    printf("   Approche: Recherche binaire + vérification\n");
    printf("   \n");
    printf("   Pour chaque ligne i dans A:\n");
    printf("   - Lignes à parcourir: (n-n'+1)\n");
    printf("   - Recherche binaire: O(log(m))\n");
    printf("   - Vérification: O(n' × m')\n");
    printf("   \n");
    printf("   Complexité: O((n-n')×log(m)×n'×m')\n");
    printf("   Amélioration: log(m) au lieu de (m-m')\n");
    printf("   Classe: Polynomiale avec facteur logarithmique\n\n");
    
    printf("3. COMPARAISON:\n");
    printf("   Gain de sousMat2 vs sousMat1: O((m-m')/log(m))\n");
    printf("   Pour m=1000, m'=10: ~990/10 ≈ 99x plus rapide\n\n");
}

/**
 * Effectue les mesures et sauvegarde dans un CSV
 */
void effectuer_mesures(const char* nom_fichier) {
    // Configurations de test
    typedef struct {
        int n, m, n_prime, m_prime;
    } Config;
    
    Config configs[] = {
        {50, 50, 5, 5},
        {100, 100, 5, 5},
        {150, 150, 5, 5},
        {200, 200, 5, 5},
        {250, 250, 5, 5},
        {300, 300, 5, 5},
        {100, 100, 10, 10},
        {200, 200, 10, 10},
        {300, 300, 10, 10},
        {400, 400, 10, 10},
        {500, 500, 10, 10},
        {200, 200, 20, 20},
        {300, 300, 20, 20},
        {400, 400, 20, 20},
        {500, 500, 20, 20}
    };
    
    int nb_configs = sizeof(configs) / sizeof(configs[0]);
    
    FILE* fichier = fopen(nom_fichier, "w");
    if (fichier == NULL) {
        fprintf(stderr, "Erreur: impossible de créer le fichier %s\n", nom_fichier);
        return;
    }
    
    // En-tête CSV
    fprintf(fichier, "N,M,N_prime,M_prime,Temps_sousMat1(s),Temps_sousMat2(s),Ratio\n");
    
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║           MESURES EXPÉRIMENTALES                              ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    printf("%-6s %-6s %-6s %-6s %-15s %-15s %-10s\n", 
           "N", "M", "N'", "M'", "sousMat1(s)", "sousMat2(s)", "Ratio");
    printf("───────────────────────────────────────────────────────────────────────────\n");
    
    for (int i = 0; i < nb_configs; i++) {
        Config cfg = configs[i];
        
        // Mesurer les deux algorithmes
        double temps1 = mesurer_sousMat1(cfg.n, cfg.m, cfg.n_prime, cfg.m_prime);
        double temps2 = mesurer_sousMat2(cfg.n, cfg.m, cfg.n_prime, cfg.m_prime);
        
        double ratio = (temps2 > 0) ? temps1 / temps2 : 0;
        
        // Afficher
        printf("%-6d %-6d %-6d %-6d %-15.6f %-15.6f %-10.2f\n",
               cfg.n, cfg.m, cfg.n_prime, cfg.m_prime, temps1, temps2, ratio);
        
        // Sauvegarder
        fprintf(fichier, "%d,%d,%d,%d,%.6f,%.6f,%.2f\n",
                cfg.n, cfg.m, cfg.n_prime, cfg.m_prime, temps1, temps2, ratio);
        
        fflush(stdout);
    }
    
    fclose(fichier);
    printf("\n✓ Résultats sauvegardés dans: %s\n\n", nom_fichier);
}

/**
 * Démonstration avec exemple
 */
void demonstration_exemple() {
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║           DÉMONSTRATION: Recherche de sous-matrice            ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    
    // Créer une petite matrice A
    int n = 6, m = 6;
    int** A = allouer_matrice(n, m);
    initialiser_matrice_random(A, n, m);
    
    // Créer B comme sous-matrice de A
    int n_prime = 3, m_prime = 3;
    int** B = allouer_matrice(n_prime, m_prime);
    copier_sous_matrice(A, B, 2, 2, n_prime, m_prime);
    
    afficher_matrice(A, n, m, "Matrice A");
    afficher_matrice(B, n_prime, m_prime, "Matrice B (à rechercher)");
    
    // Rechercher avec sousMat1
    Position result1 = sousMat1(A, n, m, B, n_prime, m_prime);
    if (result1.found) {
        printf("✓ sousMat1: Trouvé à la position (%d, %d)\n", result1.row, result1.col);
    } else {
        printf("✗ sousMat1: Non trouvé\n");
    }
    
    // Libérer
    liberer_matrice(A, n);
    liberer_matrice(B, n_prime);
    
    printf("\n");
}

int main() {
    printf("\n");
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║                                                                ║\n");
    printf("║         TP3 - EXERCICE 2                                      ║\n");
    printf("║         Recherche d'une sous-matrice                          ║\n");
    printf("║                                                                ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    
    srand(time(NULL));
    
    // 1. Analyse théorique
    afficher_analyse_theorique();
    
    // 2. Démonstration
    demonstration_exemple();
    
    // 3. Mesures expérimentales
    effectuer_mesures("dist/ex2_resultats.csv");
    
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║  Programme terminé avec succès!                               ║\n");
    printf("║  Utilisez le script Python pour générer les graphiques        ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    
    return 0;
}
