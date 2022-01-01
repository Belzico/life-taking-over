from queue import Queue
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
        self.Recorrido = Queue()
        self.pos = 0
        self.cor = cor
        self.vecmov = []
        
        #cambiar por probabilidad
        duracion = randint(0,7)
        self.Recorrido.put((duracion, None))

    
    def GenerarRecorrido(self,mapa,corulti):
        duracion = randint(0,7)
        
        if corulti[1] == None:
            return [(duracion,self.cor)]
        
        elif self.vecmov == "Random":
            ult_pos = corulti
            
            x = randint(-1,1)
            y = randint(-1,1)
            
            cornew = (ult_pos[0] + x, ult_pos[1] + y)
            if cornew[0] < mapa.SizeX and cornew[1] < mapa.SizeY:
                return [(duracion,cornew)]
            
        return []
                
    
    def GenerateVector(self):
        self.vecmov.append("Random")
    
    def Refresc(self,time,mapa):
        queueCom = Queue()
        lenrecorrido = len(self.Recorrido)
        for i in range(1,lenrecorrido):
            posrecorrido = self.Recorrido.get()
            queueCom.put((posrecorrido[0],posrecorrido[1],time))
            
            while queueCom != 0:
                posrecorrido = self.queueCom.get()
                move = (posrecorrido[0],posrecorrido[1])
                duracion = posrecorrido[0]
                rest = posrecorrido[2]
                if duracion > rest:
                    duracion = duracion - time
                    self.EfectuarFenomeno(mapa)
                    self.Recorrido.put(posrecorrido)
        
                elif duracion == rest:
                    self.Recorrido[self.pos][0] = duracion - time
                    self.EfectuarFenomeno(mapa,move)
                    listmove = self.GenerarRecorrido(mapa,move)
                    self.CambiarZona(mapa,posrecorrido,listmove)
                    for i in range(0,len(listmove) - 1):
                        self.Recorrido.append(listmove[i])
        
                elif duracion < rest:
                    rest = rest - duracion
                    self.EfectuarFenomeno(mapa,move)
                    duracion = 0
                    self.CambiarZona(time,mapa,move)
                    for i in range(1,len(listmove)):
                        queueCom.put((listmove[i][0],listmove[i][1],rest))
                
            
    def EfectuarFenomeno(self,mapa):
        print("Efectuando Fenomeno")
        return
    
    def CambiarZona(self,mapa,corulti,listmove):
        i = 0
        for zone in mapa.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == corulti:
                   i += 1
                   #eliminar fenomeno
                
                for j in range(0,len(listmove)-1):
                    if tile.Coordinates == listmove[j]:
                        i += 1
                        #añadir fenomeno
                    
                if i == 1 + len(listmove):
                    return
                    
                    
        
class Ciclon(Fenomeno):
    def __init__(self, nombre, grado, cor, mapa):
        super.__init__(nombre,grado,cor,mapa)
        
    def Rand_Mov_CC(cor_ciclon, map, poder_ciclon):
        cor_EjeX_low = cor_ciclon[1]
        cor_EjeX_up = map.SizeY-cor_ciclon[1]
        
        cor_EjeY_low = cor_ciclon[0]
        cor_EjeY_up = cor_ciclon[0]
        
        cord_rand_move = misc.randCord(-cor_EjeY_low, cor_EjeY_up, -cor_EjeX_low, cor_EjeX_up)
        cor_new = (cor_ciclon[0] + cord_rand_move[0]*poder_ciclon, cor_ciclon[1] + cord_rand_move[1]*poder_ciclon)
        return cor_new
    
    def EfectuarFenomeno(self,mapas,cor):
        if self.Recorrido[self.pos] == None:
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
        super.__init__(nombre,grado,cor,mapa)
                
        
    def EfectuarFenomeno(self,mapa):
        if self.Recorrido[self.pos] == None:
            return
        
        if self.pos == 1:
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
    

    def Lluvia_De_Rocas(self,mapa,list_rocas):
        for roca_cor in range(0,len(list_rocas)):
            for zone in mapa.Zones:
                for tile in zone.TileList:
                    if tile.Coordinates == roca_cor:
                        i = 0
                        while i < len(tile.CreatureList):
                            #Cambiar por probabilidades:
                            creature = tile.CreatureList[i]
                            death = randint(0,1)
                            if death == 1:
                                tile.CreatureList.pop(i)
                            else: 
                                i += 1
                                 
        
    def LavaRecorrido(self,mapa):
        count = self.Recorrido.qsize()
        while count != 0:
            pos_Lava = self.Recorrido.get()
            
    
    
        
class Terremoto(Fenomeno):
    def __init__(self, nombre, grado, cor, mapa):
        super().__init__(nombre, grado, cor, mapa)
        
    def EfectuarFenomeno(self,mapa):
        if self.Recorrido[self.pos] == None:
            return
        
        for zone in mapa.Zones:
            for tile in zone.TileList:
                if tile.Coordinates == self.corini:
                    return
                
    def Agrietar():
        pass
