class Fenomeno():
    def __init__(self, nombre, grado):
        self.nombre = nombre
        self.grado = grado
        
class Ciclon(Fenomeno):
    def __init__(self, nombre, grado):
        super().__init__(nombre, grado)
        
    def Efectuar_Ciclon(mapas,criatura,pos):
        pass

class ErupcionVolcánica(Fenomeno):
    def __init__(self, nombre, grado, posicion):
        super().__init__(nombre, grado)
        
        
    def Erupcion(mapas,especies):
        pass
        
class Subnami(Fenomeno):
    def __init__(self, nombre, grado):
        super().__init__(nombre, grado)
        
    def Efectuar_Subnami(mapas,especies,pos):
        pass
    
#dsfdas

def General_Nombre_Random():
    pass