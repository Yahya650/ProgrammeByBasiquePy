class Emprinte:
    def __init__(self, codeEmp, refDoc, cinAdhe, datedebut, duree):
        self.codeEmpriente = codeEmp
        self.ReferenceDocument = refDoc
        self.cinAdherent = cinAdhe
        self.dateDebut = datedebut
        self.duree = duree
        self.etat = ''

    def get_Duree(self):
        return self.duree

    def get_datdebut(self):
        return self.dateDebut

    def get_cin(self):
        return self.cinAdherent

    def get_etat(self):
        return self.etat

    def get_ReferenceDocument(self):
        return self.ReferenceDocument

    def get_CodeEnpr(self):
        return self.codeEmpriente

    def set_Etat(self, value):
        self.etat = value

    def __str__(self):
        return f"codeEmpriente {self.codeEmpriente} / ReferenceDocument :{self.ReferenceDocument} / cinAdherent :{self.cinAdherent} dateDebut :{self.dateDebut} la duree :{self.duree} l'etat :{self.etat}".title()
