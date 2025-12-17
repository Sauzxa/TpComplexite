#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour générer le rapport Word du TP3
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import os

def ajouter_titre(doc, texte, niveau=1):
    """Ajoute un titre avec formatage"""
    titre = doc.add_heading(texte, level=niveau)
    titre.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return titre

def ajouter_paragraphe(doc, texte, gras=False, italique=False):
    """Ajoute un paragraphe avec formatage optionnel"""
    p = doc.add_paragraph(texte)
    if gras or italique:
        run = p.runs[0]
        run.bold = gras
        run.italic = italique
    return p

def ajouter_code(doc, code_text):
    """Ajoute un bloc de code"""
    p = doc.add_paragraph(code_text)
    p.style = 'Intense Quote'
    run = p.runs[0]
    run.font.name = 'Courier New'
    run.font.size = Pt(9)
    return p

def ajouter_image(doc, chemin, largeur=6):
    """Ajoute une image si elle existe"""
    if os.path.exists(chemin):
        doc.add_picture(chemin, width=Inches(largeur))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return True
    return False

def creer_rapport():
    """Crée le rapport complet"""
    doc = Document()
    
    # Page de garde
    titre_principal = doc.add_heading('TP3 - Complexité Polynomiale', 0)
    titre_principal.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_paragraph()
    p = doc.add_paragraph('Rapport d\'Analyse')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.runs[0].font.size = Pt(16)
    
    doc.add_paragraph()
    p = doc.add_paragraph('Exercice 1: Produit de Matrices')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.runs[0].font.size = Pt(14)
    
    p = doc.add_paragraph('Exercice 2: Recherche de Sous-matrice')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.runs[0].font.size = Pt(14)
    
    doc.add_page_break()
    
    # ==================== EXERCICE 1 ====================
    ajouter_titre(doc, 'Exercice 1: Produit de Matrices Carrées', 1)
    
    # 1.1 Objectif
    ajouter_titre(doc, '1. Objectif', 2)
    ajouter_paragraphe(doc, 
        'Calculer le produit de deux matrices carrées C = A × B et analyser sa complexité polynomiale.')
    
    # 1.2 Formule
    ajouter_titre(doc, '2. Formule Mathématique', 2)
    ajouter_paragraphe(doc, 'Pour calculer C(n,p) = A(n,m) × B(m,p):')
    ajouter_code(doc, 'C(i,j) = Σ(A(i,k) × B(k,j))  pour k = 1...m')
    ajouter_paragraphe(doc, 'Pour des matrices carrées (n=m=p), chaque élément nécessite n multiplications et n-1 additions.')
    
    # 1.3 Complexité Théorique
    ajouter_titre(doc, '3. Complexité Théorique', 2)
    
    ajouter_titre(doc, '3.1 Complexité Temporelle', 3)
    ajouter_paragraphe(doc, 'Formule générale: O(n × m × p)')
    ajouter_paragraphe(doc, 'Pour matrices carrées (n=m=p): O(n³)', gras=True)
    ajouter_paragraphe(doc, 'Classe: Polynomiale cubique')
    doc.add_paragraph()
    ajouter_paragraphe(doc, 'Justification:')
    items = [
        'Boucle externe (i): n itérations',
        'Boucle intermédiaire (j): n itérations',
        'Boucle interne (k): n itérations',
        'Total: n × n × n = n³ opérations'
    ]
    for item in items:
        doc.add_paragraph(item, style='List Bullet')
    
    ajouter_titre(doc, '3.2 Complexité Spatiale', 3)
    ajouter_paragraphe(doc, 'Mémoire requise pour trois matrices n×n:')
    ajouter_code(doc, 'Mémoire = 3n² × 8 + 3n × 8 octets\n        = 24n² + 24n octets')
    ajouter_paragraphe(doc, 'Complexité spatiale: O(n²)', gras=True)
    
    # 1.4 Résultats Expérimentaux
    doc.add_page_break()
    ajouter_titre(doc, '4. Résultats Expérimentaux', 2)
    
    ajouter_paragraphe(doc, 'Tableau des mesures pour différentes tailles de matrices:')
    
    # Créer un tableau
    table = doc.add_table(rows=9, cols=3)
    table.style = 'Light Grid Accent 1'
    
    # En-têtes
    headers = ['N (taille)', 'Temps (s)', 'Mémoire (MB)']
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = header
        cell.paragraphs[0].runs[0].bold = True
    
    # Données
    data = [
        ['100', '0.004717', '0.23'],
        ['200', '0.041219', '0.92'],
        ['300', '0.177160', '2.07'],
        ['400', '0.464023', '3.67'],
        ['500', '0.997565', '5.73'],
        ['600', '1.913890', '8.25'],
        ['700', '2.961285', '11.23'],
        ['800', '4.580811', '14.67']
    ]
    
    for i, row_data in enumerate(data):
        for j, value in enumerate(row_data):
            table.rows[i+1].cells[j].text = value
    
    doc.add_paragraph()
    
    # 1.5 Graphiques
    ajouter_titre(doc, '5. Graphiques', 2)
    
    ajouter_titre(doc, '5.1 Temps d\'Exécution en Fonction de N', 3)
    ajouter_paragraphe(doc, 'Ce graphique montre la croissance cubique du temps d\'exécution:')
    if ajouter_image(doc, 'graphiques/temps_execution.png'):
        ajouter_paragraphe(doc, 'Figure 1: Temps d\'exécution vs taille de matrice N', italique=True)
    
    doc.add_page_break()
    
    ajouter_titre(doc, '5.2 Mémoire Utilisée en Fonction de N', 3)
    ajouter_paragraphe(doc, 'Ce graphique montre la croissance quadratique de la mémoire:')
    if ajouter_image(doc, 'graphiques/memoire_utilisee.png'):
        ajouter_paragraphe(doc, 'Figure 2: Mémoire utilisée vs taille de matrice N', italique=True)
    
    doc.add_page_break()
    
    ajouter_titre(doc, '5.3 Comparaison Théorique vs Expérimental', 3)
    ajouter_paragraphe(doc, 'Comparaison en échelles linéaire et logarithmique:')
    if ajouter_image(doc, 'graphiques/comparaison_theorique_experimental.png'):
        ajouter_paragraphe(doc, 'Figure 3: Validation du modèle O(n³)', italique=True)
    
    # 1.6 Analyse
    doc.add_page_break()
    ajouter_titre(doc, '6. Analyse de Concordance', 2)
    
    ajouter_paragraphe(doc, 'Analyse du rapport T(n)/n³:')
    ajouter_code(doc, 'Moyenne T(n)/n³: 6.32×10⁻⁹\nÉcart-type: 1.85×10⁻⁹\nCoefficient de variation: 29.35%')
    
    doc.add_paragraph()
    ajouter_paragraphe(doc, 'Conclusion:', gras=True)
    ajouter_paragraphe(doc, 
        '✓ Bonne concordance avec le modèle O(n³). Le coefficient de variation de 29.35% '
        'indique que les mesures expérimentales sont cohérentes avec la théorie. '
        'Les variations observées sont dues aux optimisations matérielles (cache CPU) '
        'et à la gestion mémoire du système.')
    
    # 1.7 Exemple de sortie
    ajouter_titre(doc, '7. Exemple de Sortie du Programme', 2)
    ajouter_code(doc, '''Matrice A (3×3):
  0.03   0.33   0.69 
  0.42   0.21   0.25 
  0.64   0.86   0.30 

Matrice B (3×3):
  0.02   0.36   0.77 
  0.32   0.14   0.11 
  0.76   0.08   0.55 

Matrice C = A × B (3×3):
  0.63   0.11   0.44 
  0.27   0.20   0.48 
  0.52   0.37   0.75''')
    
    # ==================== EXERCICE 2 ====================
    doc.add_page_break()
    ajouter_titre(doc, 'Exercice 2: Recherche de Sous-matrice', 1)
    
    # 2.1 Objectif
    ajouter_titre(doc, '1. Objectif', 2)
    ajouter_paragraphe(doc, 
        'Rechercher une matrice B(n\',m\') dans une matrice A(n,m) plus grande, '
        'avec deux approches différentes.')
    
    # 2.2 Algorithmes
    ajouter_titre(doc, '2. Algorithmes Implémentés', 2)
    
    ajouter_titre(doc, '2.1 Algorithme sousMat1 (Matrices Non Triées)', 3)
    ajouter_paragraphe(doc, 'Approche: Recherche naïve exhaustive')
    ajouter_paragraphe(doc, 'Principe:')
    items = [
        'Parcourir toutes les positions possibles (i,j) dans A',
        'Pour chaque position, vérifier si B correspond',
        'Retourner la première position trouvée'
    ]
    for item in items:
        doc.add_paragraph(item, style='List Bullet')
    
    ajouter_paragraphe(doc, 'Complexité: O(n × m × n\' × m\')', gras=True)
    ajouter_paragraphe(doc, 'Classe: Polynomiale de degré 4')
    
    doc.add_paragraph()
    
    ajouter_titre(doc, '2.2 Algorithme sousMat2 (Lignes Triées)', 3)
    ajouter_paragraphe(doc, 'Approche: Recherche binaire + vérification')
    ajouter_paragraphe(doc, 'Principe:')
    items = [
        'Pour chaque ligne i de A',
        'Utiliser la recherche binaire pour trouver le premier élément de B',
        'Vérifier si B correspond à cette position'
    ]
    for item in items:
        doc.add_paragraph(item, style='List Bullet')
    
    ajouter_paragraphe(doc, 'Complexité: O(n × log(m) × n\' × m\')', gras=True)
    ajouter_paragraphe(doc, 'Amélioration: log(m) au lieu de (m-m\')')
    
    # 2.3 Résultats
    doc.add_page_break()
    ajouter_titre(doc, '3. Résultats Expérimentaux', 2)
    
    ajouter_paragraphe(doc, 'Comparaison des deux algorithmes:')
    
    # Créer un tableau
    table = doc.add_table(rows=8, cols=6)
    table.style = 'Light Grid Accent 1'
    
    # En-têtes
    headers = ['N', 'M', 'N\'', 'M\'', 'sousMat1(s)', 'sousMat2(s)']
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = header
        cell.paragraphs[0].runs[0].bold = True
    
    # Données
    data = [
        ['100', '100', '5', '5', '0.000002', '0.000003'],
        ['200', '200', '5', '5', '0.000004', '0.000061'],
        ['300', '300', '5', '5', '0.000004', '0.000070'],
        ['200', '200', '10', '10', '0.000002', '0.000045'],
        ['400', '400', '10', '10', '0.000005', '0.000034'],
        ['500', '500', '10', '10', '0.000005', '0.000172'],
        ['500', '500', '20', '20', '0.000003', '0.000067']
    ]
    
    for i, row_data in enumerate(data):
        for j, value in enumerate(row_data):
            table.rows[i+1].cells[j].text = value
    
    doc.add_paragraph()
    
    # 2.4 Graphiques
    ajouter_titre(doc, '4. Graphiques', 2)
    
    ajouter_titre(doc, '4.1 Comparaison des Algorithmes', 3)
    ajouter_paragraphe(doc, 'Comparaison visuelle des temps d\'exécution:')
    if ajouter_image(doc, 'ex2/graphiques/ex2_comparaison.png'):
        ajouter_paragraphe(doc, 'Figure 4: Comparaison sousMat1 vs sousMat2', italique=True)
    
    doc.add_page_break()
    
    ajouter_titre(doc, '4.2 Évolution des Temps', 3)
    ajouter_paragraphe(doc, 'Évolution des temps pour différentes configurations:')
    if ajouter_image(doc, 'ex2/graphiques/ex2_evolution.png'):
        ajouter_paragraphe(doc, 'Figure 5: Évolution des temps d\'exécution', italique=True)
    
    # 2.5 Analyse
    doc.add_page_break()
    ajouter_titre(doc, '5. Analyse et Observations', 2)
    
    ajouter_paragraphe(doc, 'Observations importantes:', gras=True)
    
    items = [
        'Pour les petites matrices, les deux algorithmes ont des performances similaires',
        'L\'overhead de la recherche binaire peut rendre sousMat2 plus lent pour petites tailles',
        'Le gain théorique de sousMat2 se manifeste pour de très grandes matrices (m > 1000)',
        'Les facteurs constants et le cache CPU influencent significativement les résultats'
    ]
    for item in items:
        doc.add_paragraph(item, style='List Bullet')
    
    doc.add_paragraph()
    ajouter_paragraphe(doc, 'Conclusion:', gras=True)
    ajouter_paragraphe(doc, 
        'Les mesures expérimentales montrent que la complexité théorique ne raconte pas '
        'toute l\'histoire. Pour les tailles testées, sousMat1 est souvent plus rapide '
        'car l\'overhead de la recherche binaire domine le gain théorique. '
        'sousMat2 devient avantageux uniquement pour de très grandes valeurs de m.')
    
    # 2.6 Exemple de sortie
    ajouter_titre(doc, '6. Exemple de Sortie du Programme', 2)
    ajouter_code(doc, '''Matrice A (6×6):
  70   4  60  89  24  44 
  91  40  25  14  17  39 
  94  70  52  58  26  27 
  22  86  57   6  54  48 
  50  90  59  39  50  49 
  20  20   6  80  61  30 

Matrice B (3×3):
  52  58  26 
  57   6  54 
  59  39  50 

✓ sousMat1: Trouvé à la position (2, 2)''')
    
    # ==================== CONCLUSION GÉNÉRALE ====================
    doc.add_page_break()
    ajouter_titre(doc, 'Conclusion Générale du TP3', 1)
    
    ajouter_titre(doc, 'Apprentissages Clés', 2)
    items = [
        'Compréhension approfondie de la complexité polynomiale (O(n²), O(n³), O(n⁴))',
        'Validation expérimentale des modèles théoriques',
        'Importance des facteurs constants et du cache CPU dans les performances réelles',
        'Différence entre complexité asymptotique et performance pratique',
        'Utilisation de Python et matplotlib pour l\'analyse de données'
    ]
    for item in items:
        doc.add_paragraph(item, style='List Bullet')
    
    doc.add_paragraph()
    
    ajouter_titre(doc, 'Objectifs Atteints', 2)
    items = [
        '✓ Exercice 1: Produit de matrices avec complexité O(n³) validée',
        '✓ Exercice 2: Deux algorithmes de recherche implémentés et comparés',
        '✓ Mesures expérimentales complètes pour les deux exercices',
        '✓ Graphiques générés avec Python/matplotlib',
        '✓ Analyse de concordance théorique vs expérimentale'
    ]
    for item in items:
        doc.add_paragraph(item, style='List Bullet')
    
    doc.add_paragraph()
    
    ajouter_titre(doc, 'Perspectives', 2)
    ajouter_paragraphe(doc, 'Pour aller plus loin:')
    items = [
        'Implémenter l\'algorithme de Strassen pour le produit de matrices (O(n^2.807))',
        'Tester sousMat2 avec de très grandes matrices (m > 10000)',
        'Paralléliser les algorithmes avec OpenMP ou CUDA',
        'Étudier l\'impact du cache CPU sur les performances'
    ]
    for item in items:
        doc.add_paragraph(item, style='List Bullet')
    
    # Sauvegarder
    doc.save('TP3_Rapport_Complet.docx')
    print("✓ Rapport Word généré: TP3_Rapport_Complet.docx")

if __name__ == "__main__":
    creer_rapport()
