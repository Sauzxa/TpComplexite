#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP3 - Complexité polynomiale: Génération des graphiques
Programme pour générer les graphiques d'analyse de complexité
du produit de matrices carrées
"""

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# Configuration
CSV_FILE = "../dist/tp3_resultats.csv"
OUTPUT_DIR = "../graphiques"

def lire_donnees_csv(nom_fichier):
    """
    Lit le fichier CSV et retourne les données
    """
    n_values = []
    temps_values = []
    memoire_values = []
    
    if not os.path.exists(nom_fichier):
        print(f"Erreur: Fichier {nom_fichier} non trouvé")
        return n_values, temps_values, memoire_values
    
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    n = int(row['N'])
                    temps = float(row['Temps(s)'])
                    memoire = float(row['Memoire(MB)'])
                    
                    n_values.append(n)
                    temps_values.append(temps)
                    memoire_values.append(memoire)
                except (ValueError, KeyError) as e:
                    print(f"Erreur lors de la lecture d'une ligne: {e}")
                    continue
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
    
    return n_values, temps_values, memoire_values

def generer_graphique_temps(n_values, temps_values):
    """
    Génère le graphique du temps d'exécution en fonction de N
    """
    if not n_values or not temps_values:
        print("Aucune donnée disponible pour le graphique du temps")
        return
    
    plt.figure(figsize=(12, 8))
    
    # Tracer les points et la courbe
    plt.plot(n_values, temps_values, 'o-', color='#FF6B6B', 
             linewidth=2, markersize=8, label='Temps mesuré',
             markerfacecolor='white', markeredgewidth=2, markeredgecolor='#FF6B6B')
    
    # Ajouter une courbe de tendance O(n³)
    n_array = np.array(n_values)
    temps_array = np.array(temps_values)
    
    # Calculer le coefficient pour la courbe théorique O(n³)
    # On utilise le dernier point pour calibrer
    if len(n_values) > 0 and temps_values[-1] > 0:
        coef = temps_values[-1] / (n_values[-1] ** 3)
        temps_theorique = coef * (n_array ** 3)
        
        plt.plot(n_values, temps_theorique, '--', color='#4ECDC4', 
                linewidth=2, label='Tendance O(n³)', alpha=0.7)
    
    plt.xlabel('Taille de la matrice (N)', fontsize=12, fontweight='bold')
    plt.ylabel('Temps d\'exécution (secondes)', fontsize=12, fontweight='bold')
    plt.title('Complexité temporelle du produit de matrices carrées', 
              fontsize=14, fontweight='bold', pad=20)
    
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(fontsize=11, loc='upper left')
    
    # Ajouter les valeurs sur les points
    for i, (n, t) in enumerate(zip(n_values, temps_values)):
        if i % 2 == 0:  # Afficher un point sur deux pour éviter le chevauchement
            if t >= 1:
                label = f'{t:.2f}s'
            elif t >= 0.001:
                label = f'{t*1000:.1f}ms'
            else:
                label = f'{t*1000000:.0f}μs'
            
            plt.annotate(label, (n, t), 
                        textcoords="offset points", 
                        xytext=(0, 10), 
                        ha='center',
                        fontsize=9,
                        bbox=dict(boxstyle='round,pad=0.3', 
                                facecolor='white', 
                                alpha=0.8,
                                edgecolor='#FF6B6B'))
    
    plt.tight_layout()
    
    # Sauvegarder
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    nom_sortie = os.path.join(OUTPUT_DIR, "temps_execution.png")
    plt.savefig(nom_sortie, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique du temps généré: {nom_sortie}")

def generer_graphique_memoire(n_values, memoire_values):
    """
    Génère le graphique de la mémoire utilisée en fonction de N
    """
    if not n_values or not memoire_values:
        print("Aucune donnée disponible pour le graphique de la mémoire")
        return
    
    plt.figure(figsize=(12, 8))
    
    # Tracer les points et la courbe
    plt.plot(n_values, memoire_values, 'o-', color='#45B7D1', 
             linewidth=2, markersize=8, label='Mémoire utilisée',
             markerfacecolor='white', markeredgewidth=2, markeredgecolor='#45B7D1')
    
    # Ajouter une courbe de tendance O(n²)
    n_array = np.array(n_values)
    memoire_array = np.array(memoire_values)
    
    # Calculer le coefficient pour la courbe théorique O(n²)
    if len(n_values) > 0 and memoire_values[-1] > 0:
        coef = memoire_values[-1] / (n_values[-1] ** 2)
        memoire_theorique = coef * (n_array ** 2)
        
        plt.plot(n_values, memoire_theorique, '--', color='#96CEB4', 
                linewidth=2, label='Tendance O(n²)', alpha=0.7)
    
    plt.xlabel('Taille de la matrice (N)', fontsize=12, fontweight='bold')
    plt.ylabel('Mémoire utilisée (MB)', fontsize=12, fontweight='bold')
    plt.title('Complexité spatiale du produit de matrices carrées', 
              fontsize=14, fontweight='bold', pad=20)
    
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(fontsize=11, loc='upper left')
    
    # Ajouter les valeurs sur les points
    for i, (n, m) in enumerate(zip(n_values, memoire_values)):
        if i % 2 == 0:  # Afficher un point sur deux
            label = f'{m:.1f} MB'
            
            plt.annotate(label, (n, m), 
                        textcoords="offset points", 
                        xytext=(0, 10), 
                        ha='center',
                        fontsize=9,
                        bbox=dict(boxstyle='round,pad=0.3', 
                                facecolor='white', 
                                alpha=0.8,
                                edgecolor='#45B7D1'))
    
    plt.tight_layout()
    
    # Sauvegarder
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    nom_sortie = os.path.join(OUTPUT_DIR, "memoire_utilisee.png")
    plt.savefig(nom_sortie, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique de la mémoire généré: {nom_sortie}")

def generer_graphique_comparaison(n_values, temps_values):
    """
    Génère un graphique comparant la complexité expérimentale vs théorique
    avec échelle logarithmique pour mieux voir la relation O(n³)
    """
    if not n_values or not temps_values:
        print("Aucune donnée disponible pour le graphique de comparaison")
        return
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # Graphique 1: Échelle normale
    ax1.plot(n_values, temps_values, 'o-', color='#FF6B6B', 
             linewidth=2, markersize=8, label='Temps mesuré',
             markerfacecolor='white', markeredgewidth=2, markeredgecolor='#FF6B6B')
    
    # Courbe théorique O(n³)
    n_array = np.array(n_values)
    if len(n_values) > 0 and temps_values[-1] > 0:
        coef = temps_values[-1] / (n_values[-1] ** 3)
        temps_theorique = coef * (n_array ** 3)
        ax1.plot(n_values, temps_theorique, '--', color='#4ECDC4', 
                linewidth=2, label='Modèle O(n³)', alpha=0.7)
    
    ax1.set_xlabel('Taille N', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Temps (s)', fontsize=11, fontweight='bold')
    ax1.set_title('Échelle linéaire', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.legend(fontsize=10)
    
    # Graphique 2: Échelle logarithmique
    ax2.loglog(n_values, temps_values, 'o-', color='#FF6B6B', 
               linewidth=2, markersize=8, label='Temps mesuré',
               markerfacecolor='white', markeredgewidth=2, markeredgecolor='#FF6B6B')
    
    if len(n_values) > 0 and temps_values[-1] > 0:
        ax2.loglog(n_values, temps_theorique, '--', color='#4ECDC4', 
                  linewidth=2, label='Modèle O(n³)', alpha=0.7)
    
    ax2.set_xlabel('Taille N (log)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Temps (s) (log)', fontsize=11, fontweight='bold')
    ax2.set_title('Échelle logarithmique', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3, linestyle='--', which='both')
    ax2.legend(fontsize=10)
    
    plt.suptitle('Comparaison: Complexité Expérimentale vs Théorique O(n³)', 
                 fontsize=14, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    
    # Sauvegarder
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    nom_sortie = os.path.join(OUTPUT_DIR, "comparaison_theorique_experimental.png")
    plt.savefig(nom_sortie, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique de comparaison généré: {nom_sortie}")

def generer_tableau_analyse(n_values, temps_values):
    """
    Génère un tableau d'analyse montrant le rapport T(n)/n³
    pour vérifier la concordance avec O(n³)
    """
    if not n_values or not temps_values:
        return
    
    print("\n" + "="*70)
    print("ANALYSE DE CONCORDANCE THÉORIQUE vs EXPÉRIMENTAL")
    print("="*70)
    print(f"{'N':<10} {'Temps (s)':<15} {'T(n)/n³':<20} {'Rapport':<15}")
    print("-"*70)
    
    rapports = []
    for n, t in zip(n_values, temps_values):
        if n > 0 and t > 0:
            rapport = t / (n ** 3)
            rapports.append(rapport)
            print(f"{n:<10} {t:<15.6f} {rapport:<20.2e} {rapport/rapports[0] if rapports else 1:<15.2f}")
    
    if rapports:
        moyenne = np.mean(rapports)
        ecart_type = np.std(rapports)
        cv = (ecart_type / moyenne) * 100 if moyenne > 0 else 0
        
        print("-"*70)
        print(f"Moyenne T(n)/n³: {moyenne:.2e}")
        print(f"Écart-type: {ecart_type:.2e}")
        print(f"Coefficient de variation: {cv:.2f}%")
        print()
        
        if cv < 20:
            print("✓ CONCLUSION: Excellente concordance avec le modèle O(n³)")
            print("  Les mesures expérimentales confirment la complexité théorique.")
        elif cv < 50:
            print("✓ CONCLUSION: Bonne concordance avec le modèle O(n³)")
            print("  Les mesures expérimentales sont cohérentes avec la théorie.")
        else:
            print("⚠ CONCLUSION: Concordance modérée avec le modèle O(n³)")
            print("  Des facteurs externes peuvent influencer les mesures.")
    
    print("="*70 + "\n")

def main():
    """
    Fonction principale
    """
    print("\n" + "="*70)
    print("GÉNÉRATION DES GRAPHIQUES - TP3")
    print("Complexité polynomiale du produit de matrices")
    print("="*70 + "\n")
    
    # Lire les données
    print("Lecture des données...")
    n_values, temps_values, memoire_values = lire_donnees_csv(CSV_FILE)
    
    if not n_values:
        print("Erreur: Aucune donnée à traiter")
        print("Assurez-vous d'avoir exécuté le programme C d'abord.")
        return
    
    print(f"✓ {len(n_values)} points de données chargés\n")
    
    # Générer les graphiques
    print("Génération des graphiques...")
    generer_graphique_temps(n_values, temps_values)
    generer_graphique_memoire(n_values, memoire_values)
    generer_graphique_comparaison(n_values, temps_values)
    
    # Afficher l'analyse
    generer_tableau_analyse(n_values, temps_values)
    
    print("="*70)
    print("TERMINÉ!")
    print(f"Tous les graphiques ont été générés dans: {OUTPUT_DIR}/")
    print("  - temps_execution.png")
    print("  - memoire_utilisee.png")
    print("  - comparaison_theorique_experimental.png")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
