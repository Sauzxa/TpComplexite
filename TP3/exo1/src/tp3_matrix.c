/**
 * TP3 - Complexité polynomiale: Produit de deux matrices
 * 
 * Programme pour calculer le produit de deux matrices carrées
 * et mesurer le temps d'exécution en fonction de la taille n
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

/**
 * Alloue une matrice carrée de taille n x n
 */
double** allouer_matrice(int n) {
    double** matrice = (double**)malloc(n * sizeof(double*));
    if (matrice == NULL) {
        fprintf(stderr, "Erreur d'allocation mémoire\n");
        exit(1);
    }
    
    for (int i = 0; i < n; i++) {
        matrice[i] = (double*)malloc(n * sizeof(double));
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
void liberer_matrice(double** matrice, int n) {
    for (int i = 0; i < n; i++) {
        free(matrice[i]);
    }
    free(matrice);
}

/**
 * Initialise une matrice avec des valeurs aléatoires entre 0 et 1
 */
void initialiser_matrice(double** matrice, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matrice[i][j] = (double)rand() / RAND_MAX;
        }
    }
}

/**
 * Calcule le produit de deux matrices carrées: C = A × B
 * 
 * Formule: C(i,j) = Σ(A(i,k) × B(k,j)) pour k=0...n-1
 * 
 * Complexité théorique: O(n³)
 * - Boucle i: n itérations
 * - Boucle j: n itérations
 * - Boucle k: n itérations
 * Total: n × n × n = n³ opérations
 */
void produit_matrices(double** A, double** B, double** C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = 0.0;
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

/**
 * Mesure le temps d'exécution du produit de matrices
 * Retourne le temps en secondes
 */
double mesurer_temps_execution(int n) {
    // Allouer les matrices
    double** A = allouer_matrice(n);
    double** B = allouer_matrice(n);
    double** C = allouer_matrice(n);
    
    // Initialiser les matrices A et B
    initialiser_matrice(A, n);
    initialiser_matrice(B, n);
    
    // Mesurer le temps d'exécution
    clock_t debut = clock();
    produit_matrices(A, B, C, n);
    clock_t fin = clock();
    
    double temps = (double)(fin - debut) / CLOCKS_PER_SEC;
    
    // Libérer la mémoire
    liberer_matrice(A, n);
    liberer_matrice(B, n);
    liberer_matrice(C, n);
    
    return temps;
}

/**
 * Calcule l'espace mémoire nécessaire pour trois matrices n×n
 * Retourne la taille en octets
 */
long calculer_memoire(int n) {
    // 3 matrices de n×n éléments de type double (8 octets)
    // + 3×n pointeurs (8 octets chacun sur système 64 bits)
    long taille_elements = 3L * n * n * sizeof(double);
    long taille_pointeurs = 3L * n * sizeof(double*);
    return taille_elements + taille_pointeurs;
}

/**
 * Affiche l'analyse de complexité théorique
 */
void afficher_analyse_theorique() {
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║        ANALYSE DE COMPLEXITÉ THÉORIQUE                        ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    
    printf("1. COMPLEXITÉ TEMPORELLE:\n");
    printf("   Formule générale: C(n,p) = A(n,m) × B(m,p)\n");
    printf("   Pour chaque élément C(i,j): Σ(A(i,k) × B(k,j)) avec k=1...m\n");
    printf("   \n");
    printf("   Nombre d'opérations:\n");
    printf("   - Multiplications: n × p × m\n");
    printf("   - Additions: n × p × (m-1)\n");
    printf("   - Complexité: O(n × m × p)\n");
    printf("   \n");
    printf("   Pour matrices carrées (n=m=p):\n");
    printf("   - Complexité: O(n³)\n");
    printf("   - Classe: Polynomiale cubique\n\n");
    
    printf("2. COMPLEXITÉ SPATIALE:\n");
    printf("   Mémoire requise pour matrices carrées n×n:\n");
    printf("   - Matrice A: n² × 8 octets (double)\n");
    printf("   - Matrice B: n² × 8 octets (double)\n");
    printf("   - Matrice C: n² × 8 octets (double)\n");
    printf("   - Pointeurs: 3n × 8 octets\n");
    printf("   - Total: 3n² × 8 + 3n × 8 octets\n");
    printf("   - Complexité: O(n²)\n\n");
}

/**
 * Effectue les mesures expérimentales et sauvegarde dans un fichier CSV
 */
void effectuer_mesures(const char* nom_fichier) {
    // Tailles à tester (progression géométrique)
    int tailles[] = {10, 20, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800};
    int nb_tailles = sizeof(tailles) / sizeof(tailles[0]);
    
    FILE* fichier = fopen(nom_fichier, "w");
    if (fichier == NULL) {
        fprintf(stderr, "Erreur: impossible de créer le fichier %s\n", nom_fichier);
        return;
    }
    
    // En-tête CSV
    fprintf(fichier, "N,Temps(s),Memoire(octets),Memoire(KB),Memoire(MB)\n");
    
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║           MESURES EXPÉRIMENTALES                              ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    printf("%-10s %-15s %-20s %-15s\n", "N", "Temps (s)", "Mémoire (octets)", "Mémoire (MB)");
    printf("─────────────────────────────────────────────────────────────────\n");
    
    for (int i = 0; i < nb_tailles; i++) {
        int n = tailles[i];
        
        // Mesurer le temps d'exécution
        double temps = mesurer_temps_execution(n);
        
        // Calculer la mémoire utilisée
        long memoire = calculer_memoire(n);
        double memoire_kb = memoire / 1024.0;
        double memoire_mb = memoire / (1024.0 * 1024.0);
        
        // Afficher les résultats
        printf("%-10d %-15.6f %-20ld %-15.2f\n", n, temps, memoire, memoire_mb);
        
        // Sauvegarder dans le CSV
        fprintf(fichier, "%d,%.6f,%ld,%.2f,%.2f\n", n, temps, memoire, memoire_kb, memoire_mb);
        
        fflush(stdout);
    }
    
    fclose(fichier);
    printf("\n✓ Résultats sauvegardés dans: %s\n\n", nom_fichier);
}

/**
 * Affiche un exemple de calcul de produit matriciel
 */
void afficher_exemple() {
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║           EXEMPLE: PRODUIT DE MATRICES 3×3                    ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    
    int n = 3;
    double** A = allouer_matrice(n);
    double** B = allouer_matrice(n);
    double** C = allouer_matrice(n);
    
    // Initialiser avec des valeurs simples
    srand(42); // Seed fixe pour reproductibilité
    initialiser_matrice(A, n);
    initialiser_matrice(B, n);
    
    printf("Matrice A:\n");
    for (int i = 0; i < n; i++) {
        printf("  ");
        for (int j = 0; j < n; j++) {
            printf("%6.2f ", A[i][j]);
        }
        printf("\n");
    }
    
    printf("\nMatrice B:\n");
    for (int i = 0; i < n; i++) {
        printf("  ");
        for (int j = 0; j < n; j++) {
            printf("%6.2f ", B[i][j]);
        }
        printf("\n");
    }
    
    // Calculer le produit
    produit_matrices(A, B, C, n);
    
    printf("\nMatrice C = A × B:\n");
    for (int i = 0; i < n; i++) {
        printf("  ");
        for (int j = 0; j < n; j++) {
            printf("%6.2f ", C[i][j]);
        }
        printf("\n");
    }
    
    liberer_matrice(A, n);
    liberer_matrice(B, n);
    liberer_matrice(C, n);
    
    printf("\n");
}

int main() {
    printf("\n");
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║                                                                ║\n");
    printf("║         TP3 - COMPLEXITÉ POLYNOMIALE                          ║\n");
    printf("║         Produit de deux matrices carrées                      ║\n");
    printf("║                                                                ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    
    // Initialiser le générateur aléatoire
    srand(time(NULL));
    
    // 1. Afficher l'analyse théorique
    afficher_analyse_theorique();
    
    // 2. Afficher un exemple
    afficher_exemple();
    
    // 3. Effectuer les mesures expérimentales
    effectuer_mesures("dist/tp3_resultats.csv");
    
    printf("╔════════════════════════════════════════════════════════════════╗\n");
    printf("║  Programme terminé avec succès!                               ║\n");
    printf("║  Utilisez le script Python pour générer les graphiques        ║\n");
    printf("╚════════════════════════════════════════════════════════════════╝\n\n");
    
    return 0;
}
