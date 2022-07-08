from repository.repospectacol import SpectacolRepoFile
from service.servicespectacol import SpectacolService
from ui.consola import Consola
"""
fisier main care face legatura si ruleaza
"""
repo=SpectacolRepoFile("data/spectacol.txt")
service =SpectacolService(repo)
consola=Consola(service)

consola.ui()