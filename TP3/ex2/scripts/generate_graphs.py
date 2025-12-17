#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP3 - Exercice 2: Génération des graphiques
Comparaison des algorithmes sousMat1 et sousMat2
"""

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# Configuration
CSV_FILE = "../dist/ex2_resultats.csv"
OUTPUT_DIR = "../graphiques"

def lire_donnees_csv(nom_fichier):
    """
    Lit le fichier CSV et retourne les données
    """
    configs = []
    temps1 = []
    temps2 = []
    ratios = []
    
    if not os.path.exists(nom_fichier):
        print(f"Erreur: Fichier {nom_fichier} non trouvé")
        return configs, temps1, temps2, ratios
    
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    n = int(row['N'])
                    m = int(row['M'])
                    n_prime = int(row['N_prime'])
                    m_prime = int(row['M_prime'])
                    t1 = float(row['Temps_sousMat1(s)'])
                    t2 = float(row['Temps_sousMat2(s)'])
                    ratio = float(row['Ratio'])
                    
                    config_label = f"{n}×{m}\n({n_prime}×{m_prime})"
                    configs.append(config_label)
                    temps1.append(t1)
                    temps2.append(t2)
                    ratios.append(ratio)
                except (ValueError, KeyError) as e:
                    print(f"Erreur lors de la lecture d'une ligne: {e}")
                    continue
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
    
    return configs, temps1, temps2, ratios

def generer_graphique_comparaison(configs, temps1, temps2):
    """
    Génère un graphique comparant sousMat1 et sousMat2
    """
    if not configs:
        print("Aucune donnée disponible")
        return
    
    plt.figure(figsize=(14, 8))
    
    x = np.arange(len(configs))
    largeur = 0.35
    
    # Créer les barres
    bars1 = plt.bar(x - largeur/2, temps1, largeur, 
                    label='sousMat1 (non trié)', 
                    color='#FF6B6B', alpha=0.8, edgecolor='black')
    
    bars2 = plt.bar(x + largeur/2, temps2, largeur, 
                    label='sousMat2 (trié)', 
                    color='#4ECDC4', alpha=0.8, edgecolor='black')
    
    plt.xlabel('Configuration (N×M avec sous-matrice N\'×M\')', fontsize=12, fontweight='bold')
    plt.ylabel('Temps d\'exécution (secondes)', fontsize=12, fontweight='bold')
    plt.title('Comparaison: sousMat1 vs sousMat2', fontsize=14, fontweight='bold', pad=20)
    
    plt.xticks(x, configs, rotation=45, ha='right', fontsize=9)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    
    # Sauvegarder
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    nom_sortie = os.path.join(OUTPUT_DIR, "ex2_comparaison.png")
    plt.savefig(nom_sortie, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique de comparaison généré: {nom_sortie}")

def generer_graphique_ratio(configs, ratios):
    """
    Génère un graphique montrant le ratio de performance
    """
    if not configs:
        print("Aucune donnée disponible")
        return
    
    plt.figure(figsize=(14, 8))
    
    x = np.arange(len(configs))
    
    # Créer les barres
    bars = plt.bar(x, ratios, color='#96CEB4', alpha=0.8, edgecolor='black')
    
    # Ligne de référence à 1.0
    plt.axhline(y=1.0, color='red', linestyle='--', linewidth=2, 
                label='Ratio = 1 (même performance)', alpha=0.7)
    
    plt.xlabel('Configuration (N×M avec sous-matrice N\'×M\')', fontsize=12, fontweight='bold')
    plt.ylabel('Ratio (Temps sousMat1 / Temps sousMat2)', fontsize=12, fontweight='bold')
    plt.title('Gain de performance: sousMat2 vs sousMat1', fontsize=14, fontweight='bold', pad=20)
    
    plt.xticks(x, configs, rotation=45, ha='right', fontsize=9)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Ajouter les valeurs sur les barres
    for i, (bar, ratio) in enumerate(zip(bars, ratios)):
        if i % 2 == 0:  # Afficher un sur deux
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{ratio:.1f}x',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    
    # Sauvegarder
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    nom_sortie = os.path.join(OUTPUT_DIR, "ex2_ratio.png")
    plt.savefig(nom_sortie, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique des ratios généré: {nom_sortie}")

def generer_graphique_evolution(configs, temps1, temps2):
    """
    Génère un graphique en ligne montrant l'évolution des temps
    """
    if not configs:
        print("Aucune donnée disponible")
        return
    
    plt.figure(figsize=(14, 8))
    
    x = np.arange(len(configs))
    
    # Tracer les courbes
    plt.plot(x, temps1, 'o-', color='#FF6B6B', linewidth=2, markersize=8,
             label='sousMat1 (non trié)', markerfacecolor='white', 
             markeredgewidth=2, markeredgecolor='#FF6B6B')
    
    plt.plot(x, temps2, 's-', color='#4ECDC4', linewidth=2, markersize=8,
             label='sousMat2 (trié)', markerfacecolor='white',
             markeredgewidth=2, markeredgecolor='#4ECDC4')
    
    plt.xlabel('Configuration (N×M avec sous-matrice N\'×M\')', fontsize=12, fontweight='bold')
    plt.ylabel('Temps d\'exécution (secondes)', fontsize=12, fontweight='bold')
    plt.title('Évolution des temps d\'exécution', fontsize=14, fontweight='bold', pad=20)
    
    plt.xticks(x, configs, rotation=45, ha='right', fontsize=9)
    plt.legend(fontsize=11, loc='upper left')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    
    # Sauvegarder
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    nom_sortie = os.path.join(OUTPUT_DIR, "ex2_evolution.png")
    plt.savefig(nom_sortie, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique d'évolution généré: {nom_sortie}")

def afficher_analyse(configs, temps1, temps2, ratios):
    """
    Affiche une analyse statistique
    """
    if not configs:
        return
    
    print("\n" + "="*70)
    print("ANALYSE STATISTIQUE")
    print("="*70)
    
    ratio_moyen = np.mean(ratios)
    ratio_max = np.max(ratios)
    ratio_min = np.min(ratios)
    
    print(f"Ratio moyen (sousMat1/sousMat2): {ratio_moyen:.2f}x")
    print(f"Ratio maximum: {ratio_max:.2f}x")
    print(f"Ratio minimum: {ratio_min:.2f}x")
    print()
    
    if ratio_moyen > 1.5:
        print("✓ CONCLUSION: sousMat2 est significativement plus rapide")
        print(f"  En moyenne, sousMat2 est {ratio_moyen:.1f}x plus rapide que sousMat1")
    elif ratio_moyen > 1.1:
        print("✓ CONCLUSION: sousMat2 est plus rapide")
        print(f"  Gain de performance modéré: {ratio_moyen:.1f}x")
    else:
        print("⚠ CONCLUSION: Performance similaire")
        print("  Le gain de sousMat2 n'est pas significatif pour ces tailles")
    
    print("="*70 + "\n")

def main():
    """
    Fonction principale
    """
    print("\n" + "="*70)
    print("GÉNÉRATION DES GRAPHIQUES - EXERCICE 2")
    print("Recherche de sous-matrice")
    print("="*70 + "\n")
    
    # Lire les données
    print("Lecture des données...")
    configs, temps1, temps2, ratios = lire_donnees_csv(CSV_FILE)
    
    if not configs:
        print("Erreur: Aucune donnée à traiter")
        print("Assurez-vous d'avoir exécuté le programme C d'abord.")
        return
    
    print(f"✓ {len(configs)} configurations chargées\n")
    
    # Générer les graphiques
    print("Génération des graphiques...")
    generer_graphique_comparaison(configs, temps1, temps2)
    generer_graphique_ratio(configs, ratios)
    generer_graphique_evolution(configs, temps1, temps2)
    
    # Afficher l'analyse
    afficher_analyse(configs, temps1, temps2, ratios)
    
    print("="*70)
    print("TERMINÉ!")
    print(f"Tous les graphiques ont été générés dans: {OUTPUT_DIR}/")
    print("  - ex2_comparaison.png")
    print("  - ex2_ratio.png")
    print("  - ex2_evolution.png")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
