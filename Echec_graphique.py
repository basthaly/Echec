from tkinter import *
from random import *
from Jeu_dechec import *
from Echec_def import *
import marshal

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

#Définition

def back():
    file=True
    jeu.retour(file)
    placement()

def restart():
    global jeu
    jeu=Jeu_dechec()
    placement()

def avancement(event=0):
    test=StringVar("")
    a=action1.get()
    b=action2.get()
    jeu.action(a,b)
    action1.delete(0,len(a))
    action2.delete(0,len(b))
    placement()
    if jeu.deplacement==True:
        jeu.Try_Echec()
        placement()
    msg_erreur()

def dessin(i,j):
    if jeu.echiquier[i][j][1]==0:
        if jeu.echiquier[i][j][0]==0:
            echiquier.create_image(25+40*i,20+40*j,image=pb)
        elif jeu.echiquier[i][j][0]==1:
            echiquier.create_image(25+40*i,20+40*j,image=tb)
        elif jeu.echiquier[i][j][0]==2:
            echiquier.create_image(25+40*i,20+40*j,image=cb)
        elif jeu.echiquier[i][j][0]==3:
            echiquier.create_image(25+40*i,20+40*j,image=fb)
        elif jeu.echiquier[i][j][0]==4:
            echiquier.create_image(25+40*i,20+40*j,image=db)
        elif jeu.echiquier[i][j][0]==5:
            if jeu.blanc_echec==0:
                echiquier.create_image(25+40*i,20+40*j,image=rb)
            else:
                echiquier.create_image(25+40*i,20+40*j,image=rbr)
    elif jeu.echiquier[i][j][1]==1:
        if jeu.echiquier[i][j][0]==0:
            echiquier.create_image(25+40*i,20+40*j,image=pn)
        elif jeu.echiquier[i][j][0]==1:
            echiquier.create_image(25+40*i,20+40*j,image=tn)
        elif jeu.echiquier[i][j][0]==2:
            echiquier.create_image(25+40*i,20+40*j,image=cn)
        elif jeu.echiquier[i][j][0]==3:
            echiquier.create_image(25+40*i,20+40*j,image=fn)
        elif jeu.echiquier[i][j][0]==4:
            echiquier.create_image(25+40*i,20+40*j,image=dn)
        elif jeu.echiquier[i][j][0]==5:
            if jeu.noir_echec==0:
                echiquier.create_image(25+40*i,20+40*j,image=rn)
            else:
                echiquier.create_image(25+40*i,20+40*j,image=rnr)

def dessin_fausse(i,j,c):
    if jeu.fausse[c][1]==0:
        if jeu.fausse[c][0]==0:
            echiquier.create_image(360+40*i,20+40*j,image=pb)
        elif jeu.fausse[c][0]==1:
            echiquier.create_image(360+40*i,20+40*j,image=tb)
        elif jeu.fausse[c][0]==2:
            echiquier.create_image(360+40*i,20+40*j,image=cb)
        elif jeu.fausse[c][0]==3:
            echiquier.create_image(360+40*i,20+40*j,image=fb)
        elif jeu.fausse[c][0]==4:
            echiquier.create_image(360+40*i,20+40*j,image=db)
        elif jeu.fausse[c][0]==5:
            echiquier.create_image(360+40*i,20+40*j,image=rb)
    elif jeu.fausse[c][1]==1:
        if jeu.fausse[c][0]==0:
            echiquier.create_image(360+40*i,20+40*j,image=pn)
        elif jeu.fausse[c][0]==1:
            echiquier.create_image(360+40*i,20+40*j,image=tn)
        elif jeu.fausse[c][0]==2:
            echiquier.create_image(360+40*i,20+40*j,image=cn)
        elif jeu.fausse[c][0]==3:
            echiquier.create_image(360+40*i,20+40*j,image=fn)
        elif jeu.fausse[c][0]==4:
            echiquier.create_image(360+40*i,20+40*j,image=dn)
        elif jeu.fausse[c][0]==5:
            echiquier.create_image(360+40*i,20+40*j,image=rn)

def placement(event=0):
    echiquier.bind("<Button-1>",Clic_mouvement)
    echiquier.delete(ALL)
    echiquier.create_image(170,170, image=image)
    i=0
    for c in range(len(jeu.fausse)):
        j=c//4
        if i>=4:
            i=0
        dessin_fausse(i,j,c)
        i+=1

    for i in range (8):
        for j in range(8):
            if jeu.echiquier[i][j][0]!=-1 :
                dessin(i,j)

def Clic_mouvement(event=0):
    a=action1.get()
    b=action2.get()
    c=["A","B","C","D","E","F","G","H"]
    if a=='':
        action1.insert(0,(c[event.x//40]+str((event.y//40)+1)))
    else:
        action2.insert(0,(c[event.x//40]+str((event.y//40)+1)))
        avancement()

def aide(event=0):
    fen1.bind("<Any-KeyPress>",placement)
    echiquier.bind("<Button-1>",placement)
    echiquier._imag=imag=PhotoImage(file="Autre/aide.gif")
    echiquier.delete(ALL)
    echiquier.create_image(250,175,image=imag)

def apropos(event=0):
    fen1.bind("<Any-KeyPress>",placement)
    echiquier.bind("<Button-1>",placement)
    echiquier._imag=imag=PhotoImage(file="Autre/A_propos.gif")
    echiquier.delete(ALL)
    echiquier.create_image(250,175,image=imag)

def Pion(event=0):
    fen1.bind("<Any-KeyPress>",placement)
    echiquier.bind("<Button-1>",placement)
    echiquier._imag=imag=PhotoImage(file="Autre/Pion.gif")
    echiquier.delete(ALL)
    echiquier.create_image(250,175,image=imag)

def msg_erreur():
    pos3.config(background="grey")
    if jeu.mess.tour_b==1:
        pos3.config(text="Ce n'est pas au tour des Blanc")
        jeu.mess.tour_b=0
    elif jeu.mess.tour_n==1:
        pos3.config(text="Ce n'est pas au tour des Noir")
        jeu.mess.tour_n=0
    elif jeu.mess.erreur==1:
        pos3.config(text="Oups, Coordoonée inexploitables, voir aide")
        jeu.mess.erreur=0
    elif jeu.mess.roi==1:
        pos3.config(text="Le roi ne peut être manger")
        jeu.mess.roi=0
    elif jeu.mess.pion==1:
        pos3.config(text="Le pion n'est malheureusement pas une tour")
        jeu.mess.pion=0
    elif jeu.mess.bloquage==1:
        pos3.config(text="Pion génant la route")
        jeu.mess.bloquage=0
    elif jeu.mess.cavalier_allier==1:
        pos3.config(text="Pion allié sur la case d'arrivée")
        jeu.mess.cavalier_allier=0
    elif jeu.mess.cavalier_erreur==1:
        pos3.config(text="Position d'arrivée incorrecte")
        jeu.mess.cavalier_erreur=0
    elif jeu.mess.fou_tour==1:
        pos3.config(text="Le fou n'est pas une tour")
        jeu.mess.fou_tour=0
    elif jeu.mess.coord==1:
        pos3.config(text="Veuillez entrer de bonnes coordonnées")
        jeu.mess.coord=0
    elif jeu.mess.hors_plateau==1:
        pos3.config(text="Position hors plateau")
        jeu.mess.hors_plateau=0
    elif jeu.mess.impossible==1:
        pos3.config(text="Votre roi est en position d'Echec, cela ne vous arrange pas")
        jeu.mess.impossible=0
    elif jeu.mess.echec==1:
        pos3.config(text="Cela mettrais votre roi en echec")
        jeu.mess.echec=0
    else:
        pos3.config(text="",background="white")


def nouveau():
    global jeu
    jeu=Jeu_dechec()
    mise_en_place()
    placement()
def continuer():
    mise_en_place()

#fenetre principal
fen1 = Tk()

#Images:
image = PhotoImage(file="board/board.gif")
pb = PhotoImage(file="pion/pion_blanc.gif")
tb = PhotoImage(file="pion/tour_blanc.gif")
cb = PhotoImage(file="pion/cavalier_blanc.gif")
fb = PhotoImage(file="pion/fou_blanc.gif")
db = PhotoImage(file="pion/roi_blanc.gif") # il s'agit en réalite de la reine
rb = PhotoImage(file="pion/reine_blanc.gif")

pn = PhotoImage(file="pion/pion_noir.gif")
tn = PhotoImage(file="pion/tour_noir.gif")
cn = PhotoImage(file="pion/cavalier_noir.gif")
fn = PhotoImage(file="pion/fou_noir.gif")
dn = PhotoImage(file="pion/roi_noir.gif")
rn = PhotoImage(file="pion/reine_noir.gif")

rnr = PhotoImage(file="pion/roi_noir_rouge.gif")
rbr = PhotoImage(file="pion/roi_blanc_rouge.gif")

#Menu
menubar = Menu(fen1)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Annuler",command=back)
menu1.add_command(label="Recommencer", command=restart)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fen1.destroy)
menubar.add_cascade(label="Option", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
regle = Menu(menu2,tearoff=0)

regle.add_command(label="Pion",command=Pion)


menu2.add_cascade(label="Règle",menu=regle)
menu2.add_command(label="Aide", command=aide)
menu2.add_separator()
menu2.add_command(label="A propos", command=apropos)
menubar.add_cascade(label="Aide", menu=menu2)

fen1.config(menu=menubar)

#Création objet :
echiquier = Canvas(fen1,bg='dark grey',height=350,width=500)
pos1= Label(fen1,text="1ere position :")
pos2= Label(fen1,text="2eme position :")
pos3= Label(fen1,background="white",width=70)
action1=Entry(fen1,bg='dark grey')
action2=Entry(fen1,bg='dark grey')
valider=Button(fen1,text="Valider",command=avancement)
Nouveau=Button(fen1,text="Nouveau",command=nouveau)
Continuer=Button(fen1,text="Continuer",command=continuer)

#Touches de clavier :
fen1.bind("<Return>",avancement)
echiquier.bind("<Button-1>",Clic_mouvement)


#Modif de la fenetre
echiquier.grid(row=0,column=0,columnspan=4)
Nouveau.grid(row=1, column=0,columnspan=4)
Continuer.grid(row=2,column=0,columnspan=4)

def mise_en_place():
    echiquier.bind("<Button-1>",Clic_mouvement)
    Nouveau.destroy()
    Continuer.destroy()
    pos1.grid(row=1,column=0)
    pos2.grid(row=2,column=0)
    pos3.grid(row=3,column=0,columnspan=4)
    action1.grid(row=1,column=1)
    action2.grid(row=2,column=1)
    valider.grid(row=1,column=2,rowspan=2)


#Mise en place du jeu
echiquier.bind("<Button-1>",None)
jeu=Jeu_dechec()
a=jeu.echiquier
jeu.echiquier=marshal.load(open("save/save.txt", "rb"))
jeu.tour=marshal.load(open("save/save_tour.txt","rb"))
if a==jeu.echiquier:
    mise_en_place()
jeu.Try_Echec()
placement()


#Boucle de la fenetre
fen1.mainloop()

#Sauvegarde à la fin du programme
marshal.dump(jeu.echiquier,open("save/save.txt", "wb")) # Argh j'ai tout écrasé !
marshal.dump(jeu.tour,open("save/save_tour.txt","wb")) # Argh j'ai tout écrasé !