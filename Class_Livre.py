from Class_Document import *


class livre(Document):
    def __init__(self, nISBN, nbrpg, re, tit, the, aut, edit):

        super().__init__(re, tit, the, aut, edit)

        self.numeroISBN = nISBN
        self.nbrepage = nbrpg

    def get_Nbrpage(self):
        return self.nbrepage

    def __str__(self):
        return f"le ref de Doc (livre) : {self.get_Reference()} / le titre de livre : {self.get_titre()} / le nomb des page : {self.get_Nbrpage()} / le Auteur : {self.get_Auteur()} / la nomb de exo : {self.get_nbreExemple()} / le nomb des empr : {self.get_nbrEpr()}".title()
