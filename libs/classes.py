from .functions import *
class grafo ():
        
   def __init__(self ) -> None :
        self.Arista = {}
        pass
   def addVertice (self,vertice):
        self.Arista[vertice]={}
        pass 
   def addArista(self,origen ,destino,peso):
        if origen not in self.Arista:
            self.addVertice(origen )
        if destino not in self.Arista:
            self.addVertice(destino)
        self.addArista[origen].update({destino:peso})

   def __str__(self) -> str:
        return printDicc(self.Arista)
    



        

        pass