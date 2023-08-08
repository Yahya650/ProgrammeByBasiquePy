from Class_Document import *



class CD(Document):
    def __init__(self, typecdg, taille, re, tit, the, aut, edit):

        super().__init__(re, tit, the, aut, edit)

        self.typeCodage = typecdg
        self.taille = taille

    def get_Taille(self):
        return self.taille

    def __str__(self):
        return f"le ref de doc (CD) : {self.get_Reference()} / le titre de CD : {self.get_titre()} / la taille de cd : {self.get_Taille()} / le Auteur : {self.get_Auteur()} / la nomb de exo : {self.get_nbreExemple()} / le nomb des empr : {self.get_nbrEpr()}".title()
