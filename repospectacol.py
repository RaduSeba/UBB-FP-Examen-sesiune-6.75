from domain.entitati import Spectacol

class SpectacolRepoFile:
    def __init__(self,filename):
        """
        initializam clasa cu numele de fisier cu care vom lucara
        """
        self.__fielname=filename

    def __load_from_file(self):
        """
        functia care ne incarca datele din fisier intr o lista 
        :return:spectacol
        :rtype:list
        
        """
        with open(self.__fielname,"r") as f:
            spectacol=[]
            lines=f.readlines()
            for line in lines:
                spectacol_titlu,spectacol_artist,spectacol_gen,spectacol_durata=[token.strip() for token in line.split(" ")] 
                spectacol_durata=int(spectacol_durata)
                spe=Spectacol(spectacol_titlu,spectacol_artist,spectacol_gen,spectacol_durata)  
                spectacol.append(spe)
        f.close()
        return spectacol

    def __save_to_file(self,spectacole):
        """
        functia care ne adauga elementele in fisier

        """
        with open(self.__fielname,"w") as f:
            for spectacol in spectacole:
                spectacol_string=str(spectacol.gettitlu())+" "+str(spectacol.getartist())+" "+str(spectacol.getgen())+" "+str(spectacol.getdurata())+"\n" 
                f.write(spectacol_string)

    def store(self,spectacol):
        """
        functia cu care vom adauga spectacolele in fisier folosindu ne de load_from_file si __save_to_file
        
        """
        spectacole=self.__load_from_file()
        spectacole.append(spectacol)
        self.__save_to_file(spectacole)  

    def size(self):
        """
        functia care returneaza lungimea listei curente de spectacole
        :return:len(lista)
        :rtype:int
        """
        lista=self.__load_from_file()
        return len(lista)    

    def __find_by_index(self, all_spectacole, titlu,artist):
        """
        functia cu care gasesc indexul elementelor 
        :return:index
        :rtype:int
        """
        index = -1
        for i in range(len(all_spectacole)):
            if all_spectacole[i].gettitlu() == titlu and all_spectacole[i].getartist()==artist:
                index = i
        return index    


    def __save_to_file_nou(self,spectacole,fisier):
        """
        functia care adauga elementele intr un fisier cu numele specificat
        """
        with open("data/"+fisier+".txt","w") as f:
            for spectacol in spectacole:
               spectacol_string=str(spectacol.gettitlu())+","+str(spectacol.getartist())+","+str(spectacol.getgen())+","+str(spectacol.getdurata())+"\n"
               f.write(spectacol_string) 




    def sortare(self,fisier):
        """
        functia cu care sortam dupa artist si apoi dupa titlu si apo incarcam datele intr un fisier dat
        :param:fisier
        :paramtype:string
        
        """
        l=self.__load_from_file()    
    
        l.sort(key=lambda x: x.getartist(),reverse=False)
        l.sort(key=lambda x: x.gettitlu(),reverse=False)

        self.__save_to_file_nou(l,fisier)




    def update2(self, spectacol):
        """
        functia cu care dam update la elementele curente folosndu ne de index
        :param:spectacol
        :paramtype:spectacol
        
        """

        spectacole = self.__load_from_file()
        index = self.__find_by_index(spectacole,spectacol.gettitlu(),spectacol.getartist())
        if index==-1:
            print("NU exista spectacolul cu titlul si artistul specificat.")
            return 

        spectacole[index] = spectacol
        self.__save_to_file(spectacole)     



