# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:42:13 2019

@author: admin
"""

LISTE_ELEVE = '1_liste_eleves.csv'
FICHIER_REUSLTATS = '1_export_resultats.csv'
FICHIER_SAUVEGARDE = '2_croisement_notes.csv'

def ouvre_fichier_eleves(fichier):
    """ Ouvre le fichier contenant les noms d'élèves et leur code séparé par une virgule
        reconstruit les listes indépendantes 
    """
    noms=[]
    id_eleves=[]
    f = open(fichier, "r")
    elements=[]
    for ligne in f:
        elements = ligne.split(',')
        noms.append(elements[0])
        id_eleves.append(elements[1][:-1])
    print(noms,id_eleves )
    f.close()
    return [noms,id_eleves] 

def ouvre_fichier_resultats(fichier):
    f = open(fichier, "r")
    texte = f.read()
    f.close()
    texte_reconstruit = []
    ligne_reconstruite = ""
    fin_gdh = True
    ligne = 0
    for lettre in texte:
        if lettre == '\"':
            if fin_gdh == True:
                texte_reconstruit += '\n'
                fin_gdh = False
            else :
                fin_gdh = True
        ligne_reconstruite += lettre
        if lettre == '\n':
            texte_reconstruit.append(ligne_reconstruite)
            fin_gdh = True
            ligne_reconstruite = ""
    return texte_reconstruit
        
def cherche_ref(ref_eleve,base):
    """ Trouve l'indice de ref_eleve dans base[1]
    """
    i = 0
    for ref in base[1]:
        if ref == ref_eleve:
            return i
        i+=1
        
def ajoute_meilleur_note(base,notes):
    for ligne in notes:
        elements = ligne.split(',')
        if len(elements) > 1:
            position = cherche_ref(elements[1],base)
            if type(position) is int:
                note_actuelle = base[2][position]
                print(elements[1], elements[3], note_actuelle )
                if note_actuelle < float(elements[3]):
                    base[2][position] = float(elements[3])

def affiche(base):
    for i in range(len(base[0])):
        print(base[0][i],';',base[1][i],';',base[2][i])

def enregistre(fichier,base):
    f = open(fichier, "w")
    for i in range(len(base[0])):
        f.write(base[0][i])
        f.write(';')
        f.write(base[1][i])
        f.write(';')
        note_str = str(base[2][i]).replace('.',',')
        f.write(note_str)
        f.write('\n')
    f.close()
    print('Bien fermé')

base_eleve = ouvre_fichier_eleves(LISTE_ELEVE)
base_eleve.append([0.0] * len(base_eleve[0]))
notes = ouvre_fichier_resultats(FICHIER_REUSLTATS)
ajoute_meilleur_note(base_eleve, notes)

affiche(base_eleve)

enregistre(FICHIER_SAUVEGARDE,base_eleve)