# -*- coding: utf-8 -*-

class Client:
    def __init__(self,name,date,telNumber):
        self.nom = name
        self.date_naissance = date
        self.tel = telNumber
        
class detailCall: 
    def __init__(self, chemin):
        self.chemin = chemin
        self.data = []
        self.res = []
        self.nombre = 0
        
        
        
    def lire_cdr(self):
        
        with open(self.chemin, "r") as f:
            for i in f:
                self.i.append(self.data.strip())
            self.pile_dict()
            self.nombre = self.res[0]["Appelant"]
            
                
    def pile_dict(self):
        a = []
        b = ["Identifiant", 'type', 'Heure','appelant', 'appelé', 'Temps', 'Taxe', 'TotalVolume']
        for i in self.data:
            a = i.split('|')
            self.res.append(dict(zip(b, a)))
            
            
