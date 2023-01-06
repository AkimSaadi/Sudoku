import unittest
import verification as verif
import generer as gnrr
import numpy as np

class VerificationTest(unittest.TestCase) :
   
    def setUp (self):
        self.grille = np.array([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]])
   
    def test_carre(self):
        x=verif.test(1,2,0,self.grille)
        self.assertFalse(x)
    
    def  test_ligne(self):
        x=verif.test(5,0,2,self.grille)
        self.assertTrue(x)
        
    def test_colonne(self):
        x=verif.test (5,2,1,self.grille)
        self.assertTrue(x)

class GenererTest(unittest.TestCase) :
    
    def setUp (self):
        self.grille = np.array([[1,2,3,4],[2,3,4,1],[3,4,1,2]])
   
    def test_trouver_case_vide(self) :
        x=gnrr.trouver_case_vide(self.grille)
        self.assertFalse(x)
        
unittest.main()