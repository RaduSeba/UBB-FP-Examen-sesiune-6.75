import imp
from service.servicespectacol import SpectacolService

class Consola:
    def __init__(self,service):
        """
        initializam clasa consola folosindu ne de service
        """
        self.__service=service

    def __print_menu(self):
        """
        menilul care se printeaza mereu
        """
        print("Comenzi:adauga,modifica_spectacol,genereaza,export,exit")

    def __store(self):
        """
        functia in care introducem datele pe care le trimitem in service si le validam
        """
        k=0
        erori=[]
        titlu=input("Titlul spectacolului:")
        if titlu=="":
            erori.append("titlul nu pooate fi vid")
            k=1
        artist=input("Artistul :")
        if artist=="":
            erori.append("Artisul nu poate fi vid") 
            k=1  
        gen=input("Genul spectacolului:")
        if gen=="Comedie" or gen=="Concert" or gen=="Balet" or gen=="Altele":
            pass
        else :
            erori.append("Genul trebuie sa fie una dintre:Comedie,Balet,Concert,Altele")
            k=1 
        durata=input("Durata spectacolului:")
        try:
            durata=int(durata)
            if int(durata)<0:
                erori.append("Durata e intreg pozitiv")
                k=1
        except ValueError:
            erori.append("Durata e intreg pozitiv")
            k=1
        if k==1:
            for eror in erori:
                print(eror)
            return
        else:            
            spectacol=self.__service.adauga(titlu,artist,gen,durata)
            print("Spectacolul",spectacol,"a fost adaugat cu succes")

    def __update(self):
        """
        functia in care introducem datele pe care le trimitem in service si le validam
        """
        k=0
        erori=[]
        titlu=input("Titlul spectacolului:")
        if titlu=="":
            erori.append("titlul nu pooate fi vid")
            k=1
        artist=input("Artistul :")
        if artist=="":
            erori.append("Artisul nu poate fi vid") 
            k=1  
        gen=input("Genul spectacolului:")
        if gen=="Comedie" or gen=="Concert" or gen=="Balet" or gen=="Altele":
            pass
        else :
            erori.append("Genul trebuie sa fie una dintre:Comedie,Balet,Concert,Altele")
            k=1 
        durata=input("Durata spectacolului:")
        try:
            durata=int(durata)
            if int(durata)<0:
                erori.append("Durata e intreg pozitiv")
                k=1
        except ValueError:
            erori.append("Durata e intreg pozitiv")
            k=1
        if k==1:
            for eror in erori:
                print(eror)
            return
        else:            
            self.__service.update(titlu,artist,gen,durata)

    def __export(self):
        """
        functia care exporteaza datele in fisierul nou
        """
        fisier=input("Introduceti numele fisierului in care doriti sa exportati:")
        self.__service.export(fisier)



    def ui(self):
        """
        ui care ruleaza
        """
        while True:
            self.__print_menu()
            cmd=input("Comanda este:")
            cmd.lower().strip()
            if cmd=="adauga":
                self.__store()
            elif cmd=="exit":
                return
            elif cmd=="modifica_spectacol":
                self.__update()  
            elif cmd=="export":
                self.__export()      
            else:
                print("Comanda gresita")                  
