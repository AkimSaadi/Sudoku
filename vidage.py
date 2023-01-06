import random
import numpy as np
from verification import test

def trouver_case_vide (grille) :
    for i in range (len(grille[:,0])) :
        for j in range (len(grille[0,:])) :
            if grille[i][j] == 0 :
                position = (i,j)
                return position
    return False

def Unicite(Grille):
    nombre_solution=0
    n=len(Grille[0])
    for i in range(n):
        for j in range(n):
            if (Grille[i][j]==0) :
                for nombre in range(1,n+1):
                    if nombre_solution>1:
                        return nombre_solution
                    if test(nombre,i,j,Grille,'classique'):
                        temp=Grille[i][j]# ps besoin de stocké en temp on peut mettre directement a zero ou nombre
                        Grille[i][j]=nombre
                        nombre_solution+=Unicite(Grille)
                        if (trouver_case_vide(Grille)==False):
                            nombre_solution+=1
                        Grille[i][j]=temp # ici tu remets directement le 0
                return nombre_solution
    return nombre_solution
        


def vider_grille(new_grille,profondeur):
    x=profondeur
    numeroList=[0,1,2,3,4,5,6,7,8]
    GrilleCopie = np.copy(new_grille)
    vide=0
    while(vide< profondeur) :
        column = random.choice(numeroList)
        line =random.choice(numeroList)
        if(new_grille[line][column]!=0):
            new_grille[line][column]=0 #on vide la grille case par case 
            unic=Unicite(new_grille)
            if (unic==1):
                GrilleCopie = np.copy(new_grille)#si elle est unique on vide une autre case
                x-=1
            else : #si elle n'est pas unique il redemarque de la copie, vu que c'est random il peut enlever une case ou---> 
                vider_grille(GrilleCopie,x)#--->l'unicité continue
                return GrilleCopie 
        else :
            vide = vide - 1
        vide=vide+1
    print('cette grille est unique  et à la profondeur voulue')#par profondeur je veux dire le vide dans la grille
    return GrilleCopie
            
      
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
