# -*- coding: utf-8 -*-
"""
Créé le 25/09/2020
Création de la liste d'élèves avec le code associé.
de NOM_ELEVE:str
vers NOM_ELEVE:str, code:int
@author: Eric Buoncore
"""
# CONSTANTES: Noms des fichiers
LISTE_ELEVE = '0_liste_brute.csv'
FICHIER_SAUVEGARDE = '1_liste_eleves.csv'

# FONCTIONS
def saisie(texte, mini, maxi, defaut)->int:
    """ Affiche le texte
        Attend une saisie
        Tant que les contraintes ne sont pas satisfaites recommence
        Transtype la saisie en entier et la renvoie
    """
    test = False
    while test == False:
        entree  = input(texte)
        if entree.isdigit():
            entree_entier = int(entree)
            if entree_entier >= mini and entree_entier <= maxi:
                test = True
        else:
            if entree =="":
                entree_entier = defaut
                test = True
    return entree_entier

def ouvre_fichier_eleves(fichier:str)->list:
    """ Ouvre le fichier CSV contenant la liste des noms d'élèves.
        Un nom par ligne
        Renvoie la liste des noms
    """
    noms=[]
    f = open(fichier, "r")
    for ligne in f:
        noms.append(ligne)
        #print(noms)
    f.close()
    return noms 

def enregistre(fichier:str,table:list):
    """ Enregisre dans 'fichier' les couples nom, code
    """
    f = open(fichier, "w")
    for i in range(len(table[0])):
        f.write(table[0][i])
        f.write(',')
        f.write(str(table[1][i]))
        f.write('\n')
    f.close()
    print('Bien fermé')
    
def creation_codes(eleves:list, offset:int)->list:
    """ A partir de la liste des noms d'élèves et du décalage saisie
        construit le code de chaque élève
        Les sauts de lignes sont détectés pour signaler le passage à une autre classe
    """
    noms=[]
    codes = []
    classe = 1
    for i in range(len(eleves)):
        nom = eleves[i]
        if len(nom)==1: # Le saut de ligne signale un changement de classe
            classe += 1
        else:
            code = classe*100000 + i*1000 + ord(nom[0]) + offset
            noms.append(nom[:-1])
            codes.append(code)            
    return [noms,codes]

def affiche(table:list):
    """ Affiche la liste des valeurs: id NOM - code
    """
    for i in range(len(table[0])):
        print(i,table[0][i] ,"-",table[1][i])
    
# CORPS DU PROGRAMME
noms_eleves = ouvre_fichier_eleves(LISTE_ELEVE)

decalage = saisie("Décalage (entre 0 et 100. 10 par défaut):", 0, 100, 10)
print(decalage)
base = creation_codes(noms_eleves, decalage)

affiche(base)

enregistre(FICHIER_SAUVEGARDE,base)