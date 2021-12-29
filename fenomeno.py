from random import randint
import map
import especies
import misc
from tiles import Tile

class Fenomeno():
    def __init__(self, nombre, grado, cor, mapa):
        self.nombre = nombre
        self.grado = grado
        self.Recorrido = Fenomeno.GenerarRecorrido(mapa,cor)
        self.pos = 0
    
    def GenerarRecorrido(mapa,cor):
        distancia = randint(1,20)
        i = 0
        duracion = randint(0,7)
        duracion_aparicion = randint(0,7)
        list_Recorrido = [(duracion_aparicion,None),(duracion,cor)]
        
        for i in range(0, distancia):
            duracion = randint(0,7)
            ult_pos = list_Recorrido[-1][1]
            
            x = randint(-1,1)
            y = randint(-1,1)
            
            cornew = (ult_pos[0] + x, ult_pos[0] + y)
            list_Recorrido.append((duracion,cornew))
            
            i += 1
        
        return list_Recorrido
    
    def Refresc(self,time,mapa):
        rest = 0
        duracion = self.Recorrido[self.pos][0]
        if duracion > time:
            self.Recorrido[self.pos][0] = duracion - time
            self.EfectuarFenomeno(mapa)
            return
        
        elif duracion == time:
            self.Recorrido[self.pos][0] = duracion - time
            self.EfectuarFenomeno(mapa)
            self.CambiarZona(mapa)
            return
        
        elif duracion != 0:
            rest = time - duracion
            self.EfectuarFenomeno(mapa)
            self.Recorrido[self.pos][0] = 0
            self.CambiarZona(time,mapa)
            self.EfectuarFenomeno(mapa)
            self.Recorrido[self.pos][0] = duracion - rest
            
    def EfectuarFenomeno(self,mapa):
        print("Efectuando Fenomeno")
        return
    
    def CambiarZona(self,mapa):
        i = 0
        self.pos = self.pos + 1
        for zone in mapa.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == self.Recorrido[self.pos-1]:
                   i += 1
                   #eliminar fenomeno
                
                elif tile.Coordinates == self.Recorrido[self.pos]:
                    i += 1
                    #añadir fenomeno
                    
                if i == 2:
                    return
                    
                    
        
class Ciclon(Fenomeno):
    def __init__(self, nombre, grado):
        super().__init__(nombre, grado)
    
    def Rand_Mov_CC(cor_ciclon, map, poder_ciclon):
        cor_EjeX_low = cor_ciclon[1]
        cor_EjeX_up = map.SizeY-cor_ciclon[1]
        
        cor_EjeY_low = cor_ciclon[0]
        cor_EjeY_up = cor_ciclon[0]
        
        cord_rand_move = misc.randCord(-cor_EjeY_low, cor_EjeY_up, -cor_EjeX_low, cor_EjeY_low)
        cor_new = (cor_ciclon[0] + cord_rand_move[0]*poder_ciclon, cor_ciclon[1] + cord_rand_move[1]*poder_ciclon)
        return cor_new
    
    def Efectuar_Ciclon(mapas,especies,cor):
        ListaCriaturas = Ciclon.DetectarCriaturas(mapas,especies,cor)
        Ciclon.MoverCriaturas(mapas,ListaCriaturas)
    
    def DetectarCriaturas(mapas,especies,cor):
        creaturesMoves = []
        for zone in mapas.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == cor:
                    while tile.CreatureList > 0:
                        cordnew = Ciclon.Rand_Mov_CC(cor,mapas,1)
                        creature = tile.CreatureList.pop()
                        creaturesMoves.append((creature,cordnew))
                    return creaturesMoves

    def MoverCriaturas(mapa, ListCreature):
        while len(ListCreature) > 0:
            t = ListCreature.pop()
            for zone in mapa:
                for tile in zone.TileList:
                    if tile.Coordinates == t[1]:
                        #Cambiar las coordenadas de la ubicacion de la especie
                        tile.CreatureList.append(t[0])

class ErupcionVolcánica(Fenomeno):
    def __init__(self, nombre, grado, posicion):
        super().__init__(nombre, grado)
        
        
    def Efectuar_Erupcion(mapas,especies, cor):
        list_caida_rocas = ErupcionVolcánica.PosCaida_Rocas(mapas,cor)
        ErupcionVolcánica.Lluvia_De_Rocas(mapas,list_caida_rocas)
        Lrecorrido_lava = Define_Recorrido_Lava(mapas,cor)
        Lrecorrido_lava
        
    def PosCaida_Rocas(mapa,cor):
        for zone in mapa.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == cor:
                    cantidad_rocas = randint(0,20)
                    Lpos_caida_rocas = ErupcionVolcánica.Coordenadas_Caida_Rocas(cor,cantidad_rocas)
                    return Lpos_caida_rocas
    
    
    def Coordenadas_Caida_Rocas(cor,numero_rocas):
        pass
    
    def Lluvia_De_Rocas():
        pass
    
    def Define_Recorrido_Lava():
        pass
    
    def LavaRecorrido():
        pass
    
    
        
class Terremoto(Fenomeno):
    def __init__(self, nombre, grado):
        super().__init__(nombre, grado)
        
    def Efectuar_Terremoto(mapas,especies,cor):
        for zone in mapas.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == cor:
                    return
                
    def Agrietar():
        pass
