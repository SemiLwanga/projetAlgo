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
            
class Payement:
    
    def __init__(self,liste_dict):
        self.liste_dict = liste_dict
        self.amount = 0
    
    def description(self):
        
        for i in self.liste_dict:
            type_call = float(i["type d'appel"])
            num = i['appelé']
            if (i['durée'] != ''):
            	tempsAppel = float(i['durée'])
            else:
            	tempsAppel = 0
            total_vol = float(i['totalVolume'])
            taxe = float(i['taxe'])
            amount = 0
            if type_call == 0:
                if (num[0:4] == '24382' or num[0:4] == '24381'):
                    amount += 0.025*tempsAppel/60
                else:
                    amount += 0.05*tempsAppel/60
            elif (type_call == 1):
                if (num[0:4] == '24382' or num[0:4] == '24381'):
                    amount  += 0.001
                else:
                    amount += 0.002
            else:
                amount += total_vol*0.03
            if (taxe == 1):
                amount =amount + amount *5/100
            elif (taxe == 2):
                amount = amount + amount *16/100
            self.amount += amount
            
            
            class Statistiques:

                def __init__(self, liste_dict):
                    self.liste_dict = liste_dict
                    
                    self.nbr_appel, self.nbr_sms, self.internet, self.dure_appel = 0,0,0,0
                                       
                    self.statistique,self.stat_dict = [], {}
                    
                   
                def stat(self):
                    for i in self.liste_dict:
                        type_call = float(i["type d'appel"])
                        
                        if (i['durée'] != ''):
                        	tempsAppel = float(i['durée'])
                        else:
                        	tempsAppel = 0
                        total_vol = float(i['totalVolume'])
                        
                        if (type_call == 0):
                            self.nbr_appel += 1
                            self.dure_appel += tempsAppel
                            
                        elif (type_call == 1):
                            self.nbr_sms += 1
                        else:
                            self.internet += total_vol
                    
                    self.statistique = [self.nbr_appel, self.dure_appel, self.nbr_sms, self.internet]
                    self.have_stat()
                    
                def StatDetails(self):
                    a = ["Nombre d'appels", "Durée Appel", "SMS", "Forfait Internet"]
                    self.stat_dict = dict(zip(a, self.statistique))
        
            
                 
            
