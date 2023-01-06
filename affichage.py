from tkinter import Label, W, Button, Entry
from verification import trouveligne

def afficher_grille(grille) :
    for i in range (len(grille[:,0])) :
        if i % 3 == 0:
            print('―――――――――――――――――――――――――')
        for j in range (len(grille[0,:])) :
            if j % 3 == 0 :
                print("|", end=" ")
            if j != 8 :
                print(grille[i][j],end=" ")
            else :
              print(grille[i][j],end=' | \n')
    print('―――――――――――――――――――――――――')
    
def afficher_triple_grille(grille) :
    for i in range(len(grille)) :
        if i == 0 :
           print('―――――――――――――――――――――――――')
        if i == 3 :
           print('―――――――――――――――――――――――――――――――――')
        if i == 6 :
           print('―――――――――――――――――――――――――――――――――――――――――')
        if i == 9 :
           print('――――――――――――――――――――――――――――――――――――――――――')
        if i == 12 :
           print('         ――――――――――――――――――――――――――――――――――')
        for j in range(len(grille[0])) :
            if grille[i][j] != 0 :
                if j % 3 == 0 :
                    print("|", end=" ")
                if j != 14 :
                    if (i<3 and j == 8 ) or (i<6 and j ==11) :
                        print(grille[i,j],end=' |')
                    else :
                        print(grille[i,j],end=" ")
                else :
                    print(grille[i,j],end=' |\n')
            else :
                if j != 14 :
                    print('  ',end=" ")
                else :
                    print(' ')
    print('                  ―――――――――――――――――――――――――')
    
def interface_graphique (grille,Fenetre) :
    k=0
    n=len(grille)
    for i in range (n) :
        l=0
        for j in range (n) :
            if (grille[i,j])==10 :
                case=Label(Fenetre, text="", bg='black')
                case.grid(row=i+k,column=j+l,sticky=W) 
            elif (grille[i,j])==0 :
                case=Entry(Fenetre, font=("Courrier",15), width=3,justify='center')
                case.grid(row=i+k,column=j+l,sticky=W)
            else :
                case=Button(Fenetre, text=grille[i,j], font=("Courrier",15) ,bg='white', width = 3)
                case.grid(row=i+k,column=j+l,sticky=W)            
            if (j%3 == 2 and j!=n-1):
                l+=1
                case=Label(Fenetre, text="", bg='black')
                case.grid(row=i+k,column=j+l,sticky=W)
                l+=1
        if(i%3==2  and i!=n-1):
            case=Label(Fenetre, text="",font=("Courrier",1), bg='black')
            case.grid(row=i+k+1,column=0,sticky=W,columnspan=14)
            k=k+1   

def couleurposition(i,j):
    if(i%3==0 and j%3==0):
        return '#FB8A8A'
    if(i%3==0 and j%3==1):
        return '#FBE38A'         
    if(i%3==0 and j%3==2):
        return '#A9FB8A'
    if(i%3==1 and j%3==0):
        return '#8AFBE0'
    if(i%3==1 and j%3==1):
        return '#8AA7FB'
    if(i%3==1 and j%3==2):
       return '#E133F9'
    if(i%3==2 and j%3==0):
        return '#FB80F0'
    if(i%3==2 and j%3==1):
        return '#F9463B'
    if(i%3==2 and j%3==2):
        return '#F5FC4E'
   
def afficheGrillePosition(cadre, height, width, data, grillecopie):
    numberLines = height
    numberColumns = width
    for i in range(numberLines):
        line = list()
        for j in range(numberColumns):
            k=j
            l=i
            if(j>2):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=0,column=3)
                k=j+1
            if(j>5):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=0,column=7)
                k=j+2
            if(i>2):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=3,column=0)
                l=i+1
            if(i>5):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=7,column=0)
                l=i+2
            if(grillecopie[i][j]==0):
                caseV = Entry(cadre,width=2,font=("Courrier",15),bg=couleurposition(i,j),justify='center')
                line.append(caseV)
                caseV.grid(row = l, column = k,padx=2,pady=2)           
            else :
                caseP = Label(cadre,text=grillecopie[i][j],font=("Courrier",15),bg=couleurposition(i,j),width=2)
                caseP.grid(row = l, column = k,padx=2,pady=2)
               
        data.append(line)
  
    
def couleur(i,j):
    if(trouveligne(i*9+j)==0):
        return '#FB8A8A'
    if(trouveligne(i*9+j)==1):
        return '#268607'        
    if(trouveligne(i*9+j)==2):
        return '#A9FB8A'
    if(trouveligne(i*9+j)==3):
        return '#8AFBE0'
    if(trouveligne(i*9+j)==4):
        return '#8AA7FB'
    if(trouveligne(i*9+j)==5):
       return '#E133F9'
    if(trouveligne(i*9+j)==6):
        return '#FB80F0'
    if(trouveligne(i*9+j)==7):
        return '#F9463B'
    if(trouveligne(i*9+j)==8):
        return '#F5FC4E'
    
def afficheGrilleCouleur(cadre,  height ,  width, data, grillecopie):
    data = list()
    numberLines = height
    numberColumns = width
    for i in range(numberLines):
        line = list()
        for j in range(numberColumns):
           
            if(grillecopie[i][j]==0):
                    caseV = Entry(cadre,width=2,font=("Courrier",15),bg=couleur(i,j),justify='center')
                    line.append(caseV)
                    caseV.grid(row = i, column = j,padx=2,pady=2)
                   
            else :
                    caseP = Label(cadre,bg=couleur(i,j),text=grillecopie[i][j],font=("Courrier",15),width=2)
                    caseP.grid(row = i, column = j,padx=2,pady=2)
                   
                   
        data.append(line)

def afficheGrillePaire(cadre, height, width, data, liste, grillesudoku, grillecopie): 
    numberLines = height 
    numberColumns = width 
    for i in range(numberLines): 
        line = list()
        for j in range(numberColumns): 
            k=j
            l=i
            if(j>2):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=0,column=3)
                k=j+1
            if(j>5):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=0,column=7)
                k=j+2
            if(i>2):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=3,column=0)
                l=i+1
            if(i>5):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=7,column=0)
                l=i+2
            if(grillecopie[i][j]==0):
                if(grillesudoku[i][j]%2==0):
                    caseV = Entry(cadre,width=2,font=("Courrier",15),bg='#E5E5E5',justify='center')
                    line.append(caseV)
                    caseV.grid(row = l, column = k,padx=2,pady=2)
                else:
                    caseV = Entry(cadre,width=2,font=("Courrier",15),justify='center')
                    line.append(caseV)
                    caseV.grid(row = l, column = k,padx=2,pady=2)
                                   
            else :
                if(grillesudoku[i][j]%2==0):
                    caseP = Label(cadre,text=grillecopie[i][j],font=("Courrier",15),bg='#E5E5E5',width=2)
                    caseP.grid(row = l, column = k,padx=2,pady=2)
                else:
                    caseP = Label(cadre,text=grillecopie[i][j],font=("Courrier",15),bg='white',width=2)
                    caseP.grid(row = l, column = k,padx=2,pady=2)
        data.append(line)

def afficheGrilleSimple(cadre,  height ,  width, data, grillecopie): 
    numberLines = height 
    numberColumns = width 
    for i in range(numberLines): 
        line = list()
        for j in range(numberColumns): 
            k=j
            l=i
            if(j>2):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=0,column=3)
                k=j+1
            if(j>5):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=0,column=7)
                k=j+2
            if(i>2):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=3,column=0)
                l=i+1
            if(i>5):
                Label(cadre, text="",font=("Courrier",5),bg='black').grid(row=7,column=0)
                l=i+2
            if(grillecopie[i][j]==0):
                caseV = Entry(cadre,width=2,bg='white',font=("Courrier",15),justify='center')
                line.append(caseV)
                caseV.grid(row = l, column = k,padx=2,pady=2)
                
            else :
                caseP = Label(cadre,bg='white',text=grillecopie[i][j],font=("Courrier",15),width=2)
                caseP.grid(row = l, column = k,padx=2,pady=2)
        data.append(line)


    