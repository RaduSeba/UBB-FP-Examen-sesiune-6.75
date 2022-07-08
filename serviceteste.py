import unittest
from repository.repospectacol import SpectacolRepoFile
from domain.entitati import Spectacol
from service.servicespectacol import SpectacolService

class TestCaseProductRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        repo = SpectacolRepoFile("data/examen.txt")
        self.__service=SpectacolService(repo)


    def adauga(self):
        s1=Spectacol("Seba","Seba","Balet","120")
        s2=Spectacol("Kanye","Ye","Concert","122")
        self.__service.adauga("Seba","Seba","Balet","120")
        self.assertEqual(self.__service.__repo.size()==1)

    def update(self):
        self.__service.adauga("Seba","Seba","Balet","120")
        self.__service.update("Seba","Seba","Gras","12")
        self.assertEqual(self.__service.__repo.size()==1)