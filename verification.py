import numpy as np
from math import sqrt
import random

def regiongrille(grille):
    liste_voisin = list(range(81))
    n = 9
    for i in range(n) :
        for j in range(n) :
            l=random.choice(liste_voisin)
            grille[i][j]=l
            liste_voisin.remove(l)

grilleC = np.zeros((9, 9), dtype=int)
regiongrille(grilleC)

def trouveligne(nb):
    global grilleC
    for i in range(9) :
        for j in range(9) :
            if (grilleC[i][j]==nb):
                return i
            
def remplir_grillevoisin_classique (grille) :
    n = int(sqrt(len(grille)))
    for i in range(n) :
        for j in range(n) :
            positionGrille = i * n + j
            for x in range(n):
                b=i*n+x 
                c=x*n+j
                if x!=j:
                    grille[positionGrille][b]=1
                if x!=i:
                    grille[positionGrille][c]=1
            
            position_i = i // (n**0.5)
            position_j = j // (n**0.5)
            for x in range(n) :
                for y in range(n) :
                    position_x = x // (n**0.5)
                    position_y = y // (n**0.5)
                    if position_x == position_i  and position_y == position_j :
                        d=x*n+y
                        grille[positionGrille][d]=1
    for i in range(n**2) :
        grille[i][i]=0

def remplir_grillevoisin_couleur (grille) :
    n = int(sqrt(len(grille)))
    global grilleC
    for i in range(n) :
        for j in range(n) :
            positionGrille = i * n + j
            for x in range(n):
                b=i*n+x
                if x!=j:
                    grille[positionGrille][b]=1
                       
    for i in range(n) :
        for j in range(n) :
            positionGrille = i * n + j
            for k in range(n):
                valeur=grilleC[trouveligne(positionGrille)][k]
                grille[positionGrille][valeur]=1    
    for i in range(n**2) :
        grille[i][i]=0

def remplir_grillevoisin_diagonal(grille) :
    remplir_grillevoisin_classique (grille)
    n = 9
    for i in range(n) :
        for j in range(n) :
            if i==j:
                pi=0
                pj=0
                while pi <=8 and pj <= 8:
                    grille[i*n+j][pi*n+pj]=1
                    pi=pi+1
                    pj=pj+1
            if i+j==8:
                qi=0
                qj=8
                while qi <=8 and qj >= 0:
                    grille[i*n+j][qi*n+qj]=1
                    qi=qi+1
                    qj=qj-1
            
    for i in range(n**2) :
        grille[i][i]=0  
        
def remplir_grillevoisin_position (grille) :
    remplir_grillevoisin_classique (grille)
    n = 9
    numeroList=[0,1,2,9,10,11,18,19,20]
    for i in range(n) :
        for j in range(n) :
            positionGrille = i * n + j
            for k in range(len(numeroList)):
                positionM= 3 * numeroList[k] + ((i%3)*n+(j%3))
                grille[positionGrille][positionM]=1
    for i in range(n**2) :
        grille[i][i]=0
        
GrilleVoisinClassique = np.zeros((81,81), dtype=int)
remplir_grillevoisin_classique(GrilleVoisinClassique)
GrilleVoisinCouleur = np.zeros((81,81), dtype=int)
remplir_grillevoisin_couleur(GrilleVoisinCouleur)
GrilleVoisinDiagonal = np.zeros((81,81), dtype=int)
remplir_grillevoisin_diagonal(GrilleVoisinDiagonal)
GrilleVoisinPosition = np.zeros((81,81), dtype=int)
remplir_grillevoisin_position(GrilleVoisinPosition)

def test(chiffre, i, j, grille,variante):
    n = len(grille)
    if variante == 'classique' :
        global GrilleVoisinClassique
        grille_voisin=GrilleVoisinClassique
    if variante == 'couleur' :
        global GrilleVoisinCouleur
        grille_voisin=GrilleVoisinCouleur
    if variante == 'diagonal':
        global GrilleVoisinDiagonal
        grille_voisin=GrilleVoisinDiagonal
    if variante == 'position':
        global GrilleVoisinPosition
        grille_voisin=GrilleVoisinPosition        
    a = i * n + j
    for k in range((n**2)):
        z=grille[k//n][k%n]
        if grille_voisin[a][k] == 1:
            if z == chiffre:
                    return False
    return True