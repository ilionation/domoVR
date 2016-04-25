import unittest

from src.volet.voletObj import VoletObj


class VoletObjTest(unittest.TestCase):

# -------------------------------------
# TEST attribut 'Nom' du volet roulant
    def test_getNom(self):
        d = VoletObj()
        self.assertEquals(d.nom, 'vr_init')
        
    def test_setNom(self):
        d = VoletObj()
        d.setNom('vr_1')
        self.assertEquals(d.nom, 'vr_1')
        
    def test_setNomError(self):
        d = VoletObj()
        with self.assertRaises(TypeError):
            d.setNom(99999)

# -------------------------------------
# TEST attribut 'Numero' du volet roulant
    def test_getNumero(self):
        d = VoletObj()
        self.assertEquals(d.etat, 0)
            
    def test_setNumero(self):
        d = VoletObj()
        d.setNumero(9)
        self.assertEquals(d.numero, 9)
        
    def test_setNumeroError(self):
        d = VoletObj()
        with self.assertRaises(TypeError):
            d.setNumero('numero')

# -------------------------------------
# TEST attribut 'Etat' du volet roulant
    def test_getEtat(self):
        d = VoletObj()
        self.assertEquals(d.etat, 0)
            
    def test_setEtat(self):
        d = VoletObj()
        d.setEtat(1)
        self.assertEquals(d.etat, 1)
        
    def test_setEtatError(self):
        d = VoletObj()
        with self.assertRaises(TypeError):
            d.setEtat('etat')