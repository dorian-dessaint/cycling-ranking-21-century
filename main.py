# Prototype de calcul des points

# ==========================================
# 1. LE BAREME DES POINTS
# ==========================================
# Chaque performance rapporte un nombre de points précis.

POINTS = {
    # Classement Général (GC) sur les Grands Tours
    "gt_gc_win": 1000,       # Victoire finale
    "gt_gc_podium": 600,     # 2e ou 3e place
    "gt_gc_top5": 300,       # 4e ou 5e place
    
    # Victoires d'étapes sur les Grands Tours
    "gt_stage_win": 100,     
    
    # Monuments (les 5 classiques majeures)
    "monument_win": 500,     
    "monument_podium": 250   
}

# ==========================================
# 2. LES DONNEES DES COUREURS (Palmarès)
# ==========================================
# Dictionnaire principal : chaque coureur possède un sous-dictionnaire 
# qui associe une clé de performance à un nombre total réalisé.

palmares_db = {
    "Tadej Pogačar": {
        "gt_gc_win": 3,
        "gt_gc_podium": 1,
        "gt_stage_win": 17,
        "monument_win": 6,
        "monument_podium": 3
    },
    "Chris Froome": {
        "gt_gc_win": 4,
        "gt_gc_podium": 2,
        "gt_gc_top5": 1,
        "gt_stage_win": 7,
        "monument_win": 0,
        "monument_podium": 1
    }
}

# ==========================================
# 3. LA FONCTION DE CALCUL
# ==========================================
def calculer_score(palmares_coureur):
    """
    Additionne les points d'un coureur en multipliant 
    le nombre de réussites par la valeur du barème.
    """
    total = 0
    
    # On parcourt chaque performance (ex: "gt_stage_win": 17)
    for performance, quantite in palmares_coureur.items():
        # Si la performance existe bien dans notre barème
        if performance in POINTS:
            total += quantite * POINTS[performance]
            
    return total

# ==========================================
# 4. EXECUTION ET CLASSEMENT AUTOMATIQUE
# ==========================================
if __name__ == "__main__":
    print("--- CLASSEMENT CYCLISTE DU 21e SIECLE ---")
    
    # On trie les coureurs du score le plus grand au plus petit
    # key=lambda x: calculer_score(x[1]) dit à Python de trier selon le score calculé
    classement_trie = sorted(
        palmares_db.items(), 
        key=lambda element: calculer_score(element[1]), 
        reverse=True
    )
    
    # On affiche le classement final propre
    for position, (coureur, palmares) in enumerate(classement_trie, start=1):
        score_total = calculer_score(palmares)
        print(f"{position}. {coureur} : {score_total} points")