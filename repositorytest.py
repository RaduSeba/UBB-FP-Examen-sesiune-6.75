import unittest
from repository.repospectacol import SpectacolRepoFile
from domain.entitati import Spectacol

class TestCaseProductRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = SpectacolRepoFile("data/examen.txt")

    def test_store(self):
        s1=Spectacol("Seba","Seba","Balet","120")
        s2=Spectacol("Kanye","Ye","Concert","122")
        self.__repo.store(s1)
        self.assertEqual(self.__repo.size()==1)
        self.__repo.store(s2)
        self.assertEqual(self.__repo.size()==2)

    def  test_update(self):
        s1=Spectacol("Seba","Seba","Balet","120")
        s2=Spectacol("Kanye","Ye","Concert","122") 
        self.__repo.store(s1)
        self.__repo.update2(s2)
        self.assertEqual(self.__repo.size()==1)
        l=self.__repo.__load_from_file()
        self.assertEqual(l[0].getartist()==s2.getartist())


        

      