

import numpy as np

eleves = ["Ana", "bana", "cana", "dana", "ena", "fana", "gana", "hana", "ina", "kana"]
matieres = ["matheatique", "physique", "informatique", "chimie", "histoire", "geographie", "EPS", "TM", "EM", "ECM"]

notes = [
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
    [12, 13, 14, 10, 14, 16, 9, 16, 18, 15.5],
]


def moyenne_eleves(notes_eleve):
    """Calcule la moyenne des notes d’un élève"""
    return sum(notes_eleve) / len(notes_eleve)


def gerer_notes():
    """Retourne une liste (nom, moyenne) triée par ordre décroissant de moyenne"""
    resultat = []
    for i in range(len(eleves)):
        moyenne = moyenne_eleves(notes[i])
        resultat.append((eleves[i], moyenne))
    #resultat.sort(key=lambda x: x[1], reverse=True)
    
    return resultat
max=np.max(notes)

def affiche():
    """Affiche les résultats avec classement"""
    resul = gerer_notes()
    for i, (nom, moyenne) in enumerate(resul, start=1):
        print(f"{i} - {nom} - moyenne : {moyenne:.2f}")

        



  



























