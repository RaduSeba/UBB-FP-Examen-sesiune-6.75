from domain.entitati import Spectacol
from repository.repospectacol import SpectacolRepoFile

class SpectacolService:
    def __init__(self,repo):
        """
        initializam clasa service care face legarura intre ui si repo
        :paramtype:class
        :param:repo
        """
        self.__repo=repo

    def adauga(self,titlu,artist,gen,durata):
        """
        construieste spectacolul din datele primite si face legatura cu functia de adaugare in fisier din repo
        :param:titlu,artist,gen,durata
        :paramtype:string
        :return:spectacol
        :returntype:class
        """
        spectacol=Spectacol(titlu,artist,gen,durata)
        self.__repo.store(spectacol)
        return spectacol    

    def update(self,titlu,artist,gen,durata):
        """
        creeaza spectacolul si face legatura cu functia update
        :param:titlu,artist,gen,durata
        :paramtype:string
        """
        spectacol=Spectacol(titlu,artist,gen,durata)
        self.__repo.update2(spectacol)  


    def export(self,fisier):
        """
        face legatura cu dunctia de sortare si apoi adaugare in fisier nou
        :param:fisierul nou
        :paramtype:string
        """
        self.__repo.sortare(fisier)     

