from MyQueue import MyQueue
from random import Random, randint, random
from types import coroutine
import map
import especies
import misc
import queue
from tiles import Tile

class Fenomeno():
    def __init__(self, nombre, grado, cor, mapa):
        self.nombre = nombre
        self.grado = grado
        self.Recorrido = MyQueue()
        self.pos = 0
        self.cor = cor
        self.count_maxDistance = randint(0,10)
        self.vecmov = []
        self.map = map
        
        #cambiar por probabilidad
        duracion = randint(1,7)
        self.Recorrido.put((duracion, None))

    
    def GenerarRecorrido(self,mapa,corulti):
        duracion = randint(0,7)
        if corulti[2] == self.count_maxDistance:
            return []
        
        elif corulti[1] == None:
            return [(duracion,self.cor,0)]
        
        elif self.vecmov == "Random":
            ult_pos = corulti
            
            x = randint(-1,1)
            y = randint(-1,1)
            
            cornew = (ult_pos[1][0] + x, ult_pos[1][1] + y)
            if cornew[0] < mapa.SizeX and cornew[1] < mapa.SizeY:
                return [(duracion,cornew,corulti[2]+ 1)]
            
        return []
                
    
    def GenerateVector(self):
        self.vecmov.append("Random")
    
    def Refresc(self,time):
        queueCom = MyQueue()
        lenrecorrido = len(self.Recorrido)
        for i in range(0,lenrecorrido):
            posrecorrido = self.Recorrido.get()
            queueCom.put((posrecorrido[0],posrecorrido[1],time))
            
            while len(queueCom) != 0:
                posrecorrido = queueCom.get()
                move = (posrecorrido[0],posrecorrido[1],posrecorrido[2])
                duracion = posrecorrido[0]
                rest = posrecorrido[2]
                if duracion > rest:
                    posrecorrido = (duracion - time,posrecorrido[1],posrecorrido[2])
                    self.EfectuarFenomeno(self.map)
                    self.Recorrido.put(posrecorrido)
        
                elif duracion == rest:
                    duracion = duracion - time
                    self.EfectuarFenomeno(self.map,move)
                    listmove = self.GenerarRecorrido(self.map,move)
                    self.CambiarZona(self.map,posrecorrido,listmove)
                    for i in range(0,len(listmove) - 1):
                        self.Recorrido.append(listmove[i])
        
                elif duracion < rest:
                    rest = rest - duracion
                    self.EfectuarFenomeno(self.map,move)
                    duracion = 0
                    self.CambiarZona(time,self.map,move)
                    for i in range(0,len(listmove)):
                        queueCom.put((listmove[i][0],listmove[i][1],rest))
                
            
    def EfectuarFenomeno(self,mapa,move):
        print("Efectuando Fenomeno")
        return
    
    def CambiarZona(self,mapa,corulti,listmove):
        i = 0
        for zone in mapa.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == corulti:
                   i += 1
                   #eliminar fenomeno
                
                for j in range(0,len(listmove)):
                    if tile.Coordinates == listmove[j]:
                        i += 1
                        #añadir fenomeno
                    
                if i == 1 + len(listmove):
                    return
                    
                    
        
class Ciclon(Fenomeno):
    def __init__(self, nombre, grado, cor, mapa):
        super().__init__(nombre,grado,cor,mapa)
        
    def Rand_Mov_CC(cor_ciclon, map, poder_ciclon):
        cor_EjeX_low = cor_ciclon[1]
        cor_EjeX_up = map.SizeY-cor_ciclon[1]
        
        cor_EjeY_low = cor_ciclon[0]
        cor_EjeY_up = cor_ciclon[0]
        
        cord_rand_move = misc.randCord(-cor_EjeY_low, cor_EjeY_up, -cor_EjeX_low, cor_EjeX_up)
        cor_new = (cor_ciclon[0] + cord_rand_move[0]*poder_ciclon, cor_ciclon[1] + cord_rand_move[1]*poder_ciclon)
        return cor_new
    
    def EfectuarFenomeno(self,mapas,cor):
        if cor[1] == None:
            return
        
        ListaCriaturas = Ciclon.DetectarCriaturas(mapas,cor)
        Ciclon.MoverCriaturas(mapas,ListaCriaturas)
    
    def DetectarCriaturas(self,mapas,cor):
        creaturesMoves = []
        if self.Recorrido[self.pos] != None: 
            for zone in mapas.Zones:
                for tile in zone.TileList:
                    if tile.Coordinates == self.Recorrido[self.pos]:
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
    def __init__(self, nombre, grado, cor, mapa):
        super().__init__(nombre,grado,cor,mapa)
                
        
    def EfectuarFenomeno(self,mapa,cor):
        if cor[1] == None:
            return
        
        if cor == self.cor:
            list_caida_rocas = ErupcionVolcánica.PosCaida_Rocas(mapa,self.corvolcan)
            ErupcionVolcánica.Lluvia_De_Rocas(mapa,list_caida_rocas)
        
        ErupcionVolcánica.LavaRecorrido(mapa)
        
    def PosCaida_Rocas(self,mapa):
        for zone in mapa.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == self.cor_volcan:
                    cantidad_rocas = randint(0,20)
                    Lpos_caida_rocas = ErupcionVolcánica.Coordenadas_Caida_Rocas(cantidad_rocas)
                    return Lpos_caida_rocas
    


def General_Nombre_Random():
    pass
