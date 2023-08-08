class Adherent:
    def __init__(self, cin, nom, prenom, userName):
        self.cin = cin
        self.nom = nom
        self.prenom = prenom
        self.userName = userName

    def get_Cin(self):
        return self.cin

    def get_Nom(self):
        return self.nom

    def get_Pré(self):
        return self.prenom

    def get_User(self):
        return self.userName

    def __str__(self):
        return f"Le Cin : {self.get_Cin()} / Le nom : {self.get_Nom()} / Le prenom : {self.get_Pré()} / UserName : {self.get_User()}"
