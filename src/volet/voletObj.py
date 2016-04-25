#Objet Volet Roulant
class VoletObj(object):
    def __init__(self):
        self.nom = 'vr_init'
        # SI 0 ==> Etat STOP
        # SI 1 ==> Etat DESCENTE
        # SI 2 ==> Etat MONTE
        self.etat = 0        
        self.numero = 0

    def getNom(self):
        return self.nom

    def setNom(self, value):
        if type(value) == str:
            self.nom = value
        else:
            raise TypeError(r"'%s' est pas le bon format" % value)
    
    def getEtat(self):
        return self.etat
    
    def setEtat(self, value):
        if type(value) == int:
            self.etat = value
        else:
            raise TypeError(r"'%s' est pas le bon format" % value)
        
    def getNumero(self):
        return self.numero
    
    def setNumero(self, value):
        if type(value) == int:
            self.numero = value
        else:
            raise TypeError(r"'%s' est pas le bon format" % value)
        