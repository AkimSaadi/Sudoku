from tkinter import Label, YES, Tk, Frame, Button, X
import numpy as np
from generer import remplir_grille, remplir_grille_triple
from affichage import afficher_grille, interface_graphique, afficheGrillePosition, afficheGrilleCouleur, afficheGrillePaire, afficheGrilleSimple
from vidage import vider_grille

GrilleSudoku = np.zeros((9, 9), dtype=int)
GrilleCopie = np.zeros((9, 9), dtype=int)
liste = []
data = []


def remplir_liste_solution () :
    global GrilleSudoku, GrilleCopie
    liste = list()
    n=len(GrilleSudoku[0])
    for i in range(n):
        line = list()
        for j in range(n):
            if (GrilleCopie[i][j]!=GrilleSudoku[i][j]):
                line.append(GrilleSudoku[i][j])
        liste.append(line)
    return liste
 
def Corection():
    global data
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (data[i][j].get()!='') :
                if (int(data[i][j].get())==liste[i][j]):
                    print(data[i][j].get(),'se trouvant sur la ligne',i,'est correct',sep=' ')
                else :
                    print(data[i][j].get(),'se trouvant sur la ligne',i,'est incorrect',sep=' ')

def MenuFR() :
    cadreLangues.pack_forget()
    titre.pack_forget()
    sous_titre.pack_forget()
    bouton_play.pack_forget()
    bouton_credit.pack_forget()
    cadreMenuFR.pack(expand=YES)
    bouton_playFR.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    bouton_creditFR.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)

def MenuEN() :
    cadreLangues.pack_forget()
    titre.pack_forget()
    sous_titre.pack_forget()
    bouton_play.pack_forget()
    bouton_credit.pack_forget()
    cadreMenuEN.pack(expand=YES)
    bouton_playEN.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    bouton_creditEN.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)

def playFR():
    cadreMenuFR.pack_forget()
    bouton_playFR.pack_forget()
    bouton_creditFR.pack_forget()
    cadreplayFR.pack(expand=YES)
    grilleFR.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    grillepaireFR.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    grille3FR.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    grillediagonalFR.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    grillepositionFR.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    solutionFR.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    
def creditFR():
    cadreMenuFR.pack_forget()
    bouton_playFR.pack_forget()
    bouton_creditFR.pack_forget()
    cadrecreditFR.pack(expand=YES)
    textFR.pack()
    textFR1.pack()
    textFR2.pack()
    textFR3.pack()
    textFR4.pack()
    textFR5.pack()
    textFR6.pack()
    textFR7.pack()
    textFR8.pack()
    textFR9.pack()
    textFR10.pack()
    textFR11.pack()
    textFR12.pack()
    textFR13.pack()
    grillecouleurFR.pack()
    backcreditFR.pack()
        
def playEN():
    cadreMenuEN.pack_forget()
    bouton_playEN.pack_forget()
    bouton_creditEN.pack_forget()
    cadreplayEN.pack(expand=YES)
    grilleEN.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    grillepaireEN.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    grille3EN.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    grillediagonalEN.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    grillepositionEN.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    solutionEN.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    
def creditEN():
    cadreMenuEN.pack_forget()
    bouton_playEN.pack_forget()
    bouton_creditEN.pack_forget()
    cadrecreditEN.pack(expand=YES)
    textEN.pack()
    textEN1.pack()
    textEN2.pack()
    textEN3.pack()
    textEN4.pack()
    textEN5.pack()
    textEN6.pack()
    textEN7.pack()
    textEN8.pack()
    textEN9.pack()
    textEN10.pack()
    textEN11.pack()
    textEN12.pack()
    textEN13.pack()
    textEN14.pack()
    grillecouleurEN.pack()
    backcreditEN.pack()
    
def grillesimple():
    grilleFR.pack_forget()
    grilleEN.pack_forget()
    grillepaireFR.pack_forget()
    grillepaireEN.pack_forget()
    grille3FR.pack_forget()
    grille3EN.pack_forget()
    solutionFR.pack_forget()
    solutionEN.pack_forget()
    grillediagonalFR.pack_forget()
    grillediagonalEN.pack_forget()
    grillepositionFR.pack_forget()
    grillepositionEN.pack_forget()
    grilleFRF.pack()
    grilleFRD.pack()
 
def grillesimplecolore():
    global GrilleSudoku, GrilleCopie, liste
    grilleFR.pack_forget()
    grilleEN.pack_forget()
    grillepaireFR.pack_forget()
    grillepaireEN.pack_forget()
    grille3FR.pack_forget()
    grille3EN.pack_forget()
    solutionFR.pack_forget()
    solutionEN.pack_forget()
    grillediagonalFR.pack_forget()
    grillediagonalEN.pack_forget()
    grillepositionFR.pack_forget()
    grillepositionEN.pack_forget()
    cadreplayEN.pack_forget()
    cadreplayFR.pack_forget()
    cadregrillesimple.pack(expand=YES)
    remplir_grille(GrilleSudoku,'classique')
    afficher_grille(GrilleSudoku)
    GrilleCopie = np.copy(GrilleSudoku)
    GrilleCopie =vider_grille(GrilleCopie,1)
    afficher_grille(GrilleCopie)
    liste =remplir_liste_solution()
    afficheGrillePaire(cadregrillesimple, 9, 9, data, liste, GrilleSudoku, GrilleCopie)
    checkcolor.pack()
    backcolor.pack()


def grilletriple():
    GrilleSudokuTriple = np.zeros((15, 15), dtype=int)
    GrilleSudokuTriplevide = np.zeros((15, 15), dtype=int)
    grilleFR.pack_forget()
    grilleEN.pack_forget()
    grillepaireFR.pack_forget()
    grillepaireEN.pack_forget()
    grille3FR.pack_forget()
    grille3EN.pack_forget()
    solutionFR.pack_forget()
    solutionEN.pack_forget()
    grillediagonalFR.pack_forget()
    grillediagonalEN.pack_forget()
    grillepositionFR.pack_forget()
    grillepositionEN.pack_forget()
    cadreplayEN.pack_forget()
    cadreplayFR.pack_forget()
    cadregrillesimple.pack(expand=YES)
    remplir_grille_triple(GrilleSudokuTriple,GrilleSudokuTriplevide)
    interface_graphique(GrilleSudokuTriplevide,cadregrillesimple)

def solutiongrille():
    grilleFR.pack_forget()
    grilleEN.pack_forget()
    grillepaireFR.pack_forget()
    grillepaireEN.pack_forget()
    grille3FR.pack_forget()
    grille3EN.pack_forget()
    solutionFR.pack_forget()
    solutionEN.pack_forget()
    grillediagonalFR.pack_forget()
    grillediagonalEN.pack_forget()
    grillepositionFR.pack_forget()
    grillepositionEN.pack_forget()
    cadreplayEN.pack_forget()
    cadreplayFR.pack_forget()
    cadregrillesimple.pack(expand=YES)
    afficheGrilleSimple(cadregrillesimple, 9, 9,data,GrilleCopie)
    solution.pack()
    backsolution.pack()

def grillesimpleF():
    global GrilleSudoku, GrilleCopie, liste
    grilleFR.pack_forget()
    grilleEN.pack_forget()
    grillepaireFR.pack_forget()
    grillepaireEN.pack_forget()
    grille3FR.pack_forget()
    grille3EN.pack_forget()
    solutionFR.pack_forget()
    solutionEN.pack_forget()
    grillediagonalFR.pack_forget()
    grillediagonalEN.pack_forget()
    grillepositionFR.pack_forget()
    grillepositionEN.pack_forget()
    cadreplayEN.pack_forget()
    cadreplayFR.pack_forget()
    cadregrillesimple.pack(expand=YES)
    remplir_grille(GrilleSudoku,'classique')
    GrilleCopie = np.copy(GrilleSudoku)
    afficher_grille(GrilleSudoku)
    GrilleCopie =vider_grille(GrilleCopie,15)
    afficher_grille(GrilleCopie)
    liste =remplir_liste_solution()
    afficheGrilleSimple(cadregrillesimple, 9, 9,data,GrilleCopie)
    checksimple.pack()
    backsimple.pack()

def grillesimpleD():
    global GrilleSudoku, GrilleCopie, liste
    grilleFR.pack_forget()
    grilleEN.pack_forget()
    grillepaireFR.pack_forget()
    grillepaireEN.pack_forget()
    grille3FR.pack_forget()
    grille3EN.pack_forget()
    solutionFR.pack_forget()
    solutionEN.pack_forget()
    grillediagonalFR.pack_forget()
    grillediagonalEN.pack_forget()
    grillepositionFR.pack_forget()
    grillepositionEN.pack_forget()
    cadreplayEN.pack_forget()
    cadreplayFR.pack_forget()
    cadregrillesimple.pack(expand=YES)
    remplir_grille(GrilleSudoku,'classique')
    GrilleCopie = np.copy(GrilleSudoku)
    afficher_grille(GrilleSudoku)
    GrilleCopie =vider_grille(GrilleCopie,30)
    afficher_grille(GrilleCopie)
    liste =remplir_liste_solution()
    afficheGrilleSimple(cadregrillesimple, 9, 9,data,GrilleCopie)
    checksimple.pack()
    backsimple.pack()
    
def grillecouleur():
    global GrilleSudoku, GrilleCopie, liste
    backcreditFR.pack_forget()
    cadrecreditFR.pack_forget()
    backcreditEN.pack_forget()
    cadrecreditEN.pack_forget()
    cadregrillesimple.pack(expand=YES)
    remplir_grille(GrilleSudoku,'couleur')
    GrilleCopie = np.copy(GrilleSudoku)
    afficher_grille(GrilleSudoku)
    GrilleCopie =vider_grille(GrilleCopie,2)
    afficher_grille(GrilleCopie)
    liste =remplir_liste_solution()
    afficheGrilleCouleur(cadregrillesimple, 9, 9,data,GrilleCopie)
    checksimple.pack()
    backsimple.pack()

def grillediagonal():
    global GrilleSudoku, GrilleCopie, liste
    grilleFR.pack_forget()
    grilleEN.pack_forget()
    grillepaireFR.pack_forget()
    grillepaireEN.pack_forget()
    grille3FR.pack_forget()
    grille3EN.pack_forget()
    solutionFR.pack_forget()
    solutionEN.pack_forget()
    grillediagonalFR.pack_forget()
    grillediagonalEN.pack_forget()
    grillepositionFR.pack_forget()
    grillepositionEN.pack_forget()
    cadreplayEN.pack_forget()
    cadreplayFR.pack_forget()
    cadregrillesimple.pack(expand=YES)
    remplir_grille(GrilleSudoku,'diagonal')
    GrilleCopie = np.copy(GrilleSudoku)
    afficher_grille(GrilleSudoku)
    GrilleCopie =vider_grille(GrilleCopie,1)
    afficher_grille(GrilleCopie)
    liste =remplir_liste_solution()
    afficheGrilleSimple(cadregrillesimple, 9, 9,data,GrilleCopie)
    checkdiagonal.pack()
    backdiagonal.pack()


def grilleposition():
    global GrilleSudoku, GrilleCopie, liste
    grilleFR.pack_forget()
    grilleEN.pack_forget()
    grillepaireFR.pack_forget()
    grillepaireEN.pack_forget()
    grille3FR.pack_forget()
    grille3EN.pack_forget()
    solutionFR.pack_forget()
    solutionEN.pack_forget()
    grillediagonalFR.pack_forget()
    grillediagonalEN.pack_forget()
    grillepositionFR.pack_forget()
    grillepositionEN.pack_forget()
    cadreplayEN.pack_forget()
    cadreplayFR.pack_forget()
    cadregrillesimple.pack(expand=YES)
    remplir_grille(GrilleSudoku,'position')
    GrilleCopie = np.copy(GrilleSudoku)
    afficher_grille(GrilleSudoku)
    GrilleCopie =vider_grille(GrilleCopie,30)
    afficher_grille(GrilleCopie)
    liste =remplir_liste_solution()
    afficheGrillePosition(cadregrillesimple, 9, 9,data,GrilleCopie )
    checksimple.pack()
    backsimple.pack()
   
def RetourSimple ():
    global GrilleSudoku, GrilleCopie,liste, data
    GrilleSudoku = np.zeros((9, 9), dtype=int)
    GrilleCopie = np.zeros((9, 9), dtype=int)
    liste = []
    data = []
    cadregrillesimple.pack_forget()
    checksimple.pack_forget()
    backsimple.pack_forget()
    grillecouleurEN.pack_forget()
    grillecouleurFR.pack_forget()
    grilleFRD.pack_forget()
    grilleFRF.pack_forget()
    titre.pack()
    sous_titre.pack()
    bouton_play.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    bouton_credit.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    cadreLangues.pack(expand=YES)

def RetourColor() :
    global GrilleSudoku, GrilleCopie,liste, data
    GrilleSudoku = np.zeros((9, 9), dtype=int)
    GrilleCopie = np.zeros((9, 9), dtype=int)
    liste = []
    data = []
    cadregrillesimple.pack_forget()
    checkcolor.pack_forget()
    backcolor.pack_forget()
    titre.pack()
    sous_titre.pack()
    bouton_play.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    bouton_credit.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    cadreLangues.pack(expand=YES)
        
def RetourSolution():
    global GrilleSudoku, GrilleCopie,liste, data
    GrilleSudoku = np.zeros((9, 9), dtype=int)
    GrilleCopie = np.zeros((9, 9), dtype=int)
    liste = []
    data = []
    cadregrillesimple.pack_forget()
    solution.pack_forget()
    backsolution.pack_forget()
    titre.pack()
    sous_titre.pack()
    bouton_play.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    bouton_credit.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    cadreLangues.pack(expand=YES)

def RetourDiagonal ():
    global GrilleSudoku, GrilleCopie,liste, data
    GrilleSudoku = np.zeros((9, 9), dtype=int)
    GrilleCopie = np.zeros((9, 9), dtype=int)
    liste = []
    data = []
    cadregrillesimple.pack_forget()
    checksimple.pack_forget()
    backsimple.pack_forget()
    titre.pack()
    sous_titre.pack()
    bouton_play.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    bouton_credit.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    cadreLangues.pack(expand=YES)

def RetourCreditFR ():
    cadrecreditFR.pack_forget()
    backcreditFR.pack_forget()
    titre.pack()
    sous_titre.pack()
    bouton_play.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    bouton_credit.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    cadreLangues.pack(expand=YES)

def RetourCreditEN ():
    cadrecreditEN.pack_forget()
    backcreditEN.pack_forget()
    titre.pack()
    sous_titre.pack()
    bouton_play.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    bouton_credit.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
    cadreLangues.pack(expand=YES)  
        
def Solution():
    global data
    GrilleSudoku = np.zeros((9, 9), dtype=int)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (data[i][j].get()!='') :
                GrilleSudoku[i][j] =int(data[i][j].get())
    print('la solution est :\n')
    remplir_grille(GrilleSudoku)
    afficher_grille(GrilleSudoku)
    
fenetre = Tk() 
fenetre.title("Jeux sur grille")
fenetre.geometry("720x520")
fenetre.config(background='white')
cadreLangues = Frame(fenetre, bg='black')
cadreLangues.pack(expand=YES)
titre = Label(cadreLangues, text="Bienvenue ", font=("Courrier", 50), bg='black',fg='white')
titre.pack()
sous_titre = Label(cadreLangues, text="SUDOKU \n Veuillez choisir votre langue", font=("Courrier  ", 25), bg='black',fg='white')
sous_titre.pack()
bouton_play = Button(cadreLangues, text="Fran??ais", font=("Courrier", 25), bg='white', fg='black',command=MenuFR )
bouton_play.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
bouton_credit = Button(cadreLangues, text="English", font=("Courrier", 25), bg='WHITE', fg='black',command=MenuEN )
bouton_credit.pack(ipadx= 1,ipady = 1,padx=2,pady=2, fill=X)
#=======================================================================
cadreMenuFR = Frame(fenetre, bg='white')
bouton_playFR = Button(cadreMenuFR, text="JOUER", font=("Courrier", 25), bg='black', fg='white',width=20,command=playFR )
bouton_creditFR = Button(cadreMenuFR, text="CREDIT", font=("Courrier", 25), bg='black', fg='white',width=20,command=creditFR )
#==================================================================================================================================
cadreMenuEN = Frame(fenetre, bg='white')
bouton_playEN = Button(cadreMenuEN, text="PLAY", font=("Courrier", 25), bg='black', fg='white',width=20,command=playEN )
bouton_creditEN = Button(cadreMenuEN, text="CREDIT", font=("Courrier", 25), bg='black', fg='white',width=20,command=creditEN )
#==================================================================================================================================
cadreplayFR = Frame(fenetre, bg='white')
grilleFR = Button(cadreplayFR, text="generer une grille simple", font=("Courrier", 25), bg='black', fg='white',width=20,command=grillesimple )
grilleFRF = Button(cadreplayFR, text="Facile", font=("Courrier", 25), bg='black', fg='white',width=20,command=grillesimpleF )
grilleFRD = Button(cadreplayFR, text="Difficile", font=("Courrier", 25), bg='black', fg='white',width=20,command=grillesimpleD )
grillepaireFR = Button(cadreplayFR, text="generer une grille pair\impair", font=("Courrier", 22), bg='black', fg='white',width=20,command=grillesimplecolore )
grille3FR = Button(cadreplayFR, text="generer une grille triple", font=("Courrier", 25), bg='black', fg='white',width=20,command=grilletriple)
grillediagonalFR = Button(cadreplayFR, text="generer une grille diagonal", font=("Courrier", 25), bg='black', fg='white',width=20,command=grillediagonal )
grillepositionFR = Button(cadreplayFR, text="generer une grille position", font=("Courrier", 25), bg='black', fg='white',width=20,command=grilleposition )
solutionFR = Button(cadreplayFR, text="trouver une solution", font=("Courrier", 25), bg='black', fg='white',width=20,command=solutiongrille )

#==================================================================================================================================
cadrecreditFR = Frame(fenetre, bg='white')
textFR= Label(cadrecreditFR, text="Ce g??n??rateur de grilles de sudoku est un projet de fin de licence r??alis?? par Akim SAADI, Guillaume NGUYEN THI, ", font=("Courrier", 8), bg='white', fg='black')
textFR1= Label(cadrecreditFR, text=" Lucas ARCAS, Yaniss KHELIFI-AHMED et Zakari IKHOU, dans le cadre du projet Maths Info, avec pour professeur r??f??rent", font=("Courrier", 8), bg='white', fg='black')
textFR2= Label(cadrecreditFR, text=" Mr Benjamin MONMEGE. Nous avons utilis?? toutes les comp??tences acquises lors de notre licence, c???est pourquoi l???aboutissement d???un tel projet", font=("Courrier", 8), bg='white', fg='black')
textFR3= Label(cadrecreditFR, text=" vient cl??turer notre licence en beaut??. Nous avons pris conscience de l???acquisition de nos savoirs,et nous avons pu les renforcer.", font=("Courrier", 8), bg='white', fg='black')
textFR4= Label(cadrecreditFR, text="", font=("Courrier", 8), bg='white', fg='black')
textFR5= Label(cadrecreditFR, text="Ce projet a requis nos connaissances en informatique mais ??galement en math??matiques, ce qui nous a permis de voir le lien entre les deux  ", font=("Courrier", 8), bg='white', fg='black')
textFR6= Label(cadrecreditFR, text="disciplines. Nous avons travaill?? en groupe sur une longue dur??e, et une grande partie a ??t?? r??alis??e ?? distance, d?? au confinement instaur?? ?? la suite ", font=("Courrier", 8), bg='white', fg='black')
textFR7= Label(cadrecreditFR, text="de l?????pid??mie du Covid-19. Cette exp??rience fut tr??s enrichissante ; la communication et l???organisation du travail ??taient ", font=("Courrier", 8), bg='white', fg='black')
textFR8= Label(cadrecreditFR, text="primordiales. Nous ??tions tous ?? l?????coute et trouvions des solutions aux probl??mes ensembles. Nous avons certes", font=("Courrier", 8), bg='white', fg='black')
textFR9= Label(cadrecreditFR, text="beaucoup appris en informatique, mais ??galement sur le plan social et le bon fonctionnement du travail d?????quipe. ", font=("Courrier", 8), bg='white', fg='black')
textFR10= Label(cadrecreditFR, text="", font=("Courrier", 8), bg='white', fg='black')
textFR11= Label(cadrecreditFR, text="Ce projet fut plaisant ?? r??aliser, et nous esp??rons qu???il vous sera utile. ", font=("Courrier", 8), bg='white', fg='black')
textFR12= Label(cadrecreditFR, text="", font=("Courrier", 8), bg='white', fg='black')
textFR13= Label(cadrecreditFR, text="Merci d???avoir lu. Voici une surprise, une grille cach??e uniquement accessible ici.", font=("Courrier", 8), bg='white', fg='black')
grillecouleurFR = Button(cadrecreditFR, text="Grille Couleur", font=("Courrier", 15), bg='black', fg='white',width=15,command=grillecouleur )
backcreditFR = Button(text='Retour')
backcreditFR.config(command=RetourCreditFR)
#==================================================================================================================================
cadreplayEN = Frame(fenetre, bg='white')
grilleEN = Button(cadreplayEN, text="generate a simple grid", font=("Courrier", 25), bg='black', fg='white',width=20,command=grillesimple )
grillepaireEN = Button(cadreplayEN, text="generate a colored-pair grid", font=("Courrier", 25), bg='black', fg='white',width=20,command=grillesimplecolore )
grille3EN = Button(cadreplayEN, text="generate a triple grid", font=("Courrier", 25), bg='black', fg='white',width=20,command=grilletriple )
grillediagonalEN = Button(cadreplayEN, text="generate a diagonal grid", font=("Courrier", 25), bg='black', fg='white',width=20,command=grillediagonal )
grillepositionEN = Button(cadreplayEN, text="generate a position grid", font=("Courrier", 25), bg='black', fg='white',width=20,command=grilleposition )
solutionEN = Button(cadreplayEN, text="find a solution", font=("Courrier", 25), bg='black', fg='white',width=20,command=solutiongrille )
#==================================================================================================================================
cadrecreditEN = Frame(fenetre, bg='white')
textEN= Label(cadrecreditEN, text="", font=("Courrier", 15), bg='white', fg='black')
textEN1= Label(cadrecreditEN, text="This sudoku grid generator is an end of term project made by Akim SAADI, Guillaume NGUYEN THI, Lucas ARCAS,", font=("Courrier", 8), bg='white', fg='black')
textEN2= Label(cadrecreditEN, text=" Yaniss KHELIFI-AHMED et Zakari IKHOU, as part of the ???Math-Info??? discipline with Mr. Benjamin MONMEGE as our referent teacher. ", font=("Courrier", 8), bg='white', fg='black')
textEN3= Label(cadrecreditEN, text="We had to use all the skills earned during our formation, it???s why the completion of this project wonderfully end our degree.", font=("Courrier", 8), bg='white', fg='black')
textEN4= Label(cadrecreditEN, text="It made us aware about the knowledge gained and strengthen them.", font=("Courrier", 8), bg='white', fg='black')
textEN5= Label(cadrecreditEN, text="", font=("Courrier", 8), bg='white', fg='black')
textEN6= Label(cadrecreditEN, text="This project has needed both our expertise in It and mathematics, and help us see the correlation between the two disciplines.", font=("Courrier", 8), bg='white', fg='black')
textEN7= Label(cadrecreditEN, text="We work as a team on a long period, unfortunately for big portion in telework because of the quarantine caused by the Covid-19 pandemic,", font=("Courrier", 8), bg='white', fg='black')
textEN8= Label(cadrecreditEN, text=" nonetheless it as been a good experience as it has made us learn how the world of work is. It has been a rich experience for everyone.", font=("Courrier", 8), bg='white', fg='black')
textEN9= Label(cadrecreditEN, text=" The communication was essential and worked very well, we were attentive with each other problems and found solutions together as a team.", font=("Courrier", 8), bg='white', fg='black')
textEN10= Label(cadrecreditEN, text=" We may have learn a lot about programming but not more than what we learned about teamwork and social interaction.", font=("Courrier", 8), bg='white', fg='black')
textEN11= Label(cadrecreditEN, text="", font=("Courrier", 8), bg='white', fg='black')
textEN12= Label(cadrecreditEN, text="We pleasantly made this project and hope it will be useful for you.", font=("Courrier", 8), bg='white', fg='black')
textEN13= Label(cadrecreditEN, text="", font=("Courrier", 8), bg='white', fg='black')
textEN14= Label(cadrecreditEN, text="As to thank you for your reading we made you a small surprise, a hidden special grid only available here :", font=("Courrier", 8), bg='white', fg='black')
grillecouleurEN = Button(cadrecreditEN, text="Grille Couleur", font=("Courrier", 15), bg='black', fg='white',width=15,command=grillecouleur )
backcreditEN = Button(text='Back')
backcreditEN.config(command=RetourCreditEN)
#==================================================================================================================================
cadregrillesimple = Frame(fenetre, bg='black')
checksimple = Button(text='check', command=Corection)
solution = Button(text="solution", font=("Courrier", 25), bg='black', fg='white',width=20,command=Solution)
backsimple = Button(text='Retour')
backcolor = Button(text='Retour')
backdiagonal = Button(text='Retour')
backsolution = Button(text='Retour')
checkcolor = Button(text='check')
checkdiagonal = Button(text='check')
backsimple.config(command=RetourSimple)
backcolor.config(command=RetourColor)
backdiagonal.config(command=RetourDiagonal)
backsolution.config(command=RetourSolution)
checkcolor.config(command=Corection)
checkdiagonal.config(command=Corection)
#==================================================================================================================================
fenetre.mainloop()