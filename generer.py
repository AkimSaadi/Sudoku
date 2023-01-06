import random
from verification import test
import numpy as np
from vidage import vider_grille

def trouver_case_vide (grille) :
    for i in range (len(grille[:,0])) :
        for j in range (len(grille[0,:])) :
            if grille[i][j] == 0 :
                position = (i,j)
                return position
    return False

def remplir_grille(grille,variante) :
    position_case_vide = trouver_case_vide(grille)
    if position_case_vide == False :
        return True
    else :
        ligne, colonne = position_case_vide
    numeroList=[1,2,3,4,5,6,7,8,9]
    vide=[]
    while (numeroList != vide):
          valeur = random.choice(numeroList)
          numeroList.remove(valeur)
          if test(valeur,ligne,colonne,grille,variante):
              grille[ligne][colonne]=valeur
              if remplir_grille(grille,variante) :
                  return True
              grille[ligne][colonne]=0
    return False

def copier_dernier_carre_vers_premier_carre (grille1,grille2) :
    for i in range(6) :
        for j in range (6) :
            grille2[i][j] = grille1[i+3][j+3]
            
def remplir_grille_triple (grilletriple,GrilleSudokuTriplevide) :
    grille1 = np.zeros((9, 9), dtype=int)
    grille2 = np.zeros((9, 9), dtype=int)
    grille3 = np.zeros((9, 9), dtype=int)
    remplir_grille(grille1,'classique')
    copier_dernier_carre_vers_premier_carre(grille1, grille2)
    remplir_grille(grille2,'classique')
    copier_dernier_carre_vers_premier_carre(grille2, grille3)
    remplir_grille(grille3,'classique')
    
    for i in range (len(grilletriple)) :
        for j in range(len(grilletriple[0])):
            if i < 9 :
                if j < 9 :
                    grilletriple[i][j]=grille1[i][j]
            if i > 2 and i < 12 :
                if j > 2 and j < 12 :
                    grilletriple[i][j]=grille2[i-3][j-3]
            if i > 5 :
                if j > 5 :
                    grilletriple[i][j]=grille3[i-6][j-6]
    for i in range (len(GrilleSudokuTriplevide)) :
        for j in range(len(GrilleSudokuTriplevide[0])):
            GrilleSudokuTriplevide[i][j]=10
            
    for i in range (len(grilletriple)) :
        for j in range(len(grilletriple[0])):
            if(grilletriple[i][j]==0) :
                grilletriple[i][j]=10
    
    vider_grille(grille1,3)
    vider_grille(grille2,3)
    vider_grille(grille3,3)
    for i in range (len(GrilleSudokuTriplevide)) :
        for j in range(len(GrilleSudokuTriplevide[0])):
            if i < 9 :
                if j < 9 :
                    GrilleSudokuTriplevide[i][j]=grille1[i][j]
            if i > 2 and i < 12 :
                if j > 2 and j < 12 :
                    GrilleSudokuTriplevide[i][j]=grille2[i-3][j-3]
            if i > 5 :
                if j > 5 :
                    GrilleSudokuTriplevide[i][j]=grille3[i-6][j-6]