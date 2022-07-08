from pickle import TRUE


class Spectacol:
    def __init__(self,titlu,artist,gen,durata):
        """
        Initializam clasa cu toate datele necesare
        """
        self.__titlu=titlu
        self.__gen=gen
        self.__artrist=artist
        self.__durata=durata

    def gettitlu(self):
        return self.__titlu

    def getgen(self):
        return self.__gen

    def getartist(self):
        return self.__artrist

    def getdurata(self):
        return self.__durata 

    def setdurata(self,value):
        self.__durata=value

    def setgen(self,value):
        self.__gen=value           

    def __str__(self):
        return "Titlu: "+self.__titlu+" Artist: "+self.__artrist+" Gen: "+self.__gen+" Durata:  "+str(self.__durata)      

    def __eq__(self, o):
        if self.__durata==o.getdurata() and self.__gen==o.getgen():
            return True 
        else:
            return False                  