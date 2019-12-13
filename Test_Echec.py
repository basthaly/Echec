"""
Programme sans lien avec le programme principal étant seulement un endroit plus
clair afin de réfléchir sur le problème qu'est la mise en échec d'un roi.
"""


def echec(x1,y1,x2,y2):
    if self.echiquier[x1][y1][1]!=self.echiquier[x2][y2][1]:
        print ("Roi en échec")

for x in range (7):
    for y in range (7):
        if self.echiquier[x][y][0]==5:
            calcul=True
            v=0
            while calcul==True:
                try:
                    v+=1
                    if self.echiquier[x][y+v][0]==-1: #Calcul vers le bas
                        echec(x,y,x,y+v)
                except:
                    v=0
                    break

            while calcul==True:
                try:
                    v+=1
                    if self.echiquier[x][y-v][0]==-1: #Calcul vers le haut
                        echec(x,y,x,y-v)
                except:
                    v=0
                    break

            while calcul==True:
                try:
                    v+=1
                    if self.echiquier[x-v][y][0]==-1: # Calcul vers la gauche
                        echec(x,y,x-v,y)
                except:
                    v=0
                    break

            while calcul==True:
                try:
                    v+=1
                    if self.echiquier[x+v][y][0]==-1: # Calcul vers la droite
                        echec(x,y,x+v,y)
                except:
                    v=0
                    break

            while calcul==True:
                try:
                    v+=1
                    if self.echiquier[x-v][y-v][0]==-1: # Calcul diagonal en haut à gauche
                        echec(x,y,x-v,y-v)
                except:
                    v=0
                    break

            while calcul==True:
                try:
                    v+=1
                    if self.echiquier[x+v][y-v][0]==-1: # Calcul diagonal en haut à droite
                        echec(x,y,x+v,y-v)
                except:
                    v=0
                    break

            while calcul==True:
                try:
                    v+=1
                    if self.echiquier[x-v][y+v][0]==-1: # Calcul diagonal en bas à gauche
                        echec(x,y,x-v,y+v)
                except:
                    v=0
                    break

            while calcul==True:
                try:
                    v+=1
                    if self.echiquier[x-v][y-v][0]==-1: # Calcul diagonal en bas à droite
                        echec(x,y,x-v,y-v)
                except:
                    v=0
                    break
            """try:
                if (x2==x1+2 and yb==ya+1)\
                        or (x2==x1+1 and yb==ya+2)\
                        or (x2==x1+2 and yb==ya-1)\
                        or (x2==x1+1 and yb==ya-2)\
                        or (x2==x1-2 and yb==ya+1)\
                        or (x2==x1-1 and yb==ya+2)\
                        or (x2==x1-2 and yb==ya-1)\
                        or (x2==x1-1 and yb==ya-2): #Calcul Cheval
                            pass
            except:
                pass"""
