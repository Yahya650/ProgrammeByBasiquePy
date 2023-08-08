class Document:
    def __init__(self, re, tit, the, aut, edit):
        self.reference = re
        self.titre = tit
        self.theme = the
        self.auteur = aut
        self.editeur = edit
        self.nbreExemple = 0
        self.nbreEmpriente = 0

    def __str__(self):
        return f"le reference : {self.reference} le titre :{self.titre} le théme :{self.theme} l'auteur : {self.auteur} l'editeur : {self.editeur} nbreExemple :{self.nbreExemple} nbreEmpriente {self.nbreEmpriente} "

    def get_titre(self):
        return self.titre

    def get_Auteur(self):
        return self.auteur

    def setplus_nbrEpr(self):
        self.nbreEmpriente += 1

    def setmaynis_nbrEpr(self):
        self.nbreEmpriente -= 1

    def get_nbreExemple(self):
        return self.nbreExemple

    def set_nbreExemple(self, value):
        self.nbreExemple += value

    def set_maynNbrExo(self, value):
        self.nbreExemple -= value

    def get_Reference(self):
        return self.reference

    def get_nbrEpr(self):
        return self.nbreEmpriente