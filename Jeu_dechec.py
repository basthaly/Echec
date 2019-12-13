#Jeu d'échec

import marshal
from Echec_def import *

#systeme de pion :

    #Aucun pion=-1
    #Pion=0
    #Tour=1
    #Cavalier=2
    #Fou=3
    #Dame=4
    #Roi=5

#Couleur :

    #Aucune:-1
    #Blanc:0
    #Noir:1

def Tr(a):
    list=["A","B","C","D","E","F","G","H"]
    a=a.upper()
    for i in range (8):
        if list[i]==a[0]:
            b=i
            break
    return b

class Jeu_dechec:
    def __init__(self):
        self.mess=message()
        self.echiquier=[]
        self.fausse=[]
        self.tour=0 #Compte les tours
        self.act=False #Permet de savoir si un pion a était déplacé
        self.noir_echec=0
        self.blanc_echec=0

        for i in range (8):
            J=[]
            for j in range(8):
                J.append((-1,-1))
            self.echiquier.append(J)

        #Mise en place des pion noir
        self.echiquier[0][0]=(1,1) #Tour
        self.echiquier[1][0]=(2,1) #Cavalier
        self.echiquier[2][0]=(3,1) #Fou
        self.echiquier[3][0]=(4,1) #Dame
        self.echiquier[4][0]=(5,1) #Roi
        self.echiquier[5][0]=(3,1) #Fou
        self.echiquier[6][0]=(2,1) #Cavalier
        self.echiquier[7][0]=(1,1) #Tour
        for i in range (8):
            self.echiquier[i][1]=(0,1) #pion

        #Mise en place des pion blanc
        self.echiquier[0][7]=(1,0)
        self.echiquier[1][7]=(2,0)
        self.echiquier[2][7]=(3,0)
        self.echiquier[3][7]=(4,0)
        self.echiquier[4][7]=(5,0)
        self.echiquier[5][7]=(3,0)
        self.echiquier[6][7]=(2,0)
        self.echiquier[7][7]=(1,0)
        for i in range(8):
            self.echiquier[i][6]=(0,0)

    def __str__(self):
        a=str(self.echiquier)
        return a

    def piece(self,a):
        piece=["pion","Tour","Cavalier","Fou","Dame","Roi"]
        couleur=["Blanc","Noir"]
        b=Tr(a)
        try:
            pion=self.echiquier[b][int(a[1])-1]
            if pion[0] == -1:
                result="Aucun pion"
            else:
                result=(piece[pion[0]]+" "+couleur[pion[1]])
        except:
            result="Case hors-jeu"
        return str(result)

    def change(self,x1,x2,ya,yb):
        self.save()
        self.tour+=1
        self.deplacement=True
        if self.echiquier[x2][yb][0]!=-1:
            self.fausse.append(self.echiquier[x2][yb])
        self.echiquier[x2][yb]=self.echiquier[x1][ya]
        self.echiquier[x1][ya]=(-1,-1)
        self.act=True
        print(self.tour)

    def retour(self,file=None):
        if self.tour>0:
            self.tour-=1
            compt1=0
            compt2=0
            for i in range (8):
                for j in range(8):
                    if self.echiquier[i][j][1]!=-1:
                        compt1+=1
            self.echiquier=marshal.load(open("save/sauvegarde"+str(self.tour)+".txt", "rb"))
            for i in range (8):
                for j in range(8):
                    if self.echiquier[i][j][1]!=-1:
                        compt2+=1
            if compt2!=compt1:
                del self.fausse[len(self.fausse)-1]
            if file==True:
                self.Try_Echec()

    def save(self):
        marshal.dump(self.echiquier,open("save/sauvegarde"+str(self.tour)+".txt", "wb")) # Argh j'ai tout écrasé !

    def action(self,a,b):
        self.act=False
        self.deplacement=False
        act_tour=0
        try:
            t=self.tour%2
            x1=Tr(a)
            x2=Tr(b)
            ya=int(a[1])-1
            yb=int(b[1])-1
            if self.echiquier[x2][yb][0]==5:
                self.mess.roi=1
        except:
            act=True
            self.mess.erreur=1
            return

        #Met en place le systeme de tour
        if t==0 and self.echiquier[x1][ya][1]==0:
            act_tour=1
        elif t==1 and self.echiquier[x1][ya][1]==1:
            act_tour=1
        elif self.echiquier[x1][ya][1]==0:
            self.mess.tour_b=1
        elif self.echiquier[x1][ya][1]==1:
            self.mess.tour_n=1

        if self.echiquier[x2][yb][0]!=5 and act_tour!=0:
            try: # Prevois le hors plateau

                #Pion noir
                if self.echiquier[x1][ya][0]==0 and x1==x2 and self.echiquier[x1][ya][1]==1 :
                    if self.echiquier[x1][ya+1][0]==-1:
                        if yb==ya+1:
                            self.change(x1,x2,ya,yb)
                            if yb==7:
                                self.echiquier[x2][yb]=(4,1)

                        elif self.echiquier[x1][ya+2][0]==-1 and ya==yb-2 and ya==1:
                            self.change(x1,x2,ya,yb)

                        else:
                            self.mess.pion=1
                            self.act=True

                #Pion Blanc
                elif self.echiquier[x1][ya][0]==0 and x1==x2 and self.echiquier[x1][ya][1]==0 :
                    if self.echiquier[x1][ya-1][0]==-1:
                        if yb==ya-1:
                            self.change(x1,x2,ya,yb)
                            if yb==0:
                                self.echiquier[x2][yb]=(4,0)

                        elif self.echiquier[x1][ya-2][0]==-1 and ya==yb+2 and ya==6:
                            self.change(x1,x2,ya,yb)
                        else:
                            self.mess.pion=1
                            self.act=True

                #Pion Qui mange
                elif self.echiquier[x1][ya][0]==0 :
                     if self.echiquier[x2][yb][0]!=-1 and self.echiquier[x1][ya][1]!=self.echiquier[x2][yb][1]:
                        if ya-1==yb or ya+1==yb:
                            if x1-1==x2 or x1+1==x2:
                                self.change(x1,x2,ya,yb)
                                if yb==0:
                                    self.echiquier[x2][yb]=(4,0)
                                elif yb==7:
                                    self.echiquier[x2][yb]=(4,1)


                #tour
                elif self.echiquier[x1][ya][0]==1 or self.echiquier[x1][ya][0]==4:
                    if x1==x2:
                        if ya>yb:
                            for i in range(1,ya-yb+1):
                                if self.echiquier[x1][ya-i][0]==-1 and i!=ya-yb:
                                    pass
                                elif i==ya-yb and self.echiquier[x1][ya][1]!=self.echiquier[x1][yb][1]:
                                    self.change(x1,x2,ya,yb)
                                else:
                                    self.mess.bloquage=1
                                    self.act=True
                                    break
                        else:
                            for i in range(1,yb-ya+1):
                                if self.echiquier[x1][ya+i][0]==-1 and i!=yb-ya:
                                    pass
                                elif i==yb-ya and self.echiquier[x1][ya][1]!=self.echiquier[x1][yb][1]:
                                    self.change(x1,x2,ya,yb)
                                else:
                                    self.mess.bloquage=1
                                    self.act=True
                                    break

                    elif ya==yb:
                        if x1>x2:
                            for i in range(1,x1-x2+1):
                                if self.echiquier[x1-i][ya][0]==-1 and i!=x1-x2:
                                    pass
                                elif i==x1-x2 and self.echiquier[x1][ya][1]!=self.echiquier[x2][yb][1]:
                                    self.change(x1,x2,ya,yb)
                                else:
                                    self.mess.bloquage=1
                                    self.act=True
                                    break
                        else:
                            for i in range(1,x2-x1+1):
                                if self.echiquier[x1+i][ya][0]==-1 and i!=x2-x1:
                                    pass
                                elif i==x2-x1 and self.echiquier[x1][ya][1]!=self.echiquier[x2][yb][1]:
                                    self.change(x1,x2,ya,yb)
                                else:
                                    self.mess.bloquage=1
                                    self.act=True
                                    break

                #Cavalier:
                elif self.echiquier[x1][ya][0]==2:
                    self.act=True
                    if (x2==x1+2 and yb==ya+1)\
                    or (x2==x1+1 and yb==ya+2)\
                    or (x2==x1+2 and yb==ya-1)\
                    or (x2==x1+1 and yb==ya-2)\
                    or (x2==x1-2 and yb==ya+1)\
                    or (x2==x1-1 and yb==ya+2)\
                    or (x2==x1-2 and yb==ya-1)\
                    or (x2==x1-1 and yb==ya-2):
                        if self.echiquier[x1][ya][1]!=self.echiquier[x2][yb][1]:
                            self.change(x1,x2,ya,yb)
                        else:
                            self.mess.cavalier_allier=1
                    else:
                        self.mess.cavalier_erreur=1

                #Fou:
                if self.echiquier[x1][ya][0]==3 or self.echiquier[x1][ya][0]==4:
                    if x1<x2 and ya<yb:
                        for i in range(1,x2-x1+1):
                            if self.echiquier[x1+i][ya+i][0]==-1 and i!=x2-x1 and i!=yb-ya:
                                pass
                            elif i==x2-x1 and i==yb-ya and self.echiquier[x1][ya][1]!=self.echiquier[x2][yb][1]:
                                self.change(x1,x2,ya,yb)
                            else:
                                if x2-x1==yb-ya:
                                    self.mess.bloquage=1
                                    self.act=True
                                    break
                                else:
                                    break

                    elif x1>x2 and ya<yb:
                        for i in range(1,x1-x2+1):
                            if self.echiquier[x1-i][ya+i][0]==-1 and i!=x1-x2 and i!=yb-ya:
                                pass
                            elif i==x1-x2 and i==yb-ya and self.echiquier[x1][ya][1]!=self.echiquier[x2][yb][1]:
                                self.change(x1,x2,ya,yb)
                            else:
                                if x1-x2==yb-ya:
                                    self.mess.bloquage=1
                                    self.act=True
                                    break
                                else:
                                    break

                    elif x1>x2 and ya>yb:
                        for i in range(1,x1-x2+1):
                            if self.echiquier[x1-i][ya-i][0]==-1 and i!=x1-x2 and i!=ya-yb:
                                pass
                            elif i==x1-x2 and i==ya-yb and self.echiquier[x1][ya][1]!=self.echiquier[x2][yb][1]:
                                self.change(x1,x2,ya,yb)
                            else:
                                if x1-x2==ya-yb:
                                    self.mess.bloquage=1
                                    self.act=True
                                    break
                                else:
                                    break

                    elif x1<x2 and ya>yb:
                        for i in range(1,x2-x1+1):
                            if self.echiquier[x1+i][ya-i][0]==-1 and i!=x2-x1 and i!=ya-yb:
                                pass
                            elif i==x2-x1 and i==ya-yb and self.echiquier[x1][ya][1]!=self.echiquier[x2][yb][1]:
                                self.change(x1,x2,ya,yb)
                            else:
                                if x2-x1==ya-yb:
                                    self.mess.bloquage=1
                                    self.act=True
                                    break
                                else:
                                    break
                    else:
                        if self.echiquier[x1][ya][0]==3:
                            self.mess.fou_tour=1
                        self.act=True

                #Roi
                elif self.echiquier[x1][ya][0]==5:
                    if self.echiquier[x2][yb][1]==self.echiquier[x1][ya][1]:
                        pass
                    elif x1-1==x2 or x1+1==x2 or x1==x2:
                        if ya+1==yb or ya-1==yb or ya==yb:
                            self.change(x1,x2,ya,yb)
                if self.act==False:
                    self.act=True
                    self.mess.coord=1

            except:
                if self.act==False:
                    self.act=True
                    self.mess.hors_plateau=1


    def Roi_echec(self,couleur):
        if couleur==0:
            self.blanc_echec+=1
            if self.tour%2==1:
                self.retour()
                self.mess.echec=1
                self.blanc_echec=0
            elif self.blanc_echec==2:#Prevois les mouvement impossible si le roi est déja en echec
                self.retour()
                self.mess.impossible=1
                self.blanc_echec=1
            else:
                print("Roi blanc en echec")

        else:
            self.noir_echec+=1
            if self.tour%2==0:
                self.retour()
                self.mess.echec=1
                self.noir_echec=0
            if self.noir_echec==2 : #Prevois les mouvement impossible si le roi est déja en echec
                self.retour()
                self.mess.impossible=1
                self.noir_echec=1
            else:
                print("Roi noir en echec")

    def Try_Echec(self):
        noir=0
        blanc=0
        for x in range (8):
            for y in range (8):
                if self.echiquier[x][y][0]==5:
                    coul=self.echiquier[x][y][1]
                    if coul==0 and blanc==0:    #Permet de ne pas vérifier 2 fois la position
                        blanc=1                 # du roi en cas de mouvement impossible
                        calcul=True
                    elif coul==1 and noir==0:    #Permet de ne pas vérifier 2 fois la position
                        noir=1                  # du roi en cas de mouvement impossible
                        calcul=True
                    else:
                        calcul=False

                    v=0
                    while calcul==True: #Calcul vers le bas
                        try:
                            v+=1
                            if self.echiquier[x][y+v][0]==5 and v==1: # Calcul du Roi
                                self.Roi_echec(coul)
                                calcul=False
                            elif self.echiquier[x][y+v][0]!=-1:
                                if self.echiquier[x][y][1]!=self.echiquier[x][y+v][1]:
                                    if self.echiquier[x][y+v][0]==1 or self.echiquier[x][y+v][0]==4:
                                        self.Roi_echec(coul)
                                        calcul=False
                                    else:
                                        v=0
                                        break
                                else:
                                    v=0
                                    break
                        except:
                            v=0
                            break

                    while calcul==True: #Calcul vers le haut
                        try:
                            v+=1
                            if self.echiquier[x][y-v][0]!=-1: # Calcul du Roi
                                if y-v<0:
                                    v=0
                                    break
                                elif self.echiquier[x][y-v][0]==5 and v==1:
                                    self.Roi_echec(coul)
                                    calcul=False

                                elif self.echiquier[x][y][1]!=self.echiquier[x][y-v][1]:
                                    if self.echiquier[x][y-v][0]==1 or self.echiquier[x][y-v][0]==4:
                                        self.Roi_echec(coul)
                                        calcul=False
                                    else:
                                        v=0
                                        break
                                else:
                                    v=0
                                    break

                        except:
                            v=0
                            break

                    while calcul==True:  # Calcul vers la gauche
                        try:
                            v+=1
                            if self.echiquier[x-v][y][0]!=-1 : # Calcul du Roi
                                if x-v<0:
                                    v=0
                                    break
                                if self.echiquier[x-v][y][0]==5 and v==1:
                                    self.Roi_echec(coul)
                                    calcul=False

                                elif self.echiquier[x][y][1]!=self.echiquier[x-v][y][1]:
                                    if self.echiquier[x-v][y][0]==1 or self.echiquier[x-v][y][0]==4:
                                        self.Roi_echec(coul)
                                        calcul=False
                                    else:
                                        v=0
                                        break
                                else:
                                    v=0
                                    break
                        except:
                            v=0
                            break

                    while calcul==True: # Calcul vers la droite
                        try:
                            v+=1
                            if self.echiquier[x+v][y][0]==5 and v==1: # Calcul du Roi
                                self.Roi_echec(coul)
                                calcul=False
                            elif self.echiquier[x+v][y][0]!=-1:
                                if self.echiquier[x][y][1]!=self.echiquier[x+v][y][1]:
                                    if self.echiquier[x+v][y][0]==1 or self.echiquier[x+v][y][0]==4:
                                        self.Roi_echec(coul)
                                        calcul=False
                                    else:
                                        v=0
                                        break
                                else:
                                    v=0
                                    break
                        except:
                            v=0
                            break

                    while calcul==True: # Calcul diagonal en haut à gauche
                        try:
                            v+=1
                            if self.echiquier[x-v][y-v][0]!=-1:
                                if x-v<0  or y-v<0:
                                    v=0
                                    break
                                if self.echiquier[x-v][y-v][0]==5 and v==1: # Calcul du Roi
                                    self.Roi_echec(coul)
                                    calcul=False

                                elif self.echiquier[x][y][1]!=self.echiquier[x-v][y-v][1]:
                                    if self.echiquier[x-v][y-v][0]==3 or self.echiquier[x-v][y-v][0]==4:
                                        self.Roi_echec(coul)
                                        calcul=False
                                    else:
                                        v=0
                                        break
                                else:
                                    v=0
                                    break
                        except:
                            v=0
                            break

                    while calcul==True: # Calcul diagonal en haut à droite
                        try:
                            v+=1
                            if self.echiquier[x+v][y-v][0]!=-1:
                                if y-v<0:
                                    v=0
                                    break
                                if self.echiquier[x+v][y-v][0]==5 and v==1: # Calcul du Roi
                                    self.Roi_echec(coul)
                                    calcul=False

                                elif self.echiquier[x][y][1]!=self.echiquier[x+v][y-v][1]:
                                    if self.echiquier[x+v][y-v][0]==3 or self.echiquier[x+v][y-v][0]==4:
                                        self.Roi_echec(coul)
                                        calcul=False
                                    else:
                                        v=0
                                        break
                                else:
                                    v=0
                                    break
                        except:
                            v=0
                            break

                    while calcul==True: # Calcul diagonal en bas à gauche
                        try:
                            v+=1
                            if self.echiquier[x-v][y+v][0]!=-1:
                                if x-v<0:
                                    v=0
                                    break
                                if self.echiquier[x-v][y+v][0]==5 and v==1: # Calcul du Roi
                                    self.Roi_echec(coul)
                                    calcul=False

                                elif self.echiquier[x][y][1]!=self.echiquier[x-v][y+v][1]:
                                    if self.echiquier[x-v][y+v][0]==3 or self.echiquier[x-v][y+v][0]==4:
                                        self.Roi_echec(coul)
                                        calcul=False
                                    else:
                                        v=0
                                        break
                                else:
                                    v=0
                                    break
                        except:
                            v=0
                            break

                    while calcul==True: # Calcul diagonal en bas à droite
                        try:
                            v+=1
                            if self.echiquier[x+v][y+v][0]==5 and v==1: # Calcul du Roi
                                self.Roi_echec(coul)
                                calcul=False
                            elif self.echiquier[x+v][y+v][0]!=-1:
                                if self.echiquier[x][y][1]!=self.echiquier[x+v][y+v][1]:
                                    if self.echiquier[x+v][y+v][0]==3 or self.echiquier[x+v][y+v][0]==4:
                                        self.Roi_echec(coul)
                                        calcul=False
                                    else:
                                        v=0
                                        break
                                else:
                                    v=0
                                    break
                        except:
                            v=0
                            break

                    if calcul==True: # Calcul avec les Pions
                        if self.echiquier[x][y][1]==1:  # Roi noir
                            try:
                                if self.echiquier[x-1][y+1][0]==0 and self.echiquier[x-1][y+1][1]==0:
                                    self.Roi_echec(coul)
                                    calcul=False
                                elif self.echiquier[x+1][y+1][0]==0 and self.echiquier[x+1][y+1][1]==0:
                                    self.Roi_echec(coul)
                                    calcul=False
                            except:
                                break
                        else:                           # Roi blanc
                            try:
                                if self.echiquier[x-1][y-1][0]==0 and self.echiquier[x-1][y-1][1]==1:
                                    self.Roi_echec(coul)
                                    calcul=False
                                elif self.echiquier[x+1][y-1][0]==0 and self.echiquier[x+1][y-1][1]==1:
                                    self.Roi_echec(coul)
                                    calcul=False
                            except:
                                break

                    while calcul==True: # Calcul avec les cavaliers
                        try:
                            if self.echiquier[x+1][y-2][0]==2 and self.echiquier[x][y][1]!=self.echiquier[x+1][y-2][1]: #1D,2H
                                if y-2>=0:
                                    self.Roi_echec(coul)
                                    calcul=False
                                    break
                        except:
                            break

                        try:
                            if self.echiquier[x+2][y-1][0]==2 and self.echiquier[x][y][1]!=self.echiquier[x+2][y-1][1]: #2D,1H
                                if y-1>=0:
                                    self.Roi_echec(coul)
                                    calcul=False
                                    break
                        except:
                            break

                        try:
                            if self.echiquier[x-2][y-1][0]==2 and self.echiquier[x][y][1]!=self.echiquier[x-2][y-1][1]: #2G,1H
                                if x-2>=0 and y-1>=0:
                                    self.Roi_echec(coul)
                                    calcul=False
                                    break
                        except:
                            break

                        try:
                            if self.echiquier[x-1][y-2][0]==2 and self.echiquier[x][y][1]!=self.echiquier[x-1][y-2][1]: #1G,2H
                                if x-1>=0 and y-2>=0:
                                    self.Roi_echec(coul)
                                    calcul=False
                                    break
                        except:
                            break

                        try:
                            if self.echiquier[x-2][y+1][0]==2 and self.echiquier[x][y][1]!=self.echiquier[x-2][y+1][1]: #2G,2B
                                if x-2>=0:
                                    self.Roi_echec(coul)
                                    calcul=False
                                    break
                        except:
                            break

                        try:
                            if self.echiquier[x-1][y+2][0]==2 and self.echiquier[x][y][1]!=self.echiquier[x-1][y+2][1]: #1G,2B
                                if x-1>=0:
                                    self.Roi_echec(coul)
                                    calcul=False
                                    break
                        except:
                            break

                        try:
                            if self.echiquier[x+2][y+1][0]==2 and self.echiquier[x][y][1]!=self.echiquier[x+2][y+1][1]: # 2D,1B
                                self.Roi_echec(coul)
                        except:
                            break

                        try:
                            if self.echiquier[x+1][y+2][0]==2 and self.echiquier[x][y][1]!=self.echiquier[x+1][y+2][1]: #1D,2B
                                self.Roi_echec(coul)
                        except:
                            break
                        break
                    if calcul==True:
                        if self.echiquier[x][y][1]==0:
                            self.blanc_echec=0
                        else:
                            self.noir_echec=0

