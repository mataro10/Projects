import random
from tkinter import *
CMAX=6
BIEN_PLACE = -1
MAL_PLACE = 0
def genererCmb(c, n, m) :
    """ génère un combinaison de n symboles dans [1...m]

    c: une combinaison
    n: taille des combinaisons
    m: nombre de couleurs
    """
    for k in range(0,n):
        c[k]=random.randint(1, m)


def cmbValide(c, n, m):
    """ Prédicat de Combinaison valide
    :param c: une Combinaison
    :param n: taille de c
    :param m: nombre de couleurs
    :return: Vrai si c est valide (n symboles dans [1..m])
    """
    ok = True
    k = 0
    while k < n and ok:
        ok = ((1 <= c[k]) and (c[k] <= m))
        k += 1
        return ok

def saisirCmb(c, n, m):
    """ Saisie contrainte de la Combinaison du joueur
    :param c: une Combinaison
    :param n: taille de c
    :param m: nombre de couleurs
    """
    saisirCmb0(c, n, m)
    while not cmbValide(c, n, m):
        saisirCmb0(c, n, m)

def afficherCmb(c, n):
    """ Affiche une combinaison

    c: une combinaison
    n: taille de c
    """
    for k in range(0,n):
        valeur = c[k]
        if valeur == BIEN_PLACE:
            print("#", end="")
        elif valeur == MAL_PLACE:
            print("o", end="")
        else:
            print(valeur, end="")
    print()
def test_cmb():
    """ Test """
    mystere = [0 for x in range(CMAX)]
    genererCmb(mystere, 4, 6)
    afficherCmb(mystere, 4)

    humain = [0 for x in range (CMAX)]
    saisirCmb(humain, 4, 6)
    afficherCmb(humain, 4)

def trouverBienPlaces(copies,c ,n):
    """ Trouve et positionne les biens pkacés dans la copie

    :param copies: combinaison du code secret
    :param c:  combinaison du joueur
    :param n: taille des combinaisons
    :return: le nombre de biens places
    """
    nbp = 0
    for k in range(0,n):
        if copie[k] == c[k]:
            nbp+=1
            copie[k] = BIEN_PLACE
        return nbp

def position(valeur, c, n):
    """  Recherche linéaire d'une couleur dans une combinaison

    :param valeur: une couleur
    :param c: combinaison du joueur
    :param n: taille de c
    :return: l'indice de valeur c, -1 si elle n'existe pas
    """
    k = 0
    while k < n and c[k] !=valeur:
        k+=1
    return (k if k < n else -1)

def trouverMalPlaces(copie, c, n):
    """ Trouve et positionne les mal placés dans la copie

    :param copie: combinaison du code secret
    :param c: combinaison du joueur
    :param n: taille des combinaison
    :return: le nombre de mal placés
    """
    nmp = 0
    for k in range(0,n):
        if copie[k] != BIEN_PLACE:
            p = position(c[k], copie, n)
            if p != -1:
                nmp += 1
                copie[k] = MAL_PLACE
    return nmp

def test_cmb():
    """ Test """
    mystere = [0 for x in range(CMAX)]
    genererCmb(mystere, 4, 6)
    afficherCmb(mystere, 4)

    humain = [0 for x in range (CMAX)]
    saisirCmb(humain, 4, 6)
    afficherCmb(humain, 4)

    nbp = trouverBienPlaces(mystere, humain, 4)
    afficherCmb(mystere, 4)
    print("nbp =", nbp, sep="")
    nmp = trouverMalPlaces(mystere, humain, 4)
    afficherCmb(mystere, 4)
    print("nmp = ", nmp,sep="")

def copierCmb(src, dest, n):
    """ Recopie une combinaison

    :param src: combinaison source
    :param dest: combinaison destination
    :param n: taille des combinaison
    :return: rien
    """
    for k in range(0,n):
        dest[k] = src[k]

def etudierCode(c1, c2, n):
    """ Etudie le code humain par rapport à celui de la machine

    :param c1: combinaison du code secret
    :param c2: combinaison du joueur
    :param n: taille des combinaison
    :return:
    """
    copierCmb(c1, copie, n)
    nbp = trouverBienPlaces(copie, c2, n)
    nmp = (trouverMalPlaces(copie, c2, n) if nbp != n else 0)
    return (nbp, nmp)

def mastermind(n, m, maxcoups):
    """ lance une partie du jeu

    :param n: taille des combinaisons
    :param m: nombre de couleurs
    :param maxcoups: nombre de coups max pour l'humain
    :return:
    """
    # solution à trouver
    mystere = [0 for x in range(CMAX)]
    genererCmb(mystere, n, m)

    # nombre de coups effectués
    ncoups = 0

    # proposition == solution ?

    trouve = False

    # lance la partie

    while not trouve and (ncoups < maxcoups):
        # proposition de l'humain
        humain = [0 for x in range (CMAX)]
        saisirCmb(humain, n, m)
        # un coup de plus
        ncoups += 1
        nbp, nmp = etudierCode(mystere, humain, n)
        trouve = (nbp==n)
        # Résultat du code
        for j in range (nbp):
            print("#", end="")
        for j in range (nmp):
            print("o, end=")
        print(s,"(reste", (maxcoups-ncoups),"coups)",sep="")
        #Affiche le score de la partie
        if trouve:
            print("Gagne en ", ncoups, "coups", sep="")
        else:
            print("Perdu voici la combinaison: ",end="")
            afficherCmb(mystere, n)

def bienvenue(n, m, maxcoups):
    """ Affiche un texte d’accueil présentant le jeu
    :param n: taille des Combinaison
    :param m: nombre de couleurs
    :param maxcoups: nombre de coups maximum de l’humain
    """
    print("Pouvez-vous trouver ma combinaison de ", n, " symboles", sep="")
    print("[chiffres entre 1 et ", m, " avec repetitions possibles]", sep="")
    print("en moins de ", maxcoups, " coups? Entrez les symboles des", sep="")
    print("propositions terminees par [Entree].")
    print("(# un bien place, o un mal place)", sep="")

fenetre = Tk()
fenetre.title("Trop de la balle")
titre = Label(fenetre, text = "l'informatique")
titre.pack()
fenetre.mainloop()