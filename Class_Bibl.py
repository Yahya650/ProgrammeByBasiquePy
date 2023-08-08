from datetime import datetime, timedelta, date
from Class_CD import *
from Class_Livre import *

class Bibliothque:
    def __init__(self, codeb, adrs):
        self.codeB = codeb
        self.adresse = adrs
        self.benifice = 0
        self.adherents = []
        self.documents = []
        self.emprintes = []

    def get_emps(self):
        return self.emprintes

    def get_adh(self):
        return self.adherents

    def get_Doc(self):
        return self.documents

    def get_binifice(self):
        return self.benifice

    def set_binifice(self, value: int):
        self.benifice += value


# Srart les methods de Adherent


    def afficherAdherent(self):
        for i in range(len(self.adherents)):
            print(str(self.adherents[i]))

    def chercheAdherent(self, Cin, usernam):
        for i in range(len(self.adherents)):
            if Cin == self.adherents[i].get_Cin().upper() or usernam == self.adherents[i].get_User().lower():
                return self.adherents[i]

        return False

    def chercheAdherentConect(self, Cin, usernam):
        for i in range(len(self.adherents)):
            if Cin == self.adherents[i].get_Cin().upper() and usernam == self.adherents[i].get_User().lower():
                return self.adherents[i]

        return False

    def ajouterAdherent(self, a):
        if self.chercheAdherent(a.get_Cin(), a.get_User().lower()) == False:
            self.adherents.append(a)
            return True
        return False

    def supprimerAdherent(self, a):
        if self.chercheAdherent(a.get_Cin(), a.get_User().lower()) != False:
            self.adherents.remove(self.chercheAdherent(
                a.get_Cin(), a.get_User().lower()))
            return True
        return False
# End methods de Adherent


# Start les methods de Document


    def chercheDocument(self, Reference):
        for i in range(len(self.documents)):
            if Reference == self.documents[i].get_Reference():
                return self.documents[i]
        return False

    def ajouterDocument(self, d):
        if self.chercheDocument(d.get_Reference()) == False:
            self.documents.append(d)
            return True
        else:
            return False

    def supprimerDocument(self, d):
        if self.chercheDocument(d.get_Reference()) != False:
            self.documents.remove(d)
            return True
        else:
            return False

    # approvisionnerDocument() => had lmethode katzid 3dad nada2ir dyal document mo3ayan
    def approvisionnerDocument(self, ref, nbreExemple: int):
        for i in range(len(self.documents)):
            if ref == self.documents[i].get_Reference():
                self.documents[i].set_nbreExemple(nbreExemple)
                return True
        return False

    # kim7i wa7d lktab 3adad lmrrat mital, ktab kayn 3 dyal lmran ana 3tito 2 kim7i dak lktab 2 mrat wkikhalli wa7d
    def diminiuerDocument(self, reference, nbr):
        if self.chercheDocument(reference) != False:
            if nbr <= self.chercheDocument(reference).get_nbreExemple():
                self.chercheDocument(reference).set_maynNbrExo(nbr)
                return True
            else:
                return f'Lktab kayn ghir [ {self.chercheDocument(reference).get_nbreExemple()} ] lmrat wnta baghi tm7ih [ {nbr} ] maymkanch'.title()
        else:
            return False

    def nombreDocument(self):
        return len(self.documents)

    def achficheDocument(self, Type):
        listdedocpourAficher = []
        for i in self.documents:
            if type(self.chercheDocument(i.get_Reference())) == Type:
                listdedocpourAficher.append(
                    self.chercheDocument(i.get_Reference()))

        for i in range(len(listdedocpourAficher)):
            print(str(listdedocpourAficher[i]))

    def NomberDocument(self, Type):
        nbr = 0
        for i in self.documents:
            if type(i) == Type:
                nbr += 1
        return nbr
# End methods de Document


# Start les methods de Emprinte


    def ajouterEnprinte(self, enpr):
        if self.chercheEmprinte(enpr.get_CodeEnpr()) == False and self.disponibilite(enpr.get_ReferenceDocument(), enpr.get_datdebut(), enpr.get_Duree()) == True:
            self.emprintes.append(enpr)
            self.chercheDocument(enpr.get_ReferenceDocument()).setplus_nbrEpr()
            enpr.set_Etat('active')
            if type(self.chercheDocument(enpr.get_ReferenceDocument())) == CD:
                self.benifice += 5
            elif type(self.chercheDocument(enpr.get_ReferenceDocument())) == livre:
                self.benifice += 10
            return True
        return False

    def supprimerEmpr(self, cinAdherent):
        for i in range(len(self.emprintes)):
            if self.emprintes[i].get_cin().upper() == cinAdherent.upper():
                self.chercheDocument(
                    self.emprintes[i].get_ReferenceDocument()).setmaynis_nbrEpr()
                self.emprintes.remove(self.emprintes[i])

    def chercheEmprinte(self, codeEpr):
        for i in range(len(self.emprintes)):
            if codeEpr == self.emprintes[i].get_CodeEnpr():
                return self.emprintes[i]
        return False

    def chercheEprinte2(self, refDoc):
        TableEmp = []
        if self.chercheDocument(refDoc) != False:
            for i in range(len(self.emprintes)):
                if self.emprintes[i].get_ReferenceDocument() == refDoc and self.emprintes[i].get_etat() == 'active':
                    TableEmp.append(self.emprintes[i])
            
        else:
            return False
        return TableEmp

    def annuleEprinte(self, codeEmpr):
        if self.chercheEmprinte(codeEmpr) != False and self.chercheEmprinte(codeEmpr).get_etat() == 'active':
            self.chercheDocument(self.chercheEmprinte(
                codeEmpr).get_ReferenceDocument()).setmaynis_nbrEpr()
            self.chercheEmprinte(codeEmpr).set_Etat('passive')
            return True
        else:
            return False

    def affichEmp(self, etat: str):
        for i in range(len(self.emprintes)):
            if self.emprintes[i].get_etat() == etat:
                print(str(self.emprintes[i]))
# End methods emprinte

    def disponibilite(self, referenceDoc, dateDebut, duree):

        if self.chercheDocument(referenceDoc).get_nbreExemple() > self.chercheDocument(referenceDoc).get_nbrEpr():
            return True

        elif self.chercheEprinte2(referenceDoc) != False and self.chercheDocument(referenceDoc).get_nbreExemple() <= self.chercheDocument(referenceDoc).get_nbrEpr():
            for i in self.chercheEprinte2(referenceDoc):
                if i.get_datdebut() + timedelta(days=i.get_Duree()) < dateDebut and i.get_etat() == 'active':
                    return True
        return False
