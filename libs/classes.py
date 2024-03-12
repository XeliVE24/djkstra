class vertice():
    def __init__(self,valor) -> None:
        self.valor= valor 
        pass
pass

class grafo (arista):
    def __init__(self , origen , destino , peso ) -> None :
        super().__init__(origen ,destino,peso)
        pass