#Programme relié aux jeu d'echec

# Classe
class message:
    def __init__(self): # Chaque variable correspondra à une erreur qui sera ensuite affiché dans le programme evitant les pop-ups
        self.erreur=0
        self.roi=0
        self.pion=0
        self.bloquage=0
        self.cavalier_allier=0
        self.cavalier_erreur=0
        self.fou_tour=0
        self.coord=0
        self.hors_plateau=0
        self.impossible=0
        self.tour_n=0
        self.tour_b=0
        self.echec=0