import unittest
from domain.entitati import Spectacol

class TestCaseProductRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def testSpectacol(self):
        s1=Spectacol("Seba","Seba","Balet","120")
        self.assertEqual(s1.getartist()=="Seba")
        self.assertEqual(s1.getgen()=="Balet")
        self.assertEqual(s1.gettitlu()=="Seba")
        self.assertEqual(s1.getdurata()=="120")





    
    

    