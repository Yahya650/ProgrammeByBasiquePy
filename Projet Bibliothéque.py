import arabic_reshaper
import sys
import colorama
from colorama import init
from termcolor import colored
from rich.prompt import Prompt
from datetime import datetime, timedelta, date
import emoji
from Class_Document import *
from Class_Emprunte import *
from Class_CD import *
from Class_Livre import *
from Class_Bibl import *
from Class_Adherent import *


refer = 6

Bib = Bibliothque(0000, "24, Casa")

Bib.ajouterDocument(CD("S646", 15.5, "1", "la vie", "uyghj", "saad", "adob"))
Bib.chercheDocument("1").set_nbreExemple(3)
Bib.ajouterDocument(livre("A132", 352, "2", "L9OWA", "zdsc", "aymane", "adob"))
Bib.chercheDocument("2").set_nbreExemple(4)
Bib.ajouterDocument(
    CD("Z313", 12.7, "3", "LES FILLES", "sfdvf", "kawtar", "adob"))
Bib.chercheDocument("3").set_nbreExemple(9)
Bib.ajouterDocument(livre("S354", 400, "4", "MAN", "xcw", "amin", "adob"))
Bib.chercheDocument("4").set_nbreExemple(1)
Bib.ajouterDocument(CD("A645", 6.9, "5", "ISLAM", "ibjjbh", "zaki", "adob"))
Bib.chercheDocument("5").set_nbreExemple(7)
Bib.ajouterDocument(livre("G645", 145, "6", "MASI7", "sqdf", "sabir", "adob"))
Bib.chercheDocument("6").set_nbreExemple(2)


# traitement kat7at passive fl karyat lli salaw auto:

for i in range(len(Bib.get_emps())):
    if Bib.get_emps()[i].get_datdebut() + timedelta(days=Bib.get_emps()[i].get_Duree()) < datetime.today():
        Bib.chercheDocument(
            Bib.get_emps()[i].get_ReferenceDocument()).setmaynis_nbrEpr()
        Bib.get_emps()[i].set_Etat('passive')


for i in range(int(input("ch7al mn monkharit ghadi it9yad : ".title()))):
    print()
    print(f" L'inscription [ {i+1} ] ".upper().center(50, "#"))
    print()
    nom = input("donne moi votre nom : ".title()).upper().strip()
    pré = input("donne moi votre prénom : ".title()).upper().strip()
    usernam = input("donnee moi UserName : ".title()).strip().upper()
    cin = input(
        "donne moi numero de votre cart nationale : ".title()).upper().strip()

    while True:
        if Bib.chercheAdherent(cin, usernam.lower()) != False:
            print()
            print(" nta(i) deja Adherent ".upper().center(50, "¤"))
            print()
            nom = input("donne moi votre nom : ".title()).upper().strip()
            pré = input("donne moi votre prénom : ".title()).upper().strip()
            usernam = input("donnee moi UserName : ".title()).strip().upper()
            cin = input(
                "donne moi numero de votre cart nationale : ".title()).upper().strip()

        else:
            print()
            Bib.ajouterAdherent(Adherent(cin, nom, pré, usernam))
            print(" mabrouk wliti adherent m3ana ".upper().center(50, "¤"))
            break

q = 1

reshaped_text = arabic_reshaper.reshape(
    'هل انت مشرف ام تريد التسجيل كمنخرطة ؟')

print(f"")
print(f" {reshaped_text[::-1]} ".center(110, "-"))
print(f"")

chose1 = Prompt.ask("Ktab 'M' Ila Knti Mochrif, Ktab 'A' Ila Knti Adherent", choices=[
                    'M', 'A'], show_choices=True)

chose2 = 55

while True:
    if chose1.upper() == "A":
        reshaped_text = arabic_reshaper.reshape('مرحبا بك في مكتبت يحيى حمدي')

        print(f"")
        print(f" {reshaped_text[::-1]} ".center(110, "¤"))
        print(f"")
        # Se connecter de l'Adherent
        print()
        print(" Se connecter ".upper().center(50, "¤"))
        print()
        usernam = input("donnee moi UserName : ".title()).strip().upper()
        cin = input(
            "donne moi numero de votre cart nationale : ".title()).upper().strip()

        while True:
            if Bib.chercheAdherentConect(cin, usernam.lower()) == False:
                print()
                print(" ghalat...! ".upper().center(50, "¤"))
                print()
                usernam = input(
                    "donnee moi UserName : ".title()).strip().upper()
                cin = input(
                    "donne moi numero de votre cart nationale : ".title()).upper().strip()
            else:
                break

        print()

        print(
            f"bonjour {Bib.chercheAdherent(cin, usernam.lower()).get_Nom()} {Bib.chercheAdherent(cin, usernam.lower()).get_Pré()}")
        while True:
            if Bib.chercheAdherentConect(cin, usernam.lower()) != False:
                if chose2 == 1 or chose2 == 5 or chose2 == 6 or chose2 == 54:
                    print()
                    print(
                        f"bonjour {Bib.chercheAdherent(cin, usernam.lower()).get_Nom()} {Bib.chercheAdherent(cin, usernam.lower()).get_Pré()}")

                print(f"")
                print(f" Menu ".center(50, "~"))
                print(f"")

                print()

                print(f" [ 1 ] matb9ach monkharit ".center(50, "%").title())
                print(f" [ 2 ] show documents ".center(50, "%").title())
                print(f" [ 3 ] kira2 milaf mo3ayan ".center(50, "%").title())
                print(f" [ 4 ] ilgha2 kira2 ".center(50, "%").title())
                print(f" [ 5 ] se connecter un notre personne ".center(
                    50, "%").title())
                print(f" [ 6 ] Adherent un notre personne ".center(
                    50, "%").title())
                print(f" [ 7 ] Quitter... ".center(50, "%").title())
                chose2 = int(input())

            else:
                print()
                print(" ghalat...! ".upper().center(50, "¤"))
                print()
                usernam = input(
                    "donnee moi UserName : ".title()).strip().upper()
                cin = input(
                    "donne moi numero de votre cart nationale : ".title()).upper().strip()
                chose2 = 54
                print()

            if chose2 == 1:
                Bib.supprimerEmpr(cin)
                if Bib.supprimerAdherent(Bib.chercheAdherentConect(cin, usernam.lower())) == True:
                    print()
                    print(" mab9itich monkharit ".title().center(50, "&"))
                    print()
                    # Se connecter un notre l'Adherent
                    if len(Bib.get_adh()) >= 1:
                        while True:
                            print()
                            print(" Se connecter ".upper().center(50, "¤"))
                            print()
                            usernam = input(
                                "donne moi UserName : ".title()).strip()
                            cin = input(
                                "donne moi numero de votre cart nationale : ".title()).upper().strip()
                            print()
                            t = 1
                            if Bib.chercheAdherentConect(cin, usernam.lower()) == False:
                                break
                    else:
                        print()
                        print(" Makayn 7ta chi adherent ".upper().center(50, '¤'))
                        print()
                        t = 0
                        nom = input("donne moi votre nom : ".title()
                                    ).upper().strip()
                        pré = input("donne moi votre prénom : ".title()
                                    ).upper().strip()
                        usernam = input(
                            "donnee moi UserName : ".title()).strip().upper()
                        cin = input(
                            "donne moi numero de votre cart nationale : ".title()).upper().strip()

                        while True:
                            if t == 1:
                                b = True
                            elif t == 0:
                                b = Bib.ajouterAdherent(
                                    Adherent(cin, nom, pré, usernam))

                            if b == False:
                                print()
                                print(" ghalat...! ".upper().center(50, "¤"))
                                print()
                                nom = input(
                                    "donne moi votre nom : ".title()).upper().strip()
                                pré = input(
                                    "donne moi votre prénom : ".title()).upper().strip()
                                usernam = input(
                                    "donnee moi UserName : ".title()).strip().upper()
                                cin = input(
                                    "donne moi numero de votre cart nationale : ".title()).upper().strip()
                            else:

                                break

            if chose2 == 2:

                x = input("wach baghi tchof les CD ou les livres : ".title()
                          ).upper().strip()

                if x == "CD":
                    print()
                    Bib.achficheDocument(CD)
                    print()
                elif x == "LIVRES":
                    print()
                    Bib.achficheDocument(livre)
                    print()
                else:
                    print("Invalid choice")

            if chose2 == 3:
                x = input("chno Type dyal document lli baghi tkri, wach 'CD' ou 'LIVRES' : ".title(
                )).upper().strip()

                print()
                if x == "CD":
                    Bib.achficheDocument(CD)
                    refdoc = input(
                        "donnée moi le reference de document pour Emprinté : ".title()).strip().upper()
                    lmoda = int(input("ch7al lmoda lli baghi tkri fiha : "))

                    # get Year from user
                    year = int(Prompt.ask("Date De Début: \nAnnée"))
                    while True:
                        if year < int(date.today().strftime("%Y")):
                            print()
                            print(" erreur ".title().center(
                                50, "\N{confused face}"))
                            print()
                            year = int(Prompt.ask("Date De Début: \nAnnée"))
                        else:
                            break

                    # get mounth from user
                    mounth = int(Prompt.ask("Mois : ", choices=[
                                 '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], show_choices=False))

                    if year == int(date.today().strftime("%Y")):
                        while True:
                            if mounth < int(date.today().strftime("%m")):
                                print()
                                print(" erreur ".title().center(
                                    50, "\N{confused face}"))
                                print()
                                mounth = int(Prompt.ask("Mois : ", choices=[
                                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], show_choices=False))
                            else:
                                break

                    # get day from user
                    day = int(Prompt.ask("Jour : ", choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                              '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'], show_choices=False))

                    if year == int(date.today().strftime("%Y")):
                        while True:
                            if day < int(date.today().strftime("%d")):
                                print()
                                print(" erreur ".title().center(
                                    50, "\N{confused face}"))
                                print()
                                day = int(Prompt.ask("Jour : ", choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                                                         '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'], show_choices=False))
                            else:
                                break

                    if Bib.ajouterEnprinte(Emprinte(q, refdoc, cin, datetime(year, mounth, day), lmoda)) == False:
                        print()
                        print(f"had lkarya deja kayna ou doc not disponible".title())
                        print()

                    else:
                        q += 1
                        print()
                        print("tamat lkarya binaja7".title())
                        print()

                elif x == "LIVRES" or x == 'LIVRE4':
                    Bib.achficheDocument(livre)
                    refdoc = input(
                        "donnée moi le reference de document pour Emprinté : ".title()).strip().upper()

                    lmoda = int(input("ch7al lmoda lli baghi tkri fiha : "))

                    # get Year from user
                    year = int(Prompt.ask("Date De Début: \nAnnée"))
                    while True:
                        if year < int(date.today().strftime("%Y")):
                            print()
                            print(" erreur ".title().center(
                                50, "\N{confused face}"))
                            print()
                            year = int(Prompt.ask("Date De Début: \nAnnée"))
                        else:
                            break

                    # get mounth from user
                    mounth = int(Prompt.ask("Mois : ", choices=[
                                 '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], show_choices=False))

                    if year == int(date.today().strftime("%Y")):
                        while True:
                            if mounth < int(date.today().strftime("%m")):
                                print()
                                print(" erreur ".title().center(
                                    50, "\N{confused face}"))
                                print()
                                mounth = int(Prompt.ask("Mois : ", choices=[
                                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], show_choices=False))
                            else:
                                break

                    # get day from user
                    day = int(Prompt.ask("Jour : ", choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                              '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'], show_choices=False))

                    if year == int(date.today().strftime("%Y")):
                        while True:
                            if day < int(date.today().strftime("%d")):
                                print()
                                print(" erreur ".title().center(
                                    50, "\N{confused face}"))
                                print()
                                day = int(Prompt.ask("Jour : ", choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                          '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'], show_choices=False))
                            else:
                                break

                    if Bib.ajouterEnprinte(Emprinte(q, refdoc, cin, datetime(year, mounth, day), lmoda)) == False:
                        print()
                        print(f"had lkarya deja kayna ou doc not disponible".title())
                        print()

                    else:
                        q += 1
                        print()
                        print("tamat lkarya binaja7".title())
                        print()
                else:
                    print()
                    print("m3andk 7ta krya ou Invalid choice")
                    print()

            if chose2 == 4:
                if len(Bib.get_emps()) >= 1:
                    for i in range(len(Bib.get_emps())):
                        if Bib.get_emps()[i].get_cin() == cin:
                            print(str(Bib.get_emps()[i]))

                    print()
                    ecz = int(
                        input("ktab code dyal lkarya lli baghi Annule : "))
                    print()
                    if (Bib.annuleEprinte(ecz) == True):
                        print(" tama l2ilghaa2 binaja7 ".upper().center(50, "¤"))
                        print()
                    else:
                        print("had lkarya ga3ma kayna")
                        print()
                else:
                    print("ma3andk 7ta karya")

            if chose2 == 5:
                print()
                print(" Se connecter une notre Adherent ".upper().center(50, "¤"))
                print()
                usernam = input(
                    "donnee moi UserName : ".title()).strip().upper()
                cin = input(
                    "donne moi numero de votre cart nationale : ".title()).upper().strip()
                print()

            if chose2 == 6:
                print()
                nom = input("donne moi votre nom : ".title()).upper().strip()
                pré = input("donne moi votre prénom : ".title()
                            ).upper().strip()
                usernam = input(
                    "donnee moi UserName : ".title()).strip().upper()
                cin = input(
                    "donne moi numero de votre cart nationale : ".title()).upper().strip()

                while True:
                    if Bib.chercheAdherent(cin, usernam.lower()) != False:
                        print()
                        print(" ghalat ".upper().center(50, "¤"))
                        print()
                        nom = input("donne moi votre nom : ".title()
                                    ).upper().strip()
                        pré = input("donne moi votre prénom : ".title()
                                    ).upper().strip()
                        usernam = input(
                            "donnee moi UserName : ".title()).strip().upper()
                        cin = input(
                            "donne moi numero de votre cart nationale : ".title()).upper().strip()

                    else:
                        print()
                        Bib.ajouterAdherent(Adherent(cin, nom, pré, usernam))
                        break

            if chose2 == 7:
                print("[ 1 ] khoroj kolli")
                print("[ 2 ] dokhol lmochrif")
                chose3 = int(input())
                if chose3 == 1:
                    sys.exit("Bye...")
                elif chose3 == 2:
                    chose1 = "M"
                    break
    elif chose1.upper() == "M":
        reshaped_text = arabic_reshaper.reshape('مرحبا بك في مكتبتك')

        print(f"")
        print(f" {reshaped_text[::-1]} ".center(110, "¤"))
        print(f"")
        # Se connecter de l'Adherent
        print()
        print(" Se connecter ".upper().center(50, "¤"))
        print()
        usernam = input("donnee moi UserName : ".title()
                        ).strip().upper().upper()
        cin = input(
            "donne moi numero de votre cart nationale : ".title()).upper().strip()

        while True:
            if usernam != "YAHYAHAMDY" or cin != "BW49789":
                print()
                print(" ghalat...! ".upper().center(50, "¤"))
                print()
                usernam = input(
                    "donnee moi UserName : ".title()).strip().upper()
                cin = input(
                    "donne moi numero de votre cart nationale : ".title()).upper().strip()
            else:
                break

        print()

        print("¤"*100)
        print(f" Bonjour Admin. (Yahya, Hamdy) ".center(100, "¤"))
        print("¤"*100)

        while True:
            print(f"")
            print(f" Menu ".center(50, "~"))
            print(f"")

            print()

            print(f" [ 1 ] Cherche les Adherent ".center(50, "%").title())
            print(f" [ 2 ] Cherche les Document ".center(50, "%").title())
            print(f" [ 3 ] Add Document ".center(50, "%").title())
            print(f" [ 4 ] Supreme Document ".center(50, "%").title())
            print(f" [ 5 ] Add Exempele de Document ".center(50, "%").title())
            print(f" [ 6 ] Supremer Exempele de Document ".center(
                50, "%").title())
            print(f" [ 7 ] Afficher Les Document ".center(50, "%").title())
            print(f" [ 8 ] Afficher Les emprinte ".center(50, "%").title())
            print(f" [ 9 ] Afficher Binifice ".center(50, "%").title())
            print(f" [ 10 ] Quitter... ".center(50, "%").title())
            chose2 = int(input())

            if chose2 == 1:
                # Bib.afficherAdherent()
                qq = input("Donnee moi le UserName : ").upper()
                for i in range(len(Bib.get_adh())):
                    if qq == Bib.get_adh()[i].get_User().upper():
                        print()
                        print(" Yes, Kayn ".center(50, "@"))
                        print()
                        print(str(Bib.get_adh()[i]))
                        qsces = 0
                        break
                    else:
                        qsces = 1

                if qsces == 1:
                    print(f"makin chi wa7d bhad UserName [ {qq} ]")

            if chose2 == 2:
                # print()
                # qq1 = input(
                #     "ktab 'CD' ila bghiti tchof les Cd, ktab 'livre' ila bghiti tchof les livres, ktab 'ALL' ila bghiti tchod les document kamlin : ").strip().upper()
                # print()
                # if qq1 == CD:
                #     Bib.achficheDocument(CD)
                # elif qq1 == "LIVRE" or qq1 == "LIVRES":
                #     Bib.achficheDocument(livre)
                # elif qq1 == "ALL":
                #     Bib.achficheDocument(CD)
                #     Bib.achficheDocument(livre)

                print()
                qq3 = input(
                    "Donnee moi le Reference de Document pour Cherche : ").upper()
                print()
                if Bib.chercheDocument(qq3) != False:
                    print(str(Bib.chercheDocument(qq3)))

                else:
                    print()
                    print("gam3a kayn had document".title())
                    print()

            if chose2 == 3:

                qq4 = input(
                    "ktab 'CD' ila bghiti tzid Cd, ktab 'livre' ila bghiti tzid livrev : ").upper()

                if qq4 == 'CD':
                    typecdg = input("donnee moi le type codage : ")
                    taill = input("donnee moi la taille de CD : ")
                    titre = input("donnee moi le titre : ")
                    theme = input("donnee moi le theme : ")
                    autr = input("donnee moi le auteur : ")
                    edit = input("donnee moi le edit : ")
                    refer += 1
                    Bib.ajouterDocument(
                        CD(typecdg, taill, refer, titre, theme, autr, edit))
                    nbr1 = int(
                        input("donnée le Nombre de document : ".title()))
                    Bib.approvisionnerDocument(refer, nbr1)
                elif qq4 == 'LIVRE':
                    nIBSN = int(input("donnee moi numero ISBN : "))
                    nbrpage = input("donnee moi nombre des page de livre : ")
                    titre = input("donnee moi le titre : ")
                    theme = input("donnee moi le theme : ")
                    autr = input("donnee moi le auteur : ")
                    edit = input("donnee moi le edit : ")
                    refer += 1
                    Bib.ajouterDocument(
                        livre(nIBSN, nbrpage, refer, titre, theme, autr, edit))
                    nbr1 = int(
                        input("donnée le Nombre de document : ".title()))
                    Bib.approvisionnerDocument(refer, nbr1)
                else:
                    print("This choix not disponible".title())

            if chose2 == 4:

                Bib.achficheDocument(CD)
                Bib.achficheDocument(livre)
                print()
                ref44 = input(
                    "donnee le ref de document pour supremer".title()).upper()

                if Bib.chercheDocument(ref44) != False:
                    for i in range(len(Bib.get_emps())):
                        if Bib.get_emps()[i].get_ReferenceDocument() == ref44:
                            Bib.annuleEprinte(Bib.get_emps()[i].get_CodeEnpr())

                    Bib.supprimerDocument(Bib.chercheDocument(ref44))
                    print()
                    print("supreme success".title())
                else:
                    print()
                    print("had referonce lli dkhalti ga3ma".title())
                    print()

            if chose2 == 5:
                print()
                qq5 = int(input("ch7al mn noskha baghi tzid : ".title()))
                print()
                Bib.achficheDocument(CD)
                Bib.achficheDocument(livre)
                print()
                ref55 = input(
                    "ktab reference dyal ktab lli baghi tzid nosakh dyalo : ".title()).upper()
                print()

                if Bib.approvisionnerDocument(ref55, qq5) == True:
                    print(
                        f"had document lli type dyalo [ {type(Bib.chercheDocument(ref55))} ] w titre dyalo [ {Bib.chercheDocument(ref55).get_titre()} ] wlla 3andk mnno [ {Bib.chercheDocument(ref55).get_nbreExemple()} ] dyl noskha7".title())
                    print()
                else:
                    print("Document not exist".title())

            if chose2 == 6:
                print()
                qq5 = int(input("ch7al mn noskha baghi tn9os : ".title()))
                print()
                Bib.achficheDocument(CD)
                Bib.achficheDocument(livre)
                print()
                ref55 = input(
                    "ktab reference dyal ktab lli baghi tn9os nosakh dyalo : ".title()).upper()
                print()

                if Bib.diminiuerDocument(ref55, qq5) == True:
                    print(
                        f"had document lli type dyalo [ {type(Bib.chercheDocument(ref55))} ] w titre dyalo [ {Bib.chercheDocument(ref55).get_titre()} ] wlla 3andk mno [ {Bib.chercheDocument(ref55).get_nbreExemple()} ] dyal nosakh".title())
                    print()
                elif Bib.diminiuerDocument(ref55, qq5) == False:
                    print()
                    print("document lli baghi tn9os nosakh dyalo ga3ma kayn".title())
                    print()
                else:
                    print(Bib.diminiuerDocument(ref55, qq5))

            if chose2 == 7:
                print()
                print("[ 1 ] Afficher les Document (CD)")
                print("[ 2 ] Afficher les Document (livre)")
                print("[ 3 ] Afficher Tout les Document")
                print()
                chose8 = int(input())
                print()
                if chose8 == 1:
                    Bib.achficheDocument(CD)

                elif chose8 == 2:
                    Bib.achficheDocument(livre)

                elif chose8 == 3:
                    Bib.achficheDocument(CD)
                    Bib.achficheDocument(livre)
                print()

            if chose2 == 8:

                print()
                print("[ 1 ] Afficher Nombre Des Eprinte de document")
                print("[ 2 ] Afficher les Eprinte Active")
                print("[ 3 ] Afficher les Eprinte Passive")
                print("[ 4 ] Afficher Tout les Eprinte")
                print()
                chose4 = int(input())

                if chose4 == 1:
                    print()
                    Bib.achficheDocument(CD)
                    Bib.achficheDocument(livre)
                    print()
                    refdoc = input(
                        "donnee moi le reference de document pour 7isab nobre des emprinte : ".title()).strip()
                    print()

                    if Bib.chercheEprinte2(refdoc) != False:
                        print(
                            f"Nombre de emprinte : {len(Bib.chercheEprinte2(refdoc))}".title())
                    else:
                        print(" Document not exist ".title())

                    print()
                if chose4 == 2:
                    print()
                    Bib.affichEmp('active')
                    print()

                if chose4 == 3:
                    print()
                    Bib.affichEmp('passive')
                    print()

                if chose4 == 4:
                    print()
                    Bib.affichEmp('active')
                    Bib.affichEmp('passive')
                    print()

            if chose2 == 9:
                print()
                print(
                    f"le bénéfice actuellement de votre bibliotheque : {Bib.get_binifice()}".title())
                print()
            if chose2 == 10:
                print()
                print("[ 1 ] khoroj kolli")
                print("[ 2 ] dokhol Mode Adherent")
                print()
                chose3 = int(input())
                if chose3 == 1:
                    sys.exit("Bye...")
                elif chose3 == 2:
                    chose1 = "A"
                    break
